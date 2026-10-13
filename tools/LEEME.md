# Generador del sitio

Las páginas HTML (`index.html`, `nosotros.html`, `servicios.html`, `contacto.html`, `privacidad.html`, `404.html`) y el diccionario de idiomas `assets/js/i18n.js` se generan con `build_site.py`. Cada texto se escribe una vez como `T("español", "english")`.

Regenerar desde la raíz del proyecto:

    python tools/build_site.py . tools/catalogo-productos.json

Si editas un HTML a mano, la próxima regeneración lo sobrescribe: haz los cambios de texto en `build_site.py`. Estilos en `site.css`, interacción en `site.js`.
