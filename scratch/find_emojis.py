import re

files = ['index.html', 'projects.html', 'resume.html', 'style.css', 'script.js', 'rag-engine.js']

emoji_pattern = re.compile(
    r'[\U00010000-\U0010ffff]|[\u2600-\u27bf]|[\u2300-\u23ff]|[\u2b50-\u2b55]'
)

with open('scratch/emoji_report.txt', 'w', encoding='utf-8') as out:
    for fn in files:
        found = []
        try:
            with open(fn, 'r', encoding='utf-8') as f:
                for idx, line in enumerate(f, 1):
                    matches = emoji_pattern.findall(line)
                    if matches:
                        found.append((idx, ''.join(matches), line.strip()))
        except Exception as e:
            out.write(f"Error reading {fn}: {e}\n")
            continue
        out.write(f"=== {fn} ({len(found)} lines with emojis) ===\n")
        for idx, ems, text in found:
            out.write(f"  L{idx}: [{ems}] {text}\n")
        out.write("\n")

print("Emoji report written to scratch/emoji_report.txt")
