/**
 * PortfolioHUB — Lucca Mariz
 * Interações da página principal (vanilla JS, sem dependências).
 */

(function () {
  'use strict';

  // -----------------------------------------------------------
  // Toggle do menu mobile
  // -----------------------------------------------------------
  const toggle  = document.querySelector('.nav-toggle');
  const navMob  = document.getElementById('nav-mobile');

  if (toggle && navMob) {
    toggle.addEventListener('click', () => {
      const aberto = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!aberto));
      if (aberto) {
        navMob.setAttribute('hidden', '');
      } else {
        navMob.removeAttribute('hidden');
      }
    });

    // Fecha menu ao clicar em qualquer link mobile
    navMob.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        toggle.setAttribute('aria-expanded', 'false');
        navMob.setAttribute('hidden', '');
      });
    });
  }

  // -----------------------------------------------------------
  // Highlight do link ativo conforme a seção visível
  // -----------------------------------------------------------
  const secoes  = document.querySelectorAll('main section[id]');
  const links   = document.querySelectorAll('.nav a, .nav-mobile a');

  if ('IntersectionObserver' in window && secoes.length) {
    const obs = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute('id');
          links.forEach((l) => {
            l.style.color = l.getAttribute('href') === `#${id}`
              ? 'var(--text)'
              : '';
          });
        }
      });
    }, { rootMargin: '-40% 0px -55% 0px' });

    secoes.forEach((s) => obs.observe(s));
  }

  // -----------------------------------------------------------
  // Log discreto no console (assinatura)
  // -----------------------------------------------------------
  console.log(
    '%c PortfolioHUB v1.0.0 ',
    'background:#6c8cff;color:#0a0c10;font-weight:bold;padding:4px 8px;border-radius:4px;',
    '· por Lucca Mariz (@Ucazin)'
  );
})();
