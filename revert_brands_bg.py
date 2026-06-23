import os
import re

files_to_update = [
    'index.html',
    'parts-repairs.html',
    'garden-turf.html',
    'forestry-clearing.html',
    'transport.html',
    'tools.html',
    'battery-electric.html'
]

for filename in files_to_update:
    if not os.path.exists(filename):
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Revert to section-dark
    content = content.replace('class="section section-light-grey" id="brands"', 'class="section section-dark" id="brands"')
    
    # Revert title to include text-white
    content = re.sub(r'<h2 class="section-title">(Brands We Supply.*?)</h2>', r'<h2 class="section-title text-white">\1</h2>', content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Reverted brands background in {filename}")
