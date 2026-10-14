import re

css_file = "style.css"

with open(css_file, "r", encoding="utf-8") as f:
    css = f.read()

# Add root variables
root_vars = """
:root {
  --primary: #0ea5e9;
  --primary-glow: rgba(14, 165, 233, 0.4);
  --bg-main: #020617;
  --bg-sec: #0f172a;
  --bg-card: #1e293b;
  --text-light: #f8fafc;
  --text-muted: #94a3b8;
  --border-color: #334155;
  --gradient-main: linear-gradient(135deg, #0ea5e9, #3b82f6);
}
"""

if ":root" not in css:
    css = root_vars + css

# Replacements
replacements = {
    r'#ff6a00': 'var(--primary)',
    r'rgba\(255,\s*106,\s*0,\s*([0-9.]+)\)': r'rgba(14, 165, 233, \1)',
    r'#080808': 'var(--bg-main)',
    r'#000(?!000)': 'var(--bg-main)',
    r'#050505': 'var(--bg-main)',
    r'#0a0a0a': 'var(--bg-sec)',
    r'#0f0f0f': 'var(--bg-card)',
    r'#181818': 'var(--bg-card)',
    r'#fff(?!f)': 'var(--text-light)',
    r'#ccc': 'var(--text-muted)',
    r'#bbb': 'var(--text-muted)',
    r'#aaa': 'var(--text-muted)',
    r'#888': 'var(--text-muted)',
    r'#555': 'var(--text-muted)',
    r'#666': 'var(--text-muted)',
    r'#444': 'var(--text-muted)',
    r'#1e1e1e': 'var(--border-color)',
    r'#1a1a1a': 'var(--border-color)',
    r'#2a2a2a': 'var(--border-color)',
}

for pattern, repl in replacements.items():
    css = re.sub(pattern, repl, css, flags=re.IGNORECASE)

# Improve some specific styles
css = css.replace("background: var(--primary);", "background: var(--gradient-main);")

with open(css_file, "w", encoding="utf-8") as f:
    f.write(css)

print("CSS updated successfully!")
