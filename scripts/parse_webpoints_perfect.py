import re
import json
import os

WEBPOINTS_PATH = r"C:\Projects\webpoints.md"
PORTFOLIO_DIR = r"C:\Projects\portfolio-zer0"

with open(WEBPOINTS_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Split by sections
category_map = {
    "Hackathon": "Hackathon",
    "AI Agents": "AI Agents",
    "NLP & RAG": "NLP & RAG",
    "ML & Data": "ML & Data",
    "Systems from Scratch": "Systems from Scratch",
    "Full-Stack": "Full-Stack",
    "In Progress": "In Progress"
}

projects = []
current_cat = None

lines = content.splitlines()
i = 0
while i < len(lines):
    line = lines[i]
    if line.startswith("## ") and not line.startswith("## Homepage") and not line.startswith("## Contents") and not line.startswith("## ⭐"):
        cat_header = line.replace("## ", "").strip()
        for k in category_map:
            if k.lower() in cat_header.lower():
                current_cat = category_map[k]
                break

    elif line.startswith("### ") and current_cat:
        title = line.replace("### ", "").strip()
        # Parse project fields
        proj = {
            "title": title,
            "category": current_cat,
            "tagline": "",
            "card": "",
            "tags": [],
            "stats": "",
            "overview": "",
            "highlights": [],
            "honest": "",
            "links": "",
            "slug": re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
        }
        
        i += 1
        while i < len(lines) and not lines[i].startswith("### ") and not (lines[i].startswith("## ") and not lines[i].startswith("### ")):
            subline = lines[i]
            if subline.startswith("- **Title:**"):
                proj["title"] = subline.replace("- **Title:**", "").strip()
            elif subline.startswith("- **Tagline:**"):
                proj["tagline"] = subline.replace("- **Tagline:**", "").strip()
            elif subline.startswith("- **Card:**"):
                proj["card"] = subline.replace("- **Card:**", "").strip()
            elif subline.startswith("- **Tags:**"):
                raw_tags = subline.replace("- **Tags:**", "").strip()
                # Split by middle dot or comma
                tags = [t.strip() for t in re.split(r'[·,]', raw_tags) if t.strip()]
                proj["tags"] = tags
            elif subline.startswith("- **Stats:**"):
                proj["stats"] = subline.replace("- **Stats:**", "").strip()
            elif subline.startswith("- **Overview:**"):
                proj["overview"] = subline.replace("- **Overview:**", "").strip()
            elif subline.startswith("- **Honest note:**"):
                proj["honest"] = subline.replace("- **Honest note:**", "").strip()
            elif subline.startswith("- **Links:**"):
                proj["links"] = subline.replace("- **Links:**", "").strip()
            elif subline.startswith("  - "):
                # Highlight bullet
                hl = subline.strip().lstrip("-").strip()
                proj["highlights"].append(hl)
            i += 1
        
        # Clean fields: remove backticks
        proj["stats"] = proj["stats"].replace("`", "")
        proj["tagline"] = proj["tagline"].replace("`", "")
        proj["card"] = proj["card"].replace("`", "")
        proj["overview"] = proj["overview"].replace("`", "")
        proj["honest"] = proj["honest"].replace("`", "")
        proj["highlights"] = [h.replace("`", "") for h in proj["highlights"]]

        projects.append(proj)
        continue
    i += 1

print(f"Parsed {len(projects)} projects from webpoints.md")

# Save to projects-data.json and projects-data.js
with open(os.path.join(PORTFOLIO_DIR, "projects-data.json"), "w", encoding="utf-8") as f:
    json.dump(projects, f, indent=2, ensure_ascii=False)

with open(os.path.join(PORTFOLIO_DIR, "projects-data.js"), "w", encoding="utf-8") as f:
    f.write(f"/* 39 Projects - Advaith Narayana Sarva */\nwindow.ALL_PROJECTS = {json.dumps(projects, indent=2, ensure_ascii=False)};\n")

print("Saved pristine projects-data.json and projects-data.js without backticks!")
