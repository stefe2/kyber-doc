document.addEventListener('DOMContentLoaded', () => {
  // Create lightbox elements once
  const lightbox = document.createElement('div');
  lightbox.id = 'lightbox';
  lightbox.style.cssText = `
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.9);
    z-index: 1000;
    cursor: pointer;
  `;

  const lightboxImg = document.createElement('img');
  lightboxImg.style.cssText = `
    max-height: 90vh;
    max-width: 90vw;
    margin: auto;
    display: block;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  `;

  lightbox.appendChild(lightboxImg);
  document.body.appendChild(lightbox);

  // Add click handlers to all images
  document.querySelectorAll('.md-content img').forEach(img => {
    img.style.cursor = 'pointer';
    img.addEventListener('click', e => {
      lightboxImg.src = img.src;
      lightbox.style.display = 'block';
    });
  });

  // Close on click or ESC key
  lightbox.addEventListener('click', () => {
    lightbox.style.display = 'none';
  });

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      lightbox.style.display = 'none';
    }
  });
});