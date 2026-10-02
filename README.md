# The Advaith Daily

Portfolio site for Advaith Narayana Sarva, styled as a 1920s newspaper. Live at https://advaithsarva.github.io/portfolio/.

It lists 39 projects. 34 are public repositories under [github.com/advaithsarva](https://github.com/advaithsarva); the other 5 are private or not published yet, and their pages say so.

## What's on the site

- **Front page** (`index.html`): profile, three featured projects, the Preventvital audit, a skills index, a small terminal, and the "Archive Detective" chat box.
- **Technology Desk** (`projects.html`): all 39 projects, filterable by category and technology. Each card opens `project.html?id=<slug>`.
- **Career Record** (`resume.html`): the résumé as a web page, plus a printable PDF in `assets/`.

The site is static, with no build step and no server code. Open `index.html` through any static server:

```bash
python -m http.server 8000
```

## The Archive Detective

A retrieval chatbot that runs in the browser with no API calls. It answers from 54 short documents in `knowledge/`, one per project plus profile, education, experience, skills and research.

How it works:

1. Each query is scored two ways: BM25 over the documents, and cosine similarity over 64-dimensional vectors made with TF-IDF + truncated SVD (`scripts/build_dense_vectors.py`). These are LSA vectors, not a neural embedding model.
2. The two rankings are merged with Reciprocal Rank Fusion.
3. The answer is built from the top documents, with links back to the project pages. A few common questions (the hackathon, the Postgres agent, Preventvital, education) have hand-written answers in `scripts/build_rag_engine.py`.

Retrieval on 43 test questions with a known target document (`data/eval_results.json`): recall@1 44%, recall@3 67%, recall@5 74%, MRR 0.563. The "factual accuracy" and "hallucination rate" figures in that file grade answers that `evaluate_rag.py` itself hard-codes, so they don't measure the chatbot. Only the retrieval numbers above mean anything.

## Terminal commands

| Command | What it does |
| :--- | :--- |
| `help` | list commands |
| `whoami` | profile, internship, education |
| `projects` | six featured projects with links |
| `skills` | languages, ML/NLP, systems |
| `achievements` / `experience` | hackathon, audit, honours; work history |
| `rag <query>` | ask the Archive Detective from the terminal |
| `ls`, `cat <file>` | read `resume.md`, `stack.json`, `academics.txt` |
| `neofetch`, `matrix`, `quote` | decoration |
| `theme` | switch light/dark |

## Rebuilding the chatbot data

Edit the JSON files in `knowledge/`, then run from the repo root:

```bash
python scripts/ingest_knowledge.py      # knowledge/ -> data/knowledge_corpus.json, BM25 index, rag-knowledge.json
python scripts/build_dense_vectors.py   # -> data/knowledge_embeddings.json
python scripts/build_rag_engine.py      # -> rag-engine.js
python scripts/generate_eval_dataset.py # -> data/eval_questions.json
python scripts/evaluate_rag.py          # -> data/eval_results.json
```

Project cards come from a different source: `projects-data.json` is generated from `C:\Projects\webpoints.md` by `scripts/parse_webpoints_perfect.py`. Edit project text there, not in the JSON.

The `projects/*.html` pages are older static copies that nothing links to anymore; `project.html?id=` replaced them.

## Layout

```text
index.html, projects.html, project.html, resume.html
style.css, script.js         design system; theme, terminal, chat UI
rag-engine.js                generated; do not edit by hand
rag-knowledge.json           generated client corpus
projects-data.json / .js     generated project catalogue
knowledge/                   source documents for the chatbot
data/                        generated corpus, indexes, eval set and results
scripts/                     the pipeline above, plus older one-off generators
assets/                      résumé PDF, favicons, images
```

## License

© 2026 Advaith Narayana Sarva. All rights reserved. Each linked project repository carries its own license.
