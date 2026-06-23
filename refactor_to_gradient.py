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
    
    # Match the entire hero-bg-section
    match = re.search(r'(  <!-- Unified Hero Section -->\n  <section class="hero-bg-section" .*?</section>\n)', content, re.DOTALL)
    if not match:
        print(f"Could not find hero section in {filename}")
        continue
    
    old_html = match.group(1)
    
    # Extract components
    img_match = re.search(r'background-image: url\(\'(.*?)\'\);', old_html)
    img_src = img_match.group(1) if img_match else ""
    
    icon_match = re.search(r'<div class="detailed-icon">\s*(<svg.*?</svg>)\s*</div>', old_html, re.DOTALL)
    icon_svg = icon_match.group(1) if icon_match else ""
    
    title_match = re.search(r'<h2>(.*?)</h2>', old_html)
    title_text = title_match.group(1) if title_match else ""
    
    desc_match = re.search(r'<p>(.*?)</p>', old_html, re.DOTALL)
    desc_text = desc_match.group(1) if desc_match else ""
    
    features_block_match = re.search(r'<div class="feature-pills">(.*?)</div>\s*<div class="service-overlap-cta">', old_html, re.DOTALL)
    features_html = features_block_match.group(1).rstrip() if features_block_match else ""
    
    btn_match = re.search(r'<a href="(.*?)" class="btn btn-primary">(.*?)</a>', old_html)
    btn_href = btn_match.group(1) if btn_match else "contact.html"
    btn_text = btn_match.group(2) if btn_match else "Enquire About Pricing →"
    
    brands_block_match = re.search(r'<div class="brands-grid" style="gap: 20px;">(.*?)</div>\s*</div>\s*</div>\s*</div>\s*</section>', old_html, re.DOTALL)
    brands_html = brands_block_match.group(1) if brands_block_match else ""
    
    new_html = f"""  <!-- Premium Layout Section -->
  <section class="premium-gradient-section">
    <div class="container">
      <div class="unified-content-card fade-in">
        
        <div class="unified-card-top-grid">
          <!-- Image Side -->
          <div class="unified-card-img">
            <img src="{img_src}" alt="{title_text}">
          </div>

          <!-- Text Side -->
          <div class="unified-card-text">
            <div class="detailed-icon">
              {icon_svg}
            </div>
            <h2>{title_text}</h2>
            <p>{desc_text}</p>
            <div class="feature-pills">
{features_html}
            </div>
            <div class="service-overlap-cta" style="border-top: none; padding-top: 16px; text-align: left;">
              <a href="{btn_href}" class="btn btn-primary">{btn_text}</a>
            </div>
          </div>
        </div>

        <!-- Brands Overlay Strip -->
        <div class="brands-dark-strip" id="brands">
          <h3 class="shop-here-title">Shop Here</h3>
          <div class="brands-grid" style="gap: 20px;">
{brands_html}          </div>
        </div>

      </div>
    </div>
  </section>
"""
    
    content = content.replace(old_html, new_html)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {filename}")
