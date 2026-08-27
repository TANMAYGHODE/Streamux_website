// Streamux AI Website Interactive Engine (Firefox & Cross-Browser Tested)

document.addEventListener('DOMContentLoaded', () => {
  // Mobile Nav Toggle
  const mobileNavToggle = document.getElementById('mobileNavToggle');
  const navMenu = document.getElementById('navMenu');

  if (mobileNavToggle && navMenu) {
    mobileNavToggle.addEventListener('click', () => {
      navMenu.classList.toggle('active');
    });
  }

  // Header Scroll Blur Effect
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        navbar.style.background = 'rgba(11, 17, 32, 0.95)';
        navbar.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.5)';
      } else {
        navbar.style.background = 'rgba(11, 17, 32, 0.85)';
        navbar.style.boxShadow = 'none';
      }
    });
  }

  // Video Demo Filtering / Tabs
  const filterBtns = document.querySelectorAll('.video-filter-btn');
  const videoCards = document.querySelectorAll('.video-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => {
        b.classList.remove('active', 'btn-primary');
        b.classList.add('btn-secondary');
      });
      
      btn.classList.remove('btn-secondary');
      btn.classList.add('active', 'btn-primary');

      const filter = btn.getAttribute('data-filter');

      videoCards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (filter === 'all' || category === filter) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // Contact Form Interactivity
  const contactForm = document.getElementById('contactForm');
  const formSuccess = document.getElementById('formSuccess');

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const submitBtn = contactForm.querySelector('button[type="submit"]');
      const originalText = submitBtn.innerHTML;

      submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending Request...';
      submitBtn.disabled = true;

      setTimeout(() => {
        contactForm.reset();
        submitBtn.innerHTML = originalText;
        submitBtn.disabled = false;
        
        if (formSuccess) {
          formSuccess.style.display = 'block';
          setTimeout(() => {
            formSuccess.style.display = 'none';
          }, 5000);
        }
      }, 1500);
    });
  }

  // Counter Animation for Stats
  const statNumbers = document.querySelectorAll('.stat-number');
  let animated = false;

  const animateStats = () => {
    statNumbers.forEach(stat => {
      const target = parseInt(stat.getAttribute('data-target') || '0', 10);
      const currentText = stat.textContent || stat.innerText || '0';
      const count = parseInt(currentText.replace(/[^0-9]/g, '') || '0', 10);
      const step = Math.max(1, Math.ceil(target / 40));

      if (count < target) {
        const nextVal = Math.min(target, count + step);
        const suffix = stat.getAttribute('data-suffix') || '';
        stat.textContent = nextVal + suffix;
        setTimeout(animateStats, 30);
      } else {
        const suffix = stat.getAttribute('data-suffix') || '';
        stat.textContent = target + suffix;
      }
    });
  };

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !animated) {
          animated = true;
          animateStats();
        }
      });
    }, { threshold: 0.3 });

    const statsBanner = document.querySelector('.stats-banner');
    if (statsBanner) {
      observer.observe(statsBanner);
    }
  } else {
    // Fallback for older browsers
    animateStats();
  }
});
