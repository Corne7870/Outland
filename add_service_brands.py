import os

brands_html = {
    'Husqvarna': '''        <a href="https://www.husqvarna.com/za/" target="_blank" rel="noopener noreferrer" class="brand-logo-link">
          <img src="images/husqvarna-logo.png" alt="Husqvarna" class="brand-logo-img" style="max-height: 80px;">
          <span class="brand-name">Husqvarna</span>
        </a>''',
    'Pellenc': '''        <a href="https://www.pellenc.com/en-za/" target="_blank" rel="noopener noreferrer" class="brand-logo-link">
          <img src="images/pellenc-logo.png" alt="Pellenc" class="brand-logo-img" style="max-height: 70px;">
          <span class="brand-name">Pellenc</span>
        </a>''',
    'Total Tools': '''        <a href="https://totaltoolsonline.co.za/?gad_source=1&gad_campaignid=23780715076&gbraid=0AAAABDdbndjaM3ajn8o0pZav4e0J6uuhd&gclid=Cj0KCQjw_IXQBhCkARIsADqELbJdfUUSVOdrC7eyZ9twdL7-QbhxzaI8Y2oajh8TBp-s-kOV1YYsn54aAmc8EALw_wcB" target="_blank" rel="noopener noreferrer" class="brand-logo-link">
          <img src="images/total-tools-logo.png" alt="Total Tools" class="brand-logo-img">
          <span class="brand-name">Total Tools</span>
        </a>''',
    'Ultra Scooter': '''        <a href="https://ultrascooter.co.za/?utm_campaign=gs-2024-12-18&utm_source=google&utm_medium=pmax_shopping&gad_source=1&gad_campaignid=22043380042&gbraid=0AAAAAC1pr-OAD-LylExn8tOm9bddLuD77&gclid=CjwKCAjw8arQBhB9EiwAfIKdQuqNE7qW_1vkzO4BUZxQBglpRnuHutu17cnBiR7YTGDrejJ2BCQNxRoCedcQAvD_BwE" target="_blank" rel="noopener noreferrer" class="brand-logo-link">
          <img src="images/ultra-scooter-logo.png" alt="Ultra Scooter" class="brand-logo-img">
          <span class="brand-name">Ultra Scooter</span>
        </a>''',
    'Big Boy': '''        <a href="https://www.samotorcycles.co.za/commercial?gad_source=1&gad_campaignid=7704291830&gbraid=0AAAAACnItTV39l0O9LK68zWEVyNOzSXHL&gclid=Cj0KCQjwzqXQBhD2ARIsAKrIeU_2ohpMFGedCuWMk1kqtLIeWWKUDia_xumfeg8OmR7juFKhAfRSrewaApMgEALw_wcB" target="_blank" rel="noopener noreferrer" class="brand-logo-link">
          <img src="images/big-boy-logo.png" alt="Big Boy" class="brand-logo-img">
          <span class="brand-name">Big Boy</span>
        </a>''',
    'Multi Power': '''        <a href="https://www.multipowerimports.co.za/" target="_blank" rel="noopener noreferrer" class="brand-logo-link">
          <img src="images/multi-power-logo.png" alt="Multi Power" class="brand-logo-img" style="max-height: 80px;">
          <span class="brand-name">Multi Power</span>
        </a>'''
}

file_mapping = {
    'parts-repairs.html': ['Husqvarna', 'Big Boy', 'Total Tools', 'Ultra Scooter', 'Pellenc', 'Multi Power'],
    'garden-turf.html': ['Husqvarna', 'Multi Power', 'Pellenc'],
    'forestry-clearing.html': ['Husqvarna', 'Multi Power', 'Pellenc'],
    'transport.html': ['Big Boy', 'Ultra Scooter'],
    'tools.html': ['Total Tools'],
    'battery-electric.html': ['Total Tools', 'Husqvarna', 'Pellenc', 'Big Boy']
}

section_template = """  <!-- Brands Supported -->
  <section class="section section-dark" id="brands">
    <div class="container text-center fade-in">
      <p class="section-subtitle">Trusted Partners</p>
      <h2 class="section-title text-white">Brands We Supply</h2>
      <div class="brands-grid">
{brands_content}
      </div>
    </div>
  </section>

"""

for filename, brands in file_mapping.items():
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="brands"' in content:
        print(f"Brands section already exists in {filename}, skipping.")
        continue
    
    brands_content = "\n".join([brands_html[b] for b in brands])
    section_html = section_template.format(brands_content=brands_content)
    
    if '  <!-- CTA -->' in content:
        content = content.replace('  <!-- CTA -->', section_html + '  <!-- CTA -->')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"Could not find CTA section in {filename}")
