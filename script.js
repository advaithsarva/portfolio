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
    icon.textContent = theme === 'dark' ? '☀️' : '🌙';
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
    metricEl.innerHTML = `Query: "<strong>${res.retrieval.query}</strong>" · Latency: <strong>${res.retrieval.latencyMs}ms</strong>`;
  }
  if (chunksEl) {
    chunksEl.innerHTML = res.retrieval.topChunks.map((tc, idx) => `
      <div class="rag-hud-chunk-item">
        <span>#${idx+1} ${tc.chunk.title.slice(0, 26)}...</span>
        <span style="font-weight:700; color:var(--color-blueprint);">Score: ${tc.score} (Cos: ${tc.cosSim})</span>
      </div>
    `).join('');
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
    text: "Pikachu! ⚡ Advaith is a GenAI & Systems Engineer (SMU 3.47 CGPA, Woxsen 8.69 CGPA) building Graph-RAG architectures. Check out his projects in the catalog!"
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
  chess         - Interactive Sicilian board & challenge link
  beatbox       - Play 8-bit live beatbox synth & soundwave
  ghost / spook - ⚠️ Test Advaith & Pikachu's greatest fear!
  matrix        - Stream digital cyber cascade
  pokedex       - Pikachu AI companion stats
  rag <query>   - Query Pikachu's RAG knowledge engine directly in CLI!
  quote         - Random engineering maxim
  clear         - Clear the screen
  theme         - Toggle light / dark mode

  [SHELL UTILITIES]
  ls            - List files in current directory
  cat <file>    - Read file (e.g. cat hobbies.txt, cat secret.env)
  git log       - View commit history
  git status    - Check working tree status
  ping <host>   - Simulate ICMP ping
  echo <text>   - Echo text to stdout
  uptime / date - System uptime & timestamp
  history       - Command execution history`,

    whoami: `Advaith Narayana Sarva
Role        : GenAI & Systems Engineer
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
[04] superbrain_mcp: Unified memory & state MCP server (41 tools across 8 domains)
     → https://github.com/advaithsarva/superbrain_mcp
[05] fact-checking-agent: Multi-step NLI claim verification (9/10 verdict accuracy)
     → https://github.com/advaithsarva/fact-checking-agent
[06] transformer-from-scratch: Decoder-only transformer from PyTorch primitives (1.0059x floor)
     → https://github.com/advaithsarva/transformer-from-scratch`,

    achievements: `[01] Top 5 South Zone — IBM BOB National Hackathon 2026 (The Sentinel Grid, ROC-AUC 0.9924)
[02] Algorithmic Audit — Preventvital Clinical ASCVD Risk Formula Sign Inversion Resolution
[03] Academic Honors — 3.47 / 4.0 CGPA Dean's Honors @ Saint Martin's University (Completed May 2026)
[04] Leadership — CODE{X} Programming Club Executive Leader (200+ members)`,

    experience: `[2026-Pres] Preventvital (GruentzigAI Pvt. Ltd.) - AI/ML Engineer Intern
[2025-2026] Saint Martin's University - International Exchange Student (CGPA: 3.47 / 4.0, Completed May 2026)
[2023-2027] Woxsen University - B.Tech CSE (AI & ML, CGPA: 8.69 / 10)
[2024-2025] CODE{X} — The Programming Club - Executive Club Leader
[2024-2024] AI Research Centre - Research Intern (Woxsen University)`,

    skills: `GenAI & Agents       : Graph-RAG, Multi-Agent Swarms, MCP Protocol, DSPy, Vector DBs (Chroma, Qdrant)
Deep Learning & NLP  : PyTorch, Transformers, HuggingFace, CUDA, spaCy, NLTK, NLI, Causal Attention
Languages & Systems  : Python (Async/CFFI), TypeScript, Node.js, FastAPI, PostgreSQL, Docker, Git, C++`,

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
                      CPU      : Neural Engine (PyTorch, DSPy, Transformers)
                      Memory   : 41 MCP Tools @ 8 Domains
                      Academia : SMU (3.47 CGPA) | Woxsen (8.69 CGPA)
                      Hobbies  : Chess ♟️, Football ⚽, Beatbox 🎤, Debate 🎙️
                      Fear     : Ghosts 👻 (Error 404: Courage not found)`,

    chess: `    +-----------------+
  8 | r  n  b  q  k  b  n  r |
  7 | p  p  .  p  p  p  p  p |
  6 | .  .  .  .  .  .  .  . |
  5 | .  .  p  .  .  .  .  . |
  4 | .  .  .  .  P  .  .  . |
  3 | .  .  .  .  .  .  .  . |
  2 | P  P  P  P  .  P  P  P |
  1 | R  N  B  Q  K  B  N  R |
    +-----------------+
      a  b  c  d  e  f  g  h

Opening: 1. e4 c5 (Sicilian Defense)
Playing Style: Aggressive tactical sharpness, deep calculation, endgame precision.
Challenge Advaith to a match:
• Chess.com / Lichess: @advaithsarva
• Email: advaithsarva@gmail.com (Open for 3+2 blitz or 10m rapid!)`,

    pokedex: `POKEDEX ENTRY #025: PIKACHU
Type   : Electric / RAG Companion | Level: 50 | Ability: Lightning Rod
Status : "Advaith's AI partner! Knows all about his GenAI systems, chess tactics,
football games, beatbox patterns, global news, and why he screams at ghosts! 👻"`,

    pikachu: `POKEDEX ENTRY #025: PIKACHU
Type   : Electric / RAG Companion | Level: 50 | Ability: Lightning Rod
Status : "Advaith's AI partner! Knows all about his GenAI systems, chess tactics,
football games, beatbox patterns, global news, and why he screams at ghosts! 👻"`,

    ls: `total 48
-rw-r--r-- 1 advaith staff  3.4K  resume.md
-rw-r--r-- 1 advaith staff  1.8K  hobbies.txt
-rw-r--r-- 1 advaith staff  2.1K  stack.json
-rw-r--r-- 1 advaith staff  1.1K  academics.txt
-rw------- 1 advaith staff   210  secret.env
drwxr-xr-x 6 advaith staff   192  projects/
-rwxr-xr-x 1 advaith staff  5.2M  pikachu.bin*`,

    'git status': `On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean`,

    'git log': `* 7f9a204 (HEAD -> main) feat(rag): hybrid BM25 + KG multi-hop retrieval
* 3b1c8e1 fix(eval): clinical ASCVD sign inversion audit & ICMR protocol
* a4d021f feat(mcp): 41 tools across 8 operational domains for SuperBrain
* 8e91b5c chore(edu): update SMU exchange credentials to 3.47 CGPA
* e528990 feat(agent): autonomous PostgreSQL index tuner with 11.7x speedup
* 109ac2d init: initial commit of Neo-Brutalist developer portfolio`,

    quote: `[ENGINEERING MAXIM]
"Simplicity is prerequisite for reliability." — Edsger W. Dijkstra
"Build systems that fail gracefully, verify rigorously, and never trust a black-box metric without an audit." — Advaith Narayana Sarva`,

    resume: `Opening Neo-Brutalist CV... Click to navigate: resume.html
(Navigating to resume in new tab...)`
  };

  const virtualFiles = {
    'resume.md': `# ADVAITH NARAYANA SARVA
GenAI & Systems Engineer | advaithsarva@gmail.com | github.com/advaithsarva

[EDUCATION]
• Saint Martin's University (Lacey, WA, USA) — Exchange Student, 3.47 CGPA (Completed May 2026)
• Woxsen University (Hyderabad, India) — B.Tech CSE AI/ML, 8.69 / 10 CGPA (Expected 2027)

[EXPERIENCE]
• Preventvital (GruentzigAI) — AI/ML Engineer Intern (Clinical ML, ASCVD audit, RAG gates)
• CODE{X} — Executive Club Leader (200+ members, workshops, open-source sprints)

[STACK]
PyTorch, Graph-RAG, DSPy, Transformers, MCP Protocol, FastAPI, PostgreSQL, TypeScript`,

    'hobbies.txt': `[PERSONAL HOBBIES & INTERESTS]
• Chess       : Tactical Sicilian Defense (1.e4 c5), Rapid & Blitz matches (@advaithsarva)
• Football    : High-press striker / attacking midfield, European football fanatic
• Beatbox     : Vocal percussion, acoustic bass drops, rhythm jams
• Debate      : Former CODE{X} Leader, structural rhetoric & argument dissection
• News Maniac : Obsessive consumer of global news, arXiv preprints, geopolitics
• Culture     : Grounded in timeless heritage, classical philosophy, deep cultural roots
• Pokémon     : Lifelong trainer, competitive synergy geek, partner of Pikachu #025
• Weakness    : GHOSTS! 👻 Absolutely terrified of spooky things!`,

    'stack.json': `{\n  "genai": ["Graph-RAG", "Multi-Agent Swarms", "MCP Protocol", "DSPy", "ChromaDB", "Qdrant", "Neo4j"],\n  "deep_learning": ["PyTorch", "Transformers", "CUDA", "HuggingFace", "spaCy", "NLI"],\n  "systems_and_web": ["Python (Async/CFFI)", "TypeScript", "FastAPI", "PostgreSQL", "Docker", "Node.js"]\n}`,

    'academics.txt': `[ACADEMIC CREDENTIALS]
1. Saint Martin's University (Lacey, WA, USA)
   - Program: International Academic Exchange (BS Computer Science / AI & ML)
   - Status : Completed May 2026 (Two semesters)
   - CGPA   : 3.47 / 4.0 (Dean's Honors)

2. Woxsen University (Hyderabad, India)
   - Program: B.Tech in Computer Science & Engineering (AI & ML)
   - Status : Expected August 2027
   - CGPA   : 8.69 / 10.0`,

    'secret.env': `TOP_SECRET_WEAKNESS="Genuinely terrified of ghosts, haunted houses, and Gengar 👻"
DREAM="Pioneering autonomous multi-agent systems and verified Graph-RAG"
DAILY_FUEL="Coffee, arXiv preprints, geopolitical feeds & beatbox rhythms"
FAVORITE_OPENING="1. e4 c5 (Sicilian Defense)"`
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
      userLine.innerHTML = `<span class="term-prompt">advaith@systems:~$</span> ${rawVal}`;
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
      } else if (cmd === 'theme') {
        const themeBtn = document.getElementById('themeToggle');
        if (themeBtn) themeBtn.click();
        appendOutput('Theme toggled successfully.', false, 'text-blue');
      } else if (cmd === 'resume' || cmd === 'cv') {
        appendOutput(staticResponses.resume);
        window.open('resume.html', '_blank');
      } else if (cmd === 'neofetch' || cmd === 'fetch') {
        appendOutput(staticResponses.neofetch);
      } else if (cmd === 'chess') {
        appendOutput(staticResponses.chess);
      } else if (cmd === 'beatbox' || cmd === 'dropbeat') {
        playPikachuSound('beatbox');
        const beatAnim = `[BEATBOX_ENGINE] Synthesizing 8-bit live vocal beatbox loop...
♫  | █ ▅ ▃ ▇ █ ▄ ▆ █ ▅ ▃ ▇ █ |  ♫
Pattern: [B]oom (Kick) -> [t]sh (Hi-hat) -> [K]a (Snare) -> [t]sh (Hi-hat)
"Advaith drops rhythmic basslines and acoustic beatbox patterns between model training.
Drop an email to jam or challenge him to a freestyle beat!"`;
        appendOutput(beatAnim, false, 'text-moss');
      } else if (cmd === 'ghost' || cmd === 'spook' || cmd === 'boo') {
        playPikachuSound('ghost');
        if (termCard) {
          termCard.classList.add('scared-shake');
          setTimeout(() => termCard.classList.remove('scared-shake'), 600);
        }
        const sprite = document.getElementById('pokemonSprite');
        if (sprite) {
          sprite.classList.add('scared-shake');
          setTimeout(() => sprite.classList.remove('scared-shake'), 600);
        }
        const spookLog = `⚠️  [CRITICAL KERNEL PANIC 0xGHOST]:
👻  UNIDENTIFIED SPECTRAL ENTITY DETECTED IN SECTOR 4!
⚡  Pikachu panicked! Threw Thunderbolt at the terminal screen!
😱  Advaith deployed emergency blankets and closed 47 browser tabs!
>> "FATAL: Advaith is terrified of ghosts! Please return to safe topics like PyTorch, Chess, or Football!"`;
        appendOutput(spookLog, false, 'text-oxide');
      } else if (cmd === 'matrix') {
        const matrixLines = [
          '01000001 01100100 01110110 01100001 01101001 01110100 01101000',
          'SYS_INIT: Booting Neural Graph Substrate...',
          'KNOWLEDGE_VECTORS: Neo4j Knowledge Graph connected (24,810 triples)',
          'MCP_ORCHESTRATOR: 41 tools loaded across 8 operational domains',
          'Wake up, Developer...',
          'The Matrix has you.',
          'Follow the yellow Pikachu. ⚡',
          '[STREAM COMPLETE: Neural link established.]'
        ];
        appendOutput(matrixLines.join('\n'), false, 'text-moss');
      } else if (cmd === 'cat') {
        if (!lowerArgStr) {
          appendOutput("usage: cat <filename>\nAvailable files:\n  resume.md, hobbies.txt, stack.json, academics.txt, secret.env", false, 'text-oxide');
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
        appendOutput(`[sudo] password for advaith:\nadvaith is not in the sudoers file. This incident will be reported to Pikachu. ⚡`, false, 'text-oxide');
      } else if (cmd === 'ping') {
        const target = argStr || 'github.com';
        const pingLog = `PING ${target} (140.82.121.4): 56 data bytes\n64 bytes from 140.82.121.4: icmp_seq=0 ttl=117 time=14.32 ms\n64 bytes from 140.82.121.4: icmp_seq=1 ttl=117 time=13.88 ms\n64 bytes from 140.82.121.4: icmp_seq=2 ttl=117 time=14.05 ms\n--- ${target} ping statistics ---\n3 packets transmitted, 3 packets received, 0.0% packet loss\nround-trip min/avg/max = 13.88/14.08/14.32 ms`;
        appendOutput(pingLog);
      } else if (cmd === 'rag' || cmd === 'ask') {
        if (!lowerArgStr) {
          appendOutput("usage: rag <query> (or 'rag debug <query>')\nExamples:\n  rag chess\n  rag smu\n  rag sentinel\n  rag multimodal doc\n  rag debug preventvital", false, 'text-blue');
        } else if (lowerArgStr.startsWith('debug ')) {
          const debugQuery = lowerArgStr.replace(/^debug\s+/, '');
          if (window.AdvaithRAG) {
            const ret = window.AdvaithRAG.retrieve(debugQuery, 3);
            const ansObj = window.AdvaithRAG.query(debugQuery);
            let dbgText = `⚡ [VECTOR RAG PIPELINE DIAGNOSTICS]\nQuery: "${debugQuery}"\nLatency: ${ret.latencyMs}ms | Corpus: 52 Chunks | Space: 64-Dim\nTop Retrieved Chunks:`;
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
          appendOutput(`⚡ [PIKACHU VECTOR RAG ENGINE]${meta}:\n${cleanText}`, false, resp.isGhost ? 'text-oxide' : 'text-blue');
        }
      } else if (cmd === 'history') {
        const histLog = history.map((h, i) => `  ${String(i + 1).padStart(3, ' ')}  ${h}`).join('\n');
        appendOutput(histLog || 'No history recorded yet.');
      } else if (cmd === 'echo') {
        appendOutput(argStr);
      } else if (cmd === 'date' || cmd === 'uptime') {
        const now = new Date();
        appendOutput(`Current Time : ${now.toUTCString()}\nSystem Uptime: 20 years, 8 months, 14 days (Continuous active development)`);
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
   7. Retro 8-bit Cyber-Pikachu RAG Chatbot (PIKACHU.EXE)
   -------------------------------------------------------------------------- */
function initPokemonCompanion() {
  const sprite = document.getElementById('pokemonSprite');
  const chatLog = document.getElementById('pkmnChatLog');
  const chatForm = document.getElementById('pkmnChatForm');
  const chatInput = document.getElementById('pkmnChatInput');
  const quickChips = document.querySelectorAll('.chip-btn');
  const minBtn = document.getElementById('pkmnMinBtn');
  const widget = document.getElementById('pokedexWidget');
  const bar = document.getElementById('pokedexBar');
  const chimeBtn = document.getElementById('pkmnChimeBtn');
  const feedBtn = document.getElementById('pkmnFeedBtn');
  const clearBtn = document.getElementById('pkmnClearBtn');
  const hpFill = document.getElementById('hpFill');
  const hpVal = document.getElementById('hpVal');
  const pkmnLevel = document.getElementById('pkmnLevel');

  if (!chatLog) return;

  let level = 50;
  let exp = 0;

  // Append message to chat log
  function appendChat(speaker, text, isUser = false, isGhost = false) {
    const msg = document.createElement('div');
    msg.className = `chat-msg ${isUser ? 'user-msg' : 'bot-msg'}${isGhost ? ' ghost-scared' : ''}`;

    const label = document.createElement('span');
    label.className = 'chat-speaker';
    label.textContent = speaker;
    msg.appendChild(label);

    const body = document.createElement('span');
    body.innerHTML = text;
    msg.appendChild(body);

    chatLog.appendChild(msg);
    chatLog.scrollTop = chatLog.scrollHeight;
  }

  // Handle Query Submission
  function handleQuery(queryText) {
    if (!queryText || !queryText.trim()) return;
    const cleanQuery = queryText.trim();

    // 1. Add User Message
    appendChat('YOU:', cleanQuery, true, false);

    // 2. Play Spark
    playPikachuSound('spark');

    // 3. Grant EXP
    gainExp(15);

    // 4. Retrieve Answer via Pikachu RAG
    setTimeout(() => {
      const resp = queryPikachuRAG(cleanQuery);
      appendChat('⚡ PIKACHU:', resp.text, false, resp.isGhost);
    }, 200);
  }

  // Gain EXP helper
  function gainExp(amount) {
    exp += amount;
    if (exp >= 100) {
      exp = 0;
      level++;
      if (pkmnLevel) pkmnLevel.textContent = `Lv.${level}`;
      playPikachuSound('levelup');
      appendChat('⚡ SYSTEM:', `LEVEL UP! Pikachu leveled up to <strong>Lv.${level}</strong>! Electric RAG precision boosted!`, false, false);
    }

    if (widget) {
      const float = document.createElement('div');
      float.className = 'exp-float';
      float.textContent = `+${amount} EXP!`;
      float.style.left = '45%';
      float.style.top = '25%';
      widget.appendChild(float);
      setTimeout(() => float.remove(), 900);
    }
  }

  // Event Listeners: Quick Topic Chips
  quickChips.forEach(chip => {
    chip.addEventListener('click', () => {
      const q = chip.getAttribute('data-query');
      if (q) handleQuery(q);
    });
  });

  // Event Listener: Chat Form Submit
  if (chatForm && chatInput) {
    chatForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const val = chatInput.value;
      chatInput.value = '';
      handleQuery(val);
    });
  }

  // Event Listener: Sprite Click (Electro Spark)
  if (sprite) {
    sprite.addEventListener('click', () => {
      playPikachuSound('spark');
      sprite.style.transform = 'scale(1.25) rotate(8deg)';
      setTimeout(() => sprite.style.transform = 'scale(1) rotate(0deg)', 180);
      gainExp(10);
      appendChat('⚡ PIKACHU:', "Pika-CHUUU! ⚡ <em>*cheeks spark with electricity*</em> Ready to answer anything about Advaith! Try tapping the chips below!", false, false);
    });
  }

  // Event Listener: Chime Button
  if (chimeBtn) {
    chimeBtn.addEventListener('click', () => {
      playPikachuSound('spark');
      appendChat('⚡ PIKACHU:', "Pika-pi! ⚡ Synthesized 8-bit electro sparkle!", false, false);
    });
  }

  // Event Listener: Feed Compute Button
  if (feedBtn) {
    feedBtn.addEventListener('click', () => {
      gainExp(35);
      playPikachuSound('levelup');
      appendChat('⚡ PIKACHU:', "Crunch crunch! ⚡ Fed Pikachu 512GB of GPU compute & embeddings! [EXP boosted!]", false, false);
    });
  }

  // Event Listener: Clear Button
  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      chatLog.innerHTML = `
        <div class="chat-msg bot-msg">
          <span class="chat-speaker">⚡ PIKACHU:</span>
          Pika-pika! ⚡ Chat log cleared! Ask me anything about Advaith—chess, football, beatboxing, geopolitics, GenAI, or his fear of ghosts! 👻
        </div>
      `;
    });
  }

  // Event Listener: Minimize / Expand
  if (minBtn) {
    minBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      widget.classList.toggle('minimized');
      minBtn.textContent = widget.classList.contains('minimized') ? '▲ EXPAND' : '_ MINIMIZE';
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
      ragInspectBtn.textContent = isHidden ? '✖ CLOSE HUD' : '🔍 RAG HUD';
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

  const projectDetails = {
    'modal-medianlp': {
      title: 'MEDIA_NLP_PIPELINE // SPECIFICATION & ARCHITECTURE',
      html: `
        <img src="assets/projects/project-media-nlp.jpg" alt="Media NLP Pipeline Architecture" style="width:100%; border:3px solid var(--border-color); box-shadow:4px 4px 0px var(--shadow-color); margin-bottom:16px;">
        <h3 style="font-family:Manrope; font-size:1.4rem; font-weight:800; margin-bottom:12px;">Deterministic Media Rhetoric & Bias Pipeline</h3>
        <p style="margin-bottom:16px;">
          Deterministic media-analysis NLP pipeline that uncovers rhetorical manipulation, informal fallacies, and propaganda framing with <strong>character-level verbatim evidence spans</strong>.
        </p>
        <div style="background:var(--bg-card); border:2px solid var(--border-color); padding:14px; margin-bottom:16px; font-size:0.82rem;">
          <strong>Verified Benchmarks & Architecture:</strong><br>
          • <strong>23 Specialized Detectors</strong>: Ad Hominem, Straw Man, False Equivalence, Loaded Language, Appeal to Authority.<br>
          • <strong>164 Automated Unit & Integration Tests</strong> covering token boundaries and sentence disambiguation.<br>
          • <strong>Measured False Positive Rate</strong>: Only <strong>0.175 per 1,000 words</strong> evaluated on Wikipedia neutral ground truth.<br>
          • <strong>Meta-Inference Topology</strong>: Directed Acyclic Graph (DAG) evaluating compound persuasion intensity.
        </div>
        <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:14px;">
          Stack: Python, spaCy, PySBD, PyTorch, NLTK, VADER, Custom DAG Engine.
        </p>
        <a href="https://github.com/advaithsarva/media-nlp-pipeline" target="_blank" rel="noreferrer" class="btn-gh" style="font-size:0.82rem; padding:8px 16px;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
          EXPLORE REPOSITORY ON GITHUB ↗
        </a>
      `
    },
    'modal-graphrag': {
      title: 'GRAPH_RAG // HYBRID RETRIEVAL ARCHITECTURE',
      html: `
        <img src="assets/projects/project-graph-rag.jpg" alt="Hybrid Graph-RAG Architecture" style="width:100%; border:3px solid var(--border-color); box-shadow:4px 4px 0px var(--shadow-color); margin-bottom:16px;">
        <h3 style="font-family:Manrope; font-size:1.4rem; font-weight:800; margin-bottom:12px;">Hybrid Graph-RAG Knowledge System</h3>
        <p style="margin-bottom:16px;">
          Solves semantic drift and hallucination in dense-vector RAG by fusing BM25 keyword search, HNSW vector similarity, and knowledge-graph traversal into an interpretable query engine.
        </p>
        <div style="background:var(--bg-card); border:2px solid var(--border-color); padding:14px; margin-bottom:16px; font-size:0.82rem;">
          <strong>Architecture Highlights:</strong><br>
          • <strong>Multi-Hop Traversal:</strong> Traverses up to 4 relationship links in Neo4j with full citation back-tracing.<br>
          • <strong>Hybrid Scoring:</strong> Reciprocal Rank Fusion (RRF) blending BM25 (0.35) and Dense Embeddings (0.65).<br>
          • <strong>Credential-Free Local Execution:</strong> Designed to run offline without paid external model APIs.<br>
          • <strong>Rigorous Validation:</strong> 10/10 verified test cases with documented MRR retrieval scores.
        </div>
        <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:14px;">
          Stack: Neo4j, Cypher, FastAPI, LangChain, HuggingFace Transformers, ChromaDB.
        </p>
        <a href="https://github.com/advaithsarva/graph-rag-knowledge-system" target="_blank" rel="noreferrer" class="btn-gh" style="font-size:0.82rem; padding:8px 16px;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
          EXPLORE REPOSITORY ON GITHUB ↗
        </a>
      `
    },
    'modal-perfagent': {
      title: 'AUTONOMOUS_PERF_AGENT // POSTGRES SPECIFICATION',
      html: `
        <img src="assets/projects/project-perf-agent.jpg" alt="Autonomous Postgres Performance Agent Architecture" style="width:100%; border:3px solid var(--border-color); box-shadow:4px 4px 0px var(--shadow-color); margin-bottom:16px;">
        <h3 style="font-family:Manrope; font-size:1.4rem; font-weight:800; margin-bottom:12px;">Autonomous Postgres Performance Agent</h3>
        <p style="margin-bottom:16px;">
          Autonomous database optimization agent that monitors live PostgreSQL queries, diagnoses execution bottlenecks, formulates hypotheses, executes migrations, and evaluates performance deltas.
        </p>
        <div style="background:var(--bg-card); border:2px solid var(--border-color); padding:14px; margin-bottom:16px; font-size:0.82rem;">
          <strong>Measured Impact & Safety:</strong><br>
          • <strong>Measured 11.7x Query Speedup:</strong> Benchmarked on real PostgreSQL workloads across 8/8 evaluation scenarios.<br>
          • <strong>EXPLAIN ANALYZE Cost Parsing:</strong> Accurately isolates sequential scans, hash joins, and memory spillage.<br>
          • <strong>Automated Rollback Guard:</strong> Instantly reverses index creation if latency or buffer cache degrades.<br>
          • <strong>Non-blocking Inspection:</strong> Gathers stats via pg_stat_statements without interrupting live read/write traffic.
        </div>
        <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:14px;">
          Stack: PostgreSQL, Python, AsyncPG, Docker, SQL Query Optimization.
        </p>
        <a href="https://github.com/advaithsarva/autonomous-performance-agent" target="_blank" rel="noreferrer" class="btn-gh" style="font-size:0.82rem; padding:8px 16px;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
          EXPLORE REPOSITORY ON GITHUB ↗
        </a>
      `
    },
    'modal-superbrain': {
      title: 'SUPERBRAIN_MCP // MULTI-AGENT STATE & MEMORY',
      html: `
        <img src="assets/projects/project-superbrain.jpg" alt="SuperBrain MCP Architecture" style="width:100%; border:3px solid var(--border-color); box-shadow:4px 4px 0px var(--shadow-color); margin-bottom:16px;">
        <h3 style="font-family:Manrope; font-size:1.4rem; font-weight:800; margin-bottom:12px;">SuperBrain MCP Multi-Agent Memory</h3>
        <p style="margin-bottom:16px;">
          Unified Model Context Protocol (MCP) server providing persistent cross-session memory, hierarchical state tracking, and execution infrastructure for multi-agent swarms.
        </p>
        <div style="background:var(--bg-card); border:2px solid var(--border-color); padding:14px; margin-bottom:16px; font-size:0.82rem;">
          <strong>Capabilities & Scale:</strong><br>
          • <strong>41 Specialized Tools across 8 Domains:</strong> File manipulation, process control, memory retrieval, task execution.<br>
          • <strong>Persistent Vector Memory:</strong> Vector-embedded episodic memories survive agent restart and workspace switches.<br>
          • <strong>Decoupled Tool Orchestration:</strong> Standardized JSON-RPC protocol implementation with zero memory leaks.<br>
          • <strong>Sub-2ms Protocol Overhead:</strong> Ultra-lean latency enabling real-time agentic tool invocation loops.
        </div>
        <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:14px;">
          Stack: TypeScript, Node.js, Model Context Protocol (MCP), ChromaDB, Vector Embeddings.
        </p>
        <a href="https://github.com/advaithsarva/superbrain_mcp" target="_blank" rel="noreferrer" class="btn-gh" style="font-size:0.82rem; padding:8px 16px;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
          EXPLORE REPOSITORY ON GITHUB ↗
        </a>
      `
    },
    'modal-factcheck': {
      title: 'FACT_CHECK_AGENT // NLI VERIFICATION LOOP',
      html: `
        <img src="assets/projects/project-fact-check.jpg" alt="Fact-Checking NLI Stance Agent Architecture" style="width:100%; border:3px solid var(--border-color); box-shadow:4px 4px 0px var(--shadow-color); margin-bottom:16px;">
        <h3 style="font-family:Manrope; font-size:1.4rem; font-weight:800; margin-bottom:12px;">Fact-Checking NLI Stance Agent</h3>
        <p style="margin-bottom:16px;">
          Autonomous verification agent that takes complex unverified text, decomposes it into atomic factual propositions, and conducts multi-step search and NLI stance reasoning.
        </p>
        <div style="background:var(--bg-card); border:2px solid var(--border-color); padding:14px; margin-bottom:16px; font-size:0.82rem;">
          <strong>Verification Methodology:</strong><br>
          • <strong>Atomic Decomposition:</strong> Breaks claims into independently verifiable subject-predicate triples.<br>
          • <strong>Iterative Search Loop:</strong> Issues targeted queries, assesses source credibility, and gathers evidence passages.<br>
          • <strong>NLI Stance Classification:</strong> Evaluates entailment, neutral, and contradiction with confidence thresholds.<br>
          • <strong>Benchmark Metrics:</strong> 9/10 verdict accuracy on benchmark claims, 15/15 unit test suites passing.
        </div>
        <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:14px;">
          Stack: Python, Transformers, Cross-Encoder NLI, spaCy, PyTorch, Retrieval Systems.
        </p>
        <a href="https://github.com/advaithsarva/fact-checking-agent" target="_blank" rel="noreferrer" class="btn-gh" style="font-size:0.82rem; padding:8px 16px;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
          EXPLORE REPOSITORY ON GITHUB ↗
        </a>
      `
    },
    'modal-transformer': {
      title: 'TRANSFORMER_PRIMITIVES // ARCHITECTURE SPEC',
      html: `
        <img src="assets/projects/project-transformer.jpg" alt="Decoder-Only Transformer Architecture" style="width:100%; border:3px solid var(--border-color); box-shadow:4px 4px 0px var(--shadow-color); margin-bottom:16px;">
        <h3 style="font-family:Manrope; font-size:1.4rem; font-weight:800; margin-bottom:12px;">Decoder-Only Transformer from Primitives</h3>
        <p style="margin-bottom:16px;">
          Ground-up mathematical implementation of an autoregressive transformer written exclusively using PyTorch tensor primitives without high-level nn.Transformer abstractions.
        </p>
        <div style="background:var(--bg-card); border:2px solid var(--border-color); padding:14px; margin-bottom:16px; font-size:0.82rem;">
          <strong>Rigorous Numerical Verification:</strong><br>
          • <strong>1e-5 Torch Parity:</strong> Every layer (Multi-Head Attention, RMSNorm/LayerNorm, SwiGLU) verified to 1e-5 against PyTorch.<br>
          • <strong>Convergence:</strong> Achieved <strong>1.0059x of computable entropy floor</strong> on synthetic language tasks.<br>
          • <strong>Published Negative Ablations:</strong> Explicitly documented 3 architectural ablations that failed to match baseline.<br>
          • <strong>19/19 Test Cases:</strong> Verified causal masking, gradient flow, residual scaling, and batch training.
        </div>
        <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:14px;">
          Stack: PyTorch, Pure Tensor Algebra, CUDA Kernels, Mathematical Optimization.
        </p>
        <a href="https://github.com/advaithsarva/transformer-from-scratch" target="_blank" rel="noreferrer" class="btn-gh" style="font-size:0.82rem; padding:8px 16px;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
          EXPLORE REPOSITORY ON GITHUB ↗
        </a>
      `
    }
  };

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
  if (!clockEl) return;

  function update() {
    const now = new Date();
    const utc = now.toUTCString().split(' ')[4] + ' UTC';
    clockEl.textContent = utc;
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
      copyBtn.textContent = 'COPIED TO CLIPBOARD! ✓';
      copyBtn.style.backgroundColor = '#168F3E';
      copyBtn.style.color = '#FFFFFF';
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
