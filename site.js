(function () {
  var root = document.documentElement;
  var dictionary = window.ACC_I18N || {};
  var reverseDictionary = {};
  Object.keys(dictionary).forEach(function (spanish) {
    if (!reverseDictionary[dictionary[spanish]]) reverseDictionary[dictionary[spanish]] = spanish;
  });
  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var whatsappNumber = '573116845523'; // +57 311 684 5523

  function t(spanish) {
    return root.lang === 'en' && dictionary[spanish] ? dictionary[spanish] : spanish;
  }
  function readPreference(key) {
    try { return localStorage.getItem(key); } catch (error) { return null; }
  }
  function savePreference(key, value) {
    try { localStorage.setItem(key, value); } catch (error) {}
  }
  function clamp(value, min, max) { return Math.min(max, Math.max(min, value)); }

  // Tema
  function setTheme(theme) {
    root.setAttribute('data-theme', theme);
    document.querySelectorAll('[data-theme-toggle]').forEach(function (button) {
      var label = theme === 'dark' ? 'Cambiar a tema claro' : 'Cambiar a tema oscuro';
      button.setAttribute('aria-label', t(label));
      button.setAttribute('title', t(label));
    });
    savePreference('acc-theme', theme);
  }

  // Idioma: traduce nodos de texto y atributos con el diccionario generado
  function translateValue(value, language) {
    var text = value.trim().replace(/\s+/g, ' ');
    if (!text) return null;
    var spanish = language === 'en' ? text : reverseDictionary[text] || text;
    if (!dictionary[spanish]) return null;
    return language === 'en' ? dictionary[spanish] : spanish;
  }

  function applyLanguage(language) {
    root.setAttribute('lang', language);
    var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode: function (node) {
        return node.parentElement && node.parentElement.closest('script, style, [data-words]') ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT;
      }
    });
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (node) {
      var translated = translateValue(node.nodeValue, language);
      if (translated === null) return;
      node.nodeValue = node.nodeValue.match(/^\s*/)[0] + translated + node.nodeValue.match(/\s*$/)[0];
    });
    document.querySelectorAll('[aria-label], [title], [placeholder], [alt]').forEach(function (element) {
      ['aria-label', 'title', 'placeholder', 'alt'].forEach(function (attribute) {
        var value = element.getAttribute(attribute);
        if (!value || element.tagName === 'TITLE') return;
        var translated = translateValue(value, language);
        if (translated !== null) element.setAttribute(attribute, translated);
      });
    });
    ['title', 'meta[name="description"]'].forEach(function (selector) {
      var element = document.querySelector(selector);
      if (!element) return;
      if (!element.dataset.es) element.dataset.es = element.tagName === 'TITLE' ? element.textContent : element.getAttribute('content');
      var value = language === 'en' ? element.dataset.en : element.dataset.es;
      if (element.tagName === 'TITLE') document.title = value; else element.setAttribute('content', value);
    });
    document.querySelectorAll('[data-language]').forEach(function (button) {
      button.setAttribute('aria-pressed', button.dataset.language === language ? 'true' : 'false');
    });
    buildWordReveal();
    setTheme(root.getAttribute('data-theme') || 'dark');
    updateWhatsApp();
    updateCatalogCount();
    var reelBlock = document.querySelector('[data-reel]');
    if (reelBlock && reelBlock._sync) reelBlock._sync();
    refreshDepartment();
    savePreference('acc-lang', language);
  }

  // Estado de scroll: oculta la franja marquee y muestra "volver arriba" (sin escuchar scroll)
  var sentinel = document.querySelector('.top-sentinel');
  if (sentinel && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      root.classList.toggle('is-scrolled', !entries[0].isIntersecting);
    }).observe(sentinel);
  }
  document.querySelectorAll('[data-to-top]').forEach(function (button) {
    button.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: reducedMotion ? 'auto' : 'smooth' }); });
  });

  // Menú móvil
  var menuButton = document.querySelector('.menu-toggle');
  var overlay = document.getElementById('menu-overlay');
  function setMenu(open) {
    if (!menuButton || !overlay) return;
    menuButton.setAttribute('aria-expanded', String(open));
    menuButton.setAttribute('aria-label', t(open ? 'Cerrar menú' : 'Abrir menú'));
    overlay.classList.toggle('is-open', open);
    root.classList.toggle('menu-open', open);
    if (open) {
      overlay.removeAttribute('inert');
      var first = overlay.querySelector('a');
      if (first) setTimeout(function () { first.focus({ preventScroll: true }); }, 300);
    } else {
      overlay.setAttribute('inert', '');
    }
  }
  if (menuButton && overlay) {
    menuButton.addEventListener('click', function () { setMenu(menuButton.getAttribute('aria-expanded') !== 'true'); });
    overlay.querySelectorAll('a').forEach(function (link) { link.addEventListener('click', function () { setMenu(false); }); });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && overlay.classList.contains('is-open')) { setMenu(false); menuButton.focus(); }
    });
    window.matchMedia('(min-width: 1100px)').addEventListener('change', function (query) { if (query.matches) setMenu(false); });
  }

  // Revelado al entrar en pantalla
  if (!reducedMotion && 'IntersectionObserver' in window) {
    root.classList.add('motion-ready');
    var revealObserver = new IntersectionObserver(function (entries, observer) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    document.querySelectorAll('.reveal').forEach(function (element) { revealObserver.observe(element); });
  }

  // Bucle de scroll compartido: un solo listener pasivo, limitado con requestAnimationFrame
  // y activo solo mientras alguna sección animada está en pantalla.
  var scrollTasks = [];
  var activeTasks = new Set();
  var ticking = false;
  function runTasks() {
    ticking = false;
    activeTasks.forEach(function (task) { task.update(); });
  }
  function requestTick() {
    if (!ticking && activeTasks.size) { ticking = true; requestAnimationFrame(runTasks); }
  }
  window.addEventListener('scroll', requestTick, { passive: true });
  window.addEventListener('resize', requestTick);
  function addScrollTask(element, update) {
    var task = { element: element, update: update };
    scrollTasks.push(task);
    if (!('IntersectionObserver' in window)) { activeTasks.add(task); return; }
    new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting) activeTasks.add(task); else activeTasks.delete(task);
      update();
    }, { rootMargin: '20% 0px' }).observe(element);
  }
  function progressOf(element) {
    var rect = element.getBoundingClientRect();
    var distance = rect.height - window.innerHeight;
    return distance > 0 ? clamp(-rect.top / distance, 0, 1) : 0;
  }

  // Hero: el aguacate gira, se abre y avanza por los tres pasos
  var hero = document.querySelector('[data-hero-scroll]');
  if (hero) {
    var heroSteps = hero.querySelectorAll('.avocado-steps li');
    if (reducedMotion) {
      hero.style.setProperty('--p', '0.45');
      heroSteps.forEach(function (step) { step.classList.add('is-active'); });
    } else {
      addScrollTask(hero, function () {
        var p = progressOf(hero);
        hero.style.setProperty('--p', p.toFixed(4));
        hero.classList.toggle('is-past', p > 0.2);
        var current = p < 0.2 ? 0 : p < 0.6 ? 1 : 2;
        heroSteps.forEach(function (step, index) { step.classList.toggle('is-active', index <= current); });
      });
    }
  }

  // Frase principal: cada palabra se ilumina en orden de lectura
  var wordBlocks = document.querySelectorAll('[data-words]');
  function buildWordReveal() {
    wordBlocks.forEach(function (block) {
      var spanish = block.dataset.es;
      var text = root.lang === 'en' && dictionary[spanish] ? dictionary[spanish] : spanish;
      var accentFrom = block.dataset.accent === '' ? Infinity : Number(block.dataset.accent);
      block.textContent = '';
      text.split(' ').forEach(function (word, index, words) {
        var span = document.createElement('span');
        span.className = 'word' + (index >= accentFrom ? ' is-accent' : '');
        span.textContent = word;
        block.appendChild(span);
        if (index < words.length - 1) block.appendChild(document.createTextNode(' '));
      });
      block.setAttribute('aria-label', text);
      if (reducedMotion) block.querySelectorAll('.word').forEach(function (word) { word.classList.add('is-lit'); });
      else if (block._update) block._update();
    });
  }
  wordBlocks.forEach(function (block) {
    if (reducedMotion) return;
    block._update = function () {
      var rect = block.getBoundingClientRect();
      var start = window.innerHeight * 0.9;
      var end = window.innerHeight * 0.35;
      var p = clamp((start - rect.top) / (start - end), 0, 1);
      var words = block.querySelectorAll('.word');
      var lit = Math.round(p * words.length);
      words.forEach(function (word, index) { word.classList.toggle('is-lit', index < lit); });
    };
    addScrollTask(block, block._update);
  });

  // Video del cultivo: arranca en silencio al verse y el visitante activa el sonido
  var reelFrame = document.querySelector('[data-reel]');
  if (reelFrame) {
    var reel = reelFrame.querySelector('video');
    var soundButton = reelFrame.querySelector('[data-reel-sound]');
    var toggleButton = reelFrame.querySelector('[data-reel-toggle]');
    var seekButtons = document.querySelectorAll('[data-seek]');
    var userPaused = false;
    var playReel = function () {
      if (reel.preload === 'none') { reel.preload = 'auto'; reel.load(); }
      var attempt = reel.play();
      if (attempt && attempt.catch) attempt.catch(function () { reelFrame.classList.add('is-paused'); });
    };
    var syncReel = function () {
      var paused = reel.paused;
      reelFrame.classList.toggle('is-paused', paused);
      toggleButton.setAttribute('aria-label', t(paused ? 'Reproducir video' : 'Pausar video'));
      soundButton.setAttribute('aria-pressed', reel.muted ? 'false' : 'true');
      soundButton.querySelector('[data-sound-label]').textContent = t(reel.muted ? 'Activar sonido' : 'Desactivar sonido');
    };
    reelFrame._sync = syncReel;
    ['play', 'pause', 'volumechange'].forEach(function (type) { reel.addEventListener(type, syncReel); });
    reel.addEventListener('timeupdate', function () {
      if (!reel.duration) return;
      reelFrame.style.setProperty('--t', (reel.currentTime / reel.duration).toFixed(4));
      var active = 0;
      seekButtons.forEach(function (button, index) { if (reel.currentTime >= Number(button.dataset.seek)) active = index; });
      seekButtons.forEach(function (button, index) { button.classList.toggle('is-active', index === active); });
    });
    soundButton.addEventListener('click', function () {
      var turningOn = reel.muted;
      reel.muted = !turningOn;
      if (turningOn) { reel.currentTime = 0; userPaused = false; playReel(); }
    });
    var togglePlayback = function () {
      if (reel.paused) { userPaused = false; playReel(); } else { userPaused = true; reel.pause(); }
    };
    toggleButton.addEventListener('click', togglePlayback);
    reel.addEventListener('click', togglePlayback);
    seekButtons.forEach(function (button) {
      button.addEventListener('click', function () {
        reel.currentTime = Number(button.dataset.seek);
        userPaused = false;
        playReel();
      });
    });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        if (entries[0].isIntersecting) {
          if (!userPaused && !reducedMotion) playReel();
        } else if (!reel.paused) {
          reel.pause();
        }
      }, { threshold: 0.5 }).observe(reelFrame);
    }
    if (seekButtons[0]) seekButtons[0].classList.add('is-active');
    syncReel();
  }

  // Videos de fondo: se reproducen solo en pantalla y nunca con movimiento reducido
  document.querySelectorAll('[data-bg-video]').forEach(function (backgroundVideo) {
    if (reducedMotion || !('IntersectionObserver' in window)) return;
    new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting) {
        if (backgroundVideo.preload === 'none') { backgroundVideo.preload = 'auto'; backgroundVideo.load(); }
        var play = backgroundVideo.play();
        if (play && play.catch) play.catch(function () {});
      } else {
        backgroundVideo.pause();
      }
    }, { rootMargin: '25% 0px' }).observe(backgroundVideo);
  });

  // Contadores animados
  function formatCount(element, value) {
    element.textContent = (element.dataset.prefix || '') + value;
  }
  var counters = document.querySelectorAll('[data-count]');
  if (!reducedMotion && 'IntersectionObserver' in window) {
    var counterObserver = new IntersectionObserver(function (entries, observer) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        observer.unobserve(entry.target);
        var element = entry.target;
        var target = Number(element.dataset.count);
        var start = performance.now();
        var duration = 1400;
        (function frame(now) {
          var x = clamp((now - start) / duration, 0, 1);
          var eased = 1 - Math.pow(1 - x, 4);
          formatCount(element, Math.round(target * eased));
          if (x < 1) requestAnimationFrame(frame);
        })(start);
      });
    }, { threshold: 0.6 });
    counters.forEach(function (counter) { formatCount(counter, 0); counterObserver.observe(counter); });
  }

  // Catálogo filtrable
  var catalog = document.querySelector('[data-catalog]');
  var catalogCount = document.querySelector('[data-catalog-count]');
  var chips = document.querySelectorAll('[data-filter]');
  function updateCatalogCount() {
    if (!catalog || !catalogCount) return;
    var visible = catalog.querySelectorAll('li:not([hidden])').length;
    catalogCount.textContent = t('Mostrando {n} referencias').replace('{n}', visible);
  }
  function applyFilter(category, scroll) {
    if (!catalog) return;
    chips.forEach(function (chip) { chip.setAttribute('aria-pressed', chip.dataset.filter === category ? 'true' : 'false'); });
    var index = 0;
    catalog.querySelectorAll('li').forEach(function (item) {
      var show = category === 'all' || item.dataset.cat === category;
      item.hidden = !show;
      item.classList.remove('is-entering');
      if (show && !reducedMotion) {
        void item.offsetWidth;
        item.style.setProperty('--i', index++);
        item.classList.add('is-entering');
      }
    });
    updateCatalogCount();
    if (scroll) document.getElementById('catalogo').scrollIntoView({ behavior: reducedMotion ? 'auto' : 'smooth' });
  }
  chips.forEach(function (chip) {
    chip.addEventListener('click', function () { applyFilter(chip.dataset.filter, false); });
  });
  function filterFromHash() {
    var hash = window.location.hash.replace('#', '');
    if (catalog && ['hortalizas', 'frutas', 'tuberculos'].indexOf(hash) !== -1) applyFilter(hash, true);
  }
  window.addEventListener('hashchange', filterFromHash);

  // Mapa de departamentos (dibujado en el HTML; aquí solo la interacción)
  var homeDepartments = { 'CO-ANT': 'Nuestro origen: aquí cultivamos el aguacate Hass en Sonsón.', 'CO-DC': 'Nuestra operación comercial en Corabastos atiende desde aquí.' };
  var mapPaths = document.querySelectorAll('[data-map-geometry] path');
  var mapSelect = document.querySelector('[data-map-select]');
  var selectedDepartment = '';
  function showDepartment(code) {
    var target = null;
    mapPaths.forEach(function (path) {
      var selected = path.dataset.code === code;
      path.classList.toggle('is-selected', selected);
      path.setAttribute('aria-pressed', selected ? 'true' : 'false');
      if (selected) target = path;
    });
    if (!target) return;
    selectedDepartment = code;
    target.parentNode.insertBefore(target, target.parentNode.querySelector('.map-pin'));
    if (mapSelect) mapSelect.value = code;
    document.querySelector('[data-map-name]').textContent = target.getAttribute('aria-label');
    document.querySelector('[data-map-region]').textContent = t(target.dataset.region);
    document.querySelector('[data-map-copy]').textContent = t(homeDepartments[code] || 'Consulta con nuestro equipo la disponibilidad y los destinos vigentes.');
  }
  function refreshDepartment() {
    if (selectedDepartment) showDepartment(selectedDepartment);
  }
  mapPaths.forEach(function (path) {
    ['mouseenter', 'focus', 'click'].forEach(function (type) {
      path.addEventListener(type, function () { showDepartment(path.dataset.code); });
    });
    path.addEventListener('keydown', function (event) {
      if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); showDepartment(path.dataset.code); }
    });
  });
  if (mapSelect) mapSelect.addEventListener('change', function () { if (mapSelect.value) showDepartment(mapSelect.value); });

  // Mapa de la zona en el pie de página
  document.querySelectorAll('.footer-map').forEach(function (block) {
    var frame = block.querySelector('.footer-map-frame');
    var iframe = block.querySelector('iframe');
    var open = block.querySelector('[data-map-open]');
    var tabs = block.querySelectorAll('[role="tab"]');
    tabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        if (tab.getAttribute('aria-selected') === 'true') return;
        tabs.forEach(function (other) { other.setAttribute('aria-selected', other === tab ? 'true' : 'false'); });
        frame.classList.add('is-switching');
        iframe.addEventListener('load', function onLoad() { frame.classList.remove('is-switching'); iframe.removeEventListener('load', onLoad); });
        iframe.src = tab.dataset.mapSrc;
        open.href = tab.dataset.mapLink;
      });
    });
  });

  // WhatsApp con mensaje predeterminado en el idioma activo
  function whatsappUrl(text) {
    return 'https://wa.me/' + whatsappNumber + '?text=' + encodeURIComponent(text);
  }
  function updateWhatsApp() {
    var url = whatsappUrl(t('Hola, Agro Colombia Company. Quisiera información y una cotización de sus productos.'));
    document.querySelectorAll('[data-whatsapp-link]').forEach(function (link) { link.href = url; });
  }

  // Visor de fotos y videos del cultivo
  var dialog = document.querySelector('[data-lightbox-dialog]');
  if (dialog && typeof dialog.showModal === 'function') {
    var media = dialog.querySelector('[data-lightbox-media]');
    var caption = dialog.querySelector('[data-lightbox-caption]');
    var photos = Array.prototype.slice.call(document.querySelectorAll('[data-gallery] img'));
    var current = 0;
    var opener = null;
    var showPhoto = function (index) {
      current = (index + photos.length) % photos.length;
      var image = document.createElement('img');
      image.src = photos[current].dataset.full;
      image.alt = photos[current].alt;
      media.replaceChildren(image);
      caption.textContent = photos[current].alt + ' · ' + (current + 1) + ' / ' + photos.length;
      dialog.classList.remove('is-video');
    };
    var openDialog = function () {
      opener = document.activeElement;
      if (!dialog.open) dialog.showModal();
      root.classList.add('lightbox-open');
    };
    var closeDialog = function () { if (dialog.open) dialog.close(); };
    dialog.addEventListener('close', function () {
      media.replaceChildren();
      root.classList.remove('lightbox-open');
      if (opener) opener.focus({ preventScroll: true });
    });
    document.querySelectorAll('[data-lightbox]').forEach(function (button) {
      button.addEventListener('click', function () { openDialog(); showPhoto(Number(button.dataset.lightbox)); });
    });
    document.querySelectorAll('[data-video-src]').forEach(function (button) {
      button.addEventListener('click', function () {
        openDialog();
        var video = document.createElement('video');
        video.src = button.dataset.videoSrc;
        video.controls = true;
        video.autoplay = true;
        video.playsInline = true;
        media.replaceChildren(video);
        caption.textContent = button.dataset.videoTitle;
        dialog.classList.add('is-video');
        var attempt = video.play();
        if (attempt && attempt.catch) attempt.catch(function () {});
      });
    });
    dialog.querySelector('[data-lightbox-close]').addEventListener('click', closeDialog);
    dialog.querySelector('[data-lightbox-prev]').addEventListener('click', function () { showPhoto(current - 1); });
    dialog.querySelector('[data-lightbox-next]').addEventListener('click', function () { showPhoto(current + 1); });
    dialog.addEventListener('click', function (event) { if (event.target === dialog) closeDialog(); });
    dialog.addEventListener('keydown', function (event) {
      if (dialog.classList.contains('is-video')) return;
      if (event.key === 'ArrowLeft') showPhoto(current - 1);
      if (event.key === 'ArrowRight') showPhoto(current + 1);
    });
    var touchX = null;
    dialog.addEventListener('touchstart', function (event) { touchX = event.touches[0].clientX; }, { passive: true });
    dialog.addEventListener('touchend', function (event) {
      if (touchX === null || dialog.classList.contains('is-video')) return;
      var delta = event.changedTouches[0].clientX - touchX;
      if (Math.abs(delta) > 50) showPhoto(current + (delta < 0 ? 1 : -1));
      touchX = null;
    });
  }

  // Formulario: validación en línea y envío por correo
  var form = document.querySelector('[data-contact-form]');
  if (form) {
    var status = form.querySelector('.form-status');
    var validateField = function (field) {
      var error = document.getElementById(field.getAttribute('aria-describedby'));
      var message = '';
      if (field.validity.valueMissing) message = t('Este campo es obligatorio.');
      else if (field.validity.typeMismatch) message = t('Escribe un correo válido, por ejemplo nombre@empresa.com.');
      field.setAttribute('aria-invalid', message ? 'true' : 'false');
      if (error) error.textContent = message;
      return !message;
    };
    form.querySelectorAll('input, textarea').forEach(function (field) {
      field.addEventListener('blur', function () { if (field.value) validateField(field); });
      field.addEventListener('input', function () { if (field.getAttribute('aria-invalid') === 'true') validateField(field); });
    });
    form.addEventListener('submit', function (event) {
      event.preventDefault();
      var fields = Array.prototype.slice.call(form.querySelectorAll('input, textarea'));
      var invalid = fields.filter(function (field) { return !validateField(field); });
      status.classList.toggle('is-error', invalid.length > 0);
      if (invalid.length) {
        status.textContent = t('Revisa los campos marcados antes de continuar.');
        invalid[0].focus();
        return;
      }
      var data = new FormData(form);
      var lines = [
        'Nombre / Name: ' + data.get('name'),
        'Empresa / Company: ' + (data.get('company') || ''),
        'Correo / Email: ' + data.get('email'),
        'Teléfono / Phone: ' + (data.get('phone') || ''),
        'Ciudad / City: ' + data.get('city'),
        'Productos / Products: ' + (data.get('interest') || ''),
        '',
        data.get('message')
      ];
      var subject = t('Consulta desde la web') + ' | ' + data.get('name');
      var channel = event.submitter && event.submitter.dataset.send === 'email' ? 'email' : 'whatsapp';
      if (channel === 'whatsapp') {
        status.textContent = t('Abrimos WhatsApp con tu consulta lista para enviar.');
        window.open(whatsappUrl(subject + '\n\n' + lines.join('\n')), '_blank', 'noopener');
        return;
      }
      status.textContent = t('Abrimos tu aplicación de correo con la consulta lista para enviar.');
      window.location.href = 'mailto:agrocolombiacompany@gmail.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
    });
  }

  document.querySelectorAll('[data-year]').forEach(function (year) { year.textContent = new Date().getFullYear(); });

  // Preferencias iniciales
  var storedTheme = readPreference('acc-theme');
  setTheme(storedTheme === 'light' || storedTheme === 'dark' ? storedTheme : root.getAttribute('data-theme') || 'dark');
  applyLanguage(readPreference('acc-lang') === 'en' ? 'en' : 'es');
  document.querySelectorAll('[data-language]').forEach(function (button) {
    button.addEventListener('click', function () { applyLanguage(button.dataset.language === 'en' ? 'en' : 'es'); });
  });
  document.querySelectorAll('[data-theme-toggle]').forEach(function (button) {
    button.addEventListener('click', function () { setTheme(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark'); });
  });
  updateCatalogCount();
  filterFromHash();
  scrollTasks.forEach(function (task) { task.update(); });
})();
