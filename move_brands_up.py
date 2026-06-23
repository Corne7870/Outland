import os
import re

files_to_update = [
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
    
    # Extract the Brands Supported section
    # It starts with "  <!-- Brands Supported -->" and ends with "  </section>\n\n  <!-- CTA -->"
    match = re.search(r'(  <!-- Brands Supported -->\n  <section class="section section-dark" id="brands">.*?</section>\n\n)', content, re.DOTALL)
    
    if not match:
        print(f"Could not find Brands section in {filename}")
        continue
        
    brands_section = match.group(1)
    
    # Remove from original location
    content = content.replace(brands_section, '')
    
    # Find insertion point: After Page Header section
    # The page header ends with "</section>\n\n  <!-- Product Details -->"
    # or similar.
    header_end_match = re.search(r'(</section>\n\n)(\s*<!-- (?:Product Details|.*?))', content)
    
    if header_end_match:
        insertion_point = header_end_match.start(2)
        content = content[:insertion_point] + brands_section + content[insertion_point:]
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Moved Brands section in {filename}")
    else:
        print(f"Could not find insertion point in {filename}")
