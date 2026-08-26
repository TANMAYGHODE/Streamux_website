// Streamux.ai Interactive Script

document.addEventListener('DOMContentLoaded', () => {
  initTelemetrySimulator();
  initCounters();
  initSmoothScroll();
});

// Interactive Telemetry Simulation Component
function initTelemetrySimulator() {
  const canvas = document.getElementById('radarCanvas');
  const logBox = document.getElementById('logBox');
  const fpsDisplay = document.getElementById('hudFps');
  const latencyDisplay = document.getElementById('hudLatency');
  const threatDisplay = document.getElementById('hudThreats');

  if (!canvas || !logBox) return;

  const targets = [
    { id: 'T-101', label: 'VEHICLE [98%]', color: '#06b6d4', x: 20, y: 30, w: 80, h: 50, dx: 1.5, dy: 0.8 },
    { id: 'T-102', label: 'PERSON [94%]', color: '#8b5cf6', x: 180, y: 120, w: 45, h: 70, dx: -1.2, dy: 1.1 },
    { id: 'T-103', label: 'TARGET [99%]', color: '#ef4444', x: 260, y: 50, w: 60, h: 60, dx: 0.9, dy: -1.4 }
  ];

  // Render Target Boxes
  targets.forEach((t) => {
    const el = document.createElement('div');
    el.className = 'box-target';
    el.id = `box-${t.id}`;
    el.setAttribute('data-label', `${t.id} : ${t.label}`);
    el.style.borderColor = t.color;
    canvas.appendChild(el);
  });

  const logMessages = [
    'Object tracker initialized [TensorRT FP16]',
    'Multi-stream RTSP feed #1 decoded at 60 FPS',
    'Sub-pixel centroid offset calculated: dx=+0.12px, dy=-0.04px',
    'YOLO11x inference completed in 1.42ms',
    'Target T-101 lock confirmed (IoU = 0.94)',
    'UDP Telemetry packet dispatched to lead-angle controller',
    'CSRT correlation filter refreshed across 4 threads',
    'Keypoint estimation confidence > 96.8%'
  ];

  let frameCount = 0;

  function animate() {
    frameCount++;

    // Update target positions within canvas bounds
    targets.forEach((t) => {
      const el = document.getElementById(`box-${t.id}`);
      if (!el) return;

      t.x += t.dx;
      t.y += t.dy;

      const cw = canvas.clientWidth;
      const ch = canvas.clientHeight;

      if (t.x <= 10 || t.x + t.w >= cw - 10) t.dx *= -1;
      if (t.y <= 10 || t.y + t.h >= ch - 10) t.dy *= -1;

      el.style.left = `${t.x}px`;
      el.style.top = `${t.y}px`;
      el.style.width = `${t.w}px`;
      el.style.height = `${t.h}px`;
    });

    // Update Telemetry Displays periodically
    if (frameCount % 30 === 0 && fpsDisplay) {
      const jitterFps = (59.2 + Math.random() * 1.6).toFixed(1);
      const jitterLat = (1.1 + Math.random() * 0.4).toFixed(2);
      fpsDisplay.textContent = `${jitterFps} FPS`;
      latencyDisplay.textContent = `${jitterLat} ms`;
    }

    // Append live telemetry logs periodically
    if (frameCount % 120 === 0 && logBox) {
      const now = new Date().toISOString().substring(11, 19);
      const msg = logMessages[Math.floor(Math.random() * logMessages.length)];
      const entry = document.createElement('div');
      entry.className = 'log-entry';
      entry.innerHTML = `<span class="time">[${now}]</span> <span class="tag">[STREAMUX]</span> ${msg}`;
      logBox.appendChild(entry);
      
      // Limit logs
      if (logBox.children.length > 12) {
        logBox.removeChild(logBox.firstChild);
      }
      logBox.scrollTop = logBox.scrollHeight;
    }

    requestAnimationFrame(animate);
  }

  requestAnimationFrame(animate);
}

// Counter animation for statistics
function initCounters() {
  const counters = document.querySelectorAll('.number[data-target]');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = +entry.target.getAttribute('data-target');
        const duration = 1500;
        const stepTime = 20;
        const steps = duration / stepTime;
        const inc = target / steps;
        let current = 0;

        const timer = setInterval(() => {
          current += inc;
          if (current >= target) {
            entry.target.textContent = target + (entry.target.getAttribute('data-suffix') || '');
            clearInterval(timer);
          } else {
            entry.target.textContent = Math.floor(current) + (entry.target.getAttribute('data-suffix') || '');
          }
        }, stepTime);

        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(c => observer.observe(c));
}

// Smooth scroll handling
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        e.preventDefault();
        targetEl.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
}
