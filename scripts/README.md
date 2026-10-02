# Scripts

Build tooling for the portfolio. Run everything from the repo root.

## Chatbot pipeline

```text
knowledge/*/*.json
  -> ingest_knowledge.py      data/knowledge_corpus.json, data/bm25_index.json, rag-knowledge.json
  -> build_dense_vectors.py   data/knowledge_embeddings.json (TF-IDF + SVD, 64 dims)
  -> build_rag_engine.py      rag-engine.js
  -> generate_eval_dataset.py data/eval_questions.json
  -> evaluate_rag.py          data/eval_results.json (recall@k, MRR, latency)
```

`evaluate_rag.py` grades answers it writes itself for several questions, so only its retrieval metrics are meaningful.

## Project catalogue

- `parse_webpoints_perfect.py`: reads `C:\Projects\webpoints.md` and writes `projects-data.json` and `projects-data.js`.

## Training experiments

- `generate_chat_dataset.py`: writes question/answer pairs to `data/chat_dataset.jsonl`.
- `colab_qwen_experiments.py`, `train_lora_colab.py`: LoRA fine-tuning experiments for Colab. They aren't used by the live site.

## Older one-off generators

`build_structured_knowledge.py`, `build_new_projects_catalog.py`, `build_rag_and_pages.py`, `refactor_projects_and_skills.py` and `update_all_skills_and_netlify.py` produced earlier versions of the pages and knowledge files. They still contain text that has since been corrected (Neo4j, hobbies, "39 verified repositories"). Re-running any of them overwrites the current files with that old text, so don't, unless you update them first.
