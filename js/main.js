// Streamux AI Website Interactive Engine
// Cross-browser tested, production-grade interactivity

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Navigation Toggle
  const mobileNavToggle = document.getElementById('mobileNavToggle');
  const navMenu = document.getElementById('navMenu');

  if (mobileNavToggle && navMenu) {
    mobileNavToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      navMenu.classList.toggle('active');
      const icon = mobileNavToggle.querySelector('i');
      if (icon) {
        if (navMenu.classList.contains('active')) {
          icon.classList.remove('fa-bars');
          icon.classList.add('fa-times');
        } else {
          icon.classList.remove('fa-times');
          icon.classList.add('fa-bars');
        }
      }
    });

    // Close menu when clicking outside or clicking any nav link
    document.addEventListener('click', (e) => {
      if (!navMenu.contains(e.target) && !mobileNavToggle.contains(e.target)) {
        navMenu.classList.remove('active');
        const icon = mobileNavToggle.querySelector('i');
        if (icon) {
          icon.classList.remove('fa-times');
          icon.classList.add('fa-bars');
        }
      }
    });

    navMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        const icon = mobileNavToggle.querySelector('i');
        if (icon) {
          icon.classList.remove('fa-times');
          icon.classList.add('fa-bars');
        }
      });
    });
  }

  // 2. Header Scroll Blur & Shadow Effect
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 30) {
        navbar.style.background = 'rgba(11, 17, 32, 0.96)';
        navbar.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.5)';
      } else {
        navbar.style.background = 'rgba(11, 17, 32, 0.88)';
        navbar.style.boxShadow = 'none';
      }
    });
  }

  // 3. Video Demo Filtering / Category Tabs
  const filterBtns = document.querySelectorAll('.video-filter-btn');
  const videoCards = document.querySelectorAll('.video-card');

  if (filterBtns.length > 0) {
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
  }

  // 4. Contact Form Submission Handling (FormSubmit / Web3Forms / AJAX)
  const contactForm = document.getElementById('contactForm');
  const formSuccess = document.getElementById('formSuccess');
  const formError = document.getElementById('formError');

  if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const submitBtn = contactForm.querySelector('button[type="submit"]');
      const originalText = submitBtn.innerHTML;

      submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Submitting Request...';
      submitBtn.disabled = true;

      // Extract form fields
      const name = contactForm.querySelector('[name="name"]')?.value || contactForm.querySelector('input[type="text"]')?.value || 'Prospective Client';
      const email = contactForm.querySelector('[name="email"]')?.value || contactForm.querySelector('input[type="email"]')?.value || '';
      const phone = contactForm.querySelector('[name="phone"]')?.value || 'Not provided';
      const solution = contactForm.querySelector('[name="solution"]')?.value || contactForm.querySelector('select')?.value || 'General Inquiry';
      const requirements = contactForm.querySelector('[name="requirements"]')?.value || contactForm.querySelector('textarea')?.value || 'None specified';

      const payload = {
        name: name,
        email: email,
        phone: phone,
        solution: solution,
        requirements: requirements,
        _subject: `New Streamux AI Demo Request from ${name}`,
        _template: 'table'
      };

      try {
        // Send request via FormSubmit AJAX endpoint configured for contact@streamux.ai
        const response = await fetch('https://formsubmit.co/ajax/contact@streamux.ai', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          },
          body: JSON.stringify(payload)
        });

        if (response.ok) {
          contactForm.reset();
          if (formSuccess) {
            formSuccess.style.display = 'flex';
            setTimeout(() => {
              formSuccess.style.display = 'none';
            }, 8000);
          }
          if (formError) formError.style.display = 'none';
        } else {
          throw new Error('Server response was not ok');
        }
      } catch (err) {
        console.warn('Direct AJAX submit fallback triggered:', err);
        // Fallback: If network blocks cross-origin or service is offline, open mailto fallback cleanly
        const mailtoLink = `mailto:contact@streamux.ai?subject=${encodeURIComponent('Streamux AI Demo Request: ' + name)}&body=${encodeURIComponent(`Name: ${name}\nEmail: ${email}\nPhone: ${phone}\nSolution: ${solution}\nRequirements: ${requirements}`)}`;
        
        if (formSuccess) {
          formSuccess.innerHTML = `<i class="fas fa-check-circle"></i> Request prepared! If your email client does not open automatically, <a href="${mailtoLink}" style="color: #fff; text-decoration: underline; font-weight: bold; margin-left: 6px;">click here to email contact@streamux.ai</a>.`;
          formSuccess.style.display = 'flex';
        }
        window.location.href = mailtoLink;
      } finally {
        submitBtn.innerHTML = originalText;
        submitBtn.disabled = false;
      }
    });
  }

  // 5. Counter Animation for Stats
  const statNumbers = document.querySelectorAll('.stat-number');
  let animated = false;

  const animateStats = () => {
    statNumbers.forEach(stat => {
      const target = parseInt(stat.getAttribute('data-target') || '0', 10);
      const currentText = stat.textContent || stat.innerText || '0';
      const count = parseInt(currentText.replace(/[^0-9]/g, '') || '0', 10);
      const step = Math.max(1, Math.ceil(target / 35));

      if (count < target) {
        const nextVal = Math.min(target, count + step);
        const suffix = stat.getAttribute('data-suffix') || '';
        stat.textContent = nextVal + suffix;
        setTimeout(animateStats, 35);
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
    }, { threshold: 0.2 });

    const statsBanner = document.querySelector('.stats-banner');
    if (statsBanner) {
      observer.observe(statsBanner);
    }
  } else {
    animateStats();
  }
});
