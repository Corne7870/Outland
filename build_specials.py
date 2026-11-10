import os, re, urllib.parse

def parse_filename(f):
    base = os.path.splitext(f)[0]
    cleaned = re.sub(r'^\d+_', '', base)
    
    price_match = re.search(r'_(R?[\d,]+(?:\.\d{1,2})?)$', cleaned)
    price_str = ''
    price_val = 0.0
    if price_match:
        price_raw = price_match.group(1)
        cleaned = cleaned[:price_match.start()]
        digits_only = re.sub(r'[^\d\.]', '', price_raw)
        try:
            price_val = float(digits_only)
            price_str = f"R {price_val:,.2f}"
        except:
            price_str = ('R ' if not price_raw.startswith('R') else '') + price_raw
    
    title = cleaned.replace('_', ' ')
    title = re.sub(r'\s+', ' ', title).strip()
    return title, price_str, price_val

def render_cards(folder_name, category_id):
    files = [f for f in sorted(os.listdir(folder_name)) if f.lower().endswith('.png')]
    cards_html = []
    
    for f in files:
        title, price_str, price_val = parse_filename(f)
        img_path = f"{folder_name}/{f}"
        
        wa_text = urllib.parse.quote(f"Hi OutLand, I'm interested in the special offer: {title} ({price_str})")
        wa_url = f"https://wa.me/27828028079?text={wa_text}"
        
        escaped_title = title.replace('"', '&quot;').replace("'", "&#39;")
        escaped_price = price_str.replace('"', '&quot;')
        
        card = f'''        <div class="special-card" data-title="{escaped_title.lower()}" data-price="{escaped_price}" data-category="{category_id}">
          <div class="special-card-img-wrap" onclick="openSpecialsModal('{img_path}', '{escaped_title}', '{escaped_price}')">
            <img src="{img_path}" alt="{escaped_title} - OutLand Specials" loading="lazy">
            <div class="special-card-overlay">
              <span class="special-card-zoom-badge">🔍 Click to Enlarge Flyer</span>
            </div>
          </div>
          <div class="special-card-details">
            <h3 class="special-card-title">{escaped_title}</h3>
            <div class="special-card-footer">
              <span class="special-card-price">{escaped_price}</span>
              <a href="{wa_url}" target="_blank" rel="noopener" class="special-card-enquire" title="Enquire on WhatsApp">Enquire</a>
            </div>
          </div>
        </div>'''
        cards_html.append(card)
    return "\n".join(cards_html), len(files)

single_cards, single_count = render_cards("01_Single_offers", "single-offers")
bundle_cards, bundle_count = render_cards("02_Bundles", "bundles")

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Current specials, single offers, and bundle promotions at OutLand Power and Turf.">
  <title>Specials | OutLand Power and Turf</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Caveat:wght@600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
  <link rel="icon" href="images/logo.png" type="image/png">
</head>
<body>

  <!-- Navigation -->
  <nav class="navbar" id="navbar">
    <div class="nav-container">
      <a href="index.html" class="nav-logo">
        <img src="images/logo.png" alt="OutLand Power and Turf Logo">
        <div class="nav-logo-text">
          <div class="logo-outland">OUTLAND</div>
          <div class="logo-sub">
            <span class="logo-dash">—</span> POWER &amp; TURF <span class="logo-dash">—</span>
          </div>
        </div>
      </a>
      <div class="nav-links" id="nav-links">
        <a href="index.html">Home</a>
        <a href="about.html">About Us</a>
        <a href="products.html">Products &amp; Services</a>
        <a href="used-items.html">Used Items</a>
        <a href="gallery.html">Gallery</a>
        <a href="reviews.html">Reviews</a>
        <a href="specials.html" class="active">Specials</a>
        <a href="mechanic-referral.html">Mechanic Referral</a>
        <a href="contact.html" class="nav-cta">Contact Us</a>
      </div>
      <div class="hamburger" id="hamburger">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
  </nav>
  <div class="nav-overlay" id="nav-overlay"></div>

  <!-- Page Header -->
  <section class="page-header">
    <div class="container">
      <p class="section-subtitle">Exclusive Deals &amp; Discounts</p>
      <h1>Specials</h1>
      <p>Discover current promotional pricing on premium Husqvarna equipment and bundled package combos.</p>
    </div>
  </section>

  <!-- Specials Main Section -->
  <section class="section" id="specials-main-section">
    <div class="container">

      <!-- Two Main Interactive Category Blocks -->
      <div class="specials-blocks-grid">
        <!-- Block 1: Single Offers -->
        <div class="special-block-card active" id="block-card-single" onclick="switchSpecialsTab('single-offers')">
          <div class="block-card-header">
            <div class="block-card-icon">🏷️</div>
            <span class="block-card-badge">__SINGLE_COUNT__ Offers</span>
          </div>
          <h3 class="block-card-title">Single Offers</h3>
          <p class="block-card-desc">Special promotional pricing on individual Husqvarna equipment — chainsaws, leaf blowers, grass trimmers, brushcutters, lawn mowers, pole saws, tillers, and sprayers.</p>
          <div class="block-card-btn">
            <span>View Single Offers</span>
            <span class="block-arrow">&rarr;</span>
          </div>
        </div>

        <!-- Block 2: Bundles -->
        <div class="special-block-card" id="block-card-bundles" onclick="switchSpecialsTab('bundles')">
          <div class="block-card-header">
            <div class="block-card-icon">📦</div>
            <span class="block-card-badge">__BUNDLE_COUNT__ Bundles</span>
          </div>
          <h3 class="block-card-title">Bundles</h3>
          <p class="block-card-desc">Complete equipment combos, multi-battery kits, Aspire home series sets, and full Automower robotic setups with exceptional bundle savings.</p>
          <div class="block-card-btn">
            <span>View Bundles</span>
            <span class="block-arrow">&rarr;</span>
          </div>
        </div>
      </div>

      <!-- Filter & Search Bar -->
      <div class="specials-filter-bar">
        <div class="specials-tab-buttons">
          <button class="specials-tab-btn active" id="tab-btn-single" onclick="switchSpecialsTab('single-offers')">
            <span>🏷️ Single Offers</span>
            <span class="tab-count-badge" id="badge-count-single">__SINGLE_COUNT__</span>
          </button>
          <button class="specials-tab-btn" id="tab-btn-bundles" onclick="switchSpecialsTab('bundles')">
            <span>📦 Bundles</span>
            <span class="tab-count-badge" id="badge-count-bundles">__BUNDLE_COUNT__</span>
          </button>
        </div>

        <div class="specials-search-wrapper">
          <span class="specials-search-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></span>
          <input type="text" id="specials-search" class="specials-search-input" placeholder="Search by model or equipment (e.g. Chainsaw, Blower, Mower)..." oninput="filterSpecials()">
        </div>
      </div>

      <!-- Single Offers Gallery Block -->
      <div id="single-offers-block" class="specials-tab-content active">
        <div class="specials-content-header">
          <div>
            <h2>Single Special Offers</h2>
            <p style="color: #64748b; font-size: 0.95rem; margin-top: 4px;">Click on any flyer to view high-resolution details</p>
          </div>
          <p class="specials-count-label">Showing <span id="display-single-count">__SINGLE_COUNT__</span> offers</p>
        </div>
        <div class="specials-gallery-grid" id="grid-single-offers">
__SINGLE_CARDS__
        </div>
        <div id="no-results-single" style="display: none; text-align: center; padding: 60px 20px; color: #64748b;">
          <p style="font-size: 1.2rem; font-weight: 600;">No single offers match your search.</p>
          <button onclick="clearSearch()" class="btn btn-sm btn-outline" style="margin-top: 12px; cursor: pointer;">Clear Search</button>
        </div>
      </div>

      <!-- Bundles Gallery Block -->
      <div id="bundles-block" class="specials-tab-content" style="display: none;">
        <div class="specials-content-header">
          <div>
            <h2>Bundles &amp; Package Deals</h2>
            <p style="color: #64748b; font-size: 0.95rem; margin-top: 4px;">Click on any flyer to view high-resolution details</p>
          </div>
          <p class="specials-count-label">Showing <span id="display-bundle-count">__BUNDLE_COUNT__</span> bundles</p>
        </div>
        <div class="specials-gallery-grid" id="grid-bundles">
__BUNDLE_CARDS__
        </div>
        <div id="no-results-bundles" style="display: none; text-align: center; padding: 60px 20px; color: #64748b;">
          <p style="font-size: 1.2rem; font-weight: 600;">No bundles match your search.</p>
          <button onclick="clearSearch()" class="btn btn-sm btn-outline" style="margin-top: 12px; cursor: pointer;">Clear Search</button>
        </div>
      </div>

    </div>
  </section>

  <!-- Featured Transport Special (Velocity 150) -->
  <section class="section section-alt" style="padding: 60px 0; border-top: 1px solid #e2e8f0;">
    <div class="container">
      <div style="display: flex; gap: 48px; align-items: center; flex-wrap: wrap;">
        <div style="flex: 1; min-width: 300px; max-width: 460px;">
          <img src="images/september_special.png" alt="Special - Velocity Cargo 150" style="max-width: 100%; height: auto; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
        </div>
        <div style="flex: 1.2; min-width: 300px; line-height: 1.6; font-size: 1.05rem; color: #4a5568;">
          <span style="display: inline-block; padding: 4px 12px; border-radius: 50px; background: #fff3eb; color: #ea580c; font-weight: 700; font-size: 0.85rem; margin-bottom: 12px;">Featured Transport Special</span>
          <h2 style="color: #1a202c; font-size: 1.7rem; margin-bottom: 18px; font-weight: 800;">Velocity 150 &amp; Velocity Cargo 150</h2>
          
          <p style="margin-bottom: 16px;">Met brandstofpryse en daaglikse vervoerkoste wat aanhou styg, bied die Velocity 150-reeks ’n slim en ekonomiese oplossing met brandstofverbruik van slegs ~2.4 ℓ/100 km teen 70 km/h.</p>
          
          <p style="margin-bottom: 16px;">📦 <strong>Die Velocity Cargo 150</strong> is ideaal vir aflewerings en besigheidsgebruik met sy stewige vragrak.<br>
          🏍️ <strong>Die Velocity 150</strong> is die ideale daaglikse pendelkeuse met 3 jaar / 20,000 km fabriekswaarborg.</p>
          
          <div style="background-color: #ffffff; padding: 20px; border-radius: 8px; border-left: 4px solid #f97316; margin-top: 24px; box-shadow: 0 2px 10px rgba(0,0,0,0.04);">
            <p style="margin-bottom: 6px; font-weight: 700; color: #1a202c;">📍 OutLand Power and Turf — 9 Jakarandastraat, Jeffreysbaai</p>
            <p style="margin-bottom: 0;">📞 <a href="tel:0828028079" style="color: #f97316; text-decoration: none; font-weight: 700;">082 802 8079</a> &nbsp;|&nbsp; <a href="tel:0727318525" style="color: #f97316; text-decoration: none; font-weight: 700;">072 731 8525</a> &nbsp;|&nbsp; <a href="tel:0792113411" style="color: #f97316; text-decoration: none; font-weight: 700;">079 211 3411</a></p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="cta-section">
    <div class="container">
      <div class="fade-in">
        <h2>Want to see more equipment?</h2>
        <p>Visit our showroom at 9 Jakarand Street, Jeffreys Bay to view all items and talk with our experts.</p>
        <a href="contact.html" class="btn btn-orange">Get Directions &rarr;</a>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <img src="images/logo.png" alt="OutLand Logo">
          <p>OutLand Power and Turf (Pty) Ltd<br>Powering the Great Outdoors</p>
          <div class="footer-social">
            <a href="https://www.facebook.com/people/OutLand/61581158473050/" target="_blank" rel="noopener" aria-label="Facebook">f</a>
          </div>
        </div>
        <div>
          <h4>Quick Links</h4>
          <ul class="footer-links">
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="products.html">Products &amp; Services</a></li>
            <li><a href="used-items.html">Used Items</a></li>
            <li><a href="gallery.html">Gallery</a></li>
            <li><a href="reviews.html">Reviews</a></li>
            <li><a href="specials.html" class="active">Specials</a></li>
            <li><a href="mechanic-referral.html">Mechanic Referral</a></li>
            <li><a href="contact.html">Contact Us</a></li>
          </ul>
        </div>
        <div>
          <h4>Services</h4>
          <ul class="footer-links">
            <li><a href="products.html">Power Equipment</a></li>
            <li><a href="products.html">Turf Solutions</a></li>
            <li><a href="products.html">Maintenance &amp; Support</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <div class="footer-contact-item">
            <span class="footer-contact-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg></span>
            <span>9 Jakarand Street<br>Jeffreys Bay, 6330</span>
          </div>
          <div class="footer-contact-item">
            <span class="footer-contact-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg></span>
            <a href="tel:0828028079">082 802 8079</a>
          </div>
          <div class="footer-contact-item">
            <span class="footer-contact-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg></span>
            <a href="mailto:jean@outlandpt.co.za">jean@outlandpt.co.za</a>
          </div>
          <div class="footer-contact-item">
            <span class="footer-contact-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg></span>
            <span>
              <a href="tel:0792113411">079 211 3411</a><br>
              <a href="mailto:parts@outlandpt.co.za">parts@outlandpt.co.za</a>
            </span>
          </div>
          <div class="footer-contact-item">
            <span class="footer-contact-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></span>
            <span>Mon-Fri: 07:30-17:00<br>Sat: 08:00-12:00</span>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2025 OutLand Power and Turf (Pty) Ltd. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <!-- Specials Lightbox Modal -->
  <div class="lightbox" id="specials-lightbox">
    <span class="lightbox-close" onclick="closeSpecialsModal()">&times;</span>
    <span class="lightbox-nav lightbox-prev" onclick="prevSpecialsModal(event)">&#8249;</span>
    <span class="lightbox-nav lightbox-next" onclick="nextSpecialsModal(event)">&#8250;</span>
    <img id="specials-lightbox-img" src="" alt="Enlarged Special Offer Flyer">
    <div class="specials-lightbox-caption">
      <div>
        <span class="specials-lightbox-title" id="lightbox-title">Special Offer</span>
        &nbsp;&bull;&nbsp;
        <span class="specials-lightbox-price" id="lightbox-price"></span>
      </div>
      <a id="lightbox-wa-btn" href="#" target="_blank" rel="noopener" class="specials-lightbox-btn">
        💬 Enquire on WhatsApp
      </a>
    </div>
  </div>

  <script src="main.js"></script>
  <script>
    // ---- Interactive Specials Tabs & Modal Controller ----
    let currentCategory = 'single-offers';
    let currentModalIndex = 0;
    let visibleItemsList = [];

    function switchSpecialsTab(tabKey) {
      currentCategory = tabKey;

      // Update Cards
      const blockSingle = document.getElementById('block-card-single');
      const blockBundles = document.getElementById('block-card-bundles');
      if (tabKey === 'single-offers') {
        blockSingle.classList.add('active');
        blockBundles.classList.remove('active');
      } else {
        blockBundles.classList.add('active');
        blockSingle.classList.remove('active');
      }

      // Update Tabs
      const tabSingle = document.getElementById('tab-btn-single');
      const tabBundles = document.getElementById('tab-btn-bundles');
      if (tabKey === 'single-offers') {
        tabSingle.classList.add('active');
        tabBundles.classList.remove('active');
      } else {
        tabBundles.classList.add('active');
        tabSingle.classList.remove('active');
      }

      // Update Content Panes
      const paneSingle = document.getElementById('single-offers-block');
      const paneBundles = document.getElementById('bundles-block');
      if (tabKey === 'single-offers') {
        paneSingle.style.display = 'block';
        paneBundles.style.display = 'none';
      } else {
        paneSingle.style.display = 'none';
        paneBundles.style.display = 'block';
      }

      // Update URL hash without jumping
      if (history.replaceState) {
        history.replaceState(null, null, '#' + tabKey);
      } else {
        location.hash = tabKey;
      }

      // Re-apply search filter if any
      filterSpecials();
    }

    function filterSpecials() {
      const query = document.getElementById('specials-search').value.toLowerCase().trim();
      const currentGridId = currentCategory === 'single-offers' ? 'grid-single-offers' : 'grid-bundles';
      const noResultsId = currentCategory === 'single-offers' ? 'no-results-single' : 'no-results-bundles';
      const counterId = currentCategory === 'single-offers' ? 'display-single-count' : 'display-bundle-count';

      const grid = document.getElementById(currentGridId);
      const cards = grid.querySelectorAll('.special-card');
      let visibleCount = 0;

      cards.forEach(card => {
        const title = card.getAttribute('data-title') || '';
        const price = card.getAttribute('data-price') || '';
        const matches = title.includes(query) || price.toLowerCase().includes(query);
        if (matches) {
          card.style.display = '';
          visibleCount++;
        } else {
          card.style.display = 'none';
        }
      });

      document.getElementById(counterId).innerText = visibleCount;
      document.getElementById(noResultsId).style.display = visibleCount === 0 ? 'block' : 'none';
    }

    function clearSearch() {
      document.getElementById('specials-search').value = '';
      filterSpecials();
    }

    function getVisibleCards() {
      const currentGridId = currentCategory === 'single-offers' ? 'grid-single-offers' : 'grid-bundles';
      const grid = document.getElementById(currentGridId);
      const allCards = Array.from(grid.querySelectorAll('.special-card'));
      return allCards.filter(c => c.style.display !== 'none');
    }

    function openSpecialsModal(imgSrc, title, price) {
      const modal = document.getElementById('specials-lightbox');
      const modalImg = document.getElementById('specials-lightbox-img');
      const modalTitle = document.getElementById('lightbox-title');
      const modalPrice = document.getElementById('lightbox-price');
      const modalWa = document.getElementById('lightbox-wa-btn');

      visibleItemsList = getVisibleCards();
      currentModalIndex = visibleItemsList.findIndex(c => {
        const img = c.querySelector('img');
        return img && img.getAttribute('src') === imgSrc;
      });
      if (currentModalIndex === -1) currentModalIndex = 0;

      modalImg.src = imgSrc;
      modalTitle.innerText = title;
      modalPrice.innerText = price;
      
      const waText = encodeURIComponent('Hi OutLand, I am interested in the special offer: ' + title + ' (' + price + ')');
      modalWa.href = 'https://wa.me/27828028079?text=' + waText;

      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function closeSpecialsModal() {
      const modal = document.getElementById('specials-lightbox');
      modal.classList.remove('active');
      document.body.style.overflow = '';
    }

    function nextSpecialsModal(e) {
      if (e) e.stopPropagation();
      if (!visibleItemsList.length) visibleItemsList = getVisibleCards();
      if (!visibleItemsList.length) return;
      currentModalIndex = (currentModalIndex + 1) % visibleItemsList.length;
      updateModalFromCard(visibleItemsList[currentModalIndex]);
    }

    function prevSpecialsModal(e) {
      if (e) e.stopPropagation();
      if (!visibleItemsList.length) visibleItemsList = getVisibleCards();
      if (!visibleItemsList.length) return;
      currentModalIndex = (currentModalIndex - 1 + visibleItemsList.length) % visibleItemsList.length;
      updateModalFromCard(visibleItemsList[currentModalIndex]);
    }

    function updateModalFromCard(card) {
      const img = card.querySelector('img');
      const title = card.querySelector('.special-card-title').innerText;
      const price = card.querySelector('.special-card-price').innerText;
      
      const modalImg = document.getElementById('specials-lightbox-img');
      const modalTitle = document.getElementById('lightbox-title');
      const modalPrice = document.getElementById('lightbox-price');
      const modalWa = document.getElementById('lightbox-wa-btn');

      modalImg.src = img.getAttribute('src');
      modalTitle.innerText = title;
      modalPrice.innerText = price;

      const waText = encodeURIComponent('Hi OutLand, I am interested in the special offer: ' + title + ' (' + price + ')');
      modalWa.href = 'https://wa.me/27828028079?text=' + waText;
    }

    // Close on background click
    document.getElementById('specials-lightbox').addEventListener('click', (e) => {
      if (e.target.id === 'specials-lightbox') {
        closeSpecialsModal();
      }
    });

    // Keyboard events
    document.addEventListener('keydown', (e) => {
      const modal = document.getElementById('specials-lightbox');
      if (!modal || !modal.classList.contains('active')) return;
      if (e.key === 'Escape') closeSpecialsModal();
      if (e.key === 'ArrowRight') nextSpecialsModal();
      if (e.key === 'ArrowLeft') prevSpecialsModal();
    });

    // Check URL Hash on page load (e.g. #bundles or #single-offers)
    window.addEventListener('DOMContentLoaded', () => {
      const hash = window.location.hash.toLowerCase();
      if (hash === '#bundles' || hash === '#02_bundles') {
        switchSpecialsTab('bundles');
      } else {
        switchSpecialsTab('single-offers');
      }
    });
  </script>
</body>
</html>"""

final_html = html_template.replace("__SINGLE_COUNT__", str(single_count))\
                          .replace("__BUNDLE_COUNT__", str(bundle_count))\
                          .replace("__SINGLE_CARDS__", single_cards)\
                          .replace("__BUNDLE_CARDS__", bundle_cards)

with open('specials.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Successfully generated specials.html with {single_count} single offers and {bundle_count} bundles.")
