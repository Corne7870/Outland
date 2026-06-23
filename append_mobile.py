css = """
/* ---- Mobile Layout Adjustments ---- */
@media (max-width: 768px) {
  .premium-gradient-section {
    padding: 40px 0;
  }
  
  .unified-card-text {
    padding: 40px 24px;
  }
  
  .unified-card-text h2 {
    font-size: 1.8rem;
  }
  
  .brands-dark-strip {
    padding: 32px 16px;
  }
  
  .shop-here-title {
    font-size: 1.25rem;
  }
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(css)
print("Mobile styles appended.")
