// Streamux AI Website Interactive Engine

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
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      navbar.style.background = 'rgba(11, 17, 32, 0.95)';
      navbar.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.5)';
    } else {
      navbar.style.background = 'rgba(11, 17, 32, 0.85)';
      navbar.style.boxShadow = 'none';
    }
  });

  // Video Demo Filtering / Tabs
  const filterBtns = document.querySelectorAll('.video-filter-btn');
  const videoCards = document.querySelectorAll('.video-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active', 'btn-primary'));
      filterBtns.forEach(b => b.classList.add('btn-secondary'));
      
      btn.classList.remove('btn-secondary');
      btn.classList.add('active', 'btn-primary');

      const filter = btn.getAttribute('data-filter');

      videoCards.forEach(card => {
        if (filter === 'all' || card.getAttribute('data-category') === filter) {
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
      const target = +stat.getAttribute('data-target');
      const count = +stat.innerText.replace('+', '').replace('%', '').replace('x', '');
      const speed = target / 50;

      if (count < target) {
        const nextVal = Math.ceil(count + speed);
        const suffix = stat.getAttribute('data-suffix') || '';
        stat.innerText = nextVal + suffix;
        setTimeout(animateStats, 30);
      } else {
        const suffix = stat.getAttribute('data-suffix') || '';
        stat.innerText = target + suffix;
      }
    });
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !animated) {
        animated = true;
        animateStats();
      }
    });
  }, { threshold: 0.5 });

  const statsBanner = document.querySelector('.stats-banner');
  if (statsBanner) {
    observer.observe(statsBanner);
  }
});
