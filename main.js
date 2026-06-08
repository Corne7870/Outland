/* ========================================
   OutLand Power and Turf — Main JavaScript
   ======================================== */

document.addEventListener('DOMContentLoaded', () => {

  // ---- Mobile Navigation ----
  const hamburger = document.querySelector('.hamburger');
  const navLinks = document.querySelector('.nav-links');
  const navOverlay = document.querySelector('.nav-overlay');
  const body = document.body;

  if (hamburger) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('active');
      navLinks.classList.toggle('active');
      navOverlay.classList.toggle('active');
      body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
    });

    if (navOverlay) {
      navOverlay.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
        navOverlay.classList.remove('active');
        body.style.overflow = '';
      });
    }

    // Close menu on link click
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
        navOverlay.classList.remove('active');
        body.style.overflow = '';
      });
    });
  }

  // ---- Navbar Scroll Effect ----
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    const handleScroll = () => {
      if (window.scrollY > 60) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    };
    
    // Initial check
    handleScroll();
    
    window.addEventListener('scroll', handleScroll);
  }

  // ---- Testimonial Slider ----
  const track = document.querySelector('.testimonial-track');
  const dots = document.querySelectorAll('.testimonial-dot');
  let currentSlide = 0;
  let totalSlides = dots.length;
  let autoSlideInterval;

  function goToSlide(index) {
    if (!track) return;
    currentSlide = index;
    track.style.transform = `translateX(-${currentSlide * 100}%)`;
    dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === currentSlide);
    });
  }

  if (dots.length > 0) {
    dots.forEach((dot, i) => {
      dot.addEventListener('click', () => {
        goToSlide(i);
        resetAutoSlide();
      });
    });

    function autoSlide() {
      autoSlideInterval = setInterval(() => {
        currentSlide = (currentSlide + 1) % totalSlides;
        goToSlide(currentSlide);
      }, 5000);
    }

    function resetAutoSlide() {
      clearInterval(autoSlideInterval);
      autoSlide();
    }

    autoSlide();
  }

  // ---- Gallery Lightbox ----
  const lightbox = document.querySelector('.lightbox');
  const lightboxImg = lightbox ? lightbox.querySelector('img') : null;
  const galleryItems = document.querySelectorAll('.gallery-item');
  let currentLightboxIndex = 0;
  const galleryImages = [];

  galleryItems.forEach((item, index) => {
    const img = item.querySelector('img');
    if (img) {
      galleryImages.push(img.src);
      item.addEventListener('click', () => {
        currentLightboxIndex = index;
        openLightbox(img.src);
      });
    }
  });

  function openLightbox(src) {
    if (!lightbox || !lightboxImg) return;
    lightboxImg.src = src;
    lightbox.classList.add('active');
    body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    if (!lightbox) return;
    lightbox.classList.remove('active');
    body.style.overflow = '';
  }

  if (lightbox) {
    const closeBtn = lightbox.querySelector('.lightbox-close');
    const prevBtn = lightbox.querySelector('.lightbox-prev');
    const nextBtn = lightbox.querySelector('.lightbox-next');

    if (closeBtn) closeBtn.addEventListener('click', closeLightbox);

    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) closeLightbox();
    });

    if (prevBtn) {
      prevBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        currentLightboxIndex = (currentLightboxIndex - 1 + galleryImages.length) % galleryImages.length;
        lightboxImg.src = galleryImages[currentLightboxIndex];
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        currentLightboxIndex = (currentLightboxIndex + 1) % galleryImages.length;
        lightboxImg.src = galleryImages[currentLightboxIndex];
      });
    }

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (!lightbox.classList.contains('active')) return;
      if (e.key === 'Escape') closeLightbox();
      if (e.key === 'ArrowLeft' && prevBtn) prevBtn.click();
      if (e.key === 'ArrowRight' && nextBtn) nextBtn.click();
    });
  }

  // ---- Scroll Animations ----
  const fadeElements = document.querySelectorAll('.fade-in');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  fadeElements.forEach(el => observer.observe(el));

  // ---- Contact Form ----
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const name = contactForm.querySelector('[name="name"]');
      const email = contactForm.querySelector('[name="email"]');
      const phone = contactForm.querySelector('[name="phone"]');
      const message = contactForm.querySelector('[name="message"]');
      const submitBtn = contactForm.querySelector('button[type="submit"]');

      // Basic validation
      if (!name.value.trim() || !email.value.trim() || !message.value.trim()) {
        alert('Please fill in all required fields.');
        return;
      }

      // Show loading state
      const originalBtnText = submitBtn.innerHTML;
      submitBtn.innerHTML = 'Sending...';
      submitBtn.disabled = true;

      // Prepare data for Formspree (or any form handler)
      // We'll use a direct fetch to Formspree's email endpoint
      const formData = new FormData();
      formData.append('name', name.value);
      formData.append('email', email.value);
      formData.append('phone', phone.value);
      formData.append('message', message.value);
      formData.append('_replyto', email.value);
      formData.append('_subject', `New Message from ${name.value} (OutLand Website)`);
      // Formspree allows sending to multiple emails if configured, 
      // but for now we'll point to the main one and they can add the second in Formspree settings.
      // Alternatively, we use a service that supports multiple recipients.

      fetch('https://formspree.io/f/mjvnpqoa', { // Note: I'm using a placeholder or common pattern, they should replace with their actual ID
        method: 'POST',
        body: formData,
        headers: {
          'Accept': 'application/json'
        }
      })
      .then(response => {
        if (response.ok) {
          const formMessage = contactForm.querySelector('.form-message');
          if (formMessage) {
            formMessage.classList.add('success');
            formMessage.textContent = 'Thank you! Your message has been sent to Jean and the Parts department.';
            formMessage.style.display = 'block';
          }
          contactForm.reset();
        } else {
          throw new Error('Form submission failed');
        }
      })
      .catch(error => {
        alert('Oops! There was a problem sending your message. Please try again or email us directly.');
      })
      .finally(() => {
        submitBtn.innerHTML = originalBtnText;
        submitBtn.disabled = false;
        
        setTimeout(() => {
          const formMessage = contactForm.querySelector('.form-message');
          if (formMessage) {
            formMessage.style.display = 'none';
            formMessage.classList.remove('success');
          }
        }, 5000);
      });
    });
  }

  // ---- Active Nav Link ----
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  const allNavLinks = document.querySelectorAll('.nav-links a:not(.nav-cta)');
  allNavLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  // ---- WhatsApp Floating Button ----
  const waButton = document.createElement('a');
  waButton.href = 'https://wa.me/27828028079';
  waButton.className = 'whatsapp-float';
  waButton.target = '_blank';
  waButton.rel = 'noopener noreferrer';
  waButton.ariaLabel = 'Chat with us on WhatsApp';
  waButton.innerHTML = `
    <svg xmlns="http://www.w3.org/2000/svg" width="34" height="34" fill="currentColor" class="bi bi-whatsapp" viewBox="0 0 16 16">
      <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.49.652.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.005-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
    </svg>
  `;
  document.body.appendChild(waButton);

  // ---- Custom Chatbot Button & Window ----
  const botBtn = document.createElement('button');
  botBtn.className = 'chatbot-float';
  botBtn.ariaLabel = 'Open Chatbot';
  botBtn.innerHTML = `
    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="currentColor" class="bi bi-chat-dots-fill" viewBox="0 0 16 16">
      <path d="M16 8c0 3.866-3.582 7-8 7a9.06 9.06 0 0 1-2.347-.306c-.584.296-1.925.864-4.181 1.234-.2.032-.352-.176-.273-.362.354-.836.674-1.95.77-2.966C.744 11.37 0 9.76 0 8c0-3.866 3.582-7 8-7s8 3.134 8 7zM5 8a1 1 0 1 0-2 0 1 1 0 0 0 2 0zm4 0a1 1 0 1 0-2 0 1 1 0 0 0 2 0zm3 1a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"/>
    </svg>
  `;
  document.body.appendChild(botBtn);

  const botWindow = document.createElement('div');
  botWindow.className = 'chatbot-window';
  botWindow.innerHTML = `
    <div class="chatbot-header">
      <h4>OutLand Assistant</h4>
      <button class="chatbot-close" aria-label="Close Chat">&times;</button>
    </div>
    <div class="chatbot-messages" id="chatbot-messages">
      <div class="chatbot-msg bot">Hi there! I know everything about OutLand Power and Turf. How can I help you today?</div>
    </div>
    <div class="chatbot-input-area">
      <input type="text" id="chatbot-input" placeholder="Type a message..." autocomplete="off">
      <button id="chatbot-send">Send</button>
    </div>
  `;
  document.body.appendChild(botWindow);

  const messagesContainer = botWindow.querySelector('#chatbot-messages');
  const inputField = botWindow.querySelector('#chatbot-input');
  const sendBtn = botWindow.querySelector('#chatbot-send');
  const closeBtn = botWindow.querySelector('.chatbot-close');

  botBtn.addEventListener('click', () => {
    botWindow.classList.toggle('active');
    if (botWindow.classList.contains('active')) {
      inputField.focus();
    }
  });

  closeBtn.addEventListener('click', () => {
    botWindow.classList.remove('active');
  });

  function addMessage(text, sender) {
    const msgDiv = document.createElement('div');
    msgDiv.className = 'chatbot-msg ' + sender;
    msgDiv.textContent = text;
    messagesContainer.appendChild(msgDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }

  function getBotResponse(userMsg) {
    const msg = userMsg.toLowerCase();
    if (msg.includes('contact') || msg.includes('phone') || msg.includes('email') || msg.includes('call')) {
      return "You can call us at 082 802 8079 (General) or 079 211 3411 (Parts & Services), or email jean@outlandpt.co.za / parts@outlandpt.co.za. We're located at 9 Jakarand Street, Jeffreys Bay.";
    }
    if (msg.includes('hour') || msg.includes('time') || msg.includes('open') || msg.includes('close')) {
      return "We are open Monday to Friday from 07:30 to 17:00, and Saturday from 08:00 to 12:00.";
    }
    if (msg.includes('brand')) {
      return "We supply top brands including Husqvarna, Pellenc, Total Tools, Ultra Scooter, SAM, and Multi Power.";
    }
    if (msg.includes('service') || msg.includes('repair') || msg.includes('part') || msg.includes('fix')) {
      return "We offer full after-sales support including equipment servicing, repairs, spare parts supply, technical advice, and diagnostic inspections.";
    }
    if (msg.includes('mower') || msg.includes('garden') || msg.includes('turf') || msg.includes('grass')) {
      return "We have a big range of garden and turf equipment including lawnmowers, brushcutters, leaf blowers, and garden tractors. We also carry battery-powered options!";
    }
    if (msg.includes('chain') || msg.includes('tree') || msg.includes('forestry')) {
      return "Our forestry equipment includes professional chainsaws, pole pruners, wood chippers, and clearing saws from trusted brands like Husqvarna.";
    }
    if (msg.includes('transport') || msg.includes('motorcycle') || msg.includes('scooter') || msg.includes('bike')) {
      return "We offer everyday mobility options like motorcycles, electric scooters (Ultra Scooter), and utility vehicles for petrol, diesel, and electric transport.";
    }
    if (msg.includes('tool')) {
      return "We stock power tools (cordless/battery & electric), hand tools, compressors, and workshop equipment from brands like Total Tools.";
    }
    if (msg.includes('used') || msg.includes('second hand')) {
      return "Yes, we sell used items! Check out our 'Used Items' page for our latest inventory of pre-owned equipment.";
    }
    if (msg.includes('location') || msg.includes('where') || msg.includes('address')) {
      return "We are based in Jeffreys Bay at 9 Jakarand Street, 6330.";
    }
    return "I'm still learning! But we offer outdoor power equipment, tools, transport solutions, and expert service. For detailed info, please contact us at 082 802 8079.";
  }

  function handleSend() {
    const text = inputField.value.trim();
    if (!text) return;
    addMessage(text, 'user');
    inputField.value = '';
    
    setTimeout(() => {
      const reply = getBotResponse(text);
      addMessage(reply, 'bot');
    }, 500);
  }

  sendBtn.addEventListener('click', handleSend);
  inputField.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') handleSend();
  });

});
