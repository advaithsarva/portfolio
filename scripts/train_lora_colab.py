"""
Google Colab CLI Training Script for Qwen QLoRA Fine-Tuning
Fine-tunes Qwen3-4B / Qwen2.5-3B-Instruct on portfolio conversational dataset.
Teaches conversation style, grounded citations, and subtle Pikachu persona.

Usage in Google Colab (Terminal / CLI):
  pip install transformers peft bitsandbytes trl datasets accelerate
  python scripts/train_lora_colab.py --model Qwen/Qwen2.5-3B-Instruct --dataset data/chat_dataset.jsonl --output models/qwen_portfolio_lora
"""

import argparse
import os
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="QLoRA Fine-Tuning on Google Colab GPU")
    parser.add_argument("--model", default="Qwen/Qwen2.5-3B-Instruct", help="Base model identifier")
    parser.add_argument("--dataset", default="data/chat_dataset.jsonl", help="Conversational JSONL dataset")
    parser.add_argument("--output", default="models/qwen_portfolio_lora", help="Output path for LoRA adapter")
    parser.add_argument("--epochs", type=int, default=3, help="Training epochs")
    parser.add_argument("--batch_size", type=int, default=4, help="Batch size per GPU")
    parser.add_argument("--learning_rate", type=float, default=2e-4, help="Learning rate")
    return parser.parse_args()

def main():
    args = parse_args()
    print("==================================================")
    print("  Qwen Portfolio Assistant - QLoRA Fine-Tuner")
    print(f"  Base Model: {args.model}")
    print(f"  Dataset:    {args.dataset}")
    print(f"  Output Dir: {args.output}")
    print("==================================================")

    try:
        import torch
        from datasets import load_dataset
        from transformers import (
            AutoModelForCausalLM,
            AutoTokenizer,
            BitsAndBytesConfig,
            TrainingArguments
        )
        from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
        from trl import SFTTrainer

        if not torch.cuda.is_available():
            print("WARNING: CUDA is not available! QLoRA requires a GPU. Please run in Google Colab Pro.")
            sys.exit(1)

        print(f"CUDA Device: {torch.cuda.get_device_name(0)}")

        # 1. 4-bit Quantization Config (QLoRA)
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16,
            bnb_4bit_use_double_quant=True
        )

        # 2. Load Tokenizer & Model
        print(f"Loading {args.model} with 4-bit NF4 quantization...")
        tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        model = AutoModelForCausalLM.from_pretrained(
            args.model,
            quantization_config=bnb_config,
            device_map="auto",
            trust_remote_code=True
        )

        model = prepare_model_for_kbit_training(model)

        # 3. LoRA Configuration targeting Qwen attention & MLP projection layers
        peft_config = LoraConfig(
            r=16,
            lora_alpha=32,
            target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
            lora_dropout=0.05,
            bias="none",
            task_type="CAUSAL_LM"
        )
        model = get_peft_model(model, peft_config)
        model.print_trainable_parameters()

        # 4. Load & Format Dataset
        dataset = load_dataset("json", data_files=args.dataset, split="train")
        print(f"Loaded {len(dataset)} conversation examples.")

        def apply_chat_template(batch):
            formatted_texts = []
            for msgs in batch["messages"]:
                formatted = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=False)
                formatted_texts.append(formatted)
            return {"text": formatted_texts}

        dataset = dataset.map(apply_chat_template, batched=True)

        # 5. Training Arguments
        training_args = TrainingArguments(
            output_dir=args.output,
            num_train_epochs=args.epochs,
            per_device_train_batch_size=args.batch_size,
            gradient_accumulation_steps=2,
            learning_rate=args.learning_rate,
            logging_steps=5,
            save_strategy="epoch",
            bf16=torch.cuda.is_bf16_supported(),
            fp16=not torch.cuda.is_bf16_supported(),
            warmup_ratio=0.1,
            lr_scheduler_type="cosine",
            optim="paged_adamw_8bit"
        )

        # 6. SFT Trainer
        trainer = SFTTrainer(
            model=model,
            train_dataset=dataset,
            dataset_text_field="text",
            max_seq_length=1024,
            tokenizer=tokenizer,
            args=training_args,
            peft_config=peft_config
        )

        print("Starting QLoRA training...")
        trainer.train()

        print(f"Training complete! Saving LoRA adapter to {args.output}...")
        trainer.model.save_pretrained(args.output)
        tokenizer.save_pretrained(args.output)
        print("LoRA weights saved successfully.")

    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Please install requirements: pip install transformers peft bitsandbytes trl datasets accelerate")
        sys.exit(1)

if __name__ == "__main__":
    main()
