import re

html_file = 'Ayesha -Meera Moodboard.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

targets = [
    "gaitor_1.jpg",
    "chandra_mahal.jpg",
    "panna_meena_1.jpg",
    "sisodia_rani_1.jpg",
    "kishanbagh_1.jpg",
    "nahargarh_1.jpg",
    "amber_fort_1.jpg"
]

def remove_grid_containing(text, marker):
    marker_pos = text.find(marker)
    if marker_pos == -1:
        return text
    
    start_str = '<div class="photo-grid-'
    start_pos = text.rfind(start_str, 0, marker_pos)
    if start_pos == -1:
        return text
    
    nl_pos = text.rfind('\n', 0, start_pos)
    indent = text[nl_pos+1:start_pos]
    
    end_str = f"\n{indent}</div>\n"
    end_pos = text.find(end_str, marker_pos)
    if end_pos != -1:
        end_pos += len(end_str)
        # We also might want to remove any trailing blank lines if any, but this is safe
        return text[:nl_pos] + "\n" + text[end_pos:]
    
    return text

for t in targets:
    content = remove_grid_containing(content, t)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Empty boxes removed successfully.")
