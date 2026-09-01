import os
import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add to nav-links
    if 'href="specials.html"' not in content:
        content = content.replace('<a href="reviews.html">Reviews</a>', '<a href="reviews.html">Reviews</a>\n        <a href="specials.html">Specials</a>')
        
    # 2. Add to footer-links
    if '<li><a href="specials.html">Specials</a></li>' not in content:
        content = content.replace('<li><a href="reviews.html">Reviews</a></li>', '<li><a href="reviews.html">Reviews</a></li>\n            <li><a href="specials.html">Specials</a></li>')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
print('Done modifying HTML links.')
