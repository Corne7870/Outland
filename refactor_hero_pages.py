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
    
    # 1. Extract Brands Section
    brands_match = re.search(r'(  <!-- Brands Supported -->\n  <section class="section section-dark" id="brands">.*?</section>\n\n)', content, re.DOTALL)
    if not brands_match:
        print(f"Could not find Brands section in {filename}")
        continue
    brands_full_html = brands_match.group(1)
    
    # Extract the brands-grid content
    brands_grid_match = re.search(r'<div class="brands-grid">(.*?)</div>\n    </div>\n  </section>', brands_full_html, re.DOTALL)
    brands_html = brands_grid_match.group(1) if brands_grid_match else ""
    
    # 2. Extract Product Details Section
    details_match = re.search(r'(  <!-- Product Details -->\n  <section class="section section-alt">.*?</section>\n\n)', content, re.DOTALL)
    if not details_match:
        print(f"Could not find Product Details section in {filename}")
        continue
    details_full_html = details_match.group(1)
    
    # Extract components from new layout
    img_match = re.search(r'<img src="(.*?)" alt="(.*?)">', details_full_html)
    img_src = img_match.group(1) if img_match else ""
    img_alt = img_match.group(2) if img_match else ""
    
    icon_match = re.search(r'<div class="detailed-icon">\s*(<svg.*?</svg>)\s*</div>', details_full_html, re.DOTALL)
    icon_svg = icon_match.group(1) if icon_match else ""
    
    title_match = re.search(r'<h2>(.*?)</h2>', details_full_html)
    title_text = title_match.group(1) if title_match else ""
    
    desc_match = re.search(r'<p>(.*?)</p>', details_full_html, re.DOTALL)
    desc_text = desc_match.group(1) if desc_match else ""
    
    features_block_match = re.search(r'<div class="feature-pills">(.*?)</div>', details_full_html, re.DOTALL)
    features_html = features_block_match.group(1) if features_block_match else ""
    
    btn_match = re.search(r'<a href="(.*?)" class="btn btn-primary">(.*?)</a>', details_full_html)
    btn_href = btn_match.group(1) if btn_match else "contact.html"
    btn_text = btn_match.group(2) if btn_match else "Enquire About Pricing →"
    
    # Construct new unified HTML
    new_html = f"""  <!-- Unified Hero Section -->
  <section class="hero-bg-section" style="background-image: url('{img_src}');">
    <div class="hero-bg-overlay"></div>
    <div class="container hero-bg-container">
      <div class="content-overlay-card fade-in">
        
        <!-- Details Overlay -->
        <div class="content-overlay-text">
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

    # Remove old brands section
    content = content.replace(brands_full_html, '')
    
    # Replace old details section with new unified section
    content = content.replace(details_full_html, new_html)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {filename}")
