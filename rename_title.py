import sys

replacements = {
    "Undulo Rajasthan — Shoot Moodboard": "Jaipur Reverie — Shoot Moodboard",
    "<h1>Undulo<br>\n      <em>Rajasthan</em></h1>": "<h1>Jaipur<br>\n      <em>Reverie</em></h1>",
    "<h1>Undulo<br><em>Rajasthan</em></h1>": "<h1>Jaipur<br><em>Reverie</em></h1>",
    "उन्दुलो राजस्थान": "जयपुर रेवरी",
    "class=\"concept-word\">Undulo</div>": "class=\"concept-word\">Reverie</div>",
    "The <em>Undulo</em> Palette": "The <em>Reverie</em> Palette",
    "Meera's Undulo Rajasthan": "Meera's Jaipur Reverie",
    "Undulo Rajasthan · Sawan Collection": "Jaipur Reverie · Sawan Collection",
    "meeraa_undulo_rajasthan": "meeraa_jaipur_reverie"
}

html_file = 'Ayesha -Meera Moodboard.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

for old, new in replacements.items():
    content = content.replace(old, new)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Title updated to Jaipur Reverie.")
