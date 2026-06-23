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
    
    # We want to find the Product Details section.
    # It starts with "  <!-- Product Details -->" and ends with "  </section>\n\n  <!-- CTA -->"
    
    match = re.search(r'(  <!-- Product Details -->\n  <section class="section">.*?</section>\n\n)', content, re.DOTALL)
    if not match:
        print(f"Could not find Product Details section in {filename}")
        continue
        
    details_html = match.group(1)
    
    # Extract components
    img_match = re.search(r'<img src="(.*?)" alt="(.*?)">', details_html)
    img_src = img_match.group(1) if img_match else ""
    img_alt = img_match.group(2) if img_match else ""
    
    icon_match = re.search(r'<div class="detailed-icon">\s*(<svg.*?</svg>)\s*</div>', details_html, re.DOTALL)
    icon_svg = icon_match.group(1) if icon_match else ""
    
    title_match = re.search(r'<h2>(.*?)</h2>', details_html)
    title_text = title_match.group(1) if title_match else ""
    
    desc_match = re.search(r'<p>(.*?)</p>', details_html, re.DOTALL)
    desc_text = desc_match.group(1) if desc_match else ""
    
    features_block_match = re.search(r'<ul class="product-features">(.*?)</ul>', details_html, re.DOTALL)
    features_html = ""
    if features_block_match:
        items = re.findall(r'<li>(.*?)</li>', features_block_match.group(1), re.DOTALL)
        for item in items:
            features_html += f'            <div class="feature-pill"><span class="feature-check">✓</span> {item.strip()}</div>\n'
    
    btn_match = re.search(r'<a href="(.*?)" class="btn btn-primary">(.*?)</a>', details_html)
    btn_href = btn_match.group(1) if btn_match else "contact.html"
    btn_text = btn_match.group(2) if btn_match else "Enquire About Pricing →"
    
    # Construct new HTML
    new_html = f"""  <!-- Product Details -->
  <section class="section section-alt">
    <div class="container">
      <div class="service-overlap">
        <div class="service-overlap-img fade-in">
          <img src="{img_src}" alt="{img_alt}">
        </div>
        <div class="service-overlap-card fade-in">
          <div class="detailed-icon">
            {icon_svg}
          </div>
          <h2>{title_text}</h2>
          <p>{desc_text}</p>
          <div class="feature-pills">
{features_html}          </div>
          <div class="service-overlap-cta">
            <a href="{btn_href}" class="btn btn-primary">{btn_text}</a>
          </div>
        </div>
      </div>
    </div>
  </section>

"""

    # Replace old with new
    content = content.replace(details_html, new_html)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {filename}")
