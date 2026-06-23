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
    
    # Replace section class
    content = content.replace('class="section section-dark" id="brands"', 'class="section section-alt" id="brands"')
    
    # We need to specifically replace the text-white inside the brands section.
    # We can do this with regex to ensure we only affect the Brands We Supply title.
    # Usually it's: <h2 class="section-title text-white">Brands We Supply</h2>
    content = re.sub(r'<h2 class="section-title text-white">(Brands We Supply.*?)</h2>', r'<h2 class="section-title">\1</h2>', content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {filename}")
