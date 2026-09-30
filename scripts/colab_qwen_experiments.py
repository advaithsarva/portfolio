"""
Google Colab CLI Runner for Qwen3 Embeddings & Retrieval Experiments
Run on Colab Pro GPU using:
  python scripts/colab_qwen_experiments.py --model Qwen/Qwen3-Embedding-0.6B --output data/knowledge_embeddings.json
"""

import argparse
import json
import os
import sys
import time

def parse_args():
    parser = argparse.ArgumentParser(description="Generate Qwen Embeddings and Benchmark Retrieval")
    parser.add_argument("--corpus", default="data/knowledge_corpus.json", help="Path to knowledge corpus")
    parser.add_argument("--model", default="Qwen/Qwen3-Embedding-0.6B", help="Model name on Hugging Face")
    parser.add_argument("--fallback_model", default="Alibaba-NLP/gte-Qwen2-1.5B-instruct", help="Fallback HF model")
    parser.add_argument("--output", default="data/knowledge_embeddings.json", help="Output path for embeddings")
    parser.add_argument("--device", default="auto", help="cuda or cpu")
    return parser.parse_args()

def main():
    args = parse_args()
    print(f"==================================================")
    print(f"  Qwen Embedding Generation & Colab Benchmark")
    print(f"  Target Model: {args.model}")
    print(f"==================================================")

    if not os.path.exists(args.corpus):
        print(f"Error: Corpus not found at {args.corpus}")
        sys.exit(1)

    with open(args.corpus, "r", encoding="utf-8") as f:
        docs = json.load(f)
    print(f"Loaded {len(docs)} documents from {args.corpus}")

    # Text to embed: Title + Category + Technologies + Content
    texts_to_embed = []
    for d in docs:
        techs = ", ".join(d.get("technologies", []))
        rep = f"Title: {d['name']} | Category: {d['category']} | Stack: {techs} | {d['content']}"
        texts_to_embed.append(rep)

    try:
        import torch
        from transformers import AutoTokenizer, AutoModel
        
        device = "cuda" if (torch.cuda.is_available() and args.device == "auto") or args.device == "cuda" else "cpu"
        print(f"Using device: {device.upper()}")
        if device == "cuda":
            print(f"GPU: {torch.cuda.get_device_name(0)}")

        model_name = args.model
        print(f"Loading tokenizer and model: {model_name}...")
        try:
            tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
            model = AutoModel.from_pretrained(model_name, trust_remote_code=True).to(device)
        except Exception as e:
            print(f"Failed to load {model_name}: {e}")
            print(f"Attempting fallback model: {args.fallback_model}...")
            model_name = args.fallback_model
            tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
            model = AutoModel.from_pretrained(model_name, trust_remote_code=True).to(device)

        model.eval()

        print(f"Encoding {len(texts_to_embed)} knowledge chunks on {device}...")
        t0 = time.time()
        
        embeddings_list = []
        batch_size = 16
        with torch.no_grad():
            for i in range(0, len(texts_to_embed), batch_size):
                batch = texts_to_embed[i:i + batch_size]
                inputs = tokenizer(batch, padding=True, truncation=True, max_length=512, return_tensors="pt").to(device)
                outputs = model(**inputs)
                
                # Mean pooling or last hidden state
                if hasattr(outputs, "last_hidden_state"):
                    attention_mask = inputs["attention_mask"].unsqueeze(-1)
                    token_embeddings = outputs.last_hidden_state
                    sum_embeddings = torch.sum(token_embeddings * attention_mask, dim=1)
                    sum_mask = torch.clamp(attention_mask.sum(dim=1), min=1e-9)
                    pooled = sum_embeddings / sum_mask
                else:
                    pooled = outputs[0][:, 0]
                
                # Normalize L2
                pooled = torch.nn.functional.normalize(pooled, p=2, dim=1)
                embeddings_list.extend(pooled.cpu().numpy().tolist())

        elapsed = time.time() - t0
        print(f"Embedding generated in {elapsed:.2f}s ({len(docs)/elapsed:.1f} chunks/sec)")
        
        # Save output
        out_data = {
            "model": model_name,
            "dimension": len(embeddings_list[0]),
            "num_chunks": len(embeddings_list),
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "doc_ids": [d["id"] for d in docs],
            "embeddings": embeddings_list
        }
        
        os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(out_data, f)
        print(f"Saved dense embeddings to {args.output}")

    except ImportError:
        print("Note: PyTorch / Transformers not configured for GPU run. Please run this in Google Colab environment.")
        sys.exit(1)

if __name__ == "__main__":
    main()
