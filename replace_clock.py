import os

svg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>'

files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if '🕒' in content:
        content = content.replace('🕒', svg)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated {f}')
