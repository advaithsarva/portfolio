# 🛠️ Scripts & Build Tooling

This directory contains the data pipelines, knowledge ingestion engines, RAG compilation scripts, and model training utilities for **THE ADVAITH DAILY** portfolio.

## Pipeline Architecture

```text
knowledge/ (Raw Documents & Metadata)
     │
     ▼
scripts/ingest_knowledge.py ─────────► data/knowledge_corpus.json & data/bm25_index.json
     │
     ▼
scripts/build_dense_vectors.py ──────► data/knowledge_embeddings.json
     │
     ▼
scripts/build_rag_engine.py ─────────► rag-engine.js (Client Hybrid RAG System)
     │
     ▼
scripts/evaluate_rag.py ─────────────► data/eval_results.json (MRR & Recall Benchmarks)
```

## Script Reference

### 1. RAG Knowledge & Pipeline Tooling
- `ingest_knowledge.py`: Parses all structured documents in `knowledge/*/*.json`, generates canonical `data/knowledge_corpus.json`, and indexes BM25 lexical tokens.
- `build_dense_vectors.py`: Calculates normalized 64-dimensional semantic dense vectors for all corpus documents.
- `build_rag_engine.py`: Compiles the unified hybrid client-side RAG engine into `rag-engine.js` (dense vectors + BM25 index + Reciprocal Rank Fusion + query rewriting).
- `evaluate_rag.py`: Runs automated benchmark queries against ground-truth pairs, measuring Hit@K, MRR, and latency.

### 2. Dataset Generation & Training
- `generate_eval_dataset.py`: Synthesizes evaluation test suites from verified portfolio repositories and credentials.
- `generate_chat_dataset.py`: Formats conversational training pairs in JSONL format for fine-tuning.
- `colab_qwen_experiments.py`: Experimentation harness for Qwen series LLMs.
- `train_lora_colab.py`: LoRA fine-tuning script optimized for Google Colab GPU runtimes.

### 3. Catalog & Knowledge Generators
- `build_structured_knowledge.py`: Reconstructs the `knowledge/` category trees.
- `build_new_projects_catalog.py`: Compiles project catalog cards for `projects.html`.
- `build_rag_and_pages.py`: Page generation utilities.
- `update_all_skills_and_netlify.py`: Netlify functions and skill index synchronization.

## How to Rebuild the RAG Engine

From the repository root:
```bash
# 1. Ingest updated knowledge files
python scripts/ingest_knowledge.py

# 2. Recompile client-side hybrid RAG engine
python scripts/build_rag_engine.py

# 3. Verify benchmarks
python scripts/evaluate_rag.py
```
