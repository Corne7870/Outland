import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
issues = []

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    links = re.findall(r'href=["\'](.*?)["\']', content)
    images = re.findall(r'src=["\'](.*?)["\']', content)
    
    for link in links:
        if link.startswith('http') or link.startswith('mailto:') or link.startswith('tel:'):
            continue
        if link == '' or link == '#':
            issues.append(f'{f}: Empty or # link found.')
        elif link.endswith('.html') and link not in html_files:
            issues.append(f'{f}: Broken link to {link}')
            
    for img in images:
        if img.startswith('http'):
            continue
        if not os.path.exists(img):
            issues.append(f'{f}: Missing image {img}')

for issue in set(issues):
    print(issue)

if not issues:
    print('No broken local links or missing images found.')
