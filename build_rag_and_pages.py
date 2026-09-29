import json
import os
import re

PORTFOLIO_DIR = r"C:\Users\advai\OneDrive\Desktop\portfolio-zer0"
PROJECTS_DIR = os.path.join(PORTFOLIO_DIR, "projects")
os.makedirs(PROJECTS_DIR, exist_ok=True)

# 1. Load Projects Data
with open(os.path.join(PORTFOLIO_DIR, "projects-data.json"), "r", encoding="utf-8") as f:
    projects = json.load(f)

print(f"Loaded {len(projects)} projects")

# 2. Build RAG Knowledge Chunks
personal_chunks = [
    {
        "id": "bio-general",
        "title": "Advaith Narayana Sarva - Engineering Profile & Status",
        "category": "Profile",
        "tags": ["GenAI", "Systems", "Career", "Profile", "Status", "Open for Roles", "Internships"],
        "content": "Advaith Narayana Sarva is a GenAI & Systems Engineer building Graph-RAG architectures, multi-agent swarms, and low-level ML systems from PyTorch primitives. He is actively seeking GenAI and systems engineering internships and full-time roles across the United States, India, and worldwide remote. Contact him directly at advaithsarva@gmail.com.",
        "stats": "Actively Seeking Roles · US / India / Remote",
        "slug": ""
    },
    {
        "id": "edu-smu",
        "title": "Saint Martin's University (Lacey, WA) - International Exchange Scholar",
        "category": "Education",
        "tags": ["Education", "SMU", "Saint Martin", "GPA", "CGPA", "Exchange", "Dean's List", "USA", "3.47"],
        "content": "Advaith completed an international academic exchange at Saint Martin's University in Lacey, Washington, USA (August 2025 to May 2026, completed in May 2026 across two semesters) in BS Computer Science (AI & ML). He maintained a 3.47 / 4.0 CGPA and earned Dean's List honors. Coursework covered Distributed Systems, Machine Learning, Computer Vision, and Advanced Algorithms, alongside serving as a peer mentor in the Center for Student Success.",
        "stats": "3.47 / 4.0 CGPA · Dean's Honors · Completed May 2026",
        "slug": ""
    },
    {
        "id": "edu-woxsen",
        "title": "Woxsen University - B.Tech in CSE (AI & ML)",
        "category": "Education",
        "tags": ["Education", "Woxsen", "B.Tech", "Degree", "College", "CGPA", "Hyderabad", "India", "8.69"],
        "content": "Advaith is pursuing his B.Tech in Computer Science and Engineering (specialization in AI & ML) at Woxsen University in Hyderabad, India (expected graduation August 2027) with a current CGPA of 8.69 / 10.0.",
        "stats": "8.69 / 10 CGPA · Expected Aug 2027",
        "slug": ""
    },
    {
        "id": "exp-preventvital",
        "title": "Preventvital (GruentzigAI) - Clinical ML Audit & RAG Gates",
        "category": "Experience",
        "tags": ["Preventvital", "Clinical", "ASCVD", "Audit", "Healthcare", "Goff 2014", "ICMR", "Internship", "Work"],
        "content": "As an AI/ML Engineer Intern at Preventvital (GruentzigAI Pvt. Ltd.), Advaith audited backend ML inference architectures. He caught a critical coefficient sign inversion error in the ASCVD (cardiovascular) clinical risk calculation engine that was artificially returning a 0.1% baseline risk for untreated patients. He reproduced the calculation against the published Goff 2014 trial baseline (expected 2.1%), authored the bug report for clinical sign-off, and designed RAG & safety rules adhering to ICMR 2023 guidelines enforcing an 'engine computes, LLM explains, clinician signs' protocol.",
        "stats": "Clinical ASCVD Audit · Goff 2014 Benchmark · ICMR 2023 Protocol",
        "slug": ""
    },
    {
        "id": "achieve-ibm",
        "title": "IBM BOB National Hackathon 2026 - The Sentinel Grid",
        "category": "Achievements",
        "tags": ["IBM", "Hackathon", "Sentinel Grid", "Disaster", "ROC-AUC", "Top 5", "Award", "0.9924"],
        "content": "Advaith led engineering for The Sentinel Grid, placing in the Top 5 South Zone at the IBM BOB National Hackathon 2026. The disaster-intelligence system comprises 6,957 lines of Python, 314 automated checks, and 104 formula audits, achieving a verified ROC-AUC of 0.9924 on 473,000 real district-month soil moisture observations for Coimbatore.",
        "stats": "Top 5 South Zone · 0.9924 ROC-AUC · 314 Automated Checks",
        "slug": "the-sentinel-grid"
    },
    {
        "id": "hobby-chess",
        "title": "Chess Passion & Tactical Playstyle",
        "category": "Hobbies",
        "tags": ["Chess", "Sicilian Defense", "Tactics", "Blitz", "Rapid", "Chess.com", "Lichess", "Sport", "Game"],
        "content": "Advaith is an avid chess player who loves the Sicilian Defense (1. e4 c5), sharp counter-attacking tactical combinations, and deep endgame calculations. He actively plays rapid (10m) and blitz (3+2 / 5+3) games on Chess.com and Lichess under the handle @advaithsarva. He welcomes matches and invites anyone to challenge him to a game.",
        "stats": "1. e4 c5 Sicilian · Blitz & Rapid · @advaithsarva",
        "slug": ""
    },
    {
        "id": "hobby-football",
        "title": "Football / Soccer & Pitch Tactics",
        "category": "Hobbies",
        "tags": ["Football", "Soccer", "Pitch", "Striker", "Sports", "High-Press", "European Football"],
        "content": "On the pitch, Advaith plays football with a strong focus on high-pressing attacking coordination and rapid counter-attacks. He is an avid fan of European football tactics and loves discussing match strategies as much as playing the game.",
        "stats": "High-Press Attack · Pitch Coordinator",
        "slug": ""
    },
    {
        "id": "hobby-beatbox",
        "title": "Beatbox & Vocal Percussion",
        "category": "Hobbies",
        "tags": ["Beatbox", "Music", "Vocal", "Percussion", "Rhythm", "Bass", "Freestyle", "Jam"],
        "content": "Advaith is a skilled beatboxer who drops acoustic basslines, vocal drum loops, and freestyle rhythm patterns between model training sessions and mathematical proofs. He loves jamming and dropping live beats.",
        "stats": "Acoustic Vocal Percussion · Basslines & Loops",
        "slug": ""
    },
    {
        "id": "hobby-debate",
        "title": "Debate & Public Speaking Leadership",
        "category": "Leadership",
        "tags": ["Debate", "Speech", "CODEX", "Leadership", "Club", "Argumentation", "Fallacy", "Persuasion"],
        "content": "Advaith served as Executive Leader of CODE{X} Programming Club (200+ members). He is an experienced debater who loves structural argumentation, persuasion dynamics, and dissecting rhetorical fallacies—a passion that directly inspired his 23-detector Media NLP Rhetoric & Bias Detection Pipeline.",
        "stats": "CODE{X} Executive Leader · 200+ Members · Rhetoric Analysis",
        "slug": "media-nlp-pipeline"
    },
    {
        "id": "hobby-news-geopolitics",
        "title": "News Maniac & Geopolitical Analyst",
        "category": "Interests",
        "tags": ["News", "Geopolitics", "Global", "Diplomacy", "Foreign Policy", "arXiv", "Maniac", "Papers"],
        "content": "Advaith is an obsessive news and knowledge consumer. Every morning he consumes global news feeds, technical arXiv preprints, economic treaties, and geopolitical analyses. He loves analyzing macro power shifts, international diplomacy, and multi-lateral statecraft.",
        "stats": "Daily arXiv & Global News · Macro Statecraft",
        "slug": ""
    },
    {
        "id": "culture-heritage",
        "title": "Cultural Roots & Timeless Philosophy",
        "category": "Philosophy",
        "tags": ["Culture", "Heritage", "Roots", "Tradition", "Philosophy", "India", "Pride", "Values"],
        "content": "Advaith is deeply grounded in his cultural roots, classical philosophy, and timeless heritage. He carries authentic pride in Indian tradition and philosophical foundations, seamlessly connecting ancient principles of mindfulness and duty to modern engineering in Washington and India.",
        "stats": "Timeless Heritage · Classical Philosophy",
        "slug": ""
    },
    {
        "id": "fandom-pokemon",
        "title": "Pokémon Lore & Cyber Pikachu Companion",
        "category": "Interests",
        "tags": ["Pokemon", "Pikachu", "Lore", "GameBoy", "Nintendo", "Partner", "Generation", "Pokedex"],
        "content": "Advaith has been a lifelong Pokémon fan since childhood, mastering battle synergies, team compositions, and generational lore. That passion is why Pikachu is his official AI companion on this website!",
        "stats": "Lifelong Trainer · Gen Lore Geek · Partner #025",
        "slug": ""
    },
    {
        "id": "weakness-ghosts",
        "title": "Secret Weakness - Hilariously Terrified of Ghosts",
        "category": "Trivia",
        "tags": ["Ghost", "Ghosts", "Spook", "Horror", "Scare", "Scary", "Gengar", "Haunted", "Boo", "Fear"],
        "content": "Advaith is genuinely and hilariously terrified of ghosts, haunted houses, horror films, and Ghost-type Pokémon like Gengar! If anyone brings up ghosts, he will sprint in the opposite direction and wrap himself in three blankets. Mentioning ghosts causes Pikachu to panic and trigger an emergency screen glitch!",
        "stats": "Error 404: Courage Not Found · 100% Spook Rate",
        "slug": ""
    }
]

# Add each project as a knowledge chunk
for p in projects:
    hl_str = " ".join(p["highlights"])
    personal_chunks.append({
        "id": "proj-" + p["slug"],
        "title": p["title"] + " (" + p["category"] + ")",
        "category": p["category"],
        "tags": p["tags"] + [p["category"], p["title"], p["slug"]],
        "content": f"{p['title']}: {p['tagline']}. {p['overview']} Highlights: {hl_str} Honest note: {p['honest']} Verified link: {p['links']}",
        "stats": p["stats"],
        "slug": p["slug"]
    })

print(f"Total knowledge chunks in RAG corpus: {len(personal_chunks)}")

# Save rag-knowledge.json
with open(os.path.join(PORTFOLIO_DIR, "rag-knowledge.json"), "w", encoding="utf-8") as f:
    json.dump(personal_chunks, f, indent=2, ensure_ascii=False)

# 3. Generate rag-engine.js
rag_engine_code = f"""/* ==========================================================================
   Advaith Narayana Sarva — In-Browser Vector & BM25 Hybrid RAG Engine
   Client-Side Knowledge Retrieval & Context-Augmented Synthesis
   ========================================================================== */

(function(window) {{
  'use strict';

  const CORPUS = {json.dumps(personal_chunks, ensure_ascii=False, indent=2)};

  // 1. Text Tokenizer & Normalizer
  function tokenize(text) {{
    if (!text) return [];
    return text
      .toLowerCase()
      .replace(/[^a-z0-9\\s]/g, ' ')
      .split(/\\s+/)
      .filter(w => w.length > 1 && !STOPWORDS.has(w));
  }}

  const STOPWORDS = new Set([
    'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', 'as', 'at',
    'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'cannot', 'could',
    'did', 'do', 'does', 'doing', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has', 'have',
    'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is',
    'it', 'its', 'itself', 'let', 'me', 'more', 'most', 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once',
    'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', 'she', 'should', 'so',
    'some', 'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they',
    'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'we', 'were', 'what', 'when',
    'where', 'which', 'while', 'who', 'whom', 'why', 'with', 'would', 'you', 'your', 'yours', 'yourself', 'yourselves'
  ]);

  // 2. Build Vocabulary & Inverted Index for BM25
  const N = CORPUS.length;
  const docTokens = CORPUS.map(c => tokenize(c.title + ' ' + c.tags.join(' ') + ' ' + c.content));
  const docLens = docTokens.map(t => t.length);
  const avgDocLen = docLens.reduce((a, b) => a + b, 0) / (N || 1);

  const df = {{}};
  docTokens.forEach(tokens => {{
    const unique = new Set(tokens);
    unique.forEach(term => {{
      df[term] = (df[term] || 0) + 1;
    }});
  }});

  // IDF calculation
  const idf = {{}};
  Object.keys(df).forEach(term => {{
    idf[term] = Math.log(1 + (N - df[term] + 0.5) / (df[term] + 0.5));
  }});

  // 3. Dense Vector Embeddings (Orthogonal Hashing Subspace, d=64)
  const DIM = 64;

  function hashTermToDim(term) {{
    let hash = 0;
    for (let i = 0; i < term.length; i++) {{
      hash = ((hash << 5) - hash) + term.charCodeAt(i);
      hash |= 0;
    }}
    return Math.abs(hash) % DIM;
  }}

  function embedTokens(tokens) {{
    const vec = new Float32Array(DIM);
    tokens.forEach(term => {{
      const d = hashTermToDim(term);
      const weight = idf[term] || 1.0;
      vec[d] += weight;
    }});
    // L2 Normalize
    let norm = 0;
    for (let i = 0; i < DIM; i++) norm += vec[i] * vec[i];
    norm = Math.sqrt(norm);
    if (norm > 0) {{
      for (let i = 0; i < DIM; i++) vec[i] /= norm;
    }}
    return vec;
  }}

  const docVectors = docTokens.map(embedTokens);

  function cosineSimilarity(vecA, vecB) {{
    let dot = 0;
    for (let i = 0; i < DIM; i++) {{
      dot += vecA[i] * vecB[i];
    }}
    return Math.max(0, dot);
  }}

  // 4. BM25 Scoring
  function scoreBM25(queryTokens, docIdx, k1 = 1.5, b = 0.75) {{
    const tokens = docTokens[docIdx];
    const len = docLens[docIdx];
    const tf = {{}};
    tokens.forEach(t => {{ tf[t] = (tf[t] || 0) + 1; }});

    let score = 0;
    queryTokens.forEach(term => {{
      if (tf[term]) {{
        const termIdf = idf[term] || 0.5;
        const termTf = tf[term];
        const denom = termTf + k1 * (1 - b + b * (len / avgDocLen));
        score += termIdf * ((termTf * (k1 + 1)) / denom);
      }}
    }});
    return score;
  }}

  // 5. Hybrid Retrieval (Vector Cosine Sim + BM25 Fusion)
  function retrieve(rawQuery, topK = 3) {{
    const startTime = performance.now();
    const queryTokens = tokenize(rawQuery);
    const queryVec = embedTokens(queryTokens);

    const candidates = [];
    for (let i = 0; i < N; i++) {{
      const cosSim = cosineSimilarity(queryVec, docVectors[i]);
      const bm25 = scoreBM25(queryTokens, i);
      // Normalized hybrid score
      const hybridScore = (cosSim * 0.65) + (Math.min(bm25 / 10, 1.0) * 0.35);
      candidates.push({{
        chunk: CORPUS[i],
        cosSim: Number(cosSim.toFixed(4)),
        bm25: Number(bm25.toFixed(4)),
        score: Number(hybridScore.toFixed(4)),
        index: i
      }});
    }}

    candidates.sort((a, b) => b.score - a.score);
    const results = candidates.slice(0, topK);
    const latencyMs = Number((performance.now() - startTime).toFixed(2));

    return {{
      query: rawQuery,
      queryTokens: queryTokens,
      queryVec: Array.from(queryVec.slice(0, 8)).map(n => Number(n.toFixed(3))), // preview 8 dims
      topChunks: results,
      latencyMs: latencyMs
    }};
  }}

  // 6. Context-Augmented Generation / Response Synthesis
  function query(rawQuery) {{
    const qLower = (rawQuery || '').toLowerCase();
    
    // Ghost Check (Playful easter egg)
    const isGhost = ['ghost', 'ghosts', 'gengar', 'gastly', 'haunter', 'spook', 'horror', 'scare', 'scary', 'boo'].some(w => qLower.includes(w));
    if (isGhost) {{
      return {{
        isGhost: true,
        answer: "P-Pika-PI?! 👻⚡ <em>*shivers and cowers behind tail with sparks flying*</em> SHHHH! Don't summon Gengar! Between you and me, Advaith is <strong>genuinely terrified of ghosts</strong>, haunted houses, horror movies, and Ghost-type Pokémon! He will literally sprint across the pitch to escape! Please, let's stick to chess, PyTorch, or Electric types! 🙈⚡",
        retrieval: retrieve(rawQuery, 2),
        citations: ["weakness-ghosts"]
      }};
    }}

    const retrieval = retrieve(rawQuery, 3);
    const top = retrieval.topChunks;

    if (!top || top.length === 0 || top[0].score < 0.05) {{
      return {{
        isGhost: false,
        answer: "Pikachu! ⚡ Advaith is a GenAI & Systems Engineer building Graph-RAG architectures and autonomous agents. He also plays chess (Sicilian defense), plays football, beatboxes, follows geopolitics, and completed his SMU exchange with a 3.47 CGPA—just don't mention spooky ghosts! 👻 Try asking about his projects or hobbies!",
        retrieval: retrieval,
        citations: ["bio-general"]
      }};
    }}

    const best = top[0].chunk;
    const citations = top.map(t => t.chunk.id);
    let answerText = "";

    // Contextual phrasing based on best retrieved category
    if (best.id === 'hobby-chess') {{
      answerText = "Pika! ♟️ Advaith is a passionate chess player! He loves sharp tactical combinations and the <strong>Sicilian Defense (1. e4 c5)</strong>. He's always up for a rapid (10m) or blitz (3+2 / 5+3) match on Chess.com and Lichess (<code>@advaithsarva</code>). Reach out anytime for a game!";
    }} else if (best.id === 'hobby-football') {{
      answerText = "Chu! ⚽ On the pitch, Advaith plays football with high-pressing attacking coordination and counter-attacks. When he isn't training neural nets or testing MCP harnesses, you'll find him playing on the field or discussing European football tactics!";
    }} else if (best.id === 'hobby-beatbox') {{
      answerText = "Pika-tsh-ka-boom! 🎤 Yes! Advaith can beatbox! Between mathematical proofs and low-level code, he drops acoustic basslines, rhythm loops, and freestyle vocal percussion. Ask him for a live beatbox demo when you connect!";
    }} else if (best.id === 'hobby-debate') {{
      answerText = "Pikachu! 🎙️ Advaith is a seasoned debater and former Executive Leader at CODE{{X}}! He loves structured argumentation, logical rigour, and dissecting persuasion tactics. That passion for rhetorical analysis is what inspired his <em>Media NLP Rhetoric & Bias Detection Pipeline</em>!";
    }} else if (best.id === 'hobby-news-geopolitics') {{
      answerText = "⚡ Pika! Advaith is a true knowledge and news maniac! He starts every day devouring global news, technical arXiv preprints, and geopolitical analyses. He loves analyzing macro shifts, treaties, and international statecraft!";
    }} else if (best.id === 'culture-heritage') {{
      answerText = "✨ Pika! Advaith deeply honors his cultural roots and heritage! He draws immense grounding from classical Indian philosophy, timeless traditions, and cultural pride, carrying those values from Washington to Hyderabad!";
    }} else if (best.id === 'edu-smu') {{
      answerText = "🎓 Pika! Advaith completed his international exchange at <strong>Saint Martin's University (Lacey, WA, USA)</strong> in May 2026 across two semesters with a <strong>3.47 / 4.0 CGPA</strong> and Dean's List honors! He studied Distributed Systems, Machine Learning, and Computer Vision while mentoring peers in the Center for Student Success.";
    }} else if (best.id === 'edu-woxsen') {{
      answerText = "🎓 Pika! At <strong>Woxsen University (Hyderabad, India)</strong>, Advaith is pursuing his B.Tech in CSE (AI & ML) with an <strong>8.69 / 10 CGPA</strong> (Expected August 2027)!";
    }} else if (best.id === 'exp-preventvital') {{
      answerText = "Pika! 🔍 At Preventvital (GruentzigAI), Advaith audited backend ML inference architectures. He caught a critical coefficient sign inversion error in the ASCVD (cardiovascular) clinical risk calculation engine that was artificially returning a 0.1% baseline risk for untreated patients! He reproduced the calculation against the published Goff 2014 trial baseline (expected 2.1%), wrote up the bug report for clinical sign-off, and authored RAG & safety rules adhering to ICMR 2023 guidelines on an 'engine computes, LLM explains, clinician signs' protocol!";
    }} else if (best.id === 'achieve-ibm') {{
      answerText = "🏆 Pika-power! In the IBM BOB National Hackathon 2026, Advaith led engineering for <strong>The Sentinel Grid</strong>, placing <strong>Top 5 in the South Zone</strong>! The disaster-intelligence system comprises 6,957 lines of Python, 314 automated checks, and 104 formula audits, achieving a verified <strong>ROC-AUC of 0.9924</strong> on 473,000 district-month soil moisture observations!";
    }} else if (best.slug) {{
      // Project match!
      const proj = best;
      answerText = `🚀 Pika! <strong>${{proj.title}}</strong>:<br>${{proj.content}}<br><em>Key Metrics:</em> <code>${{proj.stats}}</code>.<br><a href="project.html?id=${{proj.slug}}" class="text-blue" style="font-weight:700; text-decoration:underline;">View Full Project Page →</a>`;
    }} else {{
      answerText = `⚡ Pika! Based on verified data:<br>${{best.content}}<br><em>Source:</em> <code>${{best.title}}</code>`;
    }}

    return {{
      isGhost: false,
      answer: answerText,
      retrieval: retrieval,
      citations: citations
    }};
  }}

  // Public Interface
  window.AdvaithRAG = {{
    corpus: CORPUS,
    retrieve: retrieve,
    query: query,
    stats: {{
      totalChunks: N,
      vocabSize: Object.keys(df).length,
      embeddingDim: DIM
    }}
  }};

  console.log(`[RAG ENGINE READY] Loaded ${{N}} chunks, ${{Object.keys(df).length}} terms, ${{DIM}}-d vector space.`);

}})(window);
"""

with open(os.path.join(PORTFOLIO_DIR, "rag-engine.js"), "w", encoding="utf-8") as f:
    f.write(rag_engine_code)

print("Generated rag-engine.js successfully")

# 4. Generate projects.html (The Catalog of all 39 projects)
projects_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Projects Catalog // Advaith Narayana Sarva — 39 Verified Systems</title>
  <meta name="description" content="Complete catalog of 39 AI Agent, NLP, RAG, ML, and Systems from Scratch projects built and verified by Advaith Narayana Sarva.">
  <link rel="stylesheet" href="style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Manrope:wght@600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
  <style>
    .catalog-header {
      padding: 40px 0 20px 0;
      border-bottom: 3px solid var(--border-color);
      margin-bottom: 30px;
    }
    .catalog-controls {
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 24px;
    }
    .filter-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    .filter-pill {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 6px 12px;
      border: 2px solid var(--border-color);
      background: var(--bg-surface);
      cursor: pointer;
      box-shadow: 2px 2px 0px var(--shadow-color);
      transition: transform 0.1s, box-shadow 0.1s;
    }
    .filter-pill:hover, .filter-pill.active {
      background: var(--color-gold);
      transform: translate(-1px, -1px);
      box-shadow: 3px 3px 0px var(--shadow-color);
    }
    .search-input {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 0.85rem;
      padding: 8px 14px;
      border: 2px solid var(--border-color);
      background: var(--bg-card);
      color: var(--text-main);
      width: 280px;
      box-shadow: 3px 3px 0px var(--shadow-color);
    }
    .projects-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 24px;
      margin-bottom: 60px;
    }
    .project-card {
      border: 3px solid var(--border-color);
      background: var(--bg-card);
      box-shadow: 5px 5px 0px var(--shadow-color);
      display: flex;
      flex-direction: column;
      padding: 20px;
      transition: transform 0.15s, box-shadow 0.15s;
    }
    .project-card:hover {
      transform: translate(-3px, -3px);
      box-shadow: 8px 8px 0px var(--shadow-color);
    }
    .card-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }
    .card-cat {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 0.7rem;
      font-weight: 700;
      padding: 3px 8px;
      background: var(--color-blueprint);
      color: #FFF;
      border: 1px solid var(--border-color);
    }
    .card-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.25rem;
      font-weight: 700;
      margin-bottom: 6px;
      line-height: 1.2;
    }
    .card-tagline {
      font-size: 0.82rem;
      color: var(--text-muted);
      margin-bottom: 12px;
      font-style: italic;
    }
    .card-stats {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 0.75rem;
      background: var(--bg-surface);
      border: 2px dashed var(--border-color);
      padding: 6px 10px;
      margin-bottom: 14px;
      font-weight: 600;
    }
    .card-desc {
      font-size: 0.86rem;
      line-height: 1.55;
      margin-bottom: 16px;
      flex-grow: 1;
    }
    .card-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 16px;
    }
    .card-tag {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 0.68rem;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      padding: 2px 6px;
    }
    .card-actions {
      display: flex;
      gap: 10px;
    }
  </style>
</head>
<body>
  <!-- Header Bar -->
  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-link">
        <span class="brand-feather">🪶</span>
        <span class="brand-title">ADVAITH // SYSTEMS</span>
      </a>
      <nav class="nav-links">
        <a href="index.html" class="nav-tab">HOME</a>
        <a href="projects.html" class="nav-tab active">PROJECTS (39)</a>
        <a href="resume.html" class="nav-tab">RESUME</a>
        <a href="index.html#terminal-section" class="nav-tab">TERMINAL</a>
        <a href="index.html#contact" class="nav-tab">CONTACT</a>
      </nav>
      <div class="header-controls">
        <button id="themeToggle" class="neo-btn icon-btn" title="Toggle Light/Dark Theme">
          <span class="theme-icon">🌙</span>
        </button>
      </div>
    </div>
  </header>

  <main class="page-container" style="max-width: 1300px; margin: 0 auto; padding: 20px;">
    <!-- Catalog Header -->
    <div class="catalog-header">
      <div class="badge-tag bg-blueprint text-white">SYSTEMS ARCHIVE // 39 REPOSITORIES</div>
      <h1 style="font-family:'Space Grotesk',sans-serif; font-size:2.4rem; font-weight:800; margin:12px 0 8px 0;">
        ENGINEERING PROJECTS CATALOG
      </h1>
      <p style="font-size:1.05rem; opacity:0.9; max-width:850px; line-height:1.6;">
        "I build systems, then prove they work." 39 verified projects spanning AI Agents, NLP, Graph-RAG, Machine Learning, and Systems Written from Scratch. Every project includes real benchmarks, automated tests, and honest limitations.
      </p>
    </div>

    <!-- Filters & Search -->
    <div class="catalog-controls">
      <div class="filter-pills" id="filterPills">
        <button class="filter-pill active" data-cat="All">ALL (39)</button>
        <button class="filter-pill" data-cat="Hackathon">HACKATHON (1)</button>
        <button class="filter-pill" data-cat="AI Agents">AI AGENTS (9)</button>
        <button class="filter-pill" data-cat="NLP & RAG">NLP & RAG (8)</button>
        <button class="filter-pill" data-cat="ML & Data">ML & DATA (5)</button>
        <button class="filter-pill" data-cat="Systems from Scratch">SYSTEMS (6)</button>
        <button class="filter-pill" data-cat="Full-Stack">FULL-STACK (6)</button>
        <button class="filter-pill" data-cat="In Progress">IN PROGRESS (4)</button>
      </div>
      <div>
        <input type="text" id="projectSearch" class="search-input" placeholder="Search by name, tag, or metric..." autocomplete="off">
      </div>
    </div>

    <!-- Grid -->
    <div class="projects-grid" id="projectsGrid">
      <!-- Injected by script -->
    </div>
  </main>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-left">
        <span class="footer-stamp">© 2026 ADVAITH NARAYANA SARVA</span>
        <span class="footer-sub">39 Verified Engineering Repositories</span>
      </div>
      <div class="footer-center">
        <a href="index.html">HOME</a> · 
        <a href="projects.html" style="font-weight:700;">PROJECTS (39)</a> · 
        <a href="resume.html">RESUME</a> · 
        <a href="index.html#terminal-section">TERMINAL</a> · 
        <a href="index.html#contact">CONTACT</a>
      </div>
      <div class="footer-right">
        <span class="time-clock" id="liveClock">UTC+00:00</span>
        <div class="footer-icons">
          <a href="https://github.com/advaithsarva" target="_blank" rel="noreferrer" title="GitHub">GH</a>
          <a href="https://www.linkedin.com/in/sarvaadvaithnarayana/" target="_blank" rel="noreferrer" title="LinkedIn">IN</a>
          <a href="https://instagram.com/advaithsarva" target="_blank" rel="noreferrer" title="Instagram">IG</a>
          <a href="mailto:advaithsarva@gmail.com" title="Email">EM</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="projects-data.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      // Theme
      const toggleBtn = document.getElementById('themeToggle');
      const html = document.documentElement;
      const savedTheme = localStorage.getItem('zer0-theme') || 'light';
      html.setAttribute('data-theme', savedTheme);
      updateThemeIcon(savedTheme);

      toggleBtn.addEventListener('click', () => {
        const current = html.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        html.setAttribute('data-theme', next);
        localStorage.setItem('zer0-theme', next);
        updateThemeIcon(next);
      });

      function updateThemeIcon(theme) {
        const icon = document.querySelector('.theme-icon');
        if (icon) icon.textContent = theme === 'dark' ? '☀️' : '🌙';
      }

      // Live Clock
      function updateClock() {
        const clock = document.getElementById('liveClock');
        if (clock) {
          const now = new Date();
          clock.textContent = now.toUTCString().split(' ')[4] + ' UTC';
        }
      }
      updateClock();
      setInterval(updateClock, 1000);

      // Render Projects
      const grid = document.getElementById('projectsGrid');
      const pills = document.querySelectorAll('.filter-pill');
      const searchInput = document.getElementById('projectSearch');
      let currentCat = 'All';
      let searchQuery = '';

      function render() {
        grid.innerHTML = '';
        const filtered = window.ALL_PROJECTS.filter(p => {
          const matchCat = (currentCat === 'All' || p.category === currentCat);
          const q = searchQuery.toLowerCase();
          const matchSearch = !q || 
            p.title.toLowerCase().includes(q) || 
            p.tagline.toLowerCase().includes(q) || 
            p.overview.toLowerCase().includes(q) || 
            p.tags.some(t => t.toLowerCase().includes(q)) || 
            p.stats.toLowerCase().includes(q);
          return matchCat && matchSearch;
        });

        if (filtered.length === 0) {
          grid.innerHTML = '<div style="grid-column: 1/-1; padding: 40px; text-align: center; border: 2px dashed var(--border-color); font-family: monospace;">No projects match your filter. Try adjusting keywords or category.</div>';
          return;
        }

        filtered.forEach(p => {
          const card = document.createElement('div');
          card.className = 'project-card';
          
          let repoBtn = '';
          if (p.links && p.links.startsWith('http')) {
            repoBtn = `<a href="${p.links}" target="_blank" class="neo-btn btn-secondary" style="padding:6px 12px; font-size:0.75rem;">GITHUB ↗</a>`;
          } else {
            repoBtn = `<span style="font-family:'IBM Plex Mono',monospace; font-size:0.7rem; padding:6px 10px; background:var(--bg-surface); border:1px solid var(--border-color); color:var(--text-muted);">PRIVATE REPO</span>`;
          }

          card.innerHTML = `
            <div class="card-meta">
              <span class="card-cat">${p.category}</span>
              <span style="font-family:'IBM Plex Mono',monospace; font-size:0.75rem; font-weight:700;">#${p.slug}</span>
            </div>
            <h3 class="card-title">${p.title}</h3>
            <div class="card-tagline">"${p.tagline}"</div>
            <div class="card-stats">⚡ ${p.stats}</div>
            <p class="card-desc">${p.card || p.overview}</p>
            <div class="card-tags">
              ${p.tags.map(t => `<span class="card-tag">${t}</span>`).join('')}
            </div>
            <div class="card-actions">
              <a href="project.html?id=${p.slug}" class="neo-btn btn-primary" style="padding:6px 14px; font-size:0.78rem;">DEEP DIVE →</a>
              ${repoBtn}
            </div>
          `;
          grid.appendChild(card);
        });
      }

      pills.forEach(pill => {
        pill.addEventListener('click', () => {
          pills.forEach(p => p.classList.remove('active'));
          pill.classList.add('active');
          currentCat = pill.getAttribute('data-cat');
          render();
        });
      });

      searchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value.trim();
        render();
      });

      render();
    });
  </script>
</body>
</html>
"""

with open(os.path.join(PORTFOLIO_DIR, "projects.html"), "w", encoding="utf-8") as f:
    f.write(projects_html)

print("Generated projects.html successfully")

# 5. Generate project.html (The Universal Deep-Dive Template)
project_detail_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title id="pageTitle">Project Deep Dive // Advaith Narayana Sarva</title>
  <link rel="stylesheet" href="style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Manrope:wght@600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
  <style>
    .project-header-box {
      border: 3px solid var(--border-color);
      background: var(--bg-card);
      padding: 36px;
      box-shadow: 6px 6px 0px var(--shadow-color);
      margin: 30px 0;
    }
    .breadcrumbs {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 0.8rem;
      margin-bottom: 16px;
      color: var(--text-muted);
    }
    .breadcrumbs a {
      color: var(--color-blueprint);
      text-decoration: underline;
    }
    .stats-strip {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin: 24px 0;
    }
    .stat-tile {
      border: 2px solid var(--border-color);
      background: var(--bg-surface);
      padding: 14px 18px;
      box-shadow: 3px 3px 0px var(--shadow-color);
    }
    .stat-tile-val {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--color-blueprint);
    }
    .stat-tile-label {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      margin-top: 4px;
    }
    .detail-section {
      border: 3px solid var(--border-color);
      background: var(--bg-card);
      padding: 28px;
      box-shadow: 5px 5px 0px var(--shadow-color);
      margin-bottom: 24px;
    }
    .detail-section h2 {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.4rem;
      font-weight: 800;
      margin-bottom: 14px;
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 8px;
    }
    .highlight-list {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    .highlight-list li {
      position: relative;
      padding-left: 26px;
      margin-bottom: 12px;
      line-height: 1.6;
      font-size: 0.95rem;
    }
    .highlight-list li::before {
      content: '✔';
      position: absolute;
      left: 0;
      color: var(--color-moss);
      font-weight: 800;
    }
    .honest-box {
      border: 2px solid var(--color-gold);
      background: #FFFBEB;
      padding: 18px;
      border-left: 8px solid var(--color-gold);
      margin-top: 16px;
    }
    [data-theme="dark"] .honest-box {
      background: #242217;
    }
    .nav-pager {
      display: flex;
      justify-content: space-between;
      gap: 16px;
      margin: 40px 0;
    }
  </style>
</head>
<body>
  <!-- Header Bar -->
  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-link">
        <span class="brand-feather">🪶</span>
        <span class="brand-title">ADVAITH // SYSTEMS</span>
      </a>
      <nav class="nav-links">
        <a href="index.html" class="nav-tab">HOME</a>
        <a href="projects.html" class="nav-tab">PROJECTS (39)</a>
        <a href="resume.html" class="nav-tab">RESUME</a>
        <a href="index.html#terminal-section" class="nav-tab">TERMINAL</a>
        <a href="index.html#contact" class="nav-tab">CONTACT</a>
      </nav>
      <div class="header-controls">
        <button id="themeToggle" class="neo-btn icon-btn" title="Toggle Light/Dark Theme">
          <span class="theme-icon">🌙</span>
        </button>
      </div>
    </div>
  </header>

  <main class="page-container" style="max-width: 1000px; margin: 0 auto; padding: 20px;">
    <!-- Breadcrumbs -->
    <div class="breadcrumbs">
      <a href="index.html">HOME</a> / <a href="projects.html">PROJECTS</a> / <span id="breadCrumbCurrent">PROJECT_ID</span>
    </div>

    <!-- Project Hero Header -->
    <div class="project-header-box" id="projectHero">
      <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:12px;">
        <span class="badge-tag bg-blueprint text-white" id="projCat">CATEGORY</span>
        <div id="projLinkBox"></div>
      </div>
      <h1 id="projTitle" style="font-family:'Space Grotesk',sans-serif; font-size:2.4rem; font-weight:800; margin:16px 0 8px 0;">PROJECT TITLE</h1>
      <p id="projTagline" style="font-size:1.15rem; font-style:italic; opacity:0.9; margin-bottom:18px;">Tagline hook goes here...</p>
      
      <!-- Stats Strip -->
      <div class="stats-strip" id="projStatsStrip"></div>

      <!-- Tags -->
      <div style="display:flex; flex-wrap:wrap; gap:8px;" id="projTags"></div>
    </div>

    <!-- Overview Section -->
    <section class="detail-section">
      <h2>01 // THE PROBLEM & THE ARCHITECTURE</h2>
      <p id="projOverview" style="font-size:1.02rem; line-height:1.7; margin-bottom:16px;">
        Overview content...
      </p>
    </section>

    <!-- Highlights Section -->
    <section class="detail-section">
      <h2>02 // VERIFIED RESULTS & WHAT I BUILT</h2>
      <ul class="highlight-list" id="projHighlights">
      </ul>
    </section>

    <!-- Google XYZ & Audit Section -->
    <section class="detail-section" id="resumeBulletsSection" style="display:none;">
      <h2>03 // GOOGLE XYZ AUDIT & CREDENTIALS</h2>
      <ul class="highlight-list" id="projResumeBullets">
      </ul>
    </section>

    <!-- Honest Note Section -->
    <section class="detail-section">
      <h2>04 // HONEST ENGINEERING LIMITATIONS</h2>
      <div class="honest-box">
        <strong style="font-family:'IBM Plex Mono',monospace; font-size:0.85rem; display:block; margin-bottom:6px;">⚠️ TRANSPARENCY & WHAT'S NEXT:</strong>
        <p id="projHonest" style="font-size:0.95rem; line-height:1.6; margin:0;"></p>
      </div>
    </section>

    <!-- Pager Navigation -->
    <div class="nav-pager">
      <a href="#" id="prevProjectBtn" class="neo-btn btn-secondary">← PREVIOUS PROJECT</a>
      <a href="projects.html" class="neo-btn btn-primary">ALL 39 PROJECTS ⊞</a>
      <a href="#" id="nextProjectBtn" class="neo-btn btn-secondary">NEXT PROJECT →</a>
    </div>
  </main>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-left">
        <span class="footer-stamp">© 2026 ADVAITH NARAYANA SARVA</span>
        <span class="footer-sub">39 Verified Engineering Repositories</span>
      </div>
      <div class="footer-center">
        <a href="index.html">HOME</a> · 
        <a href="projects.html">PROJECTS (39)</a> · 
        <a href="resume.html">RESUME</a> · 
        <a href="index.html#terminal-section">TERMINAL</a> · 
        <a href="index.html#contact">CONTACT</a>
      </div>
      <div class="footer-right">
        <span class="time-clock" id="liveClock">UTC+00:00</span>
        <div class="footer-icons">
          <a href="https://github.com/advaithsarva" target="_blank" rel="noreferrer" title="GitHub">GH</a>
          <a href="https://www.linkedin.com/in/sarvaadvaithnarayana/" target="_blank" rel="noreferrer" title="LinkedIn">IN</a>
          <a href="https://instagram.com/advaithsarva" target="_blank" rel="noreferrer" title="Instagram">IG</a>
          <a href="mailto:advaithsarva@gmail.com" title="Email">EM</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="projects-data.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      // Theme
      const toggleBtn = document.getElementById('themeToggle');
      const html = document.documentElement;
      const savedTheme = localStorage.getItem('zer0-theme') || 'light';
      html.setAttribute('data-theme', savedTheme);
      updateThemeIcon(savedTheme);

      toggleBtn.addEventListener('click', () => {
        const current = html.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        html.setAttribute('data-theme', next);
        localStorage.setItem('zer0-theme', next);
        updateThemeIcon(next);
      });

      function updateThemeIcon(theme) {
        const icon = document.querySelector('.theme-icon');
        if (icon) icon.textContent = theme === 'dark' ? '☀️' : '🌙';
      }

      // Live Clock
      function updateClock() {
        const clock = document.getElementById('liveClock');
        if (clock) {
          const now = new Date();
          clock.textContent = now.toUTCString().split(' ')[4] + ' UTC';
        }
      }
      updateClock();
      setInterval(updateClock, 1000);

      // Parse slug from URL parameter ?id=<slug>
      const params = new URLSearchParams(window.location.search);
      let slug = params.get('id') || 'the-sentinel-grid';

      let currentIdx = window.ALL_PROJECTS.findIndex(p => p.slug === slug);
      if (currentIdx === -1) currentIdx = 0;
      const proj = window.ALL_PROJECTS[currentIdx];

      // Set Document Title
      document.title = `${proj.title} // Advaith Narayana Sarva`;
      document.getElementById('breadCrumbCurrent').textContent = proj.title.toUpperCase();

      // Populate Hero
      document.getElementById('projCat').textContent = proj.category.toUpperCase();
      document.getElementById('projTitle').textContent = proj.title;
      document.getElementById('projTagline').textContent = `"${proj.tagline}"`;

      // Repo link
      const linkBox = document.getElementById('projLinkBox');
      if (proj.links && proj.links.startsWith('http')) {
        linkBox.innerHTML = `<a href="${proj.links}" target="_blank" class="neo-btn btn-primary" style="padding:8px 16px;">VIEW ON GITHUB ↗</a>`;
      } else {
        linkBox.innerHTML = `<span style="font-family:'IBM Plex Mono',monospace; font-size:0.75rem; padding:8px 14px; background:var(--bg-surface); border:2px solid var(--border-color); font-weight:700;">PRIVATE REPOSITORY</span>`;
      }

      // Stats
      const statsStrip = document.getElementById('projStatsStrip');
      const statParts = proj.stats.split('·');
      statsStrip.innerHTML = statParts.map(s => {
        return `<div class="stat-tile">
          <div class="stat-tile-val">⚡</div>
          <div class="stat-tile-label">${s.trim()}</div>
        </div>`;
      }).join('');

      // Tags
      const tagsBox = document.getElementById('projTags');
      tagsBox.innerHTML = proj.tags.map(t => `<span class="badge-tag" style="background:var(--bg-surface);">${t}</span>`).join('');

      // Overview
      document.getElementById('projOverview').textContent = proj.overview;

      // Highlights
      const hlBox = document.getElementById('projHighlights');
      hlBox.innerHTML = proj.highlights.map(h => `<li>${h}</li>`).join('');

      // Resume Bullets if available
      if (proj.resume_bullets && proj.resume_bullets.length > 0) {
        const rbSec = document.getElementById('resumeBulletsSection');
        const rbBox = document.getElementById('projResumeBullets');
        rbBox.innerHTML = proj.resume_bullets.map(b => `<li>${b}</li>`).join('');
        rbSec.style.display = 'block';
      }

      // Honest Note
      document.getElementById('projHonest').textContent = proj.honest;

      // Pager
      const prevIdx = (currentIdx - 1 + window.ALL_PROJECTS.length) % window.ALL_PROJECTS.length;
      const nextIdx = (currentIdx + 1) % window.ALL_PROJECTS.length;
      document.getElementById('prevProjectBtn').href = `project.html?id=${window.ALL_PROJECTS[prevIdx].slug}`;
      document.getElementById('prevProjectBtn').textContent = `← ${window.ALL_PROJECTS[prevIdx].title}`;
      document.getElementById('nextProjectBtn').href = `project.html?id=${window.ALL_PROJECTS[nextIdx].slug}`;
      document.getElementById('nextProjectBtn').textContent = `${window.ALL_PROJECTS[nextIdx].title} →`;
    });
  </script>
</body>
</html>
"""

with open(os.path.join(PORTFOLIO_DIR, "project.html"), "w", encoding="utf-8") as f:
    f.write(project_detail_html)

print("Generated project.html successfully")

# 6. Generate Static HTML Pages for all 39 projects in projects/<slug>.html
for idx, p in enumerate(projects):
    prev_p = projects[(idx - 1 + len(projects)) % len(projects)]
    next_p = projects[(idx + 1) % len(projects)]
    
    stat_tiles = "".join([f'<div class="stat-tile"><div class="stat-tile-val">⚡</div><div class="stat-tile-label">{s.strip()}</div></div>' for s in p["stats"].split("·")])
    tag_spans = "".join([f'<span class="badge-tag" style="background:var(--bg-surface);">{t}</span>' for t in p["tags"]])
    hl_lis = "".join([f'<li>{h}</li>' for h in p["highlights"]])
    
    repo_btn = ""
    if p["links"] and p["links"].startswith("http"):
        repo_btn = f'<a href="{p["links"]}" target="_blank" class="neo-btn btn-primary" style="padding:8px 16px;">VIEW ON GITHUB ↗</a>'
    else:
        repo_btn = '<span style="font-family:\'IBM Plex Mono\',monospace; font-size:0.75rem; padding:8px 14px; background:var(--bg-surface); border:2px solid var(--border-color); font-weight:700;">PRIVATE REPOSITORY</span>'

    rb_sec = ""
    if p.get("resume_bullets") and len(p["resume_bullets"]) > 0:
        rb_lis = "".join([f'<li>{b}</li>' for b in p["resume_bullets"]])
        rb_sec = f"""
        <section class="detail-section">
          <h2>03 // GOOGLE XYZ AUDIT & CREDENTIALS</h2>
          <ul class="highlight-list">
            {rb_lis}
          </ul>
        </section>
        """

    static_page = f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{p["title"]} // Advaith Narayana Sarva</title>
  <meta name="description" content="{p["tagline"]} {p["overview"][:150]}">
  <link rel="stylesheet" href="../style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Manrope:wght@600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
  <style>
    .project-header-box {{
      border: 3px solid var(--border-color);
      background: var(--bg-card);
      padding: 36px;
      box-shadow: 6px 6px 0px var(--shadow-color);
      margin: 30px 0;
    }}
    .breadcrumbs {{
      font-family: 'IBM Plex Mono', monospace;
      font-size: 0.8rem;
      margin-bottom: 16px;
      color: var(--text-muted);
    }}
    .breadcrumbs a {{
      color: var(--color-blueprint);
      text-decoration: underline;
    }}
    .stats-strip {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin: 24px 0;
    }}
    .stat-tile {{
      border: 2px solid var(--border-color);
      background: var(--bg-surface);
      padding: 14px 18px;
      box-shadow: 3px 3px 0px var(--shadow-color);
    }}
    .stat-tile-val {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--color-blueprint);
    }}
    .stat-tile-label {{
      font-family: 'IBM Plex Mono', monospace;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      margin-top: 4px;
    }}
    .detail-section {{
      border: 3px solid var(--border-color);
      background: var(--bg-card);
      padding: 28px;
      box-shadow: 5px 5px 0px var(--shadow-color);
      margin-bottom: 24px;
    }}
    .detail-section h2 {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.4rem;
      font-weight: 800;
      margin-bottom: 14px;
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 8px;
    }}
    .highlight-list {{
      list-style: none;
      padding: 0;
      margin: 0;
    }}
    .highlight-list li {{
      position: relative;
      padding-left: 26px;
      margin-bottom: 12px;
      line-height: 1.6;
      font-size: 0.95rem;
    }}
    .highlight-list li::before {{
      content: '✔';
      position: absolute;
      left: 0;
      color: var(--color-moss);
      font-weight: 800;
    }}
    .honest-box {{
      border: 2px solid var(--color-gold);
      background: #FFFBEB;
      padding: 18px;
      border-left: 8px solid var(--color-gold);
      margin-top: 16px;
    }}
    [data-theme="dark"] .honest-box {{
      background: #242217;
    }}
    .nav-pager {{
      display: flex;
      justify-content: space-between;
      gap: 16px;
      margin: 40px 0;
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a href="../index.html" class="brand-link">
        <span class="brand-feather">🪶</span>
        <span class="brand-title">ADVAITH // SYSTEMS</span>
      </a>
      <nav class="nav-links">
        <a href="../index.html" class="nav-tab">HOME</a>
        <a href="../projects.html" class="nav-tab">PROJECTS (39)</a>
        <a href="../resume.html" class="nav-tab">RESUME</a>
        <a href="../index.html#terminal-section" class="nav-tab">TERMINAL</a>
        <a href="../index.html#contact" class="nav-tab">CONTACT</a>
      </nav>
      <div class="header-controls">
        <button id="themeToggle" class="neo-btn icon-btn" title="Toggle Light/Dark Theme">
          <span class="theme-icon">🌙</span>
        </button>
      </div>
    </div>
  </header>

  <main class="page-container" style="max-width: 1000px; margin: 0 auto; padding: 20px;">
    <div class="breadcrumbs">
      <a href="../index.html">HOME</a> / <a href="../projects.html">PROJECTS</a> / <span>{p["title"].upper()}</span>
    </div>

    <div class="project-header-box">
      <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:12px;">
        <span class="badge-tag bg-blueprint text-white">{p["category"].upper()}</span>
        <div>{repo_btn}</div>
      </div>
      <h1 style="font-family:'Space Grotesk',sans-serif; font-size:2.4rem; font-weight:800; margin:16px 0 8px 0;">{p["title"]}</h1>
      <p style="font-size:1.15rem; font-style:italic; opacity:0.9; margin-bottom:18px;">"{p["tagline"]}"</p>
      
      <div class="stats-strip">{stat_tiles}</div>
      <div style="display:flex; flex-wrap:wrap; gap:8px;">{tag_spans}</div>
    </div>

    <section class="detail-section">
      <h2>01 // THE PROBLEM & THE ARCHITECTURE</h2>
      <p style="font-size:1.02rem; line-height:1.7; margin-bottom:16px;">
        {p["overview"]}
      </p>
    </section>

    <section class="detail-section">
      <h2>02 // VERIFIED RESULTS & WHAT I BUILT</h2>
      <ul class="highlight-list">
        {hl_lis}
      </ul>
    </section>

    {rb_sec}

    <section class="detail-section">
      <h2>04 // HONEST ENGINEERING LIMITATIONS</h2>
      <div class="honest-box">
        <strong style="font-family:'IBM Plex Mono',monospace; font-size:0.85rem; display:block; margin-bottom:6px;">⚠️ TRANSPARENCY & WHAT'S NEXT:</strong>
        <p style="font-size:0.95rem; line-height:1.6; margin:0;">{p["honest"]}</p>
      </div>
    </section>

    <div class="nav-pager">
      <a href="{prev_p['slug']}.html" class="neo-btn btn-secondary">← {prev_p["title"]}</a>
      <a href="../projects.html" class="neo-btn btn-primary">ALL 39 PROJECTS ⊞</a>
      <a href="{next_p['slug']}.html" class="neo-btn btn-secondary">{next_p["title"]} →</a>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-left">
        <span class="footer-stamp">© 2026 ADVAITH NARAYANA SARVA</span>
        <span class="footer-sub">39 Verified Engineering Repositories</span>
      </div>
      <div class="footer-center">
        <a href="../index.html">HOME</a> · 
        <a href="../projects.html">PROJECTS (39)</a> · 
        <a href="../resume.html">RESUME</a> · 
        <a href="../index.html#terminal-section">TERMINAL</a> · 
        <a href="../index.html#contact">CONTACT</a>
      </div>
      <div class="footer-right">
        <span class="time-clock" id="liveClock">UTC+00:00</span>
        <div class="footer-icons">
          <a href="https://github.com/advaithsarva" target="_blank" rel="noreferrer" title="GitHub">GH</a>
          <a href="https://www.linkedin.com/in/sarvaadvaithnarayana/" target="_blank" rel="noreferrer" title="LinkedIn">IN</a>
          <a href="https://instagram.com/advaithsarva" target="_blank" rel="noreferrer" title="Instagram">IG</a>
          <a href="mailto:advaithsarva@gmail.com" title="Email">EM</a>
        </div>
      </div>
    </div>
  </footer>

  <script>
    const toggleBtn = document.getElementById('themeToggle');
    const html = document.documentElement;
    const savedTheme = localStorage.getItem('zer0-theme') || 'light';
    html.setAttribute('data-theme', savedTheme);
    if (toggleBtn) {{
      toggleBtn.querySelector('.theme-icon').textContent = savedTheme === 'dark' ? '☀️' : '🌙';
      toggleBtn.addEventListener('click', () => {{
        const next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        html.setAttribute('data-theme', next);
        localStorage.setItem('zer0-theme', next);
        toggleBtn.querySelector('.theme-icon').textContent = next === 'dark' ? '☀️' : '🌙';
      }});
    }}
    const clock = document.getElementById('liveClock');
    if (clock) {{
      function tick() {{ clock.textContent = new Date().toUTCString().split(' ')[4] + ' UTC'; }}
      tick();
      setInterval(tick, 1000);
    }}
  </script>
</body>
</html>
"""
    with open(os.path.join(PROJECTS_DIR, f"{p['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(static_page)

print(f"Generated {len(projects)} static project pages in projects/ directory")

import subprocess
print("Calling update_all_skills_and_netlify.py to ensure all SVGs and Netlify settings are synchronized...")
subprocess.run(["python", os.path.join(PORTFOLIO_DIR, "update_all_skills_and_netlify.py")], check=True)

