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
    
    # Remove the unified-card-img block
    # It looks like:
    #          <!-- Image Side -->
    #          <div class="unified-card-img">
    #            <img src="..." alt="...">
    #          </div>
    content = re.sub(r'\s*<!-- Image Side -->\s*<div class="unified-card-img">\s*<img src=".*?" alt=".*?">\s*</div>', '', content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Removed picture from {filename}")

# Now update styles.css to make the text take 100% width
css_file = 'styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace the 55% width rule
old_css = """@media (min-width: 992px) {
  .unified-card-text {
    width: 55%;
    padding: 60px 60px 60px 40px;
  }
}"""

new_css = """@media (min-width: 992px) {
  .unified-card-text {
    width: 100%;
    padding: 60px 80px;
  }
}"""

if old_css in css_content:
    css_content = css_content.replace(old_css, new_css)
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("Updated styles.css width")
else:
    print("Could not find the old CSS rule in styles.css")

