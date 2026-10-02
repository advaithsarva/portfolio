import os
import json

PORTFOLIO_DIR = r"C:\Projects\portfolio-zer0"

# 1. CSS to append to style.css
catalog_css = """
/* ==========================================================================
   Vibrant Neo-Brutalist Projects Catalog & Dual-Card Architecture
   ========================================================================== */
.projects-hero-banner {
  padding: 36px 30px;
  background-color: var(--bg-card);
  border: 3px solid var(--border-color);
  box-shadow: 6px 6px 0px var(--shadow-color);
  margin: 24px 0 28px 0;
  position: relative;
  overflow: hidden;
}

.projects-hero-banner::after {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 140px;
  height: 100%;
  background: repeating-linear-gradient(
    45deg,
    rgba(0,0,0,0.03),
    rgba(0,0,0,0.03) 10px,
    transparent 10px,
    transparent 20px
  );
  pointer-events: none;
}

.hero-tag-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 12px;
}

.projects-hero-title {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 2.2rem;
  font-weight: 800;
  margin: 0 0 10px 0;
  letter-spacing: -0.02em;
}

.projects-hero-sub {
  font-size: 1.05rem;
  line-height: 1.6;
  color: var(--text-main);
  max-width: 880px;
  margin: 0;
}

/* Category Color System */
.cat-badge-hackathon { background-color: #FACC15 !important; color: #131200 !important; border: 2px solid #000 !important; font-weight: 800; }
.cat-badge-ai-agents { background-color: #8B5CF6 !important; color: #FFFFFF !important; border: 2px solid #000 !important; font-weight: 800; }
.cat-badge-nlp-rag { background-color: #06B6D4 !important; color: #131200 !important; border: 2px solid #000 !important; font-weight: 800; }
.cat-badge-ml-data { background-color: #10B981 !important; color: #FFFFFF !important; border: 2px solid #000 !important; font-weight: 800; }
.cat-badge-systems { background-color: #F97316 !important; color: #FFFFFF !important; border: 2px solid #000 !important; font-weight: 800; }
.cat-badge-full-stack { background-color: #2563EB !important; color: #FFFFFF !important; border: 2px solid #000 !important; font-weight: 800; }
.cat-badge-in-progress { background-color: #F43F5E !important; color: #FFFFFF !important; border: 2px solid #000 !important; font-weight: 800; }

.cat-border-hackathon { border-top: 6px solid #FACC15 !important; }
.cat-border-ai-agents { border-top: 6px solid #8B5CF6 !important; }
.cat-border-nlp-rag { border-top: 6px solid #06B6D4 !important; }
.cat-border-ml-data { border-top: 6px solid #10B981 !important; }
.cat-border-systems { border-top: 6px solid #F97316 !important; }
.cat-border-full-stack { border-top: 6px solid #2563EB !important; }
.cat-border-in-progress { border-top: 6px solid #F43F5E !important; }

/* Technology & Tooling Filter Bar */
.tech-filter-wrapper {
  margin-bottom: 24px;
}

.tech-filter-label {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.72rem;
  font-weight: 800;
  color: var(--color-blueprint);
  margin-bottom: 8px;
  display: block;
  letter-spacing: 0.06em;
}

.tech-filter-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  background-color: var(--bg-surface);
  border: 2px solid var(--border-color);
  padding: 12px;
  box-shadow: 3px 3px 0px var(--shadow-color);
}

.tech-chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.74rem;
  font-weight: 700;
  padding: 6px 12px;
  border: 2px solid var(--border-color);
  background-color: var(--bg-card);
  color: var(--text-main);
  box-shadow: 2px 2px 0px var(--shadow-color);
  cursor: pointer;
  transition: all 0.12s ease;
  user-select: none;
}

.tech-chip:hover {
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0px var(--shadow-color);
  background-color: #FEF9C3;
}

.tech-chip.active {
  background-color: #FACC15 !important;
  color: #131200 !important;
  border-color: #000000 !important;
  font-weight: 800;
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0px var(--shadow-color);
}

[data-theme="dark"] .tech-chip:hover {
  background-color: #38311B;
}

/* Category Tabs and Controls Row */
.catalog-toolbar {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 24px;
}

.catalog-cats-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.cat-pill {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.76rem;
  font-weight: 700;
  padding: 7px 14px;
  border: 2px solid var(--border-color);
  background-color: var(--bg-surface);
  color: var(--text-main);
  cursor: pointer;
  box-shadow: 2px 2px 0px var(--shadow-color);
  transition: all 0.12s ease;
}

.cat-pill:hover {
  transform: translate(-1px, -1px);
  box-shadow: 3px 3px 0px var(--shadow-color);
}

.cat-pill.active {
  background-color: var(--text-main);
  color: var(--bg-body);
  border-color: var(--text-main);
  box-shadow: 3px 3px 0px var(--shadow-color);
}

.catalog-search-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  background-color: var(--bg-card);
  padding: 12px 18px;
  border: 2px solid var(--border-color);
  box-shadow: 3px 3px 0px var(--shadow-color);
}

.search-box-wrapper {
  display: flex;
  align-items: center;
  gap: 8px;
  flex: 1;
  max-width: 480px;
}

.catalog-search-input {
  width: 100%;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.86rem;
  padding: 8px 12px;
  border: 2px solid var(--border-color);
  background-color: var(--bg-surface);
  color: var(--text-main);
}

.catalog-search-input:focus {
  outline: none;
  border-color: var(--color-blueprint);
  box-shadow: 0 0 0 2px var(--color-blueprint);
}

.view-mode-group {
  display: flex;
  align-items: center;
  gap: 6px;
}

.view-mode-label {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--text-muted);
  margin-right: 4px;
}

.view-mode-btn {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.72rem;
  font-weight: 700;
  padding: 6px 10px;
  border: 2px solid var(--border-color);
  background-color: var(--bg-surface);
  color: var(--text-main);
  cursor: pointer;
  box-shadow: 1.5px 1.5px 0px var(--shadow-color);
  transition: all 0.1s ease;
}

.view-mode-btn.active {
  background-color: var(--color-blueprint);
  color: #FFFFFF;
  border-color: var(--color-blueprint);
}

/* Projects Grid & Units */
.projects-master-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
  gap: 28px;
  margin-bottom: 60px;
}

.project-unit {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

/* Main Human Project Card */
.project-card-human {
  border: 3px solid var(--border-color);
  background-color: var(--bg-card);
  box-shadow: 5px 5px 0px var(--shadow-color);
  padding: 22px;
  display: flex;
  flex-direction: column;
  transition: transform 0.15s ease, box-shadow 0.15s ease;
  height: 100%;
}

.project-card-human:hover {
  transform: translate(-3px, -3px);
  box-shadow: 8px 8px 0px var(--shadow-color);
}

.card-top-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.card-slug-id {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--text-muted);
}

.card-headline-title {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.35rem;
  font-weight: 800;
  margin: 0 0 6px 0;
  line-height: 1.3;
}

.card-problem-tagline {
  font-size: 0.92rem;
  font-style: italic;
  color: var(--color-blueprint);
  margin-bottom: 12px;
  line-height: 1.4;
  font-weight: 600;
}

.card-human-desc {
  font-size: 0.9rem;
  line-height: 1.6;
  color: var(--text-main);
  margin-bottom: 16px;
  flex-grow: 1;
}

.card-tech-badges-row {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 18px;
}

.card-actions-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: center;
  padding-top: 12px;
  border-top: 2px dashed var(--border-color);
}

.btn-deep-dive {
  background-color: #FACC15 !important;
  color: #131200 !important;
  font-weight: 800 !important;
  border: 2px solid #000000 !important;
  padding: 7px 16px !important;
  box-shadow: 2.5px 2.5px 0px var(--shadow-color) !important;
}

.btn-deep-dive:hover {
  background-color: #EAB308 !important;
}

.btn-tech-toggle {
  background-color: var(--bg-surface);
  color: var(--text-main);
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.74rem;
  font-weight: 700;
  padding: 6px 12px;
  border: 2px solid var(--border-color);
  box-shadow: 2px 2px 0px var(--shadow-color);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-left: auto;
  transition: all 0.1s ease;
}

.btn-tech-toggle:hover {
  background-color: #E0E7FF;
  color: #1D4ED8;
  transform: translate(-1px, -1px);
}

/* Dedicated Technical Proof Card */
.project-card-tech {
  border: 2px solid var(--border-color);
  background-color: var(--bg-surface);
  box-shadow: 4px 4px 0px var(--shadow-color);
  margin-top: -4px;
  display: flex;
  flex-direction: column;
  transition: all 0.2s ease;
}

.tech-card-header {
  background-color: #1E293B;
  color: #F8FAFC;
  padding: 8px 14px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.04em;
}

.tech-card-header .dots {
  display: flex;
  gap: 5px;
}

.tech-card-header .dots span {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  display: inline-block;
}

.dot-red { background: #EF4444; }
.dot-yellow { background: #F59E0B; }
.dot-green { background: #10B981; }

.tech-card-body {
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  font-size: 0.82rem;
}

.metric-badges-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.metric-chip {
  background-color: var(--bg-card);
  border: 1.5px solid var(--border-color);
  padding: 4px 8px;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.74rem;
  font-weight: 700;
  color: var(--color-blueprint);
  box-shadow: 1.5px 1.5px 0px var(--shadow-color);
}

.tech-highlights-box {
  margin: 0;
  padding-left: 20px;
  line-height: 1.5;
  color: var(--text-main);
}

.tech-highlights-box li {
  margin-bottom: 6px;
}

.tech-honest-banner {
  background-color: #FEF3C7;
  border-left: 4px solid #F59E0B;
  padding: 8px 12px;
  font-size: 0.78rem;
  line-height: 1.45;
  color: #92400E;
}

[data-theme="dark"] .tech-honest-banner {
  background-color: #2D2516;
  color: #FBBF24;
}
"""

with open(os.path.join(PORTFOLIO_DIR, "style.css"), "r", encoding="utf-8") as f:
    style_content = f.read()

if "projects-hero-banner" not in style_content:
    with open(os.path.join(PORTFOLIO_DIR, "style.css"), "a", encoding="utf-8") as f:
        f.write("\n" + catalog_css)
    print("Added vibrant catalog CSS to style.css")
else:
    print("Catalog CSS already present in style.css")

# 2. Build the new projects.html
new_projects_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Projects Catalog // Advaith Narayana Sarva — 39 Verified Systems</title>
  <meta name="description" content="Complete catalog of 39 AI Agent, NLP, RAG, ML, and Systems from Scratch projects built and verified by Advaith Narayana Sarva.">
  <link rel="stylesheet" href="style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Manrope:wght@600;700;800&family=Space+Grotesk:wght@600;700;800&display=swap" rel="stylesheet">
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

  <main class="page-container" style="max-width: 1350px; margin: 0 auto; padding: 20px;">
    <!-- High-Density Hero Dashboard Banner -->
    <div class="projects-hero-banner">
      <div class="hero-tag-row">
        <span class="badge-tag bg-blueprint text-white">SYSTEMS ARCHIVE // 39 REPOSITORIES</span>
        <span class="badge-tag cat-badge-hackathon">★ TOP 5 SOUTH ZONE HACKATHON</span>
        <span class="badge-tag cat-badge-ai-agents">9 AI AGENTS</span>
        <span class="badge-tag cat-badge-nlp-rag">8 GRAPH-RAG &amp; NLP</span>
      </div>
      <h1 class="projects-hero-title">ENGINEERING REPOSITORIES &amp; ARCHITECTURES</h1>
      <p class="projects-hero-sub">
        "I build systems, then prove they work." 39 working repositories with reproducible code, automated test suites, and verified benchmarks. Filter by core technology or problem domain below.
      </p>
    </div>

    <!-- 01 // Interactive Skills & Technology Filter Bar -->
    <div class="tech-filter-wrapper">
      <span class="tech-filter-label">⚡ FILTER BY CORE TECHNOLOGY &amp; TOOLING:</span>
      <div class="tech-filter-bar" id="techFilterBar">
        <button type="button" class="tech-chip active" data-tech="all">
          <span>ALL TECH (39)</span>
        </button>
        <button type="button" class="tech-chip" data-tech="python">
          <svg class="tech-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M11.92 2C6.98 2 7.28 4.14 7.28 4.14L7.3 6.34H12.1V7.07H5.32S2 6.7 2 11.66C2 16.62 4.9 16.36 4.9 16.36H6.55V14.07C6.55 11.38 8.87 11.45 8.87 11.45H13.68C15.93 11.45 16.14 9.35 16.14 9.35V4.32C16.14 4.32 16.51 2 11.92 2ZM9.07 3.51C9.64 3.51 10.1 3.97 10.1 4.54C10.1 5.11 9.64 5.57 9.07 5.57C8.5 5.57 8.04 5.11 8.04 4.54C8.04 3.97 8.5 3.51 9.07 3.51Z" fill="#3776AB"/><path d="M12.08 22C17.02 22 16.72 19.86 16.72 19.86L16.7 17.66H11.9V16.93H18.68S22 17.3 22 12.34C22 7.38 19.1 7.64 19.1 7.64H17.45V9.93C17.45 12.62 15.13 12.55 15.13 12.55H10.32C8.07 12.55 7.86 14.65 7.86 14.65V19.68C7.86 19.68 7.49 22 12.08 22ZM14.93 20.49C14.36 20.49 13.9 20.03 13.9 19.46C13.9 18.89 14.36 18.43 14.93 18.43C15.5 18.43 15.96 18.89 15.96 19.46C15.96 20.03 15.5 20.49 14.93 20.49Z" fill="#FFD43B"/></svg>
          <span>Python (34)</span>
        </button>
        <button type="button" class="tech-chip" data-tech="sql">
          <svg class="tech-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3" fill="#336791" stroke="#131200"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>
          <span>SQL &amp; Databases</span>
        </button>
        <button type="button" class="tech-chip" data-tech="aws">
          <svg class="tech-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M18.75 14.45c-2.3 1.55-5.35 2.37-8.25 2.37-4.1 0-7.8-1.5-10.6-4-.2-.18-.04-.42.2-.28 3.02 1.76 6.7 2.82 10.4 2.82 2.6 0 5.42-.64 7.95-1.97.38-.2.7.27.3.56z" fill="#FF9900"/><path d="M19.78 13.43c-.3-.37-1.92-.18-2.65-.09-.22.03-.26-.14-.06-.27 1.3-.87 3.42-.62 3.68-.3.26.32-.08 2.43-1.31 3.39-.19.15-.36.07-.27-.13.3-.67.91-2.23.61-2.6z" fill="#FF9900"/><path d="M6.5 8h1.8v4.5H6.5zm4 -2h1.8v6.5h-1.8zm4 2h1.8v4.5h-1.8z" fill="#232F3E"/></svg>
          <span>AWS Cloud</span>
        </button>
        <button type="button" class="tech-chip" data-tech="docker">
          <svg class="tech-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4.6 11.2h2.2v2.2H4.6zm2.8 0h2.2v2.2H7.4zm2.8 0h2.2v2.2h-2.2zm2.8 0h2.2v2.2h-2.2zm-5.6-2.8h2.2v2.2H7.4zm2.8 0h2.2v2.2h-2.2zm2.8 0h2.2v2.2h-2.2zm2.8 0h2.2v2.2h-2.2zm-2.8-2.8h2.2v2.2h-2.2z" fill="#2496ED"/><path d="M22.5 11.5c-.5-.4-1.5-.5-2.2-.2-.2-.7-.7-1.4-1.4-1.8l-.6-.3-.4.6c-.4.6-.5 1.4-.4 2.1-.8.4-2.1.4-2.9 0H1c-.3 1.8.2 4.1 1.6 5.6 1.7 1.9 4.3 2.7 7.4 2.7 6.4 0 11.2-3.8 12.3-7.7.7-.2 1.4-.7 1.7-1.3l.1-.3-.6-.7h-.6z" fill="#2496ED"/></svg>
          <span>Docker</span>
        </button>
        <button type="button" class="tech-chip" data-tech="pytorch">
          <svg class="tech-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12.6 2.1a1 1 0 0 0-1.2 0L6.2 6.3a8.8 8.8 0 1 0 11.6 0L12.6 2.1zm-1.8 17.5a6.8 6.8 0 0 1-4.8-11.6l4.8-3.9 4.8 3.9a6.8 6.8 0 0 1-4.8 11.6z" fill="#EE4C2C"/><circle cx="15.8" cy="6.2" r="1.5" fill="#EE4C2C"/></svg>
          <span>PyTorch &amp; ML</span>
        </button>
        <button type="button" class="tech-chip" data-tech="neo4j">
          <svg class="tech-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="6" cy="18" r="3.5" fill="#008CC1"/><circle cx="18" cy="18" r="3.5" fill="#008CC1"/><circle cx="18" cy="6" r="3.5" fill="#008CC1"/><circle cx="6" cy="6" r="3.5" fill="#008CC1"/><path d="M8.5 7.5l7 7M8.5 16.5l7-7M6 9.5v5M18 9.5v5" stroke="#008CC1" stroke-width="2"/></svg>
          <span>Graph &amp; Neo4j</span>
        </button>
        <button type="button" class="tech-chip" data-tech="fastapi">
          <svg class="tech-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" fill="#009688"/><path d="M12.8 4.5L7.2 13.2h4.5l-1.5 6.3 6.6-9.6h-4.8l.8-5.4z" fill="#ffffff"/></svg>
          <span>FastAPI &amp; APIs</span>
        </button>
        <button type="button" class="tech-chip" data-tech="node">
          <svg class="tech-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="24" height="24" rx="3" fill="#3178C6"/><path d="M4 10.5h6.5M7.25 10.5v8" stroke="#ffffff" stroke-width="2.2" stroke-linecap="square"/><path d="M13.5 17c1 .8 2.3 1.1 3.5.7 1.1-.4 1.8-1.5 1.5-2.6-.4-1.3-2.1-1.6-3.2-2.1-1-.4-1.8-1.2-1.6-2.3.2-1.1 1.2-1.9 2.3-1.9 1 0 2 .4 2.7 1" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round"/></svg>
          <span>TypeScript &amp; Node</span>
        </button>
        <button type="button" class="tech-chip" data-tech="nlp">
          <svg class="tech-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83" stroke="#F59E0B"/><circle cx="12" cy="12" r="4" fill="#F59E0B"/></svg>
          <span>NLP &amp; RAG</span>
        </button>
        <button type="button" class="tech-chip" data-tech="linux">
          <svg class="tech-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5" stroke="#10B981"/><line x1="12" y1="19" x2="20" y2="19" stroke="#10B981"/></svg>
          <span>Linux &amp; Systems</span>
        </button>
      </div>
    </div>

    <!-- 02 // Category Pills & View Switcher Row -->
    <div class="catalog-toolbar">
      <div class="catalog-cats-row" id="categoryPills">
        <button class="cat-pill active" data-cat="All">ALL (39)</button>
        <button class="cat-pill" data-cat="Hackathon">HACKATHON (1)</button>
        <button class="cat-pill" data-cat="AI Agents">AI AGENTS (9)</button>
        <button class="cat-pill" data-cat="NLP &amp; RAG">NLP &amp; RAG (8)</button>
        <button class="cat-pill" data-cat="ML &amp; Data">ML &amp; DATA (5)</button>
        <button class="cat-pill" data-cat="Systems from Scratch">SYSTEMS (6)</button>
        <button class="cat-pill" data-cat="Full-Stack">FULL-STACK (6)</button>
        <button class="cat-pill" data-cat="In Progress">IN PROGRESS (4)</button>
      </div>

      <!-- Search & View Mode Switcher -->
      <div class="catalog-search-row">
        <div class="search-box-wrapper">
          <span style="font-family:'IBM Plex Mono',monospace; font-weight:800;">🔍</span>
          <input type="text" id="projectSearch" class="catalog-search-input" placeholder="Search by name, problem, algorithm, or metric...">
        </div>

        <div style="font-family:'IBM Plex Mono',monospace; font-size:0.75rem; font-weight:700;">
          Showing <span id="matchCount" style="color:var(--color-blueprint); font-weight:800;">39</span> of 39 repositories
        </div>

        <div class="view-mode-group">
          <span class="view-mode-label">VIEW:</span>
          <button type="button" class="view-mode-btn active" id="btnViewHuman" title="Clean, human-readable product cards">🎯 PRODUCT</button>
          <button type="button" class="view-mode-btn" id="btnViewTech" title="Hardcore engineering proof &amp; metric audit cards">🔬 TECH AUDIT</button>
          <button type="button" class="view-mode-btn" id="btnViewBoth" title="Show both product overview and technical card">⚡ DUAL VIEW</button>
        </div>
      </div>
    </div>

    <!-- 03 // 39 Projects Master Grid (Dual-Card Architecture) -->
    <div class="projects-master-grid" id="projectsGrid"></div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-left">
        <span class="footer-stamp">© 2026 ADVAITH NARAYANA SARVA</span>
        <span class="footer-sub">39 Projects</span>
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
  <script src="tech-icons.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      // Theme Toggle
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

      // Live UTC Clock
      function updateClock() {
        const clock = document.getElementById('liveClock');
        if (clock) {
          const now = new Date();
          clock.textContent = now.toUTCString().split(' ')[4] + ' UTC';
        }
      }
      updateClock();
      setInterval(updateClock, 1000);

      // Filtering & View State
      const grid = document.getElementById('projectsGrid');
      const catPills = document.querySelectorAll('.cat-pill');
      const techChips = document.querySelectorAll('.tech-chip');
      const searchInput = document.getElementById('projectSearch');
      const matchCountSpan = document.getElementById('matchCount');

      let currentCat = 'All';
      let currentTech = 'all';
      let searchQuery = '';
      let viewMode = 'human'; // 'human', 'tech', 'both'

      // View Mode Buttons
      const btnHuman = document.getElementById('btnViewHuman');
      const btnTech = document.getElementById('btnViewTech');
      const btnBoth = document.getElementById('btnViewBoth');

      function setViewMode(mode) {
        viewMode = mode;
        [btnHuman, btnTech, btnBoth].forEach(b => b.classList.remove('active'));
        if (mode === 'human') btnHuman.classList.add('active');
        else if (mode === 'tech') btnTech.classList.add('active');
        else if (mode === 'both') btnBoth.classList.add('active');
        render();
      }

      btnHuman.addEventListener('click', () => setViewMode('human'));
      btnTech.addEventListener('click', () => setViewMode('tech'));
      btnBoth.addEventListener('click', () => setViewMode('both'));

      // Helper: Category Theme Classes
      function getCategoryClasses(cat) {
        const c = String(cat).toLowerCase();
        if (c.includes('hackathon')) return { badge: 'cat-badge-hackathon', border: 'cat-border-hackathon' };
        if (c.includes('agent')) return { badge: 'cat-badge-ai-agents', border: 'cat-border-ai-agents' };
        if (c.includes('nlp') || c.includes('rag')) return { badge: 'cat-badge-nlp-rag', border: 'cat-border-nlp-rag' };
        if (c.includes('ml') || c.includes('data')) return { badge: 'cat-badge-ml-data', border: 'cat-border-ml-data' };
        if (c.includes('system')) return { badge: 'cat-badge-systems', border: 'cat-border-systems' };
        if (c.includes('full-stack') || c.includes('fullstack')) return { badge: 'cat-badge-full-stack', border: 'cat-border-full-stack' };
        if (c.includes('progress')) return { badge: 'cat-badge-in-progress', border: 'cat-border-in-progress' };
        return { badge: 'bg-blueprint text-white', border: '' };
      }

      // Helper: Check if project matches selected technology filter
      function matchesTech(p, techKey) {
        if (!techKey || techKey === 'all') return true;
        const allText = (p.tags.join(' ') + ' ' + p.overview + ' ' + p.title).toLowerCase();
        if (techKey === 'python') return allText.includes('python');
        if (techKey === 'sql') return allText.includes('sql') || allText.includes('postgres') || allText.includes('sqlite') || allText.includes('database');
        if (techKey === 'aws') return allText.includes('aws') || allText.includes('cloud') || allText.includes('s3') || allText.includes('ec2') || allText.includes('terraform');
        if (techKey === 'docker') return allText.includes('docker') || allText.includes('container');
        if (techKey === 'pytorch') return allText.includes('pytorch') || allText.includes('torch') || allText.includes('machine learning');
        if (techKey === 'neo4j') return allText.includes('neo4j') || allText.includes('graph') || allText.includes('cypher');
        if (techKey === 'fastapi') return allText.includes('fastapi') || allText.includes('flask') || allText.includes('api');
        if (techKey === 'node') return allText.includes('node') || allText.includes('typescript') || allText.includes('javascript') || allText.includes('express');
        if (techKey === 'nlp') return allText.includes('nlp') || allText.includes('rag') || allText.includes('llm') || allText.includes('spacy');
        if (techKey === 'linux') return allText.includes('linux') || allText.includes('bash') || allText.includes('shell') || allText.includes('operating systems') || allText.includes('c');
        return true;
      }

      // Main Render Function
      function render() {
        grid.innerHTML = '';
        const filtered = window.ALL_PROJECTS.filter(p => {
          const matchCat = (currentCat === 'All' || p.category === currentCat || (currentCat === 'Systems from Scratch' && p.category.includes('System')));
          const matchT = matchesTech(p, currentTech);
          const q = searchQuery.toLowerCase();
          const matchQ = !q || 
            p.title.toLowerCase().includes(q) || 
            p.tagline.toLowerCase().includes(q) || 
            p.overview.toLowerCase().includes(q) || 
            p.tags.some(t => t.toLowerCase().includes(q)) || 
            p.stats.toLowerCase().includes(q);
          return matchCat && matchT && matchQ;
        });

        matchCountSpan.textContent = filtered.length;

        if (filtered.length === 0) {
          grid.innerHTML = '<div style="grid-column: 1/-1; padding: 50px 20px; text-align: center; border: 3px dashed var(--border-color); background:var(--bg-card); font-family: monospace; font-size: 1.05rem;">No repositories match this combination. Try clicking "ALL TECH" or resetting search keywords.</div>';
          return;
        }

        filtered.forEach(p => {
          const catStyles = getCategoryClasses(p.category);
          const unit = document.createElement('div');
          unit.className = 'project-unit';

          // Clean metrics for technical card
          const statItems = p.stats.split('·').map(s => s.trim()).filter(Boolean);
          const metricBadgesHtml = statItems.map(s => `<span class="metric-chip">⚡ ${s}</span>`).join('');

          // Highlights for technical card
          const highlightsHtml = (p.highlights || []).slice(0, 3).map(h => `<li>${h}</li>`).join('');

          // Repo action button
          let repoBtn = '';
          if (p.links && p.links.startsWith('http')) {
            repoBtn = `<a href="${p.links}" target="_blank" class="neo-btn btn-secondary" style="padding:6px 12px; font-size:0.75rem;">GITHUB ↗</a>`;
          } else {
            repoBtn = `<span style="font-family:'IBM Plex Mono',monospace; font-size:0.68rem; padding:6px 10px; background:var(--bg-surface); border:1.5px solid var(--border-color); color:var(--text-muted);">PRIVATE REPO</span>`;
          }

          // Tech tags with logos
          const tagsHtml = p.tags.map(t => window.TechIcons ? window.TechIcons.renderTechBadge(t) : `<span class="badge-tag">${t}</span>`).join('');

          // Human Product Card HTML
          const humanCardHtml = `
            <div class="project-card-human ${catStyles.border}">
              <div class="card-top-row">
                <span class="badge-tag ${catStyles.badge}">${p.category.toUpperCase()}</span>
                <span class="card-slug-id">#${p.slug}</span>
              </div>
              <h3 class="card-headline-title">${p.title}</h3>
              <div class="card-problem-tagline">"${p.tagline}"</div>
              <p class="card-human-desc">${p.card || p.overview}</p>
              
              <div class="card-tech-badges-row">
                ${tagsHtml}
              </div>

              <div class="card-actions-row">
                <a href="project.html?id=${p.slug}" class="neo-btn btn-deep-dive">DEEP DIVE →</a>
                ${repoBtn}
                <button type="button" class="btn-tech-toggle" data-slug="${p.slug}" title="Toggle Technical Proof &amp; Metric Card">
                  <span>🔬 TECH SPECS</span>
                  <span class="toggle-arrow">▾</span>
                </button>
              </div>
            </div>
          `;

          // Dedicated Technical Proof Card HTML
          const techCardHtml = `
            <div class="project-card-tech" id="techCard-${p.slug}" style="${viewMode === 'human' ? 'display:none;' : 'display:flex;'}">
              <div class="tech-card-header">
                <span>⚡ SPECS_AND_METRICS.LOG // #${p.slug}</span>
                <div class="dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
              </div>
              <div class="tech-card-body">
                <div>
                  <strong style="font-family:'IBM Plex Mono',monospace; font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">VERIFIED BENCHMARKS &amp; AUDIT:</strong>
                  <div class="metric-badges-grid">
                    ${metricBadgesHtml}
                  </div>
                </div>

                <div>
                  <strong style="font-family:'IBM Plex Mono',monospace; font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">PROVEN IMPLEMENTATION HIGHLIGHTS:</strong>
                  <ul class="tech-highlights-box">
                    ${highlightsHtml}
                  </ul>
                </div>

                <div class="tech-honest-banner">
                  <strong>⚠️ LIMITATION &amp; WHAT'S NEXT:</strong> ${p.honest}
                </div>
              </div>
            </div>
          `;

          // Compose unit based on view mode
          if (viewMode === 'tech') {
            unit.innerHTML = techCardHtml;
            // Force display block for tech mode
            unit.querySelector('.project-card-tech').style.display = 'flex';
          } else {
            unit.innerHTML = humanCardHtml + techCardHtml;
          }

          grid.appendChild(unit);
        });

        // Attach event listeners for per-card tech toggles
        document.querySelectorAll('.btn-tech-toggle').forEach(btn => {
          btn.addEventListener('click', (e) => {
            const slug = btn.getAttribute('data-slug');
            const targetTechCard = document.getElementById(`techCard-${slug}`);
            const arrow = btn.querySelector('.toggle-arrow');
            if (targetTechCard) {
              if (targetTechCard.style.display === 'none' || !targetTechCard.style.display) {
                targetTechCard.style.display = 'flex';
                arrow.textContent = '▴';
                btn.style.backgroundColor = '#FACC15';
                btn.style.color = '#131200';
              } else {
                targetTechCard.style.display = 'none';
                arrow.textContent = '▾';
                btn.style.backgroundColor = '';
                btn.style.color = '';
              }
            }
          });
        });
      }

      // Category Pill Listeners
      catPills.forEach(pill => {
        pill.addEventListener('click', () => {
          catPills.forEach(p => p.classList.remove('active'));
          pill.classList.add('active');
          currentCat = pill.getAttribute('data-cat');
          render();
        });
      });

      // Technology Chip Listeners
      techChips.forEach(chip => {
        chip.addEventListener('click', () => {
          techChips.forEach(c => c.classList.remove('active'));
          chip.classList.add('active');
          currentTech = chip.getAttribute('data-tech');
          render();
        });
      });

      // Search Input Listener
      searchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value.trim();
        render();
      });

      // Initial Render
      render();
    });
  </script>
</body>
</html>
"""

with open(os.path.join(PORTFOLIO_DIR, "projects.html"), "w", encoding="utf-8") as f:
    f.write(new_projects_html)

print("Generated new vibrant projects.html with Dual-Card architecture and tech filters.")
