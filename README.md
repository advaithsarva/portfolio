# 📰 THE ADVAITH DAILY — Technical Broadsheet & Engineering Archive

> **AI • Computing • Research & Engineering**  
> *The verified engineering record, technical dispatches, and interactive knowledge archives of Advaith Narayana Sarva.*

[![Live Site](https://img.shields.io/badge/Edition-Digital%20Vol.%20I-6F2923.svg)](https://advaithsarva.github.io)
[![Verified Repositories](https://img.shields.io/badge/Repositories-39%20Audited-171512.svg)](projects.html)
[![RAG System](https://img.shields.io/badge/RAG%20Engine-Hybrid%20Dense%20%2B%20BM25-263A42.svg)](#-the-archive-detective-rag-system)
[![Status](https://img.shields.io/badge/Systems%20Terminal-Amber%20CRT%20Online-FFB000.svg)](#-engineering-archive-terminal)

---

## 🏛️ Concept & Architectural Metaphor

*The Advaith Daily* operates as a **fictional technical publication and living computational archive** set in an alternate history of computing:

```text
                     THE TECHNICAL ARCHIVE
                               │
            ┌──────────────────┼──────────────────┐
            ▼                  ▼                  ▼
      1920s BROADSHEET     1980s CRT TERMINAL   ARCHIVE DETECTIVE
         [BROWSE]              [EXPLORE]             [ASK]
            │                  │                  │
            └──────────────────┼──────────────────┘
                               ▼
                  39 VERIFIED REPOSITORIES & DATA
```

1. **1920s Newspaper Broadsheet (Browse)**: Multi-column editorial composition, warm aged newsprint ground (`#E8DCC2`), carbon printer's ink (`#171512`), high-contrast display headlines (`Playfair Display`), drop caps, hairline rules, and department classification.
2. **1980s CRT Terminal (Explore)**: Physical bezel container with amber phosphor luminescence (`#FFB000`), subtle CRT bloom, scanlines overlay, and interactive command-line dispatch system.
3. **The Archive Detective (Ask)**: Intelligent query desk featuring Chief Investigator Detective Pikachu, providing grounded RAG evidence retrieval with citation back-tracing across 39 audited repositories.

---

## 📁 Repository Directory Structure

```text
portfolio-zer0/
├── index.html                   # Front Page broadsheet editorial spread & lead dispatches
├── projects.html                # Technology Desk: 39 verified repositories catalog
├── project.html                 # Technical Dossier: individual report deep dive viewer
├── resume.html                  # Career Record: official curriculum vitae & credentials
├── style.css                    # Complete 1920s broadsheet design system & CRT tokens
├── script.js                    # Interactive engine: Three.js canvas, theme, terminal, & audio
├── rag-engine.js                # Compiled hybrid client-side vector + BM25 RAG engine
├── rag-knowledge.json           # Client knowledge corpus (55 chunks across 8 domains)
├── projects-data.js             # Project metadata catalog & taxonomy definitions
├── projects-data.json           # Raw canonical projects dataset
├── tech-icons.js                # Monochrome SVG iconography dictionary
├── .nojekyll                    # Bypass Jekyll processing on GitHub Pages
├── .gitignore                   # Version control exclusion rules
│
├── assets/                      # Static assets & media
│   ├── pikachu.png              # Detective Pikachu mascot illustration
│   ├── feather-mark.svg         # Publication insignia
│   ├── Advaith_Narayana_Sarva_Resume.pdf  # Printable curriculum vitae
│   └── projects/                # Curated technical schematics & project figures
│
├── data/                        # Processed knowledge bases & evaluation artifacts
│   ├── knowledge_corpus.json    # Canonical structured knowledge chunks
│   ├── knowledge_embeddings.json# 64-dim normalized semantic embeddings
│   ├── bm25_index.json          # Sparse lexical inverted index
│   ├── eval_dataset.json        # RAG evaluation benchmark test cases
│   └── eval_results.json        # Benchmarked precision, latency, and MRR
│
├── knowledge/                   # Markdown / JSON source documents
│   ├── about/                   # Editorial profiles & personal pursuits
│   ├── achievements/            # Hackathons (IBM BOB Top 5, 0.9924 ROC-AUC)
│   ├── education/               # Academic records (SMU 3.47 CGPA, Woxsen 8.69 CGPA)
│   ├── experience/              # Clinical audits (Preventvital ASCVD sign fix)
│   ├── github/                  # Open-source archive statistics
│   ├── projects/                # Technical reports for 39 repositories
│   ├── research/                # NLP bias, NLI verification, & transformer primitives
│   └── skills/                  # Core systems, languages, and frameworks
│
├── notebooks/                   # Jupyter & Google Colab research notebooks
│   └── colab_qwen_experiments.ipynb
│
├── projects/                    # 39 static project archive pages
│   ├── autonomous-performance-agent.html
│   ├── graph-rag-knowledge-system.html
│   ├── media-nlp-pipeline.html
│   └── ... (36 additional static project pages)
│
└── scripts/                     # Python data pipelines & build tooling
    ├── README.md                # Tooling documentation & pipeline reference
    ├── ingest_knowledge.py      # Knowledge corpus ingestion pipeline
    ├── build_dense_vectors.py   # Normalized dense vector embeddings generator
    ├── build_rag_engine.py      # Production hybrid RAG engine compiler
    └── evaluate_rag.py          # Automated retrieval evaluation benchmark
```

---

## 🔍 The Archive Detective (RAG System)

The Archive Detective uses a **hybrid retrieval-augmented generation (RAG)** pipeline:

```text
Visitor Query (e.g. "What projects involve RAG?")
      │
      ▼
Query Processor & Context Resolver
      │
      ├──► Dense Semantic Vector Search (64-dim Subspace)
      ├──► Sparse BM25 Lexical Scoring (Exact Term Match)
      ▼
Reciprocal Rank Fusion (RRF: 0.35 BM25 + 0.65 Dense)
      │
      ▼
Grounded Synthesizer & Hallucination Guardrails
      │
      ▼
Case Findings + Verified Evidence Links (Report No. 002, 003, etc.)
```

- **Accuracy**: Zero hallucinations on portfolio facts; every answer is traceable to verified knowledge chunks.
- **Latency**: Sub-15ms local client execution without external paid API dependencies.
- **Mascot Personality**: 90–95% rigorous technical communication with a subtle (<10%) Detective Pikachu flavor.

---

## 💻 Engineering Archive Terminal

Accessible on the front page or by typing commands directly:

| Command | Action |
| :--- | :--- |
| `help` | Lists all available system commands |
| `whoami` | Displays engineer profile, status, and education (SMU 3.47 CGPA) |
| `projects` | Lists primary AI agents, NLP pipelines, and systems |
| `skills` | Displays core technology stacks by desk |
| `achievements` | IBM BOB Hackathon, clinical ML audit, academic honors |
| `chess` | Interactive Sicilian Defense (1. e4 c5) challenge board |
| `beatbox` | Synthesizes live 8-bit vocal beatbox rhythm via Web Audio API |
| `ghost` / `spook`| Tests the engineer's archival aversion to spectral apparitions! |
| `rag <query>` | Queries the RAG knowledge engine directly in the CLI |
| `theme` | Toggles contrast mode (Carbon Newsprint / Aged Paper) |

---

## 🚀 GitHub Pages Deployment

The portfolio is 100% static with **zero build dependencies** and zero external runtime requirements. The hybrid vector + BM25 RAG engine runs entirely client-side in the browser:

```bash
# 1. Preview locally using Python built-in server
python -m http.server 8000
```

### Deploying to GitHub Pages:
1. Push this repository to GitHub:
   ```bash
   git add .
   git commit -m "feat: complete 1920s broadsheet newspaper portfolio"
   git push origin main
   ```
2. In your GitHub repository:
   - Navigate to **Settings** → **Pages**.
   - Under **Build and deployment** / **Source**, select **Deploy from a branch**.
   - Select branch **`main`** and folder **`/ (root)`**, then click **Save**.
   - The `.nojekyll` file in the root ensures all static assets, scripts, and fonts are served directly.
3. Your site will be live at `https://<username>.github.io/<repo-name>/`!

---

## 📜 License & Copyright

© 2026 Advaith Narayana Sarva. All rights reserved. Open-source code repositories referenced in the publication are licensed under their respective MIT/Apache licenses.
