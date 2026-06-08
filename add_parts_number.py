import os

files = [f for f in os.listdir('.') if f.endswith('.html')] + ['main.js']
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update footer in all html files
    footer_old = '''          <div class="footer-contact-item">
            <span class="footer-contact-icon">⚙️</span>
            <a href="mailto:parts@outlandpt.co.za">parts@outlandpt.co.za</a>
          </div>'''
    
    footer_new = '''          <div class="footer-contact-item">
            <span class="footer-contact-icon">⚙️</span>
            <span>
              <a href="tel:0792113411">079 211 3411</a><br>
              <a href="mailto:parts@outlandpt.co.za">parts@outlandpt.co.za</a>
            </span>
          </div>'''
    content = content.replace(footer_old, footer_new)
    
    # 2. Update contact.html main contact section
    contact_old = '''            <div class="contact-item-text">
              <h4>Parts & Services</h4>
              <p><a href="mailto:parts@outlandpt.co.za">parts@outlandpt.co.za</a></p>
            </div>'''
    
    contact_new = '''            <div class="contact-item-text">
              <h4>Parts & Services</h4>
              <p><a href="tel:0792113411">079 211 3411</a></p>
              <p><a href="mailto:parts@outlandpt.co.za">parts@outlandpt.co.za</a></p>
            </div>'''
    content = content.replace(contact_old, contact_new)
    
    # 3. Update main.js chatbot logic
    mainjs_old = '''return "You can call us at 082 802 8079 or email jean@outlandpt.co.za (General) / parts@outlandpt.co.za (Parts/Workshop). We're located at 9 Jakarand Street, Jeffreys Bay.";'''
    
    mainjs_new = '''return "You can call us at 082 802 8079 (General) or 079 211 3411 (Parts & Services), or email jean@outlandpt.co.za / parts@outlandpt.co.za. We're located at 9 Jakarand Street, Jeffreys Bay.";'''
    content = content.replace(mainjs_old, mainjs_new)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print("Replacements complete.")
