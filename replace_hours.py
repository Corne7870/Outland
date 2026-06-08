import os

files = [f for f in os.listdir('.') if f.endswith('.html')] + ['main.js']
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replacements
    content = content.replace('07:30-13:00', '08:00-12:00')
    content = content.replace('07:30 - 13:00', '08:00 - 12:00')
    content = content.replace('from 07:30 to 13:00', 'from 08:00 to 12:00')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print("Replacements complete.")
