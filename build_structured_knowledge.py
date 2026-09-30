"""
Build Structured Knowledge Base for Advaith Narayana Sarva's Portfolio
Organizes all verified portfolio knowledge into clean, rich-metadata documents under knowledge/
"""
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KNOWLEDGE_DIR = os.path.join(BASE_DIR, "knowledge")

# Load existing projects data
with open(os.path.join(BASE_DIR, "projects-data.json"), "r", encoding="utf-8") as f:
    projects = json.load(f)

# 1. Populating knowledge/about/
about_docs = [
    {
        "id": "about-bio",
        "type": "about",
        "name": "Personal Bio & Engineering Profile",
        "category": "Profile",
        "technologies": ["Python", "PyTorch", "Neo4j", "Docker", "FastAPI"],
        "date": "2026",
        "source": "index.html#home",
        "section": "Hero & Introduction",
        "github_url": "https://github.com/advaithsarva",
        "demo_url": "index.html#home",
        "tags": ["Bio", "Advaith Narayana Sarva", "GenAI", "Systems Engineer", "Profile", "Summary"],
        "stats": "39 Repositories · 3.47 SMU CGPA · 8.69 Woxsen CGPA",
        "slug": "bio",
        "content": "Advaith Narayana Sarva is an AI & Systems Engineer specializing in interpretable meta-inference, Graph-RAG architectures, and autonomous multi-agent harnesses. He builds low-level systems from scratch (such as a decoder-only transformer and C-level memory allocators) while engineering production RAG pipelines and clinical ML audit systems. He is actively seeking GenAI and systems engineering internships and full-time opportunities."
    },
    {
        "id": "about-interests",
        "type": "about",
        "name": "Technical & Personal Interests",
        "category": "Interests",
        "technologies": ["Chess Tactics", "Vocal Percussion", "Geopolitics", "Football"],
        "date": "2026",
        "source": "rag-knowledge.json#hobbies",
        "section": "Personal Profile",
        "github_url": "",
        "demo_url": "index.html#home",
        "tags": ["Hobbies", "Chess", "Sicilian Defense", "Football", "Beatboxing", "Debate", "Geopolitics", "Heritage"],
        "stats": "Sicilian Defense (1. e4 c5) · Blitz/Rapid @advaithsarva",
        "slug": "interests",
        "content": "Outside of coding, Advaith is a competitive chess player specializing in the Sicilian Defense (1. e4 c5) on Chess.com and Lichess (@advaithsarva). He plays attacking counter-football, practices vocal percussion (beatboxing), has a strong background in competitive debate and rhetorical analysis, and follows global geopolitics and technology preprints daily. Note: He has an amusing, genuine terror of horror movies and ghosts (especially Gengar)!"
    },
    {
        "id": "about-contact",
        "type": "about",
        "name": "Contact & Social Channels",
        "category": "Contact",
        "technologies": ["Email", "LinkedIn", "GitHub", "Instagram"],
        "date": "2026",
        "source": "index.html#contact",
        "section": "Contact Information",
        "github_url": "https://github.com/advaithsarva",
        "demo_url": "mailto:advaithsarva@gmail.com",
        "tags": ["Contact", "Email", "LinkedIn", "Hire", "Social", "Inquiries"],
        "stats": "Open to US, India & Remote Roles",
        "slug": "contact",
        "content": "Advaith is reachable via email at advaithsarva@gmail.com. His professional profile is on LinkedIn at linkedin.com/in/sarvaadvaithnarayana/ and his public code repositories are hosted at github.com/advaithsarva. Instagram handle: @advaithsarva."
    }
]

for doc in about_docs:
    filename = f"{doc['slug']}.json"
    with open(os.path.join(KNOWLEDGE_DIR, "about", filename), "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2)

# 2. Populating knowledge/education/
education_docs = [
    {
        "id": "edu-smu",
        "type": "education",
        "name": "Saint Martin's University (Lacey, WA) - Exchange Scholar",
        "category": "Education",
        "technologies": ["Distributed Systems", "Machine Learning", "Computer Vision", "Advanced Algorithms"],
        "date": "Aug 2025 - May 2026",
        "source": "resume.html#education",
        "section": "International Academic Exchange",
        "github_url": "",
        "demo_url": "resume.html#education",
        "tags": ["Saint Martin's University", "SMU", "Lacey", "Washington", "USA", "Exchange", "Dean's List", "3.47 CGPA"],
        "stats": "3.47 / 4.0 CGPA · Dean's List Honors · Completed May 2026",
        "slug": "smu-exchange",
        "content": "Advaith attended Saint Martin's University in Lacey, Washington, USA as an International Exchange Scholar from August 2025 to May 2026 (completed in May 2026 across two semesters) in BS Computer Science (AI & ML track). He maintained a 3.47 / 4.0 CGPA, earned Dean's List honors, and studied Distributed Systems, Machine Learning, Computer Vision, and Advanced Algorithms, while serving as a peer mentor in the Center for Student Success."
    },
    {
        "id": "edu-woxsen",
        "type": "education",
        "name": "Woxsen University (Hyderabad, India) - B.Tech in CSE",
        "category": "Education",
        "technologies": ["Data Structures", "Deep Learning", "Operating Systems", "Computer Networks", "Database Management Systems"],
        "date": "Aug 2023 - Aug 2027",
        "source": "resume.html#education",
        "section": "Undergraduate Degree",
        "github_url": "",
        "demo_url": "resume.html#education",
        "tags": ["Woxsen University", "Hyderabad", "B.Tech", "Computer Science", "AI & ML", "8.69 CGPA"],
        "stats": "8.69 / 10.0 CGPA · Expected August 2027",
        "slug": "woxsen-degree",
        "content": "Advaith is pursuing his Bachelor of Technology in Computer Science and Engineering with specialization in Artificial Intelligence & Machine Learning at Woxsen University, Hyderabad, India. He currently holds an 8.69 / 10.0 cumulative CGPA with anticipated graduation in August 2027. Relevant coursework: Design & Analysis of Algorithms, NLP, Autonomous Multi-Agent Systems, Neural Networks, Database Systems."
    }
]

for doc in education_docs:
    filename = f"{doc['slug']}.json"
    with open(os.path.join(KNOWLEDGE_DIR, "education", filename), "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2)

# 3. Populating knowledge/experience/
experience_docs = [
    {
        "id": "exp-preventvital",
        "type": "experience",
        "name": "Preventvital (GruentzigAI Pvt. Ltd.) - AI/ML Engineer Intern",
        "category": "Experience",
        "technologies": ["Python", "FastAPI", "PostgreSQL", "RAG Safety", "Clinical Risk Modeling"],
        "date": "May 2025 - Jul 2025",
        "source": "resume.html#experience",
        "section": "Industry Experience",
        "github_url": "",
        "demo_url": "resume.html#experience",
        "tags": ["Preventvital", "GruentzigAI", "Clinical ML", "ASCVD", "Goff 2014", "ICMR 2023", "Internship"],
        "stats": "Identified critical ASCVD calculation defect (0.1% vs 2.1% baseline) · Authored ICMR sign-off protocol",
        "slug": "preventvital-internship",
        "content": "At Preventvital (GruentzigAI), Advaith audited backend ML inference architectures for cardiovascular risk calculation. He identified a critical coefficient sign inversion error in the ASCVD clinical risk calculation that was artificially calculating 0.1% baseline risk for untreated patients. He reproduced the calculation against the published Goff 2014 trial baseline (expected 2.1%), wrote the bug report for clinical sign-off, and authored RAG & safety rules adhering to ICMR 2023 guidelines on an 'engine computes, LLM explains, clinician signs' protocol."
    },
    {
        "id": "exp-codex-club",
        "type": "experience",
        "name": "CODE{X} Programming Club - Executive Leader",
        "category": "Experience",
        "technologies": ["Python", "Full-Stack Development", "Git", "Competitive Programming"],
        "date": "Mar 2024 - Aug 2025",
        "source": "resume.html#leadership",
        "section": "Campus Leadership",
        "github_url": "",
        "demo_url": "resume.html#leadership",
        "tags": ["CODE{X}", "Club Executive", "Hackathons", "Mentorship", "Algorithms"],
        "stats": "Organized hackathons · Conducted peer code reviews · Mentored junior developers",
        "slug": "codex-leadership",
        "content": "As Executive Leader at CODE{X} Programming Club, Advaith organized algorithmic hackathons, conducted peer code reviews, coordinated competitive programming workshops, and mentored junior developers in Python and modern full-stack workflows."
    },
    {
        "id": "exp-woxsen-research",
        "type": "experience",
        "name": "AI Research Centre, Woxsen University - Research Intern",
        "category": "Experience",
        "technologies": ["Python", "Django", "Machine Learning", "Applied AI"],
        "date": "Feb 2024 - Apr 2024",
        "source": "resume.html#experience",
        "section": "Academic Research",
        "github_url": "",
        "demo_url": "resume.html#experience",
        "tags": ["AI Research Centre", "Research Intern", "Django", "Applied ML"],
        "stats": "Engineered Django web modules and UI interfaces for applied ML academic tools",
        "slug": "woxsen-research-intern",
        "content": "Advaith built Django-based web modules and UI interfaces applying applied ML methods to academic research tools at the AI Research Centre at Woxsen University."
    }
]

for doc in experience_docs:
    filename = f"{doc['slug']}.json"
    with open(os.path.join(KNOWLEDGE_DIR, "experience", filename), "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2)

# 4. Populating knowledge/achievements/
achievement_docs = [
    {
        "id": "achieve-ibm-sentinel",
        "type": "achievement",
        "name": "IBM BOB National Hackathon 2026 - Top 5 South Zone (The Sentinel Grid)",
        "category": "Achievements",
        "technologies": ["Python", "XGBoost", "LightGBM", "Automated Testing", "Climate AI"],
        "date": "2026",
        "source": "resume.html#honors",
        "section": "Hackathons & Honors",
        "github_url": "https://github.com/advaithsarva/the-sentinel-grid",
        "demo_url": "project.html?id=the-sentinel-grid",
        "tags": ["IBM BOB Hackathon", "The Sentinel Grid", "Top 5", "ROC-AUC 0.9924", "Disaster AI"],
        "stats": "Top 5 South Zone · 0.9924 ROC-AUC · 314 automated checks · 6,957 LOC",
        "slug": "ibm-bob-sentinel-grid",
        "content": "Advaith led engineering for The Sentinel Grid, placing in the Top 5 South Zone at the IBM BOB National Hackathon 2026. The disaster-intelligence system comprises 6,957 lines of Python, 314 automated checks, and 104 formula audits, achieving a verified ROC-AUC of 0.9924 on 473,000 real district-month soil moisture observations for Coimbatore."
    },
    {
        "id": "achieve-smu-deans-list",
        "type": "achievement",
        "name": "Saint Martin's University Dean's List Honors",
        "category": "Achievements",
        "technologies": ["Academic Excellence", "Distributed Systems", "Algorithms"],
        "date": "2025 - 2026",
        "source": "resume.html#honors",
        "section": "Academic Honors",
        "github_url": "",
        "demo_url": "resume.html#honors",
        "tags": ["Dean's List", "Saint Martin's University", "Academic Honors", "3.47 CGPA"],
        "stats": "Maintained 3.47 / 4.0 GPA across two rigorous semesters in the United States",
        "slug": "smu-deans-list",
        "content": "Earned Dean's List honors at Saint Martin's University in Lacey, WA during his international exchange program, recognizing exceptional academic standing in advanced computer science and artificial intelligence coursework."
    }
]

for doc in achievement_docs:
    filename = f"{doc['slug']}.json"
    with open(os.path.join(KNOWLEDGE_DIR, "achievements", filename), "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2)

# 5. Populating knowledge/skills/
skill_docs = [
    {
        "id": "skill-ai-ml-nlp",
        "type": "skill",
        "name": "AI, NLP, LLMs & Deep Learning Architecture",
        "category": "Technologies",
        "technologies": ["PyTorch", "Hugging Face Transformers", "spaCy", "Neo4j", "Graph-RAG", "Cross-Encoder NLI"],
        "date": "2026",
        "source": "resume.html#skills",
        "section": "Core Technologies",
        "github_url": "https://github.com/advaithsarva",
        "demo_url": "resume.html#skills",
        "tags": ["PyTorch", "Transformers", "NLP", "LLMs", "RAG", "Graph-RAG", "Embeddings", "Meta-Inference"],
        "stats": "15+ AI & NLP pipelines · Custom transformer from scratch · Graph-RAG RRF",
        "slug": "ai-ml-nlp",
        "content": "Advaith specializes in deep learning architectures, computational semantics, and retrieval augmented generation. Key competencies: PyTorch from primitives (attention mechanisms, KV-cache, rotary embeddings, LayerNorm), Hugging Face Transformers, spaCy custom tokenization DAGs, cross-encoder NLI for factual verification, and Graph-RAG hybrid search fusing BM25, dense HNSW, and multi-hop Neo4j Cypher traversals."
    },
    {
        "id": "skill-agents",
        "type": "skill",
        "name": "Autonomous Agent Systems & Tool Orchestration",
        "category": "Technologies",
        "technologies": ["Model Context Protocol (MCP)", "LangChain", "Autonomous Agents", "Tool Calling", "Hierarchical State"],
        "date": "2026",
        "source": "resume.html#skills",
        "section": "Agent Architectures",
        "github_url": "https://github.com/advaithsarva",
        "demo_url": "projects.html?cat=AI+Agents",
        "tags": ["Autonomous Agents", "MCP", "SuperBrain", "Multi-Agent Swarms", "Tool Execution"],
        "stats": "9 Autonomous Agent repositories · 41 MCP tools · 11.7x autonomous Postgres speedup",
        "slug": "autonomous-agents",
        "content": "Advaith designs autonomous multi-agent harnesses with deterministic guardrails. Implementations include SuperBrain MCP (41 standardized tools with persistent vector memory across sessions), autonomous database tuning agents (executing explain analyze loops and automated rollback guards), and recursive web research verification agents."
    },
    {
        "id": "skill-systems-backend",
        "type": "skill",
        "name": "Systems Programming, Databases & Backend Engineering",
        "category": "Technologies",
        "technologies": ["Python", "PostgreSQL", "Docker", "FastAPI", "TypeScript", "Node.js", "Linux", "AWS"],
        "date": "2026",
        "source": "resume.html#skills",
        "section": "Systems & Infrastructure",
        "github_url": "https://github.com/advaithsarva",
        "demo_url": "resume.html#skills",
        "tags": ["Python", "SQL", "PostgreSQL", "FastAPI", "Docker", "Linux", "Bash", "AWS Cloud", "Systems"],
        "stats": "C memory allocators · Custom HTTP servers · Asynchronous query pipelines",
        "slug": "systems-and-infrastructure",
        "content": "Advaith is grounded in systems engineering and low-level mechanics: Linux/Bash scripting, Docker containerization, asynchronous FastAPI/AsyncPG backends, PostgreSQL query optimization and indexing, TypeScript/Node.js, and low-level systems implemented from scratch (custom malloc/free with mmap, custom HTTP/1.1 server socket engines, and deterministic cache architectures)."
    }
]

for doc in skill_docs:
    filename = f"{doc['slug']}.json"
    with open(os.path.join(KNOWLEDGE_DIR, "skills", filename), "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2)

# 6. Populating knowledge/research/
research_docs = [
    {
        "id": "research-eval-gap",
        "type": "research",
        "name": "Eval Gap Research: AI Grading Without Ground Truth",
        "category": "Research",
        "technologies": ["Python", "LLM Evaluation", "Confidence Scoring", "Rubrics"],
        "date": "2026",
        "source": "projects-data.json#eval-gap-research",
        "section": "Research & Evaluation",
        "github_url": "",
        "demo_url": "project.html?id=eval-gap-research",
        "tags": ["LLM Evaluation", "Eval Gap", "AI Judge", "Checklist Rubrics", "Research"],
        "stats": "1.00 vs 0.31 good vs bad separation · n = 8 directional study",
        "slug": "eval-gap-research",
        "content": "Eval Gap Research investigates how to evaluate AI agents when no formal ground truth test exists. It measures whether an AI judge using structured rubrics can separate good from bad outputs cleanly, isolating where confidence signals fail on subtly incorrect answers. Early findings demonstrated 1.00 vs 0.31 score separation on n=8 samples with ongoing multi-model cross-rubric validation."
    },
    {
        "id": "research-meta-inference",
        "type": "research",
        "name": "Interpretable Meta-Inference DAG Topologies",
        "category": "Research",
        "technologies": ["Python", "DAG", "spaCy", "Symbolic AI", "Formal Fallacies"],
        "date": "2025 - 2026",
        "source": "projects-data.json#media-nlp-pipeline",
        "section": "Computational Semantics",
        "github_url": "https://github.com/advaithsarva/media-nlp-pipeline",
        "demo_url": "project.html?id=media-nlp-pipeline",
        "tags": ["Meta-Inference", "DAG", "Verbatim Evidence", "Informal Fallacy", "NLP"],
        "stats": "0.175 false positive rate per 1,000 words on Wikipedia · 23 fallacy detectors",
        "slug": "meta-inference-dag",
        "content": "Advaith's research in interpretable meta-inference focuses on deterministic Directed Acyclic Graph (DAG) engines that uncouple semantic interpretation from black-box LLMs. By combining syntactic sentence disambiguation, lexical boundary checks, and verbatim evidence spans, the Media NLP Pipeline achieves a rigorous false positive rate of 0.175 per 1,000 words on neutral Wikipedia ground truth across 23 informal fallacy detectors."
    }
]

for doc in research_docs:
    filename = f"{doc['slug']}.json"
    with open(os.path.join(KNOWLEDGE_DIR, "research", filename), "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2)

# 7. Populating knowledge/projects/ (All 39 projects with rich metadata!)
for p in projects:
    slug = p["slug"]
    doc = {
        "id": f"proj-{slug}",
        "type": "project",
        "name": p["title"],
        "category": p["category"],
        "technologies": p["tags"],
        "date": "2025 - 2026",
        "source": f"projects/{slug}.html",
        "section": "Engineering Repositories",
        "github_url": p["links"] if p["links"].startswith("http") else "",
        "demo_url": f"project.html?id={slug}",
        "tags": p["tags"] + [p["title"], p["category"], slug],
        "stats": p["stats"],
        "slug": slug,
        "content": f"{p['title']} ({p['category']}): \"{p['tagline']}\". {p['overview']} Key highlights: {' '.join(p['highlights'])} Honest limitation/tradeoff: {p['honest']} Verified metrics: {p['stats']}."
    }
    with open(os.path.join(KNOWLEDGE_DIR, "projects", f"{slug}.json"), "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2)

# 8. Populating knowledge/github/ (Repository catalogue index)
github_doc = {
    "id": "github-all-repos",
    "type": "github",
    "name": "Verified GitHub Repositories Catalog",
    "category": "Repositories",
    "technologies": ["Git", "GitHub", "Python", "TypeScript", "Docker"],
    "date": "2026",
    "source": "https://github.com/advaithsarva",
    "section": "Public Code",
    "github_url": "https://github.com/advaithsarva",
    "demo_url": "projects.html",
    "tags": ["GitHub", "Repositories", "Open Source", "advaithsarva"],
    "stats": "39 Verified Repositories",
    "slug": "repositories",
    "content": f"Advaith maintains 39 verified software engineering and research repositories on GitHub (github.com/advaithsarva). Spanning AI Agents (9), NLP & RAG (8), Systems from Scratch (6), Machine Learning & Data (5), Full-Stack Systems (6), and In-Progress Evaluation Research (4). Featured public repositories include the-sentinel-grid, media-nlp-pipeline, graph-rag-knowledge-system, autonomous-performance-agent, superbrain_mcp, and fact-checking-agent."
}

with open(os.path.join(KNOWLEDGE_DIR, "github", "repositories.json"), "w", encoding="utf-8") as f:
    json.dump(github_doc, f, indent=2)

print(f"Successfully generated structured knowledge base across all 8 categories!")
