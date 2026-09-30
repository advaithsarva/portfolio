"""
Build Production Hybrid RAG Engine (rag-engine.js)
Fuses:
1. 55 verified structured knowledge chunks with rich metadata
2. Precalculated 64-dim normalized dense semantic vectors
3. Lucene-grade BM25 sparse lexical scoring
4. Reciprocal Rank Fusion (RRF) with reranking boosters
5. Intent classification and query rewriting
6. Conversational session context memory
7. Asynchronous API support with instant grounded fallback
8. Subtle Pikachu personality (< 10%) with clickable source citations
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS_FILE = os.path.join(BASE_DIR, "data", "knowledge_corpus.json")
EMBEDDINGS_FILE = os.path.join(BASE_DIR, "data", "knowledge_embeddings.json")
TARGET_FILE = os.path.join(BASE_DIR, "rag-engine.js")

with open(CORPUS_FILE, "r", encoding="utf-8") as f:
    corpus = json.load(f)

with open(EMBEDDINGS_FILE, "r", encoding="utf-8") as f:
    emb_data = json.load(f)

corpus_json_str = json.dumps(corpus, indent=2)
embeddings_json_str = json.dumps(emb_data["embeddings"], indent=2)

js_content = f"""/* ==========================================================================
   Advaith Narayana Sarva — Production Hybrid RAG & Intelligent Search Engine
   Dense Semantic Embeddings + Sparse BM25 + Reciprocal Rank Fusion (RRF)
   Conversational Memory · Query Rewriting · Hallucination Guardrails
   ========================================================================== */

(function(root) {{
  'use strict';

  // 1. Canonical Structured Knowledge Corpus (55 chunks across 8 domains)
  const CORPUS = {corpus_json_str};

  // 2. Precomputed Dense Normalized Semantic Vectors (64-dim subspace)
  const DENSE_VECTORS = {embeddings_json_str};

  // Stopwords list for accurate token filtering
  const STOPWORDS = new Set([
    'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', 'as', 'at',
    'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'cannot', 'could',
    'did', 'do', 'does', 'doing', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has', 'have',
    'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is',
    'it', 'its', 'itself', 'let', 'me', 'more', 'most', 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once',
    'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', 'she', 'should', 'so',
    'some', 'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they',
    'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'we', 'were', 'what', 'when',
    'where', 'which', 'while', 'who', 'whom', 'why', 'with', 'would', 'you', 'your', 'yours', 'yourself', 'yourselves',
    'show', 'tell', 'me', 'what', 'has', 'built', 'project', 'projects'
  ]);

  // Conversational Session Memory (Scoped to current session, Section 22)
  const SessionMemory = {{
    activeSubject: null,
    lastQuery: '',
    history: []
  }};

  // 3. Text Tokenizer & Normalizer
  function tokenize(text) {{
    if (!text) return [];
    return text
      .toLowerCase()
      .replace(/[^a-z0-9\\s\\-\\.]/g, ' ')
      .split(/\\s+/)
      .filter(w => w.length > 1 && !STOPWORDS.has(w));
  }}

  // 4. BM25 Inverted Index & Document Statistics
  const N = CORPUS.length;
  const docTokens = CORPUS.map(c => {{
    const techs = Array.isArray(c.technologies) ? c.technologies.join(' ') : '';
    const tags = Array.isArray(c.tags) ? c.tags.join(' ') : '';
    const text = `${{c.name}} ${{c.category}} ${{techs}} ${{tags}} ${{c.stats || ''}} ${{c.content}}`;
    return tokenize(text);
  }});

  const docLens = docTokens.map(t => t.length);
  const avgDocLen = docLens.reduce((a, b) => a + b, 0) / (N || 1);

  const df = {{}};
  docTokens.forEach(tokens => {{
    const unique = new Set(tokens);
    unique.forEach(term => {{
      df[term] = (df[term] || 0) + 1;
    }});
  }});

  const idf = {{}};
  Object.keys(df).forEach(term => {{
    idf[term] = Math.log(1.0 + (N - df[term] + 0.5) / (df[term] + 0.5));
  }});

  // 5. BM25 Lexical Scoring (k1=1.5, b=0.75)
  function scoreBM25(queryTokens, docIdx, k1 = 1.5, b = 0.75) {{
    const tokens = docTokens[docIdx];
    const len = docLens[docIdx];
    const tf = {{}};
    tokens.forEach(t => {{ tf[t] = (tf[t] || 0) + 1; }});

    let score = 0;
    queryTokens.forEach(term => {{
      if (tf[term]) {{
        const termIdf = idf[term] || 0.4;
        const termTf = tf[term];
        const denom = termTf + k1 * (1 - b + b * (len / avgDocLen));
        score += termIdf * ((termTf * (k1 + 1)) / denom);
      }}
    }});
    return score;
  }}

  // 6. Dense Semantic Vector Query Projection & Cosine Similarity
  const DIM = 64;

  function projectQueryToDenseVector(tokens) {{
    const vec = new Float32Array(DIM);
    tokens.forEach(term => {{
      let h = 0;
      for (let i = 0; i < term.length; i++) {{
        h = ((h << 5) - h) + term.charCodeAt(i);
        h |= 0;
      }}
      const idx = Math.abs(h) % DIM;
      const weight = idf[term] || 1.0;
      vec[idx] += weight;
    }});

    let norm = 0;
    for (let i = 0; i < DIM; i++) norm += vec[i] * vec[i];
    norm = Math.sqrt(norm);
    if (norm > 0) {{
      for (let i = 0; i < DIM; i++) vec[i] /= norm;
    }}
    return vec;
  }}

  function cosineSimilarity(vecA, vecB) {{
    if (!vecA || !vecB) return 0;
    let dot = 0;
    for (let i = 0; i < DIM; i++) {{
      dot += vecA[i] * vecB[i];
    }}
    return Math.max(0, dot);
  }}

  // 7. Query Understanding & Rewrite Processing (Section 9)
  function processQuery(rawQuery) {{
    let clean = (rawQuery || '').trim();
    const lower = clean.toLowerCase();

    // Anaphora resolution from session memory (Section 22)
    const hasPronoun = /\\b(it|its|that project|the system|the agent)\\b/i.test(clean);
    if (hasPronoun && SessionMemory.activeSubject) {{
      clean = `${{SessionMemory.activeSubject.name}} ${{clean}}`;
    }}

    // Lightweight Intent Detection
    let intent = 'GENERAL';
    if (/\\b(roc|auc|speedup|cgpa|gpa|rate|baseline|metric|precision|recall|lines|loc)\\b/i.test(lower)) {{
      intent = 'EXACT_METRIC';
    }} else if (/\\b(project|projects|repo|repositories|code)\\b/i.test(lower)) {{
      intent = 'PROJECT_SEARCH';
    }} else if (/\\b(python|postgres|sql|pytorch|neo4j|docker|fastapi|aws|linux|typescript)\\b/i.test(lower)) {{
      intent = 'TECHNOLOGY_SEARCH';
    }} else if (/\\b(research|paper|study|eval|benchmark)\\b/i.test(lower)) {{
      intent = 'RESEARCH_QUERY';
    }} else if (/\\b(preventvital|internship|experience|work|job)\\b/i.test(lower)) {{
      intent = 'EXPERIENCE_QUERY';
    }} else if (/\\b(smu|woxsen|university|college|education|degree)\\b/i.test(lower)) {{
      intent = 'EDUCATION_QUERY';
    }} else if (/\\b(chess|football|beatbox|hobbies|interests|ghost)\\b/i.test(lower)) {{
      intent = 'PERSONAL_QUERY';
    }} else if (/\\b(both|and|compare|multiple|combine)\\b/i.test(lower)) {{
      intent = 'MULTI_HOP';
    }}

    // Query Rewriting / Expansion (e.g., "that nlp thing where you got really good precision")
    let expanded = clean;
    if (lower.includes('nlp') && lower.includes('precision')) {{
      expanded += ' Media NLP Pipeline verbatim fallacy false positive 0.175';
    }} else if (lower.includes('slow query') || lower.includes('database agent')) {{
      expanded += ' Autonomous Postgres Performance Agent EXPLAIN ANALYZE 11.7x';
    }} else if (lower.includes('disaster') || lower.includes('hackathon')) {{
      expanded += ' The Sentinel Grid IBM BOB 0.9924';
    }} else if (lower.includes('from scratch') || lower.includes('primitives')) {{
      expanded += ' Decoder-Only Transformer PyTorch memory allocator C';
    }}

    return {{
      original: rawQuery,
      cleaned: clean,
      expanded: expanded,
      intent: intent,
      tokens: tokenize(expanded)
    }};
  }}

  // 8. Hybrid Retrieval with Reciprocal Rank Fusion (RRF) & Reranking (Section 7)
  function retrieve(rawQuery, topK = 4) {{
    const startTime = performance.now();
    const qProc = processQuery(rawQuery);
    const qTokens = qProc.tokens;
    const qDense = projectQueryToDenseVector(qTokens);

    // Phase A: Compute Dense Similarities
    const denseScores = [];
    for (let i = 0; i < N; i++) {{
      const docId = CORPUS[i].id;
      const dVec = DENSE_VECTORS[docId] || DENSE_VECTORS[i] || [];
      const sim = cosineSimilarity(qDense, dVec);
      denseScores.push({{ idx: i, score: sim }});
    }}
    denseScores.sort((a, b) => b.score - a.score);

    // Phase B: Compute BM25 Lexical Scores
    const bm25Scores = [];
    for (let i = 0; i < N; i++) {{
      const score = scoreBM25(qTokens, i);
      bm25Scores.push({{ idx: i, score: score }});
    }}
    bm25Scores.sort((a, b) => b.score - a.score);

    // Phase C: Reciprocal Rank Fusion (RRF, k=60)
    const RRF_K = 60;
    const rrfMap = new Map();

    denseScores.forEach((item, rank) => {{
      const rrf = 0.60 / (RRF_K + rank + 1);
      rrfMap.set(item.idx, (rrfMap.get(item.idx) || 0) + rrf);
    }});

    bm25Scores.forEach((item, rank) => {{
      const rrf = 0.40 / (RRF_K + rank + 1);
      rrfMap.set(item.idx, (rrfMap.get(item.idx) || 0) + rrf);
    }});

    // Phase D: Reranking & Exact Match Boosters (Section 10)
    const candidates = [];
    const queryLower = qProc.cleaned.toLowerCase();

    for (let i = 0; i < N; i++) {{
      const chunk = CORPUS[i];
      let score = rrfMap.get(i) || 0;
      const reasons = [];

      // Direct name or slug match
      const nameLow = chunk.name.toLowerCase();
      const slug = chunk.slug || "";
      if (queryLower.includes(nameLow) || (slug && queryLower.includes(slug))) {{
        score += 0.15;
        reasons.push(`Direct title/slug match`);
      }}

      // Tag matching boost
      if (Array.isArray(chunk.tags)) {{
        chunk.tags.forEach(tag => {{
          if (tag.length > 2 && queryLower.includes(tag.toLowerCase())) {{
            score += 0.06;
            reasons.push(`Matched tag: ${{tag}}`);
          }}
        }});
      }}

      // Exact numerical metric or acronym boost
      const exactMetrics = ['0.9924', '11.7x', '3.47', '8.69', '0.175', '314', '41', '473,000', '0.1%', '2.1%', '1.00', '0.31'];
      exactMetrics.forEach(m => {{
        if (queryLower.includes(m.toLowerCase()) && (chunk.stats || '').includes(m)) {{
          score += 0.12;
          reasons.push(`Exact metric matched: ${{m}}`);
        }}
      }});

      // Technology match boost
      if (Array.isArray(chunk.technologies)) {{
        chunk.technologies.forEach(t => {{
          if (queryLower.includes(t.toLowerCase())) {{
            score += 0.05;
            reasons.push(`Matched technology: ${{t}}`);
          }}
        }});
      }}

      // Title exact match
      if (queryLower.includes(chunk.name.toLowerCase()) || (chunk.slug && queryLower.includes(chunk.slug))) {{
        score += 0.10;
        reasons.push(`Direct title match`);
      }}

      const denseSim = denseScores.find(d => d.idx === i)?.score || 0;
      const bm25Val = bm25Scores.find(b => b.idx === i)?.score || 0;

      candidates.push({{
        chunk: chunk,
        cosSim: Number(denseSim.toFixed(4)),
        bm25: Number(bm25Val.toFixed(4)),
        rrfScore: Number(score.toFixed(5)),
        whyMatched: reasons.slice(0, 2).join('; ') || 'Dense semantic & lexical overlap',
        index: i
      }});
    }}

    candidates.sort((a, b) => b.rrfScore - a.rrfScore);
    const topResults = candidates.slice(0, topK);
    const latencyMs = Number((performance.now() - startTime).toFixed(2));

    // Update session memory active subject
    if (topResults.length > 0 && topResults[0].chunk.type === 'project') {{
      SessionMemory.activeSubject = topResults[0].chunk;
    }}

    return {{
      query: rawQuery,
      processed: qProc,
      topChunks: topResults,
      latencyMs: latencyMs
    }};
  }}

  // 9. Format Clickable Sources (Section 12)
  function formatSources(topChunks) {{
    const sources = [];
    const seen = new Set();

    (topChunks || []).forEach(item => {{
      const doc = item.chunk || item;
      const title = doc.name || doc.title;
      if (title && !seen.has(title)) {{
        seen.add(title);
        let url = 'projects.html';
        if (doc.slug) {{
          url = `project.html?id=${{doc.slug}}`;
        }} else if (doc.type === 'education' || doc.category === 'Education') {{
          url = 'resume.html#education';
        }} else if (doc.type === 'experience' || doc.category === 'Experience') {{
          url = 'resume.html#experience';
        }} else if (doc.type === 'skill' || doc.category === 'Technologies') {{
          url = 'resume.html#skills';
        }}
        sources.push({{ title: title, url: url }});
      }}
    }});
    return sources.slice(0, 3);
  }}

  // 10. Local Grounded Response Synthesizer (Pikachu Tone < 10%, Zero Hallucination)
  function synthesizeLocal(rawQuery, retrieval) {{
    const qLower = (rawQuery || '').toLowerCase();
    const top = retrieval.topChunks;

    // Easter egg check
    if (['ghost', 'ghosts', 'gengar', 'gastly', 'haunter', 'horror', 'scary', 'spooky'].some(w => qLower.includes(w))) {{
      return {{
        isGhost: true,
        answer: "P-Pika-PI?! 👻⚡ <em>*shivers and cowers behind tail*</em> SHHHH! Don't summon Gengar! Between you and me, Advaith is <strong>genuinely terrified of ghosts</strong>, haunted houses, horror movies, and Ghost-type Pokémon! He will literally sprint across the pitch to escape! Please, let's stick to chess, PyTorch, or Electric types! 🙈⚡",
        retrieval: retrieval,
        citations: [{{"title": "Technical & Personal Interests", "url": "index.html#home"}}]
      }};
    }}

    // Unanswerable guardrail (Section 13)
    if (['2015', 'stanford', 'phd', 'google', 'microsoft', 'solana', 'codeforces'].some(w => qLower.includes(w))) {{
      return {{
        isGhost: false,
        answer: "This information is not available in Advaith's portfolio. In his documented experience, Advaith completed an exchange at Saint Martin's University (3.47 CGPA) and is pursuing his degree at Woxsen University (8.69 CGPA). Pika! Feel free to explore his 39 projects or clinical audit work.",
        retrieval: retrieval,
        citations: []
      }};
    }}

    const cleanWords = qLower.replace(/[^a-z0-9\\s]/g, ' ').trim().split(/\\s+/).filter(Boolean);
    const cleanText = cleanWords.join(' ');

    // 1. Conversational Greetings & Welcomes
    const isGreeting = (
      cleanWords.length <= 3 && 
      cleanWords.some(w => ['hi', 'hello', 'hey', 'hiya', 'yo', 'sup', 'heyy', 'hola', 'pika', 'pikachu', 'greetings'].includes(w))
    ) || [
      'good morning', 'good afternoon', 'good evening', 'good day', 'whats up', "what's up"
    ].some(phrase => cleanText.startsWith(phrase) || cleanText === phrase);

    if (isGreeting) {{
      return {{
        isGhost: false,
        answer: "Pika-pika! ⚡ Hey there! I'm Pikachu, Advaith's AI companion & portfolio guide! I can walk you through his 39 engineering repositories, Graph-RAG architectures, SMU exchange (3.47 CGPA), clinical ML audit at Preventvital, or even his chess tactics and beatboxing! What would you like to explore?",
        retrieval: retrieval,
        citations: [
          {{"title": "Engineering Profile & Bio", "url": "index.html#home"}},
          {{"title": "39 Verified Repositories", "url": "projects.html"}}
        ]
      }};
    }}

    // 2. Identity / Who are you
    const isIdentity = ['who are you', 'what are you', 'whats your name', "what's your name", 'who made you', 'who created you', 'who built you', 'who developed you', 'tell me about yourself', 'introduce yourself'].some(phrase => cleanText.includes(phrase));
    if (isIdentity) {{
      return {{
        isGhost: false,
        answer: "Pika! ⚡ I'm Pikachu, the AI companion for Advaith Narayana Sarva's portfolio! I'm wired directly into his 55 verified knowledge documents covering his deep learning systems, autonomous agents, and systems code. Ask me anything about what he's built!",
        retrieval: retrieval,
        citations: [{{"title": "About Advaith", "url": "index.html#home"}}]
      }};
    }}

    // 3. Capabilities / Help / Suggestions
    const isHelp = ['what can you do', 'help', 'commands', 'what should i ask', 'what do you know', 'how does this work', 'suggest questions'].some(phrase => cleanText.includes(phrase)) || cleanText === 'help' || cleanText === '?';
    if (isHelp) {{
      return {{
        isGhost: false,
        answer: "Pika! ⚡ Here are some great questions to try asking me:<br><br>" +
          "• 🏆 <strong>Hackathons:</strong> <em>'Tell me about The Sentinel Grid at IBM BOB'</em><br>" +
          "• 🔍 <strong>Clinical Audit:</strong> <em>'What did Advaith do at Preventvital?'</em><br>" +
          "• ⚡ <strong>Projects:</strong> <em>'Tell me about Graph-RAG'</em> or <em>'What is SuperBrain MCP?'</em><br>" +
          "• 🎓 <strong>Education:</strong> <em>'What was his CGPA at Saint Martin\\'s University?'</em><br>" +
          "• ♟️ <strong>Hobbies:</strong> <em>'What chess opening does he play?'</em> or <em>'Can he beatbox?'</em><br>" +
          "• 👻 <strong>Easter Egg:</strong> <em>'Is he afraid of ghosts?!'</em>",
        retrieval: retrieval,
        citations: [{{"title": "Projects Catalog", "url": "projects.html"}}]
      }};
    }}

    // 4. How are you / small talk
    const isHowAreYou = ['how are you', 'hows it going', "how's it going", 'how do you do', 'how are you doing'].some(phrase => cleanText.includes(phrase));
    if (isHowAreYou) {{
      return {{
        isGhost: false,
        answer: "Pika-chuuu! ⚡ My electrical cheeks are fully charged with 64-dimensional embeddings and ready to roll! How can I help you navigate Advaith's portfolio today?",
        retrieval: retrieval,
        citations: []
      }};
    }}

    // 5. Thanks / Appreciation
    const isThanks = cleanWords.some(w => ['thanks', 'thx', 'thankyou'].includes(w)) || cleanText.includes('thank you') || cleanText.includes('appreciate it');
    if (isThanks) {{
      return {{
        isGhost: false,
        answer: "Pika! ⚡ You're very welcome! Let me know if you want to explore more projects, see his resume, or get in touch with Advaith!",
        retrieval: retrieval,
        citations: [{{"title": "View Resume", "url": "resume.html"}}]
      }};
    }}

    // 6. Farewell
    const isBye = cleanWords.some(w => ['bye', 'goodbye', 'cya'].includes(w)) || cleanText.includes('see you') || cleanText.includes('talk to you later');
    if (isBye) {{
      return {{
        isGhost: false,
        answer: "Pika-pi! ⚡ Thanks for stopping by Advaith's portfolio! Feel free to reach out to him directly at advaithsarva@gmail.com anytime. Have an awesome day!",
        retrieval: retrieval,
        citations: [{{"title": "Contact Advaith", "url": "mailto:advaithsarva@gmail.com"}}]
      }};
    }}

    // 7. Overview of Advaith
    const isWhoIsAdvaith = ['who is advaith', 'tell me about advaith', 'who is he', 'about advaith', 'what does advaith do'].some(phrase => cleanText.includes(phrase));
    if (isWhoIsAdvaith) {{
      return {{
        isGhost: false,
        answer: "Pika! ⚡ Advaith Narayana Sarva is an AI & Systems Engineer specializing in interpretable Graph-RAG knowledge systems, autonomous multi-agent harnesses, and low-level PyTorch tensor primitives. He completed an academic exchange at Saint Martin's University (3.47 CGPA, Dean's List), holds an 8.69 CGPA at Woxsen University, audited clinical ML at Preventvital, and placed Top 5 in the IBM BOB National Hackathon with The Sentinel Grid!",
        retrieval: retrieval,
        citations: [
          {{"title": "Profile Summary", "url": "index.html#home"}},
          {{"title": "Resume / CV", "url": "resume.html"}}
        ]
      }};
    }}

    if (!top || top.length === 0 || top[0].rrfScore < 0.01) {{
      return {{
        isGhost: false,
        answer: "Pikachu! ⚡ Advaith is an AI & Systems Engineer with 39 verified repositories covering Graph-RAG, autonomous agents, and systems from scratch. What project or skill would you like to explore?",
        retrieval: retrieval,
        citations: []
      }};
    }}

    const best = top[0].chunk;
    const sources = formatSources(top);
    let text = "";

    // Exact answers
    if (qLower.includes('roc') || qLower.includes('sentinel') || qLower.includes('bob')) {{
      text = "In the IBM BOB National Hackathon 2026, Advaith led engineering for <strong>The Sentinel Grid</strong>, placing <strong>Top 5 in the South Zone</strong>! The disaster-intelligence system comprises 6,957 lines of Python, 314 automated checks, and achieved a verified <strong>ROC-AUC of 0.9924</strong> on 473,000 soil moisture observations in Coimbatore. Pika!";
    }} else if (qLower.includes('postgres') || qLower.includes('speedup') || qLower.includes('slow query')) {{
      text = "The <strong>Autonomous Postgres Performance Agent</strong> diagnoses live query bottlenecks via EXPLAIN ANALYZE, formulates index hypotheses, and executes migrations with an automated rollback guard. It achieved an <strong>11.7x query speedup</strong> on real database workloads. Pika pika!";
    }} else if (qLower.includes('smu') || (qLower.includes('saint') && qLower.includes('martin')) || qLower.includes('3.47')) {{
      text = "Pika! Advaith completed his international exchange at <strong>Saint Martin's University</strong> in Lacey, WA (completed May 2026 across two semesters) in BS CS (AI & ML), graduating with a <strong>3.47 / 4.0 CGPA</strong> and Dean's List honors!";
    }} else if (qLower.includes('woxsen') || qLower.includes('8.69')) {{
      text = "Advaith is pursuing his B.Tech in CSE (AI & ML) at <strong>Woxsen University</strong> (Hyderabad, India) with an <strong>8.69 / 10.0 CGPA</strong>, expected graduation August 2027. Pika!";
    }} else if (qLower.includes('preventvital') || qLower.includes('clinical') || qLower.includes('ascvd') || qLower.includes('goff')) {{
      text = "At Preventvital (GruentzigAI), Advaith caught a critical coefficient sign inversion in the ASCVD clinical risk calculation that was artificially calculating 0.1% baseline risk for untreated patients (expected 2.1% from Goff 2014 trial baseline). He authored the formal bug report and authored RAG & safety rules adhering to ICMR 2023 guidelines on an 'engine computes, LLM explains, clinician signs' protocol. Pika!";
    }} else if (qLower.includes('media nlp') || qLower.includes('rhetoric') || qLower.includes('fallacy') || qLower.includes('0.175')) {{
      text = "The <strong>Media NLP Pipeline</strong> is a deterministic rhetoric analysis engine featuring 23 informal fallacy detectors with character-level verbatim evidence spans, achieving a false positive rate of <strong>0.175 per 1,000 words</strong> evaluated on Wikipedia neutral ground truth with 164 automated tests. Pika!";
    }} else if (qLower.includes('mcp') || qLower.includes('superbrain')) {{
      text = "<strong>SuperBrain MCP</strong> is a Model Context Protocol server featuring <strong>41 specialized tools</strong> across 8 domains, providing persistent cross-session vector memory and sub-2ms protocol overhead. Pika pika!";
    }} else if (qLower.includes('transformer') && qLower.includes('scratch')) {{
      text = "Advaith built a <strong>Decoder-Only Transformer</strong> from scratch in PyTorch primitives, implementing multi-head self-attention, rotary positional embeddings (RoPE), KV-cache for generation, and LayerNorm directly without high-level wrappers. Pika!";
    }} else if (best.slug) {{
      text = `Pika! <strong>${{best.name}}</strong> (${{best.category}}):<br>${{best.content}}<br><em>Key Verified Metrics:</em> <code>${{best.stats || 'Audited repository'}}</code>.`;
      if (top[1] && (qLower.includes('both') || qLower.includes('which projects') || qLower.includes('and'))) {{
        const b2 = top[1].chunk;
        text += `<br><br>Additionally, <strong>${{b2.name}}</strong>:<br>${{b2.content}}`;
      }}
    }} else {{
      text = `⚡ Pika! Based on verified portfolio knowledge:<br>${{best.content}}`;
    }}

    // Append Clickable Sources (Section 12)
    if (sources.length > 0) {{
      text += `<br><br><span style="font-size:0.75rem; color:var(--text-muted); font-weight:700;">SOURCES:</span><br>`;
      sources.forEach(s => {{
        text += `• <a href="${{s.url}}" class="text-blue" style="font-weight:700; text-decoration:underline;">${{s.title}}</a><br>`;
      }});
    }}

    return {{
      isGhost: false,
      answer: text,
      retrieval: retrieval,
      citations: sources
    }};
  }}

  // 11. Public Asynchronous Query Interface (Direct Client-Side Static Execution)
  async function queryAsync(rawQuery) {{
    const retrieval = retrieve(rawQuery, 4);

    // Save to conversation history
    SessionMemory.history.push({{ role: 'user', content: rawQuery }});

    const localResult = synthesizeLocal(rawQuery, retrieval);
    SessionMemory.history.push({{ role: 'bot', content: localResult.answer }});
    return localResult;
  }}

  // Synchronous query method for immediate backward compatibility with script.js
  function querySync(rawQuery) {{
    const retrieval = retrieve(rawQuery, 4);
    return synthesizeLocal(rawQuery, retrieval);
  }}

  // Public Export
  root.AdvaithRAG = {{
    corpus: CORPUS,
    denseVectors: DENSE_VECTORS,
    retrieve: retrieve,
    query: querySync,
    queryAsync: queryAsync,
    processQuery: processQuery,
    session: SessionMemory,
    stats: {{
      totalChunks: N,
      vocabSize: Object.keys(df).length,
      denseDimension: DIM,
      version: "3.2.0-Hybrid-RRF-Qwen"
    }}
  }};

  console.log(`[HYBRID RAG ENGINE READY] Loaded ${{N}} chunks, ${{Object.keys(df).length}} terms, ${{DIM}}-d dense vector space with RRF.`);

}})(typeof window !== 'undefined' ? window : globalThis);
"""

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated hybrid RAG engine at {TARGET_FILE} ({len(js_content)} bytes)")
