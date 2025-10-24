import os

ROOT_DIR = "public"
INDEX_FILE = os.path.join(ROOT_DIR, "index.html")

ICONS = {
    ".html": "https://pomf2.lain.la/f/ct3uvtq.webp",
    ".htm": "https://pomf2.lain.la/f/ct3uvtq.webp",
    ".png": "https://pomf2.lain.la/f/62n6172.png",
    ".jpg": "https://pomf2.lain.la/f/62n6172.png",
    ".jpeg": "https://pomf2.lain.la/f/62n6172.png",
    ".gif": "https://pomf2.lain.la/f/62n6172.png",
    ".js": "https://pomf2.lain.la/f/ct3uvtq.webp",
    ".css": "https://pomf2.lain.la/f/ct3uvtq.webp",
    ".json": "https://pomf2.lain.la/f/ct3uvtq.webp",
    ".txt": "https://pomf2.lain.la/f/ct3uvtq.webp",
    ".zip": "https://pomf2.lain.la/f/6dlghiti.png",
    ".mp3": "https://pomf2.lain.la/f/xozen8pr.png",
    ".ogg": "https://pomf2.lain.la/f/xozen8pr.png",
    ".wav": "https://pomf2.lain.la/f/xozen8pr.png",
}
DEFAULT_ICON = "https://pomf2.lain.la/f/ct3uvtq.webp"

BOTTOM_IMAGE_URL = "https://pomf2.lain.la/f/jasn10yn.png"
BOTTOM_IMAGE_LINK = "https://minidoom.one"

file_list = []
for subdir, dirs, files in os.walk(ROOT_DIR):
    for file in files:
        if file == "index.html":
            continue
        rel_dir = os.path.relpath(subdir, ROOT_DIR)
        rel_path = os.path.join(rel_dir, file) if rel_dir != "." else file
        file_list.append(rel_path.replace("\\", "/"))

current_dir = os.path.basename(os.path.abspath(ROOT_DIR))

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{current_dir}</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
<style>
body {{
    font-family: 'Poppins', sans-serif;
    background: #000000;
    background-image:
        linear-gradient(#484848aa 1px, transparent 1px),
        linear-gradient(90deg, #484848aa 1px, transparent 1px);
    background-size: 41px 41px;
    color: white;
    margin: 0;
    height: 100vh;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
}}
h1 {{
    color: #FFFFFF;
    text-align: center;
}}
ul {{
    list-style: none;
    padding: 0;
    max-width: 600px;
    width: 100%;
    overflow-y: auto;
    flex-grow: 1;
}}
li {{
    background-color: #1e1e1e;
    margin: 0.5rem 0;
    padding: 0.75rem 1rem;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.5);
    display: flex;
    align-items: center;
}}
li a {{
    text-decoration: none;
    color: #ffffff;
    flex-grow: 1;
}}
li a:hover {{
    color: #4a90e2;
}}
.icon {{
    width: 24px;
    height: 24px;
    margin-right: 0.75rem;
}}
.bottom-container {{
    position: fixed;
    bottom: 20px;
}}
.bottom-image {{
    max-width: 200px;
    border-radius: 12px;
    transition: transform 0.3s;
}}
.bottom-image:hover {{
    transform: scale(1.1);
}}
</style>
</head>
<body>
<h1>{current_dir}</h1>
<ul>
"""

for f in sorted(file_list):
    ext = os.path.splitext(f)[1].lower()
    icon_url = ICONS.get(ext, DEFAULT_ICON)
    html_content += f'  <li><img class="icon" src="{icon_url}" alt="{ext} icon"><a href="/{f}">{f}</a></li>\n'

html_content += f"""</ul>
<div class="bottom-container">
    <a href="{BOTTOM_IMAGE_LINK}" target="_blank">
        <img class="bottom-image" src="{BOTTOM_IMAGE_URL}" alt="Bottom Image">
    </a>
</div>
</body>
</html>
"""

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"okay done")
