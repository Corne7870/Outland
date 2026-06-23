import os

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
    
    # Replace section-alt with section-light-grey on the brands section
    if 'class="section section-alt" id="brands"' in content:
        content = content.replace('class="section section-alt" id="brands"', 'class="section section-light-grey" id="brands"')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"No match found in {filename}")
