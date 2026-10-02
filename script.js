/* ==========================================================================
   Advaith Narayana Sarva — Interactive Portfolio Engine
   Author: Advaith Narayana Sarva
   ========================================================================== */

import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initBrain3D();
  initCarousel();
  initTerminal();
  initPokemonCompanion();
  initArchiveSearch();
  initModals();
  initLiveClock();
  initCopyEmail();
  initMobileNav();
});

/* --------------------------------------------------------------------------
   1. Theme Management (Light / Dark)
   -------------------------------------------------------------------------- */
function initTheme() {
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
    window.dispatchEvent(new CustomEvent('themeChanged', { detail: { theme: next } }));
  });
}

function updateThemeIcon(theme) {
  const icon = document.querySelector('.theme-icon');
  if (icon) {
    icon.textContent = theme === 'dark' ? 'LIGHT' : 'DARK';
  }
}

/* --------------------------------------------------------------------------
   2. Three.js 3D Neural Graph Brain (From zer0brandkit)
   -------------------------------------------------------------------------- */
function initBrain3D() {
  const container = document.getElementById('brainCanvasContainer');
  if (!container) return;

  const scene = new THREE.Scene();
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  scene.background = new THREE.Color(isDark ? 0x12121A : 0xE7DFC9);

  const width = container.clientWidth || 400;
  const height = container.clientHeight || 380;

  const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100);
  camera.position.set(0, 0.5, 4.2);

  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  container.appendChild(renderer.domElement);

  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.enablePan = false;
  controls.minDistance = 2.5;
  controls.maxDistance = 6.5;
  controls.autoRotate = true;
  controls.autoRotateSpeed = 1.2;

  // ZER0 Brand Colors
  const INKS = [0x2547C9, 0xD63031, 0x168F3E, 0x16161F];
  let seed = 7;
  const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;

  const wrinkle = (x, y, z) =>
    Math.sin(7.1 * x + 3.3 * z) * Math.sin(5.7 * y + 2.1 * x) * 0.5 +
    Math.sin(11.3 * z + 4.7 * y) * Math.sin(9.1 * x) * 0.35;

  function randomDir() {
    const u = rnd() * 2 - 1, t = rnd() * Math.PI * 2, s = Math.sqrt(1 - u * u);
    return [s * Math.cos(t), u, s * Math.sin(t)];
  }

  const pts = [];
  for (let i = 0; i < 950; i++) {
    const [dx, dy, dz] = randomDir();
    let x = dx * 1.0;
    let y = dy * 0.85;
    let z = dz * 1.25;
    const w = wrinkle(x, y, z) * 0.14;
    x += dx * w; y += dy * w; z += dz * w;
    const cleft = Math.exp(-Math.abs(x) * 4.0) * 0.22;
    z -= cleft;
    pts.push(new THREE.Vector3(x, y, z));
  }

  // Draw node points
  const pGeo = new THREE.BufferGeometry().setFromPoints(pts);
  const colors = [];
  for (let i = 0; i < pts.length; i++) {
    const hex = INKS[Math.floor(rnd() * INKS.length)];
    const c = new THREE.Color(hex);
    colors.push(c.r, c.g, c.b);
  }
  pGeo.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));

  const pMat = new THREE.PointsMaterial({
    size: 0.055,
    vertexColors: true,
  });
  const pointCloud = new THREE.Points(pGeo, pMat);
  scene.add(pointCloud);

  // Synaptic Edges
  const edgePts = [];
  const edgeColors = [];
  const maxDist = 0.22;

  for (let i = 0; i < pts.length; i++) {
    let links = 0;
    for (let j = i + 1; j < pts.length && links < 3; j++) {
      const d = pts[i].distanceTo(pts[j]);
      if (d < maxDist) {
        edgePts.push(pts[i], pts[j]);
        const c = new THREE.Color(INKS[Math.floor(rnd() * INKS.length)]);
        edgeColors.push(c.r, c.g, c.b, c.r, c.g, c.b);
        links++;
      }
    }
  }

  const lineGeo = new THREE.BufferGeometry().setFromPoints(edgePts);
  lineGeo.setAttribute('color', new THREE.Float32BufferAttribute(edgeColors, 3));
  const lineMat = new THREE.LineBasicMaterial({
    vertexColors: true,
    transparent: true,
    opacity: 0.35
  });
  const lines = new THREE.LineSegments(lineGeo, lineMat);
  scene.add(lines);

  // Resize listener
  window.addEventListener('resize', () => {
    const w = container.clientWidth || 400;
    const h = container.clientHeight || 380;
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
  });

  // Theme update listener
  window.addEventListener('themeChanged', (e) => {
    scene.background = new THREE.Color(e.detail.theme === 'dark' ? 0x12121A : 0xE7DFC9);
  });

  // Render loop
  function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
  }
  animate();
}

/* --------------------------------------------------------------------------
   3. Featured Projects Carousel (Aligned with carousel_ref.jpg)
   -------------------------------------------------------------------------- */
function initCarousel() {
  const track = document.getElementById('projectsTrack');
  const prevBtn = document.getElementById('prevProjectBtn');
  const nextBtn = document.getElementById('nextProjectBtn');
  const indicators = document.querySelectorAll('.dot-indicator');
  const cards = document.querySelectorAll('.project-card');

  if (!track || !cards.length) return;

  let currentIndex = 0;
  const maxIndex = cards.length - 1;

  function updateCarousel(index) {
    currentIndex = Math.max(0, Math.min(index, maxIndex));
    const cardWidth = cards[0].offsetWidth + 24; // card width + gap
    track.style.transform = `translateX(-${currentIndex * cardWidth}px)`;

    indicators.forEach((dot, i) => {
      dot.classList.toggle('active', i === currentIndex);
    });
  }

  prevBtn.addEventListener('click', () => updateCarousel(currentIndex - 1));
  nextBtn.addEventListener('click', () => updateCarousel(currentIndex + 1));

  indicators.forEach(dot => {
    dot.addEventListener('click', () => {
      const slide = parseInt(dot.getAttribute('data-slide'), 10);
      updateCarousel(slide);
    });
  });

  // Touch Swipe on mobile
  let startX = 0;
  track.addEventListener('touchstart', e => {
    startX = e.touches[0].clientX;
  }, { passive: true });

  track.addEventListener('touchend', e => {
    const diff = startX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 40) {
      if (diff > 0) updateCarousel(currentIndex + 1);
      else updateCarousel(currentIndex - 1);
    }
  }, { passive: true });

  window.addEventListener('resize', () => updateCarousel(currentIndex));
}

/* --------------------------------------------------------------------------
   4. Synthesized Audio Engine (8-bit Web Audio API)
   -------------------------------------------------------------------------- */
function playPikachuSound(type = 'spark') {
  try {
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (!AudioCtx) return;
    const audioCtx = new AudioCtx();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();

    if (type === 'spark') {
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(1318.51, audioCtx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(1975.53, audioCtx.currentTime + 0.12);
      gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.18);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start();
      osc.stop(audioCtx.currentTime + 0.2);
    } else if (type === 'ghost') {
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(174.61, audioCtx.currentTime);
      osc.frequency.linearRampToValueAtTime(138.59, audioCtx.currentTime + 0.15);
      osc.frequency.linearRampToValueAtTime(110.00, audioCtx.currentTime + 0.35);
      gain.gain.setValueAtTime(0.12, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.4);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start();
      osc.stop(audioCtx.currentTime + 0.42);
    } else if (type === 'levelup') {
      osc.type = 'square';
      osc.frequency.setValueAtTime(523.25, audioCtx.currentTime);
      osc.frequency.setValueAtTime(659.25, audioCtx.currentTime + 0.08);
      osc.frequency.setValueAtTime(783.99, audioCtx.currentTime + 0.16);
      osc.frequency.setValueAtTime(1046.50, audioCtx.currentTime + 0.24);
      gain.gain.setValueAtTime(0.09, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.38);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start();
      osc.stop(audioCtx.currentTime + 0.4);
    } else if (type === 'beatbox') {
      const now = audioCtx.currentTime;
      // Kick 1
      const kOsc = audioCtx.createOscillator();
      const kGain = audioCtx.createGain();
      kOsc.frequency.setValueAtTime(160, now);
      kOsc.frequency.exponentialRampToValueAtTime(32, now + 0.16);
      kGain.gain.setValueAtTime(0.35, now);
      kGain.gain.exponentialRampToValueAtTime(0.001, now + 0.16);
      kOsc.connect(kGain);
      kGain.connect(audioCtx.destination);
      kOsc.start(now);
      kOsc.stop(now + 0.16);

      // Hi-hat
      setTimeout(() => {
        try {
          const t = audioCtx.currentTime;
          const hOsc = audioCtx.createOscillator();
          const hGain = audioCtx.createGain();
          hOsc.type = 'triangle';
          hOsc.frequency.setValueAtTime(6500, t);
          hGain.gain.setValueAtTime(0.1, t);
          hGain.gain.exponentialRampToValueAtTime(0.001, t + 0.07);
          hOsc.connect(hGain);
          hGain.connect(audioCtx.destination);
          hOsc.start(t);
          hOsc.stop(t + 0.07);
        } catch(e) {}
      }, 140);

      // Snare
      setTimeout(() => {
        try {
          const t = audioCtx.currentTime;
          const sOsc = audioCtx.createOscillator();
          const sGain = audioCtx.createGain();
          sOsc.type = 'square';
          sOsc.frequency.setValueAtTime(260, t);
          sOsc.frequency.exponentialRampToValueAtTime(70, t + 0.16);
          sGain.gain.setValueAtTime(0.25, t);
          sGain.gain.exponentialRampToValueAtTime(0.001, t + 0.16);
          sOsc.connect(sGain);
          sGain.connect(audioCtx.destination);
          sOsc.start(t);
          sOsc.stop(t + 0.16);
        } catch(e) {}
      }, 280);

      // Kick 2 + Hat
      setTimeout(() => {
        try {
          const t = audioCtx.currentTime;
          const k2Osc = audioCtx.createOscillator();
          const k2Gain = audioCtx.createGain();
          k2Osc.frequency.setValueAtTime(140, t);
          k2Osc.frequency.exponentialRampToValueAtTime(28, t + 0.18);
          k2Gain.gain.setValueAtTime(0.3, t);
          k2Gain.gain.exponentialRampToValueAtTime(0.001, t + 0.18);
          k2Osc.connect(k2Gain);
          k2Gain.connect(audioCtx.destination);
          k2Osc.start(t);
          k2Osc.stop(t + 0.18);
        } catch(e) {}
      }, 420);
    }
  } catch (e) {
    // AudioContext policy bypass
  }
}

/* /* --------------------------------------------------------------------------
   5. Pikachu Genuine Vector RAG Engine Integration
   -------------------------------------------------------------------------- */
function updateRagHud(res) {
  const metricEl = document.getElementById('ragHudMetric');
  const chunksEl = document.getElementById('ragHudChunks');
  if (!res || !res.retrieval) return;

  if (metricEl) {
    const lat = res.retrieval.latencyMs || 0;
    const mode = res.mode ? ` [${res.mode.toUpperCase()}]` : '';
    metricEl.innerHTML = `Query: "<strong>${res.retrieval.query}</strong>" · Latency: <strong>${lat}ms</strong>${mode}`;
  }
  if (chunksEl && res.retrieval.topChunks) {
    chunksEl.innerHTML = res.retrieval.topChunks.map((tc, idx) => {
      const doc = tc.chunk || tc;
      const title = doc.name || doc.title || 'Knowledge Chunk';
      const score = tc.rrfScore || tc.score || 0;
      return `
        <div class="rag-hud-chunk-item">
          <span>#${idx+1} ${title.slice(0, 24)}...</span>
          <span style="font-weight:700; color:var(--color-blueprint);">RRF: ${score} (Cos: ${tc.cosSim || 0})</span>
        </div>
      `;
    }).join('');
  }
}

function queryPikachuRAG(rawQuery) {
  const sprite = document.getElementById('pokemonSprite');
  const termCard = document.querySelector('.terminal-card');

  if (window.AdvaithRAG) {
    const res = window.AdvaithRAG.query(rawQuery);
    if (res.isGhost) {
      playPikachuSound('ghost');
      if (sprite) {
        sprite.classList.add('scared-shake');
        setTimeout(() => sprite.classList.remove('scared-shake'), 600);
      }
      if (termCard) {
        termCard.classList.add('scared-shake');
        setTimeout(() => termCard.classList.remove('scared-shake'), 600);
      }
      return {
        isGhost: true,
        text: res.answer,
        retrieval: res.retrieval
      };
    }

    updateRagHud(res);

    return {
      isGhost: false,
      text: res.answer,
      retrieval: res.retrieval
    };
  }

  // Fallback if RAG engine hasn't loaded yet
  return {
    isGhost: false,
    text: "Pikachu! Advaith is a Gen AI Engineer (SMU 3.47 CGPA, Woxsen 8.69 CGPA) building Graph-RAG architectures. Inspect the technology desk catalog for verified reports."
  };
}

/* --------------------------------------------------------------------------
   6. Interactive In-Browser Terminal (terminal.sh)
   -------------------------------------------------------------------------- */
function initTerminal() {
  const input = document.getElementById('terminalInput');
  const consoleOutput = document.getElementById('consoleOutput');
  const termCard = document.querySelector('.terminal-card');
  if (!input || !consoleOutput) return;

  const history = [];
  let historyIdx = -1;

  const staticResponses = {
    help: `Available Commands:
  [PROFILE & INFO]
  whoami        - Engineering profile, status & education (SMU 3.47 CGPA)
  projects      - List primary GenAI, Agent & NLP systems
  skills        - Core technical stack & capabilities
  achievements  - Hackathons, algorithmic audits & honors
  experience    - Professional & academic trajectory
  resume / cv   - View & open printable web resume
  contact       - Display verified contact methods

  [INTERACTIVE & EASTER EGGS]
  neofetch      - System specs, stack overview & ASCII badge
  matrix        - Stream digital cyber cascade
  detective     - The Archive Detective (Detective Pikachu) dossier
  rag <query>   - Query Detective Pikachu's RAG knowledge engine directly in CLI!
  quote         - Random engineering maxim
  clear         - Clear the screen
  theme         - Toggle light / dark mode

  [SHELL UTILITIES]
  ls            - List files in current directory
  cat <file>    - Read file (e.g. cat resume.md, cat stack.json)
  git log       - View commit history
  git status    - Check working tree status
  ping <host>   - Simulate ICMP ping
  echo <text>   - Echo text to stdout
  uptime / date - System uptime & timestamp
  history       - Command execution history`,

    whoami: `Advaith Narayana Sarva
Role        : Gen AI Engineer
Status      : Actively Seeking GenAI Internships & Roles (US, India, Global)
Internship  : AI/ML Engineer Intern @ Preventvital (GruentzigAI Pvt. Ltd.)
Exchange    : Saint Martin's University, Lacey, WA (Aug 2025 – May 2026, CGPA: 3.47 / 4.0, Completed May 2026)
Degree      : B.Tech in CSE (AI & ML) @ Woxsen University (Expected 08/2027, CGPA: 8.69 / 10)
Core Focus  : Graph-RAG, Multi-Agent Orchestration, Interpretable NLP, PyTorch`,

    projects: `[01] media-nlp-pipeline: Deterministic rhetoric & bias pipeline (23 detectors, 164 tests)
     → https://github.com/advaithsarva/media-nlp-pipeline
[02] graph-rag-knowledge-system: Hybrid BM25 + Vector + KG multi-hop retrieval (10/10 tests)
     → https://github.com/advaithsarva/graph-rag-knowledge-system
[03] autonomous-performance-agent: PostgreSQL query watcher & index tuner (11.7x speedup)
     → https://github.com/advaithsarva/autonomous-performance-agent
[04] superbrain_mcp: Persistent-memory MCP server (41 tools, 8 memory types) — private repo
[05] fact-checking-agent: Multi-step NLI claim verification (9/10 verdict accuracy)
     → https://github.com/advaithsarva/fact-checking-agent
[06] transformer-from-scratch: Decoder-only transformer from PyTorch primitives (1.0059x theoretical best loss)
     → https://github.com/advaithsarva/transformer-from-scratch`,

    achievements: `[01] Top 5 South Zone — IBM BOB National Hackathon 2026 (The Sentinel Grid, ROC-AUC 0.9924)
[02] Clinical Audit — Found a sign error in Preventvital's ASCVD risk formula (0.1% vs ~2.1%)
[03] Academic Honors — 3.47 / 4.0 CGPA Dean's Honors @ Saint Martin's University (Completed May 2026)
[04] Leadership — CODE{X} Programming Club Executive Leader (200+ members)`,

    experience: `[2026-Pres] Preventvital (GruentzigAI Pvt. Ltd.) - AI/ML Engineer Intern
[2025-2026] Saint Martin's University - International Exchange Student (CGPA: 3.47 / 4.0, Completed May 2026)
[2023-2027] Woxsen University - B.Tech CSE (AI & ML, CGPA: 8.69 / 10)
[2024-2025] CODE{X} — The Programming Club - Executive Club Leader
[2024-2024] AI Research Centre - Research Intern (Woxsen University)`,

    skills: `GenAI & Agents       : Hybrid RAG (BM25 + dense + RRF), MCP, LangGraph, ChromaDB, human-in-the-loop agents
Deep Learning & NLP  : PyTorch, Transformers, Hugging Face, sentence-transformers, spaCy, NLTK, NLI
Languages & Systems  : Python, TypeScript, Node.js, FastAPI, Flask, PostgreSQL, SQLite, Docker, Linux`,

    contact: `Email    : advaithsarva@gmail.com
LinkedIn : https://www.linkedin.com/in/sarvaadvaithnarayana/
GitHub   : https://github.com/advaithsarva
Instagram: @advaithsarva (https://instagram.com/advaithsarva)`,

    neofetch: `       /\\_/\\          advaith@systems
      ( o.o )         ----------------
       > ^ <          OS       : Arch Linux / macOS / Ubuntu
      /     \\         Host     : Advaith Systems (x86_64)
     (_______)        Kernel   : 6.9.1-genai-custom
                      Uptime   : 20+ years (Continuous learning)
                      Shell    : zsh 5.9 (x86_64-systems)
                      Terminal : Neo-Brutalist v2.4 (xterm-256color)
                      CPU      : Neural Engine (PyTorch, Transformers)
                      Memory   : 41 MCP Tools · 8 Memory Types
                      Academia : SMU (3.47 CGPA) | Woxsen (8.69 CGPA)
                      Projects : 39 (34 public on GitHub)`,

    detective: `THE ARCHIVE DETECTIVE // CASE No. 001
Character: Detective Pikachu · Chief Archive Investigator
Department: Special Investigations Branch · The Advaith Daily
Jurisdiction: 39 Projects (34 Public Repositories) & Academic Records
Grounded Evidence:
  • SMU International Exchange (3.47 / 4.0 CGPA, Dean's List)
  • Woxsen University B.Tech AI/ML (8.69 / 10.0 CGPA)
  • Preventvital Clinical Audit (ASCVD sign error found, awaiting clinical sign-off)
  • IBM BOB South Zone Top 5 (The Sentinel Grid, 0.9924 ROC-AUC)
  • Autonomous Postgres Performance Agent (11.7x Speedup)
Status: Active. Type 'rag <query>' or inquire via the bottom-right Archive Detective!`,

    pokedex: `THE ARCHIVE DETECTIVE // CASE No. 001
Character: Detective Pikachu · Chief Archive Investigator
Department: Special Investigations Branch · The Advaith Daily
Audit Record: 39 Projects · Hybrid Retrieval · Hybrid Dense & Sparse RRF
Status: Active. Type 'rag <query>' or use the Archive Detective console!`,

    pikachu: `THE ARCHIVE DETECTIVE // CASE No. 001
Character: Detective Pikachu · Chief Archive Investigator
Department: Special Investigations Branch · The Advaith Daily
Audit Record: 39 Projects · Hybrid Retrieval · Hybrid Dense & Sparse RRF
Status: Active. Type 'rag <query>' or use the Archive Detective console!`,

    ls: `total 48
-rw-r--r-- 1 advaith staff  3.4K  resume.md
-rw-r--r-- 1 advaith staff  2.1K  stack.json
-rw-r--r-- 1 advaith staff  1.1K  academics.txt
drwxr-xr-x 6 advaith staff   192  projects/
-rwxr-xr-x 1 advaith staff  5.2M  pikachu.bin*`,

    'git status': `On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean`,

    'git log': `* (HEAD -> main) real history: github.com/advaithsarva/portfolio/commits/main`,

    quote: `[ENGINEERING MAXIM]
"Simplicity is prerequisite for reliability." — Edsger W. Dijkstra
"Build systems that fail gracefully, verify rigorously, and never trust a black-box metric without an audit." — Advaith Narayana Sarva`,

    resume: `Opening Neo-Brutalist CV... Click to navigate: resume.html
(Navigating to resume in new tab...)`
  };

  const virtualFiles = {
    'resume.md': `# ADVAITH NARAYANA SARVA
Gen AI Engineer | advaithsarva@gmail.com | github.com/advaithsarva

[EDUCATION]
• Saint Martin's University (Lacey, WA, USA) — Exchange Student, 3.47 CGPA (Completed May 2026)
• Woxsen University (Hyderabad, India) — B.Tech CSE AI/ML, 8.69 / 10 CGPA (Expected 2027)

[EXPERIENCE]
• Preventvital (GruentzigAI) — AI/ML Engineer Intern (ASCVD risk-formula audit, clinical RAG safety rules)
• CODE{X} — Executive Club Leader (200+ members, workshops, open-source sprints)

[STACK]
PyTorch, Hybrid RAG, Transformers, MCP, FastAPI, PostgreSQL, TypeScript`,

    'stack.json': `{\n  "genai": ["Hybrid RAG", "MCP", "LangGraph", "ChromaDB"],\n  "deep_learning": ["PyTorch", "Transformers", "Hugging Face", "spaCy", "NLI"],\n  "systems_and_web": ["Python", "TypeScript", "FastAPI", "PostgreSQL", "Docker", "Node.js"]\n}`,

    'academics.txt': `[ACADEMIC CREDENTIALS]
1. Saint Martin's University (Lacey, WA, USA)
   - Program: International Academic Exchange (BS Computer Science / AI & ML)
   - Status : Completed May 2026 (Two semesters)
   - CGPA   : 3.47 / 4.0 (Dean's Honors)

2. Woxsen University (Hyderabad, India)
   - Program: B.Tech in Computer Science & Engineering (AI & ML)
   - Status : Expected August 2027
   - CGPA   : 8.69 / 10.0`
  };

  function appendOutput(content, isHtml = false, colorClass = '') {
    const el = document.createElement(isHtml ? 'div' : 'pre');
    el.className = `term-line ${colorClass}`.trim();
    el.style.whiteSpace = 'pre-wrap';
    el.style.opacity = '0.95';
    if (isHtml) {
      el.innerHTML = content;
    } else {
      el.textContent = content;
    }
    consoleOutput.insertBefore(el, input.parentElement);
    consoleOutput.scrollTop = consoleOutput.scrollHeight;
  }

  // Keyboard navigation for history (Up/Down) & execution (Enter)
  input.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (history.length > 0 && historyIdx > 0) {
        historyIdx--;
        input.value = history[historyIdx];
      } else if (history.length > 0 && historyIdx === -1) {
        historyIdx = history.length - 1;
        input.value = history[historyIdx];
      }
      return;
    }

    if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (historyIdx >= 0 && historyIdx < history.length - 1) {
        historyIdx++;
        input.value = history[historyIdx];
      } else {
        historyIdx = -1;
        input.value = '';
      }
      return;
    }

    if (e.key === 'Enter') {
      const rawVal = input.value.trim();
      if (!rawVal) return;

      history.push(rawVal);
      historyIdx = -1;

      // Print prompt echo
      const userLine = document.createElement('p');
      userLine.className = 'term-line';
      userLine.innerHTML = `<span class="term-prompt">ARCHIVE://advaith/systems&gt;&nbsp;</span>${rawVal}`;
      consoleOutput.insertBefore(userLine, input.parentElement);

      // Parse command and args
      const parts = rawVal.match(/(?:[^\s"]+|"[^"]*")+/g) || [];
      const cmd = (parts[0] || '').toLowerCase();
      const rawArgs = parts.slice(1).map(p => p.replace(/^"(.*)"$/, '$1'));
      const argStr = rawArgs.join(' ').trim();
      const lowerArgStr = argStr.toLowerCase();

      // Clear input
      input.value = '';

      // Command dispatch
      if (cmd === 'clear') {
        const lines = consoleOutput.querySelectorAll('.term-line');
        lines.forEach(l => l.remove());
      } else if (cmd === 'archive' || cmd === 'archives' || cmd === 'reports') {
        appendOutput(staticResponses.projects);
      } else if (cmd === 'correspondent' || cmd === 'detective' || cmd === 'case' || cmd === 'pokedex' || cmd === 'pikachu') {
        appendOutput(staticResponses.detective);
      } else if (cmd === 'credentials' || cmd === 'academics') {
        appendOutput(virtualFiles['academics.txt']);
      } else if (cmd === 'theme') {
        const themeBtn = document.getElementById('themeToggle');
        if (themeBtn) themeBtn.click();
        appendOutput('Theme toggled successfully.', false, 'text-blue');
      } else if (cmd === 'resume' || cmd === 'cv') {
        appendOutput(staticResponses.resume);
        window.open('resume.html', '_blank');
      } else if (cmd === 'neofetch' || cmd === 'fetch') {
        appendOutput(staticResponses.neofetch);
      } else if (cmd === 'matrix') {
        const matrixLines = [
          '01000001 01100100 01110110 01100001 01101001 01110100 01101000',
          'SYS_INIT: Booting Neural Graph Substrate...',
          'KNOWLEDGE_GRAPH: NetworkX graph loaded',
          'MCP_ORCHESTRATOR: 41 tools loaded',
          'Wake up, Developer...',
          'The Matrix has you.',
          'Follow the Chief Archive Investigator.',
          '[STREAM COMPLETE: Neural link established.]'
        ];
        appendOutput(matrixLines.join('\n'), false, 'text-moss');
      } else if (cmd === 'cat') {
        if (!lowerArgStr) {
          appendOutput("usage: cat <filename>\nAvailable files:\n  resume.md, stack.json, academics.txt", false, 'text-oxide');
        } else if (virtualFiles[lowerArgStr]) {
          appendOutput(virtualFiles[lowerArgStr]);
        } else if (lowerArgStr === 'pikachu.bin') {
          appendOutput("[PIKACHU.BIN: Binary executable: 8-bit cyber companion initialized with level 50 exp!]", false, 'text-blue');
        } else {
          appendOutput(`cat: ${argStr}: No such file or directory. Type 'ls' for file list.`, false, 'text-oxide');
        }
      } else if (cmd === 'ls' || cmd === 'dir') {
        appendOutput(staticResponses.ls);
      } else if (cmd === 'git') {
        if (lowerArgStr === 'log') {
          appendOutput(staticResponses['git log']);
        } else if (lowerArgStr === 'status' || !lowerArgStr) {
          appendOutput(staticResponses['git status']);
        } else {
          appendOutput(`git: '${argStr}' is not a recognized demo git command. Try 'git log' or 'git status'.`);
        }
      } else if (cmd === 'sudo') {
        appendOutput(`[sudo] password for advaith:\nadvaith is not in the sudoers ledger. This incident will be reported to the Gazette archives.`, false, 'text-oxide');
      } else if (cmd === 'ping') {
        const target = argStr || 'github.com';
        const pingLog = `PING ${target} (140.82.121.4): 56 data bytes\n64 bytes from 140.82.121.4: icmp_seq=0 ttl=117 time=14.32 ms\n64 bytes from 140.82.121.4: icmp_seq=1 ttl=117 time=13.88 ms\n64 bytes from 140.82.121.4: icmp_seq=2 ttl=117 time=14.05 ms\n--- ${target} ping statistics ---\n3 packets transmitted, 3 packets received, 0.0% packet loss\nround-trip min/avg/max = 13.88/14.08/14.32 ms`;
        appendOutput(pingLog);
      } else if (cmd === 'rag' || cmd === 'ask') {
        if (!lowerArgStr) {
          appendOutput("usage: rag <query> (or 'rag debug <query>')\nExamples:\n  rag graph rag\n  rag smu\n  rag sentinel\n  rag multimodal doc\n  rag debug preventvital", false, 'text-blue');
        } else if (lowerArgStr.startsWith('debug ')) {
          const debugQuery = lowerArgStr.replace(/^debug\s+/, '');
          if (window.AdvaithRAG) {
            const ret = window.AdvaithRAG.retrieve(debugQuery, 3);
            const ansObj = window.AdvaithRAG.query(debugQuery);
            let dbgText = `[ARCHIVAL RAG PIPELINE DIAGNOSTICS]\nQuery: "${debugQuery}"\nLatency: ${ret.latencyMs}ms | Corpus: 52 Chunks | Space: 64-Dim\nTop Retrieved Chunks:`;
            ret.topChunks.forEach((c, idx) => {
              dbgText += `\n[${idx+1}] ${c.chunk.title}\n    Score: ${c.score} (CosSim: ${c.cosSim} | BM25: ${c.bm25})\n    Category: ${c.chunk.category}`;
            });
            dbgText += `\n\nSynthesized Output:\n${ansObj.answer.replace(/<br\s*[\/]?>/gi, '\n').replace(/<[^>]*>/g, '')}`;
            appendOutput(dbgText, false, 'text-moss');
          }
        } else {
          const resp = queryPikachuRAG(argStr);
          // Convert HTML to readable plaintext for CLI
          const cleanText = resp.text
            .replace(/<br\s*[\/]?>/gi, '\n')
            .replace(/<\/?strong>/gi, '')
            .replace(/<\/?em>/gi, '')
            .replace(/<\/?code>/gi, '')
            .replace(/<a[^>]*>(.*?)<\/a>/gi, '$1');
          const meta = resp.retrieval && resp.retrieval.topChunks[0] ? ` [Score: ${resp.retrieval.topChunks[0].score}, ${resp.retrieval.latencyMs}ms]` : '';
          appendOutput(`[THE ARCHIVE DETECTIVE // INTELLIGENCE DOSSIER]${meta}:\n${cleanText}`, false, resp.isGhost ? 'text-oxide' : 'text-blue');
        }
      } else if (cmd === 'history') {
        const histLog = history.map((h, i) => `  ${String(i + 1).padStart(3, ' ')}  ${h}`).join('\n');
        appendOutput(histLog || 'No history recorded yet.');
      } else if (cmd === 'echo') {
        appendOutput(argStr);
      } else if (cmd === 'date' || cmd === 'uptime') {
        const now = new Date();
        const istStr = now.toLocaleString('en-IN', { timeZone: 'Asia/Kolkata', hour12: false }) + ' IST';
        appendOutput(`Current Time : ${istStr}\nSystem Uptime: 20 years, 8 months, 14 days (Continuous active development)`);
      } else if (cmd === 'quote' || cmd === 'fortune') {
        appendOutput(staticResponses.quote);
      } else if (staticResponses[cmd]) {
        appendOutput(staticResponses[cmd]);
      } else {
        appendOutput(`zsh: command not found: ${cmd}. Type 'help' for available commands.`, false, 'text-oxide');
      }

      consoleOutput.scrollTop = consoleOutput.scrollHeight;
    }
  });
}

/* --------------------------------------------------------------------------
   7. The Archive Detective (Detective Pikachu) Technical Archive RAG System
   -------------------------------------------------------------------------- */
function initPokemonCompanion() {
  const sprite = document.getElementById('pokemonSprite');
  const spriteFront = document.getElementById('pokemonSpriteFront');
  const chatLog = document.getElementById('pkmnChatLog');
  const chatLogFront = document.getElementById('pkmnChatLogFront');
  const chatForm = document.getElementById('pkmnChatForm');
  const chatFormFront = document.getElementById('pkmnChatFormFront');
  const chatInput = document.getElementById('pkmnChatInput');
  const chatInputFront = document.getElementById('pkmnChatInputFront');
  const quickChips = document.querySelectorAll('.chip-btn');
  const minBtn = document.getElementById('pkmnMinBtn');
  const widget = document.getElementById('pokedexWidget');
  const bar = document.getElementById('pokedexBar');
  const chimeBtn = document.getElementById('pkmnChimeBtn');
  const feedBtn = document.getElementById('pkmnFeedBtn');
  const clearBtn = document.getElementById('pkmnClearBtn');
  const tickerText = document.getElementById('tickerText');
  const tickerTextFront = document.getElementById('tickerTextFront');

  if (!chatLog && !chatLogFront) return;

  // Contextual memory tracking for multi-turn queries
  let lastInvestigatedSubject = null;

  function setTicker(text) {
    if (tickerText) tickerText.textContent = text;
    if (tickerTextFront) tickerTextFront.textContent = text;
  }

  // Escape HTML helper
  function escapeHtml(str) {
    return str
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  // Append message to chat log
  function appendChat(speaker, text, isUser = false, isGhost = false, citations = null) {
    const logs = [chatLog, chatLogFront].filter(Boolean);
    let citationsHtml = '';
    if (!isUser && !text.includes('evidence-consulted-box') && citations && citations.length > 0) {
      citationsHtml = `
        <div class="evidence-consulted-box">
          <span class="evidence-header-label">EVIDENCE CONSULTED:</span>
          <ul class="evidence-list">
            ${citations.map(c => `<li>• <a href="${c.url}" class="evidence-link">${c.title}</a> <span class="evidence-report-action">[READ REPORT →]</span></li>`).join('')}
          </ul>
        </div>
      `;
    }

    logs.forEach(log => {
      const msg = document.createElement('div');
      msg.className = `chat-msg ${isUser ? 'user-msg' : 'bot-msg'}${isGhost ? ' ghost-scared' : ''}`;

      if (isUser) {
        msg.innerHTML = `
          <span class="chat-speaker">${speaker}</span>
          <div class="user-query-text">${escapeHtml(text)}</div>
        `;
      } else {
        msg.innerHTML = `
          <div class="case-header-stamp">
            <span class="chat-speaker">${speaker}</span>
            <span class="case-stamp-tag">${isGhost ? 'SPECTRAL ANOMALY' : 'VERIFIED ARCHIVAL EVIDENCE'}</span>
          </div>
          <div class="findings-body">${text}</div>
          ${citationsHtml}
        `;
      }

      log.appendChild(msg);
      log.scrollTop = log.scrollHeight;
    });
  }

  // Handle Query Submission with 3-Stage Investigation Pipeline
  async function handleQuery(queryText) {
    if (!queryText || !queryText.trim()) return;
    const cleanQuery = queryText.trim();

    // Contextual pronoun / follow-up resolution (e.g. "what was its speedup?")
    let queryToSearch = cleanQuery;
    const isFollowUp = (
      /\b(it|its|that|this|the project|the system|the agent|speedup|roc|auc|precision|recall)\b/i.test(cleanQuery) ||
      (/^\b(what|how|why|tell me more|details|metrics|results|link|repo|code)\b/i.test(cleanQuery) && cleanQuery.split(/\s+/).length <= 6)
    );
    if (isFollowUp && lastInvestigatedSubject) {
      queryToSearch = `${lastInvestigatedSubject} ${cleanQuery}`;
    }

    // 1. Add User Case Inquiry
    appendChat('CASE ENQUIRY SUBMITTED:', cleanQuery, true, false);

    // 2. Play subtle spark chime
    playPikachuSound('spark');

    // 3. Stage 1: Case File Opened
    setTicker('STAGE 1: CASE FILE OPENED · INVESTIGATING...');

    // Temporary investigation progress stepper
    const stepper = document.createElement('div');
    stepper.className = 'investigation-flow-card';
    stepper.innerHTML = `
      <div class="inv-stage-indicator active" id="invStage1"><span class="inv-badge">STAGE 1</span> CASE FILE OPENED</div>
      <div class="inv-stage-indicator" id="invStage2"><span class="inv-badge">STAGE 2</span> SEARCHING THE ARCHIVES...</div>
      <div class="inv-stage-indicator" id="invStage3"><span class="inv-badge">STAGE 3</span> EVIDENCE FOUND</div>
    `;
    chatLog.appendChild(stepper);
    chatLog.scrollTop = chatLog.scrollHeight;

    // Transition to Stage 2 after 100ms
    setTimeout(() => {
      setTicker('STAGE 2: SEARCHING THE ARCHIVES... 39 REPOSITORIES');
      const s2 = stepper.querySelector('#invStage2');
      if (s2) s2.classList.add('active');
    }, 100);

    // Execute async RAG query with fallback
    let responseData = null;
    let isGhost = false;

    if (window.AdvaithRAG && typeof window.AdvaithRAG.queryAsync === 'function') {
      try {
        responseData = await window.AdvaithRAG.queryAsync(queryToSearch);
      } catch (err) {
        console.warn('Async query failed, utilizing local sync fallback:', err);
      }
    }

    if (!responseData) {
      responseData = queryPikachuRAG(queryToSearch);
      responseData.answer = responseData.text;
    }

    // Track active project subject for subsequent multi-turn queries
    if (responseData.retrieval && responseData.retrieval.topChunks && responseData.retrieval.topChunks[0]) {
      const topChunk = responseData.retrieval.topChunks[0].chunk;
      if (topChunk && (topChunk.type === 'project' || topChunk.slug)) {
        lastInvestigatedSubject = topChunk.name;
      }
    }

    isGhost = responseData.isGhost || false;

    // Stage 3: Evidence Found
    setTimeout(() => {
      setTicker('STAGE 3: EVIDENCE FOUND · COMPILING FINDINGS');
      const s3 = stepper.querySelector('#invStage3');
      if (s3) s3.classList.add('active');
    }, 180);

    // Render Final Detective Case Findings
    setTimeout(() => {
      if (stepper && stepper.parentNode) {
        stepper.parentNode.removeChild(stepper);
      }

      if (isGhost) {
        playPikachuSound('ghost');
        if (sprite) {
          sprite.classList.add('scared-shake');
          setTimeout(() => sprite.classList.remove('scared-shake'), 600);
        }
      }

      updateRagHud(responseData);
      appendChat('THE ARCHIVE DETECTIVE // CASE FINDINGS:', responseData.answer, false, isGhost, responseData.citations);
      setTicker('EVIDENCE RETRIEVED · CASE No. 001');
    }, 280);
  }

  // Event Listeners: Quick Topic Chips
  quickChips.forEach(chip => {
    chip.addEventListener('click', () => {
      const q = chip.getAttribute('data-query');
      if (q) handleQuery(q);
    });
  });

  // Event Listener: Chat Form Submit (Drawer & Front Broadsheet)
  if (chatForm && chatInput) {
    chatForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const val = chatInput.value;
      chatInput.value = '';
      handleQuery(val);
    });
  }

  if (chatFormFront && chatInputFront) {
    chatFormFront.addEventListener('submit', (e) => {
      e.preventDefault();
      const val = chatInputFront.value;
      chatInputFront.value = '';
      handleQuery(val);
    });
  }

  // Event Listener: Detective Avatar Tap
  [sprite, spriteFront].filter(Boolean).forEach(el => {
    el.addEventListener('click', () => {
      playPikachuSound('spark');
      el.style.transform = 'scale(1.1) rotate(3deg)';
      setTimeout(() => el.style.transform = 'scale(1) rotate(0deg)', 180);
      appendChat(
        'THE ARCHIVE DETECTIVE // OFFICIAL DISPATCH:',
        "Pika! Case file active. I am cross-examining Advaith's 39 projects and technical dossiers. Submit any enquiry to inspect the documented evidence.",
        false,
        false
      );
    });
  });

  // Event Listener: Case Chime Button
  if (chimeBtn) {
    chimeBtn.addEventListener('click', () => {
      playPikachuSound('spark');
      appendChat('THE ARCHIVE DETECTIVE // SIGNAL BELL:', "Pika-pi! Editorial wire transmission chime verified.", false, false);
    });
  }

  // Event Listener: Archive Sync Button
  if (feedBtn) {
    feedBtn.addEventListener('click', () => {
      playPikachuSound('levelup');
      appendChat('THE ARCHIVE DETECTIVE // ARCHIVE SYNC:', "Archive index synchronized. Knowledge dossiers for all 39 projects are loaded in the hybrid broadsheet register.", false, false);
      setTicker('ARCHIVE SYNC CONFIRMED · 39 REPOSITORIES');
    });
  }

  // Event Listener: Clear Button / New Case
  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      lastInvestigatedSubject = null;
      setTicker('CASE FILE OPENED · STANDBY FOR ENQUIRY');
      chatLog.innerHTML = `
        <div class="chat-msg bot-msg detective-msg">
          <div class="case-header-stamp">
            <span class="chat-speaker">THE ARCHIVE DETECTIVE // SPECIAL ENQUIRY No. 001</span>
            <span class="case-stamp-tag">NEW CASE FILE</span>
          </div>
          <div class="findings-body">
            Pika! Case dossier cleared. Standing by for your next enquiry. What technical record or project shall we investigate?
          </div>
        </div>
      `;
    });
  }

  // Event Listener: Minimize / Expand
  if (minBtn) {
    minBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      widget.classList.toggle('minimized');
      minBtn.textContent = widget.classList.contains('minimized') ? 'EXPAND ▲' : 'MINIMIZE _';
    });
  }

  // Event Listener: RAG Inspector HUD Toggle
  const ragInspectBtn = document.getElementById('pkmnRagInspectBtn');
  const ragHudPanel = document.getElementById('ragInspectorPanel');
  if (ragInspectBtn && ragHudPanel) {
    ragInspectBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const isHidden = ragHudPanel.style.display === 'none';
      ragHudPanel.style.display = isHidden ? 'block' : 'none';
      ragInspectBtn.textContent = isHidden ? 'CLOSE DOSSIER' : 'EVIDENCE DOSSIER';
    });
  }

  if (bar) {
    bar.addEventListener('click', () => {
      if (widget.classList.contains('minimized')) {
        widget.classList.remove('minimized');
        if (minBtn) minBtn.textContent = '_ MINIMIZE';
      }
    });
  }
}

/* --------------------------------------------------------------------------
   6. Project Architecture Modal
   -------------------------------------------------------------------------- */
function initModals() {
  const modal = document.getElementById('projectModal');
  const closeBtn = document.getElementById('modalCloseBtn');
  const content = document.getElementById('modalContent');
  const title = document.getElementById('modalTitle');
  const openBtns = document.querySelectorAll('.open-modal-btn');

  const projectDetails = {};  // ponytail: no page has .open-modal-btn; old specs held false claims

  openBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const modalKey = btn.getAttribute('data-modal');
      const data = projectDetails[modalKey];
      if (data) {
        title.textContent = data.title;
        content.innerHTML = data.html;
        modal.classList.add('open');
        modal.setAttribute('aria-hidden', 'false');
      }
    });
  });

  closeBtn.addEventListener('click', () => {
    modal.classList.remove('open');
    modal.setAttribute('aria-hidden', 'true');
  });

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.classList.remove('open');
      modal.setAttribute('aria-hidden', 'true');
    }
  });
}

/* --------------------------------------------------------------------------
   7. Live Clock, Copy Email, Mobile Nav
   -------------------------------------------------------------------------- */
function initLiveClock() {
  const clockEl = document.getElementById('liveClock');
  const mastheadClockEl = document.getElementById('liveClockMasthead');
  if (!clockEl && !mastheadClockEl) return;

  function update() {
    const now = new Date();
    const ist = now.toLocaleTimeString('en-US', {
      timeZone: 'Asia/Kolkata',
      hour12: false
    }) + ' IST';
    if (clockEl) clockEl.textContent = ist;
    if (mastheadClockEl) mastheadClockEl.textContent = ist;
  }
  update();
  setInterval(update, 1000);
}

function initCopyEmail() {
  const copyBtn = document.getElementById('copyEmailBtn');
  if (!copyBtn) return;

  copyBtn.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText('advaithsarva@gmail.com');
      const originalText = copyBtn.textContent;
      copyBtn.textContent = 'TELEGRAPH ADDRESS COPIED';
      copyBtn.style.backgroundColor = 'var(--text-main)';
      copyBtn.style.color = 'var(--bg-canvas)';
      setTimeout(() => {
        copyBtn.textContent = originalText;
        copyBtn.style.backgroundColor = '';
        copyBtn.style.color = '';
      }, 2000);
    } catch (err) {
      window.location.href = 'mailto:advaithsarva@gmail.com';
    }
  });
}

function initMobileNav() {
  const mobileBtn = document.getElementById('mobileMenuBtn');
  const navMenu = document.getElementById('navMenu');
  if (!mobileBtn || !navMenu) return;

  mobileBtn.addEventListener('click', () => {
    navMenu.classList.toggle('open');
  });

  document.querySelectorAll('.nav-tab').forEach(tab => {
    tab.addEventListener('click', () => {
      navMenu.classList.remove('open');
    });
  });
}

/* --------------------------------------------------------------------------
   8. Front-Page Archive Intelligent Search (Search the Archives)
   -------------------------------------------------------------------------- */
function initArchiveSearch() {
  const input = document.getElementById('archiveSearchInput');
  const btn = document.getElementById('archiveSearchBtn');
  const results = document.getElementById('archiveSearchResults');
  const chips = document.querySelectorAll('.archive-search-chip');
  if (!input || !results) return;

  function performSearch(query) {
    if (!query || !query.trim()) {
      results.style.display = 'none';
      results.innerHTML = '';
      return;
    }
    const q = query.trim();

    if (!window.AdvaithRAG) {
      results.innerHTML = `<div style="padding:16px; font-family:'IBM Plex Mono',monospace; font-size:0.85rem;">Initializing archive index...</div>`;
      results.style.display = 'block';
      return;
    }

    const retrieval = window.AdvaithRAG.retrieve(q, 4);
    if (!retrieval || !retrieval.topChunks || retrieval.topChunks.length === 0) {
      results.innerHTML = `<div style="padding:16px; font-family:'IBM Plex Mono',monospace; font-size:0.85rem; border:2px dashed var(--border-color); background:var(--bg-card);">No archived reports directly matched "<strong>${q}</strong>". Try querying "autonomous agents", "RAG", or "clinical audit".</div>`;
      results.style.display = 'block';
      return;
    }

    let html = `<div style="margin-bottom:12px; font-family:'IBM Plex Mono',monospace; font-size:0.75rem; font-weight:800; color:var(--color-blueprint);">RETRIEVED ${retrieval.topChunks.length} ARCHIVAL DISPATCHES (${retrieval.latencyMs}ms latency · Dense + BM25):</div>`;

    retrieval.topChunks.forEach((item, idx) => {
      const doc = item.chunk;
      const score = Math.round(item.score * 100);
      const category = doc.category || 'Technology';
      const slug = doc.slug || (doc.name || '').toLowerCase().replace(/[^a-z0-9]+/g, '-');
      const snippet = doc.whyMatched || (doc.text ? doc.text.slice(0, 150) + '...' : 'Verified archival technical report.');
      const link = doc.type === 'project' ? `project.html?id=${slug}` : 'resume.html';

      html += `
        <div class="archive-result-card">
          <div class="archive-result-meta">
            <span class="badge-tag">${category.toUpperCase()}</span>
            <span class="archive-result-score">RELEVANCE: ${score}%</span>
          </div>
          <h4 class="archive-result-title">${doc.title || doc.name}</h4>
          <p class="archive-result-snippet">${snippet}</p>
          <div style="margin-top:10px;">
            <a href="${link}" class="neo-btn btn-primary" style="font-size:0.72rem; padding:4px 10px;">EXAMINE REPORT ↗</a>
          </div>
        </div>
      `;
    });

    results.innerHTML = html;
    results.style.display = 'block';
  }

  if (btn) {
    btn.addEventListener('click', () => performSearch(input.value));
  }

  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      performSearch(input.value);
    }
  });

  chips.forEach(chip => {
    chip.addEventListener('click', () => {
      const q = chip.getAttribute('data-query');
      if (q) {
        input.value = q;
        performSearch(q);
      }
    });
  });
}

