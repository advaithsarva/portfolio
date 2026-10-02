import os
import json
import re

PORTFOLIO_DIR = r"C:\Projects\portfolio-zer0"
PROJECTS_DIR = os.path.join(PORTFOLIO_DIR, "projects")

# 1. Tech SVG Icons Dictionary
SVG_ICONS = {
    "python": '''<svg class="tech-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M11.92 2C6.98 2 7.28 4.14 7.28 4.14L7.3 6.34H12.1V7.07H5.32S2 6.7 2 11.66C2 16.62 4.9 16.36 4.9 16.36H6.55V14.07C6.55 11.38 8.87 11.45 8.87 11.45H13.68C15.93 11.45 16.14 9.35 16.14 9.35V4.32C16.14 4.32 16.51 2 11.92 2ZM9.07 3.51C9.64 3.51 10.1 3.97 10.1 4.54C10.1 5.11 9.64 5.57 9.07 5.57C8.5 5.57 8.04 5.11 8.04 4.54C8.04 3.97 8.5 3.51 9.07 3.51Z" fill="#3776AB"/><path d="M12.08 22C17.02 22 16.72 19.86 16.72 19.86L16.7 17.66H11.9V16.93H18.68S22 17.3 22 12.34C22 7.38 19.1 7.64 19.1 7.64H17.45V9.93C17.45 12.62 15.13 12.55 15.13 12.55H10.32C8.07 12.55 7.86 14.65 7.86 14.65V19.68C7.86 19.68 7.49 22 12.08 22ZM14.93 20.49C14.36 20.49 13.9 20.03 13.9 19.46C13.9 18.89 14.36 18.43 14.93 18.43C15.5 18.43 15.96 18.89 15.96 19.46C15.96 20.03 15.5 20.49 14.93 20.49Z" fill="#FFD43B"/></svg>''',
    "sql": '''<svg class="tech-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3" fill="#336791" stroke="#131200"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>''',
    "postgresql": '''<svg class="tech-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z" fill="#336791"/></svg>''',
    "aws": '''<svg class="tech-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M18.75 14.45c-2.3 1.55-5.35 2.37-8.25 2.37-4.1 0-7.8-1.5-10.6-4-.2-.18-.04-.42.2-.28 3.02 1.76 6.7 2.82 10.4 2.82 2.6 0 5.42-.64 7.95-1.97.38-.2.7.27.3.56z" fill="#FF9900"/><path d="M19.78 13.43c-.3-.37-1.92-.18-2.65-.09-.22.03-.26-.14-.06-.27 1.3-.87 3.42-.62 3.68-.3.26.32-.08 2.43-1.31 3.39-.19.15-.36.07-.27-.13.3-.67.91-2.23.61-2.6z" fill="#FF9900"/><path d="M6.5 8h1.8v4.5H6.5zm4 -2h1.8v6.5h-1.8zm4 2h1.8v4.5h-1.8z" fill="#232F3E"/></svg>''',
    "docker": '''<svg class="tech-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4.6 11.2h2.2v2.2H4.6zm2.8 0h2.2v2.2H7.4zm2.8 0h2.2v2.2h-2.2zm2.8 0h2.2v2.2h-2.2zm-5.6-2.8h2.2v2.2H7.4zm2.8 0h2.2v2.2h-2.2zm2.8 0h2.2v2.2h-2.2zm2.8 0h2.2v2.2h-2.2zm-2.8-2.8h2.2v2.2h-2.2z" fill="#2496ED"/><path d="M22.5 11.5c-.5-.4-1.5-.5-2.2-.2-.2-.7-.7-1.4-1.4-1.8l-.6-.3-.4.6c-.4.6-.5 1.4-.4 2.1-.8.4-2.1.4-2.9 0H1c-.3 1.8.2 4.1 1.6 5.6 1.7 1.9 4.3 2.7 7.4 2.7 6.4 0 11.2-3.8 12.3-7.7.7-.2 1.4-.7 1.7-1.3l.1-.3-.6-.7h-.6z" fill="#2496ED"/></svg>''',
    "pytorch": '''<svg class="tech-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12.6 2.1a1 1 0 0 0-1.2 0L6.2 6.3a8.8 8.8 0 1 0 11.6 0L12.6 2.1zm-1.8 17.5a6.8 6.8 0 0 1-4.8-11.6l4.8-3.9 4.8 3.9a6.8 6.8 0 0 1-4.8 11.6z" fill="#EE4C2C"/><circle cx="15.8" cy="6.2" r="1.5" fill="#EE4C2C"/></svg>''',
    "neo4j": '''<svg class="tech-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="6" cy="18" r="3.5" fill="#008CC1"/><circle cx="18" cy="18" r="3.5" fill="#008CC1"/><circle cx="18" cy="6" r="3.5" fill="#008CC1"/><circle cx="6" cy="6" r="3.5" fill="#008CC1"/><path d="M8.5 7.5l7 7M8.5 16.5l7-7M6 9.5v5M18 9.5v5" stroke="#008CC1" stroke-width="2"/></svg>''',
    "fastapi": '''<svg class="tech-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" fill="#009688"/><path d="M12.8 4.5L7.2 13.2h4.5l-1.5 6.3 6.6-9.6h-4.8l.8-5.4z" fill="#ffffff"/></svg>''',
    "typescript": '''<svg class="tech-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="24" height="24" rx="3" fill="#3178C6"/><path d="M4 10.5h6.5M7.25 10.5v8" stroke="#ffffff" stroke-width="2.2" stroke-linecap="square"/><path d="M13.5 17c1 .8 2.3 1.1 3.5.7 1.1-.4 1.8-1.5 1.5-2.6-.4-1.3-2.1-1.6-3.2-2.1-1-.4-1.8-1.2-1.6-2.3.2-1.1 1.2-1.9 2.3-1.9 1 0 2 .4 2.7 1" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round"/></svg>''',
    "react": '''<svg class="tech-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="2.2" fill="#61DAFB"/><ellipse cx="12" cy="12" rx="10" ry="4.2" stroke="#61DAFB" stroke-width="1.6" transform="rotate(0 12 12)"/><ellipse cx="12" cy="12" rx="10" ry="4.2" stroke="#61DAFB" stroke-width="1.6" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="10" ry="4.2" stroke="#61DAFB" stroke-width="1.6" transform="rotate(120 12 12)"/></svg>''',
    "git": '''<svg class="tech-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M21.6 10.9L13.1 2.4a2 2 0 0 0-2.8 0L8.5 4.2l3.4 3.4a2.2 2.2 0 0 1 2.8 2.8l3.3 3.3a2.2 2.2 0 1 1-1.4 1.4l-3.1-3.1v4.8a2.2 2.2 0 1 1-2 0V9.8L5.7 7A2 2 0 0 0 2.4 9.8l8.5 8.5a2 2 0 0 0 2.8 0l7.9-7.9a2 2 0 0 0 0-2.8z" fill="#F05032"/></svg>''',
    "linux": '''<svg class="tech-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5" stroke="#10B981"/><line x1="12" y1="19" x2="20" y2="19" stroke="#10B981"/></svg>''',
    "huggingface": '''<svg class="tech-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" fill="#FFD21E"/><circle cx="8.5" cy="10" r="1.5" fill="#131200"/><circle cx="15.5" cy="10" r="1.5" fill="#131200"/><path d="M8 14.5s1.5 2.5 4 2.5 4-2.5 4-2.5" stroke="#131200" stroke-width="2" stroke-linecap="round"/></svg>''',
    "ai": '''<svg class="tech-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83" stroke="#F59E0B"/><circle cx="12" cy="12" r="4" fill="#F59E0B"/></svg>''',
    "default": '''<svg class="tech-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" stroke="currentColor"/><path d="M7 8h10M7 12h7M7 16h4" stroke="currentColor"/></svg>'''
}

def get_icon_for_tag(tag):
    tl = tag.lower()
    if "python" in tl or "numpy" in tl or "pandas" in tl or "scipy" in tl or "scikit" in tl:
        return SVG_ICONS["python"]
    elif "sql" in tl or "sqlite" in tl or "database" in tl:
        return SVG_ICONS["sql"]
    elif "postgres" in tl:
        return SVG_ICONS["postgresql"]
    elif "aws" in tl or "cloud" in tl or "s3" in tl or "ec2" in tl or "s3" in tl:
        return SVG_ICONS["aws"]
    elif "docker" in tl or "container" in tl:
        return SVG_ICONS["docker"]
    elif "pytorch" in tl or "torch" in tl:
        return SVG_ICONS["pytorch"]
    elif "neo4j" in tl or "graph" in tl or "cypher" in tl:
        return SVG_ICONS["neo4j"]
    elif "fastapi" in tl or "api" in tl or "rest" in tl:
        return SVG_ICONS["fastapi"]
    elif "typescript" in tl or "ts" in tl:
        return SVG_ICONS["typescript"]
    elif "react" in tl or "ui" in tl or "frontend" in tl or "next" in tl:
        return SVG_ICONS["react"]
    elif "git" in tl or "github" in tl:
        return SVG_ICONS["git"]
    elif "linux" in tl or "bash" in tl or "shell" in tl or "cffi" in tl:
        return SVG_ICONS["linux"]
    elif "hugging" in tl or "hf" in tl or "transformer" in tl or "bert" in tl:
        return SVG_ICONS["huggingface"]
    elif "ai" in tl or "genai" in tl or "agent" in tl or "llm" in tl or "rag" in tl or "dspy" in tl or "nlp" in tl or "fallacy" in tl:
        return SVG_ICONS["ai"]
    return SVG_ICONS["default"]

def render_tag_badge(tag):
    icon = get_icon_for_tag(tag)
    return f'<span class="badge-tag tech-badge-item">{icon}<span>{tag}</span></span>'

# 2. Write tech-icons.js for Client-Side Dynamic Usage
tech_icons_js = f"""/* Client-side Tech Icon Library for Advaith Portfolio */
(function(root) {{
  'use strict';
  const SVG_MAP = {json.dumps(SVG_ICONS)};

  function getTechIcon(tag) {{
    const tl = String(tag || '').toLowerCase();
    if (tl.includes('python') || tl.includes('numpy') || tl.includes('pandas') || tl.includes('scipy') || tl.includes('scikit')) return SVG_MAP['python'];
    if (tl.includes('sql') || tl.includes('sqlite') || tl.includes('database')) return SVG_MAP['sql'];
    if (tl.includes('postgres')) return SVG_MAP['postgresql'];
    if (tl.includes('aws') || tl.includes('cloud') || tl.includes('s3') || tl.includes('ec2')) return SVG_MAP['aws'];
    if (tl.includes('docker') || tl.includes('container')) return SVG_MAP['docker'];
    if (tl.includes('pytorch') || tl.includes('torch')) return SVG_MAP['pytorch'];
    if (tl.includes('neo4j') || tl.includes('graph') || tl.includes('cypher')) return SVG_MAP['neo4j'];
    if (tl.includes('fastapi') || tl.includes('api') || tl.includes('rest')) return SVG_MAP['fastapi'];
    if (tl.includes('typescript') || tl.includes('ts')) return SVG_MAP['typescript'];
    if (tl.includes('react') || tl.includes('ui') || tl.includes('frontend') || tl.includes('next')) return SVG_MAP['react'];
    if (tl.includes('git') || tl.includes('github')) return SVG_MAP['git'];
    if (tl.includes('linux') || tl.includes('bash') || tl.includes('shell') || tl.includes('cffi')) return SVG_MAP['linux'];
    if (tl.includes('hugging') || tl.includes('hf') || tl.includes('transformer') || tl.includes('bert')) return SVG_MAP['huggingface'];
    if (tl.includes('ai') || tl.includes('genai') || tl.includes('agent') || tl.includes('llm') || tl.includes('rag') || tl.includes('dspy') || tl.includes('nlp')) return SVG_MAP['ai'];
    return SVG_MAP['default'];
  }}

  function renderTechBadge(tag) {{
    return `<span class="badge-tag tech-badge-item">${{getTechIcon(tag)}}<span>${{tag}}</span></span>`;
  }}

  root.TechIcons = {{
    SVG_MAP,
    getTechIcon,
    renderTechBadge
  }};
}})(typeof window !== 'undefined' ? window : this);
"""

with open(os.path.join(PORTFOLIO_DIR, "tech-icons.js"), "w", encoding="utf-8") as f:
    f.write(tech_icons_js)
print("Created tech-icons.js")

# 3. Create netlify.toml and _redirects
netlify_toml = """[build]
  publish = "."

[[redirects]]
  from = "/resume"
  to = "/resume.html"
  status = 200

[[redirects]]
  from = "/projects"
  to = "/projects.html"
  status = 200

[[redirects]]
  from = "/project"
  to = "/project.html"
  status = 200

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
    Access-Control-Allow-Origin = "*"

[[headers]]
  for = "*.json"
  [headers.values]
    Content-Type = "application/json"
    Access-Control-Allow-Origin = "*"
    Cache-Control = "public, max-age=3600"

[[headers]]
  for = "*.js"
  [headers.values]
    Content-Type = "application/javascript"
    Access-Control-Allow-Origin = "*"

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
"""

with open(os.path.join(PORTFOLIO_DIR, "netlify.toml"), "w", encoding="utf-8") as f:
    f.write(netlify_toml)

with open(os.path.join(PORTFOLIO_DIR, "_redirects"), "w", encoding="utf-8") as f:
    f.write("/resume    /resume.html   200\n/projects  /projects.html 200\n/project   /project.html  200\n")

print("Created netlify.toml and _redirects")

# 4. Generate the 12-Card Core Tooling Grid HTML for index.html
skills_core_grid = """
      <!-- Core Technology Logos & Tooling Grid -->
      <div class="tech-stack-overview">
        <div class="tech-stack-header">
          <span class="tech-stack-tag">TOOLING &amp; CLOUD ECOSYSTEM</span>
          <h3 class="tech-stack-title">CORE ENGINEERING STACK WITH DIRECT BENCHMARKS</h3>
          <p class="tech-stack-desc">Battle-tested tools and frameworks utilized across 39 production-grade repositories, clinical ML audits, and national hackathons.</p>
        </div>

        <div class="tech-logos-grid">
          <!-- Python -->
          <div class="tech-logo-card">
            <div class="tech-logo-icon-wrap" style="background:#EBF3FA;">
              """ + SVG_ICONS["python"].replace('width="18" height="18"', 'width="34" height="34"') + """
            </div>
            <div class="tech-logo-info">
              <h4 class="tech-logo-name">Python</h4>
              <span class="tech-logo-role">Core Lang / Async</span>
              <p class="tech-logo-desc">Advanced async pipelines, PyTorch CFFI low-level kernels, NumPy vectorized math, and DSPy assertions.</p>
            </div>
          </div>

          <!-- SQL / PostgreSQL -->
          <div class="tech-logo-card">
            <div class="tech-logo-icon-wrap" style="background:#EBF5FB;">
              """ + SVG_ICONS["sql"].replace('width="18" height="18"', 'width="34" height="34"') + """
            </div>
            <div class="tech-logo-info">
              <h4 class="tech-logo-name">SQL &amp; PostgreSQL</h4>
              <span class="tech-logo-role">Relational / Schemas</span>
              <p class="tech-logo-desc">Relational schema design, ACID transactional integrity, complex analytical joins, and indexed query optimizations.</p>
            </div>
          </div>

          <!-- AWS -->
          <div class="tech-logo-card">
            <div class="tech-logo-icon-wrap" style="background:#FFF8E7;">
              """ + SVG_ICONS["aws"].replace('width="18" height="18"', 'width="34" height="34"') + """
            </div>
            <div class="tech-logo-info">
              <h4 class="tech-logo-name">AWS Cloud</h4>
              <span class="tech-logo-role">Cloud Architecture</span>
              <p class="tech-logo-desc">EC2 GPU compute instances, S3 vector dataset storage, serverless Lambda event routing, and Bedrock model orchestration.</p>
            </div>
          </div>

          <!-- Docker -->
          <div class="tech-logo-card">
            <div class="tech-logo-icon-wrap" style="background:#E8F4FD;">
              """ + SVG_ICONS["docker"].replace('width="18" height="18"', 'width="34" height="34"') + """
            </div>
            <div class="tech-logo-info">
              <h4 class="tech-logo-name">Docker</h4>
              <span class="tech-logo-role">Containers / DevOps</span>
              <p class="tech-logo-desc">Multi-stage container builds, reproducible CUDA runtime environments, and isolated multi-service Docker Compose networks.</p>
            </div>
          </div>

          <!-- PyTorch -->
          <div class="tech-logo-card">
            <div class="tech-logo-icon-wrap" style="background:#FDEEE9;">
              """ + SVG_ICONS["pytorch"].replace('width="18" height="18"', 'width="34" height="34"') + """
            </div>
            <div class="tech-logo-info">
              <h4 class="tech-logo-name">PyTorch</h4>
              <span class="tech-logo-role">Deep Learning / Tensors</span>
              <p class="tech-logo-desc">Building multi-head self-attention mechanisms, cross-attention decoders, and custom gradient loss functions from scratch.</p>
            </div>
          </div>

          <!-- Neo4j -->
          <div class="tech-logo-card">
            <div class="tech-logo-icon-wrap" style="background:#E6F5FC;">
              """ + SVG_ICONS["neo4j"].replace('width="18" height="18"', 'width="34" height="34"') + """
            </div>
            <div class="tech-logo-info">
              <h4 class="tech-logo-name">Neo4j Graph DB</h4>
              <span class="tech-logo-role">Graph-RAG &amp; Cypher</span>
              <p class="tech-logo-desc">Entity extraction, knowledge-graph traversal, multi-hop Cypher queries, and topological cluster analysis for RAG.</p>
            </div>
          </div>

          <!-- TypeScript -->
          <div class="tech-logo-card">
            <div class="tech-logo-icon-wrap" style="background:#EBF2FA;">
              """ + SVG_ICONS["typescript"].replace('width="18" height="18"', 'width="34" height="34"') + """
            </div>
            <div class="tech-logo-info">
              <h4 class="tech-logo-name">TypeScript</h4>
              <span class="tech-logo-role">Typed Systems / Node</span>
              <p class="tech-logo-desc">Strict type-safety, Model Context Protocol (MCP) server development, async microservices, and client-side runtimes.</p>
            </div>
          </div>

          <!-- FastAPI -->
          <div class="tech-logo-card">
            <div class="tech-logo-icon-wrap" style="background:#E6F7F5;">
              """ + SVG_ICONS["fastapi"].replace('width="18" height="18"', 'width="34" height="34"') + """
            </div>
            <div class="tech-logo-info">
              <h4 class="tech-logo-name">FastAPI</h4>
              <span class="tech-logo-role">High-Throughput APIs</span>
              <p class="tech-logo-desc">Asynchronous streaming endpoints, Pydantic strict payload validation, WebSocket communication, and OpenAPI contracts.</p>
            </div>
          </div>

          <!-- Hugging Face -->
          <div class="tech-logo-card">
            <div class="tech-logo-icon-wrap" style="background:#FEF9E7;">
              """ + SVG_ICONS["huggingface"].replace('width="18" height="18"', 'width="34" height="34"') + """
            </div>
            <div class="tech-logo-info">
              <h4 class="tech-logo-name">Hugging Face</h4>
              <span class="tech-logo-role">Transformers / LLMs</span>
              <p class="tech-logo-desc">PEFT LoRA fine-tuning, Tokenizers, AutoModel architectures, and quantized model deployments across local GPUs.</p>
            </div>
          </div>

          <!-- Git & CI/CD -->
          <div class="tech-logo-card">
            <div class="tech-logo-icon-wrap" style="background:#FDEFEF;">
              """ + SVG_ICONS["git"].replace('width="18" height="18"', 'width="34" height="34"') + """
            </div>
            <div class="tech-logo-info">
              <h4 class="tech-logo-name">Git &amp; GitHub Actions</h4>
              <span class="tech-logo-role">Version Control / CI/CD</span>
              <p class="tech-logo-desc">Automated testing suites, branch protection rules, semantic versioning, and continuous deployment workflows.</p>
            </div>
          </div>

          <!-- Linux / Bash -->
          <div class="tech-logo-card">
            <div class="tech-logo-icon-wrap" style="background:#EAF8F2;">
              """ + SVG_ICONS["linux"].replace('width="18" height="18"', 'width="34" height="34"') + """
            </div>
            <div class="tech-logo-info">
              <h4 class="tech-logo-name">Linux &amp; POSIX Bash</h4>
              <span class="tech-logo-role">Kernel / Systems Admin</span>
              <p class="tech-logo-desc">Systemd daemon services, memory profile tracing with htop/valgrind, and automated shell deployment pipelines.</p>
            </div>
          </div>

          <!-- React / Web -->
          <div class="tech-logo-card">
            <div class="tech-logo-icon-wrap" style="background:#EDFBFE;">
              """ + SVG_ICONS["react"].replace('width="18" height="18"', 'width="34" height="34"') + """
            </div>
            <div class="tech-logo-info">
              <h4 class="tech-logo-name">React &amp; Modern UI</h4>
              <span class="tech-logo-role">Neo-Brutalist Frontends</span>
              <p class="tech-logo-desc">Component state management, responsive grid layouts, high-contrast accessible design, and real-time dashboard visualization.</p>
            </div>
          </div>
        </div>
      </div>
"""

# 5. Read and update index.html
with open(os.path.join(PORTFOLIO_DIR, "index.html"), "r", encoding="utf-8") as f:
    index_content = f.read()

# Replace or inject in Section 04
section_04_target = '<section class="section-container" id="skills">'
if section_04_target in index_content:
    # Find section-header-row
    match = re.search(r'(<section class="section-container" id="skills">\s*<div class="section-header-row">.*?</div>\s*</div>)', index_content, re.DOTALL)
    if match:
        old_header = match.group(1)
        new_section_content = old_header + "\n" + skills_core_grid
        index_content = index_content.replace(old_header, new_section_content)
        with open(os.path.join(PORTFOLIO_DIR, "index.html"), "w", encoding="utf-8") as f:
            f.write(index_content)
        print("Updated index.html with Core Tech Logos Grid")
    else:
        print("Could not match section-header-row in index.html")

# 6. Add CSS for tech logos & badges to style.css
css_addition = """
/* ==========================================================================
   Tech Stack Logos & Tooling Badges (Neo-Brutalist Architecture)
   ========================================================================== */
.tech-stack-overview {
  margin-bottom: 32px;
}

.tech-stack-header {
  margin-bottom: 20px;
}

.tech-stack-tag {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.72rem;
  font-weight: 800;
  color: var(--color-blueprint);
  letter-spacing: 0.08em;
  display: inline-block;
  margin-bottom: 6px;
}

.tech-stack-title {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.5rem;
  font-weight: 800;
  margin: 0 0 6px 0;
  letter-spacing: -0.02em;
}

.tech-stack-desc {
  font-size: 0.92rem;
  color: var(--text-muted);
  max-width: 800px;
  line-height: 1.5;
  margin: 0;
}

.tech-logos-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 16px;
  margin-top: 20px;
}

.tech-logo-card {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  padding: 16px;
  border: 3px solid var(--border-color);
  background-color: var(--bg-card);
  box-shadow: 4px 4px 0px var(--shadow-color);
  transition: transform 0.12s ease, box-shadow 0.12s ease;
}

.tech-logo-card:hover {
  transform: translate(-3px, -3px);
  box-shadow: 7px 7px 0px var(--shadow-color);
}

.tech-logo-icon-wrap {
  width: 52px;
  height: 52px;
  border: 2px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-shadow: 2px 2px 0px var(--shadow-color);
}

.tech-logo-info {
  flex: 1;
}

.tech-logo-name {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.05rem;
  font-weight: 800;
  margin: 0 0 2px 0;
}

.tech-logo-role {
  display: inline-block;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.68rem;
  font-weight: 700;
  color: var(--color-blueprint);
  margin-bottom: 6px;
  text-transform: uppercase;
}

.tech-logo-desc {
  font-size: 0.78rem;
  line-height: 1.45;
  color: var(--text-muted);
  margin: 0;
}

/* Universal Tech Tag Badge with Icon */
.badge-tag.tech-badge-item,
.card-tag.tech-badge-item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  vertical-align: middle;
  transition: transform 0.1s ease, box-shadow 0.1s ease;
  cursor: default;
}

.badge-tag.tech-badge-item:hover,
.card-tag.tech-badge-item:hover {
  transform: translate(-1px, -1px);
  box-shadow: 2px 2px 0px var(--shadow-color);
}

.tech-icon {
  display: inline-block;
  vertical-align: middle;
  flex-shrink: 0;
}
"""

with open(os.path.join(PORTFOLIO_DIR, "style.css"), "r", encoding="utf-8") as f:
    style_content = f.read()

if "tech-logos-grid" not in style_content:
    with open(os.path.join(PORTFOLIO_DIR, "style.css"), "a", encoding="utf-8") as f:
        f.write("\n" + css_addition)
    print("Added tech stack CSS to style.css")
else:
    print("tech-logos-grid CSS already present in style.css")

# 7. Update build_rag_and_pages.py to generate badges with SVG logos for all 39 static project pages
with open(os.path.join(PORTFOLIO_DIR, "projects-data.json"), "r", encoding="utf-8") as f:
    projects = json.load(f)

for idx, p in enumerate(projects):
    prev_p = projects[(idx - 1 + len(projects)) % len(projects)]
    next_p = projects[(idx + 1) % len(projects)]
    
    stat_tiles = "".join([f'<div class="stat-tile"><div class="stat-tile-val">⚡</div><div class="stat-tile-label">{s.strip()}</div></div>' for s in p["stats"].split("·")])
    tag_spans = "".join([render_tag_badge(t) for t in p["tags"]])
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
          <h2>03 // GOOGLE XYZ AUDIT &amp; CREDENTIALS</h2>
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
      
      <div style="margin-top: 18px;">
        <span style="font-family:'IBM Plex Mono',monospace; font-size:0.75rem; font-weight:700; color:var(--text-muted); display:block; margin-bottom:8px;">TECHNOLOGIES &amp; TOOLING:</span>
        <div style="display:flex; flex-wrap:wrap; gap:8px;">{tag_spans}</div>
      </div>
    </div>

    <section class="detail-section">
      <h2>01 // THE PROBLEM &amp; THE ARCHITECTURE</h2>
      <p style="font-size:1.02rem; line-height:1.7; margin-bottom:16px;">
        {p["overview"]}
      </p>
    </section>

    <section class="detail-section">
      <h2>02 // VERIFIED RESULTS &amp; WHAT I BUILT</h2>
      <ul class="highlight-list">
        {hl_lis}
      </ul>
    </section>

    {rb_sec}

    <section class="detail-section">
      <h2>04 // HONEST ENGINEERING LIMITATIONS</h2>
      <div class="honest-box">
        <strong style="font-family:'IBM Plex Mono',monospace; font-size:0.85rem; display:block; margin-bottom:6px;">⚠️ TRANSPARENCY &amp; WHAT'S NEXT:</strong>
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

print(f"Generated {len(projects)} static project pages with Tech SVG logos in projects/ directory")

# 8. Update project.html (the dynamic universal page) to load tech-icons.js and render tags with logos
with open(os.path.join(PORTFOLIO_DIR, "project.html"), "r", encoding="utf-8") as f:
    phtml = f.read()

# Add script src for tech-icons.js if missing
if "tech-icons.js" not in phtml:
    phtml = phtml.replace('<script src="projects-data.js"></script>', '<script src="projects-data.js"></script>\n  <script src="tech-icons.js"></script>')

# Update tag rendering in project.html
old_tag_render = 'p.tags.map(t => `<span class="badge-tag" style="background:var(--bg-surface);">${t}</span>`).join(\'\')'
new_tag_render = 'p.tags.map(t => window.TechIcons ? window.TechIcons.renderTechBadge(t) : `<span class="badge-tag">${t}</span>`).join(\'\')'

if old_tag_render in phtml:
    phtml = phtml.replace(old_tag_render, new_tag_render)

with open(os.path.join(PORTFOLIO_DIR, "project.html"), "w", encoding="utf-8") as f:
    f.write(phtml)
print("Updated project.html to render tags with SVG logos")

# 9. Update projects.html to load tech-icons.js and render tags with logos
with open(os.path.join(PORTFOLIO_DIR, "projects.html"), "r", encoding="utf-8") as f:
    pshtml = f.read()

if "tech-icons.js" not in pshtml:
    pshtml = pshtml.replace('<script src="projects-data.js"></script>', '<script src="projects-data.js"></script>\n  <script src="tech-icons.js"></script>')

old_ps_tags = "p.tags.map(t => `<span class=\"card-tag\">${t}</span>`).join('')"
new_ps_tags = "p.tags.map(t => window.TechIcons ? window.TechIcons.renderTechBadge(t) : `<span class=\"card-tag\">${t}</span>`).join('')"

if old_ps_tags in pshtml:
    pshtml = pshtml.replace(old_ps_tags, new_ps_tags)

with open(os.path.join(PORTFOLIO_DIR, "projects.html"), "w", encoding="utf-8") as f:
    f.write(pshtml)
print("Updated projects.html to render tags with SVG logos")
