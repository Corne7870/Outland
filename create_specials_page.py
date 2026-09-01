import re

with open('gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title & Meta
content = re.sub(r'<title>.*?</title>', '<title>Specials | OutLand Power and Turf</title>', content)
content = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Current specials and promotions at OutLand Power and Turf.">', content)

# 2. Update Active Nav Links
content = content.replace('class="active">Gallery</a>', '>Gallery</a>')
content = content.replace('<a href="specials.html">Specials</a>', '<a href="specials.html" class="active">Specials</a>')

# 3. Update Page Header
header_pattern = r'<!-- Page Header -->.*?<!-- Gallery Grid -->'
new_header = '''<!-- Page Header -->
  <section class="page-header">
    <div class="container">
      <p class="section-subtitle">Great Deals</p>
      <h1>Specials</h1>
      <p>Check out our latest promotions and discounts.</p>
    </div>
  </section>

  <!-- Specials Section -->'''
content = re.sub(header_pattern, new_header, content, flags=re.DOTALL)

# 4. Update Main Content (replace gallery grid with single image)
gallery_pattern = r'<section class="section">.*?<!-- CTA -->'
new_content = '''<section class="section">
    <div class="container fade-in" style="text-align: center;">
      <img src="images/september_special.png" alt="Current Special Offer" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
    </div>
  </section>

  <!-- CTA -->'''
content = re.sub(gallery_pattern, new_content, content, flags=re.DOTALL)

with open('specials.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("specials.html created successfully.")
