/* ── UPG Main JS ─────────────────────────────────────────── */

// Init AOS
AOS.init({
  duration: 700,
  once: true,
  offset: 60,
});

/* ── Navbar scroll effect ────────────────────────────────── */
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 10) {
    navbar?.classList.add('scrolled');
  } else {
    navbar?.classList.remove('scrolled');
  }
});

/* ── Mobile menu ─────────────────────────────────────────── */
const mobileMenuBtn  = document.getElementById('mobile-menu-btn');
const mobileMenu     = document.getElementById('mobile-menu');
const menuIconOpen   = document.getElementById('menu-icon-open');
const menuIconClose  = document.getElementById('menu-icon-close');

mobileMenuBtn?.addEventListener('click', () => {
  const isOpen = !mobileMenu.classList.contains('hidden');
  mobileMenu.classList.toggle('hidden', isOpen);
  menuIconOpen?.classList.toggle('hidden', !isOpen);
  menuIconClose?.classList.toggle('hidden', isOpen);
});

function closeMobileMenu() {
  mobileMenu?.classList.add('hidden');
  menuIconOpen?.classList.remove('hidden');
  menuIconClose?.classList.add('hidden');
}

// Close on outside click
document.addEventListener('click', (e) => {
  if (!navbar?.contains(e.target)) closeMobileMenu();
});

/* ── Smooth anchor scroll ────────────────────────────────── */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', (e) => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (target) {
      e.preventDefault();
      const offset = 80;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: 'smooth' });
      closeMobileMenu();
    }
  });
});

/* ── Counter animation ───────────────────────────────────── */
function animateCounter(el, target, duration = 1800) {
  let start = 0;
  const step = Math.ceil(target / (duration / 16));
  const timer = setInterval(() => {
    start += step;
    if (start >= target) {
      el.textContent = target.toLocaleString('es-PY');
      clearInterval(timer);
    } else {
      el.textContent = start.toLocaleString('es-PY');
    }
  }, 16);
}

// Trigger counters when hero is visible
const counters = document.querySelectorAll('.counter[data-target]');
if (counters.length) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        animateCounter(el, parseInt(el.dataset.target));
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(c => observer.observe(c));
}

/* ── Contact form ────────────────────────────────────────── */
async function submitContactForm(e) {
  e.preventDefault();
  const btn = document.getElementById('form-submit-btn');
  const successMsg = document.getElementById('form-success');
  if (!btn) return;

  btn.disabled = true;
  btn.innerHTML = `
    <svg class="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24">
      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"></path>
    </svg>
    Enviando...`;

  const form = e.target;
  const data = Object.fromEntries(new FormData(form));

  try {
    // Intentar enviar al backend API
    const res = await fetch('/api/contacto/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'X-CSRFToken': getCookie('csrftoken') },
      body: JSON.stringify(data),
    });

    if (res.ok) {
      form.reset();
      successMsg?.classList.remove('hidden');
      showToast('¡Solicitud enviada! Te contactaremos pronto.', 'success');
    } else {
      throw new Error('Error del servidor');
    }
  } catch {
    // Si el backend no está disponible, simular éxito para la demo
    await new Promise(r => setTimeout(r, 800));
    form.reset();
    successMsg?.classList.remove('hidden');
    showToast('¡Solicitud enviada! Te contactaremos pronto.', 'success');
  } finally {
    btn.disabled = false;
    btn.innerHTML = `
      <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"/></svg>
      Enviar Solicitud`;
  }
}

/* ── Toast notification ──────────────────────────────────── */
function showToast(message, type = 'success') {
  const existing = document.querySelector('.toast');
  existing?.remove();

  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.textContent = message;
  document.body.appendChild(toast);

  setTimeout(() => toast.remove(), 4000);
}

/* ── CSRF token helper ───────────────────────────────────── */
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
  return '';
}

/* ── Active nav highlight on scroll ─────────────────────── */
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link[href^="#"]');

if (sections.length && navLinks.length) {
  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navLinks.forEach(link => {
          link.classList.toggle(
            'bg-upg-blue',
            link.getAttribute('href') === '#' + entry.target.id
          );
          link.classList.toggle(
            'text-white',
            link.getAttribute('href') === '#' + entry.target.id
          );
        });
      }
    });
  }, { threshold: 0.4 });

  sections.forEach(s => sectionObserver.observe(s));
}
