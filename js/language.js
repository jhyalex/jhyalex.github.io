(function () {
  'use strict';
  document.addEventListener('click', function (event) {
    var link = event.target.closest('[data-language]');
    if (!link) return;
    try { localStorage.setItem('fuguang-language', link.getAttribute('data-language')); } catch (_) {}
  });
  // Persist a deliberate choice; every link also works with JavaScript disabled.
  try {
    if (location.pathname === '/' && localStorage.getItem('fuguang-language') === 'en') {
      location.replace('/en/' + location.search + location.hash);
    }
  } catch (_) {}
}());
