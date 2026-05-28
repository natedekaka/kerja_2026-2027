(() => {
  'use strict';

  /* ─── Dark mode ─── */
  const toggle = document.getElementById('themeToggle');
  const html = document.documentElement;
  if (localStorage.getItem('dark') === 'true') {
    html.classList.add('dark-mode');
    toggle.textContent = '\u2600';
  }
  if (toggle) {
    toggle.addEventListener('click', () => {
      const on = html.classList.toggle('dark-mode');
      localStorage.setItem('dark', on);
      toggle.textContent = on ? '\u2600' : '\u263d';
    });
  }

  /* ─── Back to top ─── */
  const btt = document.getElementById('backToTop');
  if (btt) {
    let ticking = false;
    window.addEventListener('scroll', () => {
      if (!ticking) {
        requestAnimationFrame(() => {
          btt.classList.toggle('visible', window.scrollY > 300);
          ticking = false;
        });
        ticking = true;
      }
    });
    btt.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }

  /* ─── Mobile hamburger ─── */
  const hamburger = document.getElementById('hamburgerBtn');
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('sidebarOverlay');
  if (hamburger && sidebar && overlay) {
    function closeSidebar() {
      sidebar.classList.remove('open');
      overlay.classList.remove('active');
      hamburger.style.display = '';
    }
    hamburger.addEventListener('click', () => {
      sidebar.classList.toggle('open');
      overlay.classList.toggle('active');
      hamburger.style.display = 'none';
    });
    overlay.addEventListener('click', closeSidebar);
    document.addEventListener('keydown', e => { if (e.key === 'Escape') closeSidebar(); });
  }

  /* ─── Animate progress bars on scroll ─── */
  const fillBars = () => {
    document.querySelectorAll('.progress-bar-fill[style*="width: 0"]').forEach(bar => {
      const rect = bar.closest('.progress-item').getBoundingClientRect();
      if (rect.top < window.innerHeight - 40) {
        const pct = bar.getAttribute('data-pct') || '100';
        bar.style.width = pct + '%';
      }
    });
  };
  window.addEventListener('scroll', () => { requestAnimationFrame(fillBars); });
  window.addEventListener('load', () => { setTimeout(fillBars, 200); });

  /* ─── Search filter ─── */
  const searchInput = document.getElementById('docSearch');
  const clearBtn = document.getElementById('searchClear');
  if (searchInput) {
    /* collect all searchable items */
    const items = [];
    document.querySelectorAll('.grade-card, .teacher-card, .identity-section, .stat-card').forEach(el => {
      items.push({ el, text: el.textContent.toLowerCase() });
    });
    /* also collect all links from grade cards */
    const gradeLinks = [];
    document.querySelectorAll('.grade-card .links a').forEach(a => {
      gradeLinks.push({ el: a, href: a.getAttribute('href'), text: a.textContent.toLowerCase() });
    });

    searchInput.addEventListener('input', () => {
      const q = searchInput.value.trim().toLowerCase();
      if (q) {
        clearBtn.classList.add('visible');
      } else {
        clearBtn.classList.remove('visible');
      }

      /* filter items */
      let anyMatch = false;
      items.forEach(item => {
        const match = !q || item.text.includes(q);
        item.el.style.display = match ? '' : 'none';
        if (match && q) anyMatch = true;
      });

      /* highlight matching links */
      gradeLinks.forEach(gl => {
        const match = !q || gl.text.includes(q);
        gl.el.style.opacity = match ? '1' : '0.25';
        if (!q) gl.el.style.opacity = '1';
      });
    });
  }
  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      if (searchInput) {
        searchInput.value = '';
        searchInput.dispatchEvent(new Event('input'));
        searchInput.focus();
      }
    });
  }
})();
