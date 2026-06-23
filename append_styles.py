css_to_add = """
/* ---- Premium Gradient Layout ---- */
.premium-gradient-section {
  width: 100%;
  padding: 80px 0;
  background: linear-gradient(135deg, var(--blue-dark) 0%, var(--blue) 50%, #204060 100%);
  position: relative;
}

.unified-content-card {
  width: 100%;
  max-width: 1100px;
  background: linear-gradient(to bottom right, #ffffff, #f0f4f8);
  border-radius: var(--radius);
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.4);
  overflow: hidden;
  margin: 0 auto;
}

.unified-card-top-grid {
  display: flex;
  flex-direction: column;
}

.unified-card-text {
  width: 100%;
  padding: 60px 80px;
  text-align: center;
}

.unified-card-text h2 {
  font-size: 2.2rem;
  color: var(--blue-dark);
  margin-bottom: 16px;
}

.unified-card-text p {
  color: var(--text-light);
  font-size: 1.1rem;
  line-height: 1.8;
  margin-bottom: 32px;
}

.brands-dark-strip {
  background: #08131e;
  padding: 40px 20px;
  text-align: center;
}

.shop-here-title {
  color: var(--white);
  font-size: 1.5rem;
  margin-bottom: 32px;
  text-transform: uppercase;
  letter-spacing: 2px;
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(css_to_add)

print('CSS appended correctly.')
