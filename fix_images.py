import os

def replace_in_file(filename, old_str, new_str):
    if not os.path.exists(filename): return
    with open(filename, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace(old_str, new_str)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(c)

replace_in_file('about.html', 'src=""', 'src="images/signage.jpg"')
replace_in_file('gallery.html', 'src=""', 'src="images/husqvarna-showroom.jpg"')
replace_in_file('used-items.html', 'src="images/ITEM_IMAGE.jpg"', 'src="images/guy-working-machine.jpg"')
print('Images replaced.')
