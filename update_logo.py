import os

files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    old_logo = '''        <div class="nav-logo-text">
          OutLand Power & Turf
          <span>Powering the Great Outdoors</span>
        </div>'''
    
    new_logo = '''        <div class="nav-logo-text">
          <div class="logo-outland">OUTLAND</div>
          <div class="logo-sub">
            <span class="logo-dash">—</span> POWER &amp; TURF <span class="logo-dash">—</span>
          </div>
        </div>'''
    
    # Also another version if there are differences
    old_logo_2 = '''        <div class="nav-logo-text">
          OutLand Power &amp; Turf
          <span>Powering the Great Outdoors</span>
        </div>'''
    
    content = content.replace(old_logo, new_logo)
    content = content.replace(old_logo_2, new_logo)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print("Logo HTML updated.")
