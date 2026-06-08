import os

files = [f for f in os.listdir('.') if f.endswith('.html')] + ['styles.css', 'main.js']
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'logo.jpg' in content:
        content = content.replace('logo.jpg', 'logo.png')
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
print("Reverted to logo.png.")
