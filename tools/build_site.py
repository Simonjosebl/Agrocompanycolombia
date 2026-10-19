"""Genera las páginas estáticas de Agro Colombia Company.
Cada texto visible se declara una vez con T(es, en); el diccionario resultante
se escribe en assets/js/i18n.js para el cambio de idioma en el navegador."""
import json, re, sys, unicodedata
from html import escape
from pathlib import Path

ROOT = Path(sys.argv[1])
CATALOG = json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
SITE = 'https://www.agrocolombiacompany.com'
import time
VERSION = time.strftime('%Y%m%d%H%M')
EMAIL = 'agrocolombiacompany@gmail.com'
IG = 'https://www.instagram.com/agrocolombiacompany/'
FB = 'https://www.facebook.com/share/1GnSrKpnuH/'
WA = '573116845523'
LEGAL_NAME = 'Agro Colombia Company S.A.S.'
NIT = '901.910.572-4'
WA_DISPLAY = '+57 311 684 5523'

DICT = {}
def T(es, en):
    key = ' '.join(es.split())
    if key in DICT and DICT[key] != en:
        raise SystemExit(f'Traducción en conflicto: {key!r}: {DICT[key]!r} vs {en!r}')
    DICT[key] = en
    return es

def icon(name, cls=''):
    return f'<i class="icon icon-{name}{(" " + cls) if cls else ""}" aria-hidden="true"></i>'

ARROW = icon('arrow-up-right')

def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

PRODUCT_EN = {
 'Acelga': 'Chard', 'Ahuyama': 'Pumpkin', 'Ajo': 'Garlic', 'Alcachofa': 'Artichoke', 'Apio': 'Celery',
 'Arveja verde sabanera': 'Savanna green peas', 'Berenjena': 'Eggplant', 'Brócoli': 'Broccoli', 'Calabacín': 'Zucchini',
 'Calabaza': 'Butternut squash', 'Cebolla cabezona blanca': 'White onion', 'Cebolla cabezona roja': 'Red bulb onion',
 'Cebolla roja': 'Purple onion', 'Cilantro': 'Cilantro', 'Coliflor': 'Cauliflower', 'Espinaca': 'Spinach',
 'Frijol verde': 'Fresh green beans', 'Haba verde sabanera': 'Savanna fava beans', 'Habichuela': 'String beans',
 'Lechuga': 'Lettuce', 'Mazorca': 'Corn on the cob', 'Pepino cohombro': 'Long cucumber', 'Pepino común': 'Cucumber',
 'Pimentón': 'Bell pepper', 'Rábano rojo': 'Red radish', 'Remolacha': 'Beetroot', 'Repollo': 'Cabbage',
 'Tomate chonto': 'Chonto tomato', 'Tomate larga vida': 'Long life tomato', 'Tomate Milano': 'Milano tomato',
 'Zanahoria': 'Carrot',
 'Aguacate Hass': 'Hass avocado', 'Banano': 'Banana', 'Banano bocadillo': 'Baby banana', 'Borojó': 'Borojó',
 'Carambolo': 'Star fruit', 'Coco': 'Coconut', 'Curuba': 'Banana passionfruit', 'Granadilla': 'Sweet granadilla',
 'Guayaba': 'Guava', 'Guanábana': 'Soursop', 'Lima Tahití': 'Tahiti lime', 'Limón común': 'Common lemon',
 'Lulo': 'Lulo', 'Mandarina': 'Mandarin', 'Mango Tommy': 'Tommy mango', 'Mango Yulima': 'Yulima mango',
 'Maracuyá': 'Passion fruit', 'Mora': 'Andean blackberry', 'Naranja': 'Orange', 'Papaya': 'Papaya', 'Piña': 'Pineapple',
 'Pitahaya': 'Dragon fruit', 'Sandía': 'Watermelon', 'Manzana verde': 'Green apple', 'Manzana roja': 'Red apple',
 'Melón': 'Melon', 'Uchuva': 'Goldenberry', 'Durazno': 'Peach', 'Ciruela': 'Plum', 'Fresa': 'Strawberry',
 'Arándano': 'Blueberry', 'Frambuesa': 'Raspberry', 'Mora azul': 'Dark blackberry', 'Kiwi': 'Kiwi',
 'Tamarindo': 'Tamarind', 'Pera': 'Pear', 'Níspero': 'Loquat', 'Nectarina': 'Nectarine', 'Cereza': 'Cherry',
 'Uva verde': 'Green grape', 'Uva roja': 'Red grape', 'Aguacate papelillo': 'Papelillo avocado',
 'Aguacate lorena': 'Lorena avocado',
 'Papa criolla': 'Criolla potato', 'Papa pastusa': 'Pastusa potato', 'Papa sabanera': 'Sabanera potato',
 'Yuca': 'Cassava', 'Ñame': 'Yam', 'Arracacha': 'Arracacha', 'Oca': 'Oca', 'Ibias': 'Ibias',
 'Cebolla larga': 'Spring onion', 'Plátano hartón': 'Hartón plantain', 'Plátano dominico': 'Dominico plantain',
 'Plátano guineo': 'Guineo banana', 'Plátano manzano': 'Manzano banana', 'Plátano cachaco': 'Cachaco plantain',
}
CATS = [
 ('hortalizas', T('Hortalizas', 'Vegetables'), 'cat-hortalizas.webp',
  T('Una selección completa de hortalizas frescas, con calidad y disponibilidad para tu operación.',
    'A complete range of fresh vegetables, with the quality and availability your operation needs.')),
 ('frutas', T('Frutas', 'Fruits'), 'cat-frutas.webp',
  T('Frutas frescas y variadas, seleccionadas en los cultivos para abastecer tu negocio todo el año.',
    'Fresh, varied fruit selected at the farm to supply your business all year.')),
 ('tuberculos', T('Tubérculos y plátanos', 'Tubers and plantains'), 'cat-tuberculos.webp',
  T('Papas, raíces y plátanos de alta calidad, ideales para distintos tipos de preparación.',
    'High quality potatoes, roots and plantains for every kind of preparation.')),
]
COUNTS = {k: len(v) for k, v in CATALOG.items()}
TOTAL = sum(COUNTS.values())
for item in [i for v in CATALOG.values() for i in v]:
    T(item['name'], PRODUCT_EN[item['name']])

def tile(item, lazy=True):
    return (f'<figure class="product-tile"><img src="assets/imgs/productos/{item["img"]}" alt="{escape(item["name"])}" '
            f'width="480" height="360"{" loading=\"lazy\"" if lazy else ""} decoding="async" />'
            f'<figcaption>{escape(item["name"])}</figcaption></figure>')

# ---------------------------------------------------------------- cultivo propio
CROP_PHOTOS = [
 ('982279', T('Racimo de aguacates Hass en el árbol', 'Cluster of Hass avocados on the tree'), 'wide'),
 ('982260', T('Lotes de aguacate Hass en las montañas de Sonsón', 'Hass avocado plots in the mountains of Sonsón'), 'wide'),
 ('982258', T('Ramas cargadas de aguacate Hass', 'Branches loaded with Hass avocados'), ''),
 ('982232', T('Canastillas de aguacate Hass recién cosechado', 'Crates of freshly harvested Hass avocados'), ''),
 ('982252', T('Frutos en desarrollo entre el follaje', 'Fruit developing among the leaves'), 'wide'),
 ('982259', T('Cultivo en ladera, Sonsón, Antioquia', 'Hillside orchard in Sonsón, Antioquia'), ''),
 ('982240', T('Árbol de aguacate Hass en producción', 'Hass avocado tree in production'), ''),
 ('982253', T('Aguacates Hass creciendo bajo el sol', 'Hass avocados growing in the sun'), 'wide'),
 ('982256', T('Árbol joven bien formado', 'Well formed young tree'), ''),
 ('982255', T('Hileras del cultivo', 'Orchard rows'), 'wide'),
 ('982234', T('Árbol de aguacate Hass en el lote', 'Hass avocado tree in the plot'), ''),
 ('982254', T('Frutos de aguacate Hass en la rama', 'Hass avocados on the branch'), 'wide'),
 ('982251', T('Follaje sano y nuevos brotes', 'Healthy foliage and new shoots'), ''),
 ('982249', T('Árbol en plena producción', 'Tree in full production'), ''),
 ('982239', T('Copa del árbol con frutos', 'Tree canopy with fruit'), ''),
 ('982235', T('Árbol joven en el lote', 'Young tree in the plot'), ''),
 ('982250', T('Cultivo rodeado de montaña', 'Orchard surrounded by mountains'), ''),
 ('982257', T('Árbol de aguacate Hass', 'Hass avocado tree'), ''),
]
CROP_VIDEOS = [
 ('recorrido-lote', T('Recorrido por el lote', 'Walk through the plot'), T('Así crecen nuestros árboles en Sonsón.', 'How our trees grow in Sonsón.'), 'landscape', '0:40'),
 ('arboles-con-fruto', T('Árboles con fruto', 'Trees bearing fruit'), T('Aguacate Hass listo para la cosecha.', 'Hass avocados ready for harvest.'), 'portrait', '0:37'),
 ('seleccion-canastillas', T('Selección en canastillas', 'Sorting into crates'), T('El cuidado continúa después de la cosecha.', 'Care continues after harvest.'), 'portrait', '0:26'),
]

def crop_gallery():
    items = ''.join(
        f'<li class="gallery-item{" is-wide" if wide else ""} reveal" style="--d:{i % 3}"><button type="button" data-lightbox="{i}" aria-label="{T("Ampliar foto", "Enlarge photo")}: {escape(alt)}">'
        f'<img src="assets/imgs/cultivo/{f}-sm.webp" data-full="assets/imgs/cultivo/{f}.webp" alt="{escape(alt)}" loading="lazy" decoding="async" /></button></li>'
        for i, (f, alt, wide) in enumerate(CROP_PHOTOS))
    return f'<ul class="gallery-grid" data-gallery>{items}</ul>'

def crop_videos():
    return '<div class="video-grid">' + ''.join(
        f'<button type="button" class="video-card is-{shape} reveal" style="--d:{i}" data-video-src="assets/videos/cultivo/{name}.mp4" data-video-title="{escape(title)}">'
        f'<img src="assets/videos/cultivo/{name}.jpg" alt="" loading="lazy" /><span class="video-play">{icon("play")}</span>'
        f'<span class="video-meta"><b>{title}</b><small>{text} · {dur}</small></span></button>'
        for i, (name, title, text, shape, dur) in enumerate(CROP_VIDEOS)) + '</div>'

LIGHTBOX = None
def lightbox():
    return f'''  <dialog class="lightbox" data-lightbox-dialog aria-label="{T("Visor de fotos y videos", "Photo and video viewer")}">
    <button class="lightbox-close icon-button" type="button" data-lightbox-close aria-label="{T("Cerrar", "Close")}">{icon("x")}</button>
    <button class="lightbox-nav is-prev icon-button" type="button" data-lightbox-prev aria-label="{T("Anterior", "Previous")}">{icon("arrow-left")}</button>
    <figure class="lightbox-stage"><div data-lightbox-media></div><figcaption data-lightbox-caption></figcaption></figure>
    <button class="lightbox-nav is-next icon-button" type="button" data-lightbox-next aria-label="{T("Siguiente", "Next")}">{icon("arrow-right")}</button>
  </dialog>
'''

# ---------------------------------------------------------------- certificaciones
def _logo(name):
    for ext in ('svg', 'png', 'webp'):
        if (ROOT / f'assets/imgs/certificaciones/{name}.{ext}').exists():
            return f'assets/imgs/certificaciones/{name}.{ext}'
    raise SystemExit(f'Falta el logo de {name}')

CERTS = [
 ('rainforest-alliance', 'Rainforest Alliance', 'https://www.rainforest-alliance.org/',
  T('Agricultura sostenible: conservación de los ecosistemas, bienestar de los trabajadores y de las comunidades rurales.', 'Sustainable agriculture: protecting ecosystems and the wellbeing of farm workers and rural communities.')),
 ('globalgap', 'GLOBALG.A.P.', 'https://www.globalgap.org/',
  T('Estándar internacional de buenas prácticas agrícolas: inocuidad alimentaria, trazabilidad y sostenibilidad del cultivo.', 'International good agricultural practice standard: food safety, traceability and sustainable farming.')),
 ('ica', 'ICA', 'https://www.ica.gov.co/',
  T('Registro ante el Instituto Colombiano Agropecuario, la autoridad sanitaria y fitosanitaria para exportar desde Colombia.', 'Registered with the Colombian Agricultural Institute, the plant health authority for exports from Colombia.')),
]
ICA_SUB = '<small>' + T('Instituto Colombiano Agropecuario', 'Colombian Agricultural Institute') + '</small>'

def cert_cards():
    return '<div class="cert-grid">' + ''.join(
        f'<a class="cert-card reveal" style="--d:{i}" href="{url}" target="_blank" rel="noopener" aria-label="{name}: {T("sitio oficial", "official website")}">'
        f'<span class="cert-logo"><img src="{_logo(key)}" alt="{name}" loading="lazy" /></span>'
        f'<span class="cert-body"><b>{name}</b>{ICA_SUB if key == "ica" else ""}<p>{text}</p>'
        f'<span class="cert-link">{T("Sitio oficial", "Official website")} {icon("arrow-up-right")}</span></span></a>'
        for i, (key, name, url, text) in enumerate(CERTS)) + '</div>'

def cert_strip():
    return ''.join(f'<a href="{url}" target="_blank" rel="noopener" title="{name}"><img src="{_logo(key)}" alt="{name}" loading="lazy" /></a>' for key, name, url, _ in CERTS)

# ---------------------------------------------------------------- partes comunes
NAV = [('index.html', T('Inicio', 'Home')), ('nosotros.html', T('Nosotros', 'About us')),
       ('servicios.html', T('Abastecimiento', 'Supply')), ('contacto.html', T('Contacto', 'Contact'))]

MARQUEE = [
 T('Aguacate Hass colombiano de exportación', 'Colombian Hass avocados for export'),
 T('Origen: Sonsón, Antioquia', 'Origin: Sonsón, Antioquia'),
 T('Certificados Rainforest Alliance, GLOBALG.A.P. e ICA', 'Rainforest Alliance, GLOBALG.A.P. and ICA certified'),
 T('Capacidad de suministro de 50 toneladas', '50 ton supply capacity'),
 T('Calibres del 12 al 32', 'Sizes 12 to 32'),
 T('Abastecimiento nacional desde Corabastos, Bogotá', 'National supply from Corabastos, Bogotá'),
]

def head(title_es, title_en, desc_es, desc_en, path, image='assets/imgs/origen/cultivo-hass-montana.jpg', extra=''):
    url = f'{SITE}/{"" if path == "index.html" else path}'
    return f'''<!doctype html>
<html lang="es" data-theme="dark">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <title data-en="{escape(title_en)}">{escape(title_es)}</title>
  <meta name="description" content="{escape(desc_es)}" data-en="{escape(desc_en)}" />
  <meta name="theme-color" content="#011d07" />
  <link rel="icon" type="image/png" href="assets/imgs/brand/favicon-agrocolombia.png" />
  <link rel="apple-touch-icon" href="assets/imgs/brand/favicon-agrocolombia.png" />
  <link rel="canonical" href="{url}" />
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="es_CO" />
  <meta property="og:site_name" content="Agro Colombia Company" />
  <meta property="og:title" content="{escape(title_es)}" />
  <meta property="og:description" content="{escape(desc_es)}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{SITE}/{image}" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <script>
    (function () {{
      var d = document.documentElement, t, l;
      try {{ t = localStorage.getItem('acc-theme'); l = localStorage.getItem('acc-lang'); }} catch (e) {{}}
      d.setAttribute('data-theme', t === 'light' || t === 'dark' ? t : 'dark');
      if (l === 'en') d.setAttribute('lang', 'en');
    }})();
  </script>
  <link rel="stylesheet" href="assets/css/icons.css?v={VERSION}" />
  <link rel="stylesheet" href="site.css?v={VERSION}" />
{extra}</head>
<body>
'''

def header(current):
    links = ''.join(f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{label}</a>' for h, label in NAV)
    overlay_links = ''.join(
        f'<a href="{h}" style="--i:{i}"{" aria-current=\"page\"" if h == current else ""}><small>0{i + 1}</small>{label}</a>'
        for i, (h, label) in enumerate(NAV))
    items = ''.join(f'<span class="marquee-item"><img src="assets/imgs/brand/avocado-mark.svg" alt="" />{m}</span>' for m in MARQUEE)
    return f'''  <a class="skip-link" href="#contenido">{T("Saltar al contenido", "Skip to content")}</a>
  <div class="top-sentinel" aria-hidden="true" style="position:absolute;top:0;height:120px;width:1px"></div>
  <div class="site-top">
    <div class="marquee-bar" role="region" aria-label="{T("Novedades", "Highlights")}">
      <div class="marquee-track"><div class="marquee-group">{items}</div><div class="marquee-group" aria-hidden="true">{items}</div></div>
    </div>
    <header class="site-header">
      <div class="island">
        <a class="brand-lockup" href="index.html" aria-label="{T("Agro Colombia Company, inicio", "Agro Colombia Company, home")}"><img src="assets/imgs/brand/favicon-agrocolombia.png" alt="" width="40" height="40" /><span>Agro Colombia <small>Company</small></span></a>
        <nav class="site-nav" aria-label="{T("Navegación principal", "Main navigation")}">{links}</nav>
        <div class="header-preferences">
          <div class="language-switch" role="group" aria-label="{T("Idioma", "Language")}"><button type="button" data-language="es" aria-pressed="true">ES</button><button type="button" data-language="en" aria-pressed="false">EN</button></div>
          <button class="icon-button theme-toggle" type="button" data-theme-toggle aria-label="{T("Cambiar tema", "Toggle theme")}">{icon("sun")}{icon("moon")}</button>
          <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="menu-overlay" aria-label="{T("Abrir menú", "Open menu")}"><span></span><span></span></button>
        </div>
        <a class="header-cta" href="contacto.html">{T("Cotizar", "Get a quote")} {ARROW}</a>
      </div>
    </header>
  </div>
  <div class="menu-overlay" id="menu-overlay" inert>
    <nav aria-label="{T("Menú móvil", "Mobile menu")}">{overlay_links}</nav>
    <div class="overlay-foot" style="--i:5">
      <a class="button button-gold" href="contacto.html">{T("Solicita tu cotización", "Request a quote")} {ARROW}</a>
      <div class="social-row">{social_links()}</div>
    </div>
  </div>
'''

def social_links():
    return (f'<a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{icon("instagram-logo")}</a>'
            f'<a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{icon("facebook-logo")}</a>'
            f'<a href="mailto:{EMAIL}" aria-label="{T("Correo electrónico", "Email")}">{icon("envelope-simple")}</a>'
            f'<a href="{SITE}" aria-label="{T("Sitio web", "Website")}">{icon("globe-simple")}</a>'
            f'<a href="https://wa.me/{WA}" data-whatsapp-link target="_blank" rel="noopener" aria-label="WhatsApp">{icon("whatsapp-logo")}</a>')

MAPS = {
 'bogota': ('https://www.openstreetmap.org/export/embed.html?bbox=-74.1720%2C4.6150%2C-74.1380%2C4.6400&layer=mapnik&marker=4.6275%2C-74.1545',
            'https://www.google.com/maps/search/?api=1&query=Corabastos+Bogot%C3%A1'),
 'sonson': ('https://www.openstreetmap.org/export/embed.html?bbox=-75.3550%2C5.6850%2C-75.2700%2C5.7380&layer=mapnik&marker=5.7114%2C-75.3108',
            'https://www.google.com/maps/search/?api=1&query=Sons%C3%B3n+Antioquia'),
}

def footer():
    cats = ''.join(f'<li><a href="servicios.html#{k}">{name}</a></li>' for k, name, _, _ in CATS)
    nav = ''.join(f'<li><a href="{h}">{label}</a></li>' for h, label in NAV)
    return f'''  <footer class="site-footer on-dark">
    <div class="footer-top">
      <div class="footer-cta reveal">
        <p class="eyebrow">{T("Dónde estamos", "Where we are")}</p>
        <h2 class="h-section">{T("De las montañas de Sonsón", "From the mountains of Sonsón")} <em>{T("a Corabastos, Bogotá.", "to Corabastos, Bogotá.")}</em></h2>
        <p class="muted">{T("Nuestra producción nace en Sonsón, Antioquia, y nuestra operación comercial y logística atiende desde Corabastos, una de las principales centrales de abastos del país.", "Our production starts in Sonsón, Antioquia, and our commercial and logistics operation serves clients from Corabastos, one of the country’s main wholesale markets.")}</p>
        <div class="hero-links">
          <a class="button button-gold" href="contacto.html">{T("Escríbenos", "Contact us")} {ARROW}</a>
          <a class="text-link" href="https://wa.me/{WA}" data-whatsapp-link target="_blank" rel="noopener">{icon("whatsapp-logo")} {WA_DISPLAY}</a>
        </div>
      </div>
      <div class="footer-map reveal" style="--d:1">
        <div class="footer-map-tabs">
          <div role="tablist" aria-label="{T("Ubicaciones", "Locations")}">
            <button type="button" role="tab" aria-selected="true" data-map-src="{MAPS["bogota"][0]}" data-map-link="{MAPS["bogota"][1]}">{icon("map-pin")}{T("Corabastos, Bogotá", "Corabastos, Bogotá")}</button>
            <button type="button" role="tab" aria-selected="false" data-map-src="{MAPS["sonson"][0]}" data-map-link="{MAPS["sonson"][1]}">{icon("plant")}{T("Sonsón, Antioquia", "Sonsón, Antioquia")}</button>
          </div>
          <a class="text-link" href="{MAPS["bogota"][1]}" target="_blank" rel="noopener" data-map-open>{T("Abrir en Google Maps", "Open in Google Maps")} {ARROW}</a>
        </div>
        <div class="footer-map-frame"><iframe title="{T("Mapa de la zona de operación", "Map of our operating area")}" src="{MAPS["bogota"][0]}" loading="lazy" referrerpolicy="no-referrer"></iframe></div>
      </div>
    </div>
    <div class="footer-main">
      <div class="footer-brand">
        <a class="brand-lockup" href="index.html"><img src="assets/imgs/brand/favicon-agrocolombia.png" alt="" width="40" height="40" loading="lazy" /><span>Agro Colombia <small>Company</small></span></a>
        <p>{T("Cultivando oportunidades.", "Cultivating opportunity.")}<br />{T("Del campo colombiano hacia nuevos mercados.", "From Colombian fields to new markets.")}</p>
        <div class="social-row">{social_links()}</div>
      </div>
      <div class="footer-col"><h3>{T("Navegación", "Navigation")}</h3><ul>{nav}</ul></div>
      <div class="footer-col"><h3>{T("Exportación", "Export")}</h3><ul><li><a href="index.html#ficha">{T("Ficha técnica", "Technical sheet")}</a></li><li><a href="index.html#proceso">{T("Proceso de exportación", "Export process")}</a></li><li><a href="index.html#certificaciones">{T("Certificaciones", "Certifications")}</a></li></ul>
        <h3 class="footer-sub">{T("Abastecimiento nacional", "National supply")}</h3><ul>{cats}<li><a href="assets/docs/catalogo-nacional-agro-colombia.pdf" target="_blank" rel="noopener">{T("Catálogo PDF", "PDF catalog")} {ARROW}</a></li></ul></div>
      <div class="footer-col"><h3>{T("Contacto", "Contact")}</h3><ul>
        <li><a href="https://wa.me/{WA}" data-whatsapp-link target="_blank" rel="noopener">{icon("whatsapp-logo")}{WA_DISPLAY}</a></li>
        <li><a href="mailto:{EMAIL}">{icon("envelope-simple")}{EMAIL}</a></li>
        <li><a href="{IG}" target="_blank" rel="noopener">{icon("instagram-logo")}@agrocolombiacompany</a></li>
        <li><a href="{FB}" target="_blank" rel="noopener">{icon("facebook-logo")}Facebook</a></li>
        <li><span>{icon("map-pin")}{T("Corabastos, Bogotá D. C.", "Corabastos, Bogotá D. C.")}</span></li>
        <li><span>{icon("plant")}{T("Sonsón, Antioquia", "Sonsón, Antioquia")}</span></li>
      </ul></div>
    </div>
    <div class="footer-certs"><span>{T("Certificaciones", "Certifications")}</span><div>{cert_strip()}</div></div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> {LEGAL_NAME} · NIT {NIT} · {T("Bogotá D. C., Colombia", "Bogotá D. C., Colombia")}</span>
      <nav class="footer-legal" aria-label="{T("Enlaces legales", "Legal links")}"><a href="privacidad.html">{T("Política de privacidad", "Privacy policy")}</a><a href="privacidad.html#terminos">{T("Términos de uso", "Terms of use")}</a></nav>
      <span>{T("Hecho en Colombia", "Made in Colombia")}</span>
    </div>
  </footer>
  <a class="whatsapp-float" href="https://wa.me/{WA}" data-whatsapp-link target="_blank" rel="noopener" aria-label="{T("Escríbenos por WhatsApp", "Message us on WhatsApp")}"><span class="whatsapp-float-icon">{icon("whatsapp-logo")}</span><span class="whatsapp-float-text"><small>{T("¿Hablamos?", "Let’s talk")}</small>{T("Escríbenos por WhatsApp", "Message us on WhatsApp")}</span></a>
{lightbox()}  <button class="to-top" type="button" data-to-top aria-label="{T("Volver arriba", "Back to top")}">{icon("arrow-down")}</button>
  <script src="assets/js/i18n.js?v={VERSION}"></script>
  <script src="site.js?v={VERSION}"></script>
</body>
</html>
'''

def page_hero(crumb, eyebrow, title_html, lead, media, actions=''):
    return f'''    <section class="page-hero on-dark">
      {media}
      <nav class="breadcrumb reveal" aria-label="{T("Ruta", "Breadcrumb")}"><a href="index.html">{T("Inicio", "Home")}</a><span aria-hidden="true">/</span><span>{crumb}</span></nav>
      <p class="eyebrow reveal" style="--d:1">{eyebrow}</p>
      <h1 class="reveal" style="--d:2">{title_html}</h1>
      <p class="lead reveal" style="--d:3">{lead}</p>
      {f'<div class="hero-links reveal" style="--d:4">{actions}</div>' if actions else ''}
    </section>
'''

def bg_video(name, label=''):
    return (f'<video data-bg-video muted loop playsinline preload="none" poster="assets/videos/fondos/{name}.jpg" aria-hidden="true">'
            f'<source src="assets/videos/fondos/{name}.mp4" type="video/mp4" /></video>')

EXPORT_PERKS = [('medal', T('Certificaciones internacionales', 'International certifications')), ('package', T('Calibres del 12 al 32', 'Sizes 12 to 32')), ('headset', T('Atención comercial personalizada', 'Personal sales support'))]
NATIONAL_PERKS = [('hand-coins', T('Pago contra entrega', 'Cash on delivery')), ('truck', T('Envío gratis en Bogotá', 'Free delivery in Bogotá')), ('coins', T('Precios mayoristas', 'Wholesale prices'))]

def closing(title_a, title_b, text, video='cosecha', perks=None, cta=None):
    return f'''    <section class="closing on-dark">
      {bg_video(video)}
      <div class="closing-copy">
        <p class="eyebrow reveal">{T("Cultivemos juntos", "Let’s grow together")}</p>
        <h2 class="h-display reveal" style="--d:1">{title_a} <em>{title_b}</em></h2>
        <p class="reveal" style="--d:2">{text}</p>
        <a class="button button-gold reveal" style="--d:3" href="contacto.html">{cta or T("Solicita tu cotización", "Request a quote")} {ARROW}</a>
        <ul class="closing-perks reveal" style="--d:4">{''.join(f'<li>{icon(ic)}{label}</li>' for ic, label in (perks or EXPORT_PERKS))}</ul>
      </div>
    </section>
'''

# ---------------------------------------------------------------- aguacate SVG
AVOCADO_SVG = '''<svg viewBox="0 0 400 520" aria-hidden="true" focusable="false">
  <defs>
    <radialGradient id="av-skin" cx="36%" cy="30%" r="78%"><stop offset="0" stop-color="#4d7030"/><stop offset=".42" stop-color="#2b4719"/><stop offset=".78" stop-color="#15270f"/><stop offset="1" stop-color="#080f06"/></radialGradient>
    <radialGradient id="av-volume" cx="40%" cy="36%" r="70%"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".55"/></radialGradient>
    <radialGradient id="av-spec" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fff" stop-opacity=".42"/><stop offset=".6" stop-color="#fff" stop-opacity=".08"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
    <linearGradient id="av-rim" x1="0" y1="0" x2="1" y2="0"><stop offset=".7" stop-color="#d7ad43" stop-opacity="0"/><stop offset="1" stop-color="#e9c96a" stop-opacity=".22"/></linearGradient>
    <radialGradient id="av-flesh" cx="50%" cy="62%" r="62%"><stop offset="0" stop-color="#f8f1b8"/><stop offset=".45" stop-color="#efe79c"/><stop offset=".7" stop-color="#dfe17f"/><stop offset=".86" stop-color="#b3cd5a"/><stop offset=".95" stop-color="#77a03a"/><stop offset="1" stop-color="#456f25"/></radialGradient>
    <radialGradient id="av-gloss" cx="36%" cy="34%" r="55%"><stop offset="0" stop-color="#fff" stop-opacity=".42"/><stop offset=".35" stop-color="#fff" stop-opacity=".12"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
    <radialGradient id="av-seed" cx="34%" cy="28%" r="80%"><stop offset="0" stop-color="#d9a26a"/><stop offset=".38" stop-color="#a1632f"/><stop offset=".75" stop-color="#6b3a18"/><stop offset="1" stop-color="#3f200b"/></radialGradient>
    <radialGradient id="av-cavity" cx="50%" cy="40%" r="62%"><stop offset="0" stop-color="#e9dd92"/><stop offset=".75" stop-color="#ddd185"/><stop offset="1" stop-color="#a99d50"/></radialGradient>
    <radialGradient id="av-ground" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#000" stop-opacity=".45"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
    <linearGradient id="av-leaf" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5f8f35"/><stop offset=".55" stop-color="#2f5d1f"/><stop offset="1" stop-color="#173a12"/></linearGradient>
    <pattern id="av-fl" width="70" height="70" patternUnits="userSpaceOnUse"><image preserveAspectRatio="none" href="data:image/webp;base64,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" width="70" height="70"/></pattern>
    <pattern id="av-sd" width="110" height="110" patternUnits="userSpaceOnUse"><image preserveAspectRatio="none" href="data:image/webp;base64,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" width="110" height="110"/></pattern>
    <radialGradient id="av-cav-shade" cx="50%" cy="50%" r="50%"><stop offset=".72" stop-color="#6b6a2a" stop-opacity="0"/><stop offset="1" stop-color="#6b6a2a" stop-opacity=".45"/></radialGradient>
    <pattern id="av-tex" width="44" height="44" patternUnits="userSpaceOnUse"><image preserveAspectRatio="none" href="data:image/webp;base64,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" width="44" height="44"/></pattern>
  </defs>
  <g class="avocado-half is-left">
    <ellipse cx="200" cy="506" rx="118" ry="12" fill="url(#av-ground)"/>
    <path d="M200 40C168 40 150 70 142 110C134 152 112 178 92 214C66 260 56 300 58 350C62 440 126 500 200 500C274 500 338 440 342 350C344 300 334 260 308 214C288 178 266 152 258 110C250 70 232 40 200 40Z" fill="#18290f"/>
    <path d="M200 40C168 40 150 70 142 110C134 152 112 178 92 214C66 260 56 300 58 350C62 440 126 500 200 500C274 500 338 440 342 350C344 300 334 260 308 214C288 178 266 152 258 110C250 70 232 40 200 40Z" fill="url(#av-tex)" style="mix-blend-mode:overlay" opacity=".8"/>
    <path d="M200 56C176 56 162 82 156 118C149 160 126 188 106 224C82 268 73 304 75 350C79 428 136 484 200 484C264 484 321 428 325 350C327 304 318 268 294 224C274 188 251 160 244 118C238 82 224 56 200 56Z" fill="url(#av-flesh)"/>
    <path d="M200 56C176 56 162 82 156 118C149 160 126 188 106 224C82 268 73 304 75 350C79 428 136 484 200 484C264 484 321 428 325 350C327 304 318 268 294 224C274 188 251 160 244 118C238 82 224 56 200 56Z" fill="url(#av-fl)" style="mix-blend-mode:soft-light" opacity=".45"/>
    <path d="M200 56C176 56 162 82 156 118C149 160 126 188 106 224C82 268 73 304 75 350C79 428 136 484 200 484C264 484 321 428 325 350C327 304 318 268 294 224C274 188 251 160 244 118C238 82 224 56 200 56Z" fill="none" stroke="#3f6d22" stroke-width="7" opacity=".8"/><path d="M200 56C176 56 162 82 156 118C149 160 126 188 106 224C82 268 73 304 75 350C79 428 136 484 200 484C264 484 321 428 325 350C327 304 318 268 294 224C274 188 251 160 244 118C238 82 224 56 200 56Z" fill="none" stroke="#8fb84a" stroke-width="3" opacity=".55" transform="translate(200 270) scale(.975) translate(-200 -270)"/>
    <g fill="none" stroke="#b9bf66" stroke-width="1.4" stroke-linecap="round" opacity=".55"><path d="M200 70C196 140 186 210 176 276"/><path d="M200 70C204 140 214 210 224 276"/><path d="M184 96C160 170 136 232 132 300"/><path d="M216 96C240 170 264 232 268 300"/><path d="M140 300C122 352 130 410 160 452"/><path d="M260 300C278 352 270 410 240 452"/></g>
    <path d="M200 56C176 56 162 82 156 118C149 160 126 188 106 224C82 268 73 304 75 350C79 428 136 484 200 484C264 484 321 428 325 350C327 304 318 268 294 224C274 188 251 160 244 118C238 82 224 56 200 56Z" fill="url(#av-gloss)"/>
    <g class="avocado-seed">
      <ellipse cx="200" cy="350" rx="64" ry="76" fill="#000" opacity=".22" transform="translate(4 8)"/>
      <ellipse cx="200" cy="348" rx="62" ry="74" fill="url(#av-seed)"/>
      <ellipse cx="200" cy="348" rx="62" ry="74" fill="url(#av-sd)" style="mix-blend-mode:soft-light" opacity=".35"/>
      <path d="M150 378C160 410 186 424 214 422C190 414 168 400 150 378Z" fill="#c9a27a" opacity=".45"/>
      <path d="M236 290C252 300 260 318 260 336C252 318 244 304 236 290Z" fill="#c9a27a" opacity=".4"/>
      <ellipse cx="200" cy="348" rx="61" ry="73" fill="none" stroke="#3a1d09" stroke-width="2" opacity=".55"/>
      <ellipse cx="178" cy="314" rx="20" ry="27" fill="url(#av-spec)"/>
      <ellipse cx="172" cy="306" rx="6" ry="9" fill="#fff" opacity=".35"/>
    </g>
  </g>
  <g class="avocado-half is-right">
    <ellipse cx="200" cy="506" rx="118" ry="12" fill="url(#av-ground)"/>
    <path d="M200 40C168 40 150 70 142 110C134 152 112 178 92 214C66 260 56 300 58 350C62 440 126 500 200 500C274 500 338 440 342 350C344 300 334 260 308 214C288 178 266 152 258 110C250 70 232 40 200 40Z" fill="#18290f"/>
    <path d="M200 40C168 40 150 70 142 110C134 152 112 178 92 214C66 260 56 300 58 350C62 440 126 500 200 500C274 500 338 440 342 350C344 300 334 260 308 214C288 178 266 152 258 110C250 70 232 40 200 40Z" fill="url(#av-tex)" style="mix-blend-mode:overlay" opacity=".8"/>
    <path d="M200 56C176 56 162 82 156 118C149 160 126 188 106 224C82 268 73 304 75 350C79 428 136 484 200 484C264 484 321 428 325 350C327 304 318 268 294 224C274 188 251 160 244 118C238 82 224 56 200 56Z" fill="url(#av-flesh)"/>
    <path d="M200 56C176 56 162 82 156 118C149 160 126 188 106 224C82 268 73 304 75 350C79 428 136 484 200 484C264 484 321 428 325 350C327 304 318 268 294 224C274 188 251 160 244 118C238 82 224 56 200 56Z" fill="url(#av-fl)" style="mix-blend-mode:soft-light" opacity=".45"/>
    <path d="M200 56C176 56 162 82 156 118C149 160 126 188 106 224C82 268 73 304 75 350C79 428 136 484 200 484C264 484 321 428 325 350C327 304 318 268 294 224C274 188 251 160 244 118C238 82 224 56 200 56Z" fill="none" stroke="#3f6d22" stroke-width="7" opacity=".8"/><path d="M200 56C176 56 162 82 156 118C149 160 126 188 106 224C82 268 73 304 75 350C79 428 136 484 200 484C264 484 321 428 325 350C327 304 318 268 294 224C274 188 251 160 244 118C238 82 224 56 200 56Z" fill="none" stroke="#8fb84a" stroke-width="3" opacity=".55" transform="translate(200 270) scale(.975) translate(-200 -270)"/>
    <g fill="none" stroke="#b9bf66" stroke-width="1.4" stroke-linecap="round" opacity=".55"><path d="M200 70C196 140 186 210 176 276"/><path d="M200 70C204 140 214 210 224 276"/><path d="M184 96C160 170 136 232 132 300"/><path d="M216 96C240 170 264 232 268 300"/><path d="M140 300C122 352 130 410 160 452"/><path d="M260 300C278 352 270 410 240 452"/></g>
    <path d="M200 56C176 56 162 82 156 118C149 160 126 188 106 224C82 268 73 304 75 350C79 428 136 484 200 484C264 484 321 428 325 350C327 304 318 268 294 224C274 188 251 160 244 118C238 82 224 56 200 56Z" fill="url(#av-gloss)"/>
    <ellipse cx="200" cy="348" rx="66" ry="78" fill="url(#av-cavity)"/>
    <ellipse cx="200" cy="348" rx="66" ry="78" fill="url(#av-fl)" style="mix-blend-mode:soft-light" opacity=".3"/>
    <ellipse cx="200" cy="348" rx="66" ry="78" fill="url(#av-cav-shade)"/>
    <ellipse cx="200" cy="348" rx="66" ry="78" fill="none" stroke="#9c8f45" stroke-width="2.5" opacity=".55"/>
    <ellipse cx="188" cy="322" rx="22" ry="30" fill="url(#av-spec)" opacity=".7"/>
  </g>
  <g class="avocado-whole">
    <path d="M200 44C201 34 203 26 206 18" stroke="#4a2a12" stroke-width="7" stroke-linecap="round" fill="none"/>
    <g class="avocado-leaf"><g transform="translate(205 30) rotate(-20) scale(.7)">
      <path d="M0 0C22 -24 68 -27 104 0C68 24 22 21 0 0Z" fill="#7ea24a"/>
      <path d="M0 0C22 -24 68 -27 104 0Z" fill="url(#av-leaf)"/>
      <path d="M8 -6C30 -18 62 -20 88 -6" stroke="#fff" stroke-opacity=".2" stroke-width="6" stroke-linecap="round" fill="none"/>
      <path d="M0 0Q52 -2 104 0" stroke="#d9e3a0" stroke-width="1.8" stroke-linecap="round" fill="none"/>
      <g stroke="#cbd98d" stroke-width="1" stroke-linecap="round" opacity=".6" fill="none"><path d="M18 -1L30 -13"/><path d="M34 -1L48 -16"/><path d="M52 -1L66 -15"/><path d="M70 -1L82 -10"/><path d="M18 0L30 11"/><path d="M34 0L48 14"/><path d="M52 0L66 13"/><path d="M70 0L82 9"/></g>
    </g></g>
    <path d="M200 40C168 40 150 70 142 110C134 152 112 178 92 214C66 260 56 300 58 350C62 440 126 500 200 500C274 500 338 440 342 350C344 300 334 260 308 214C288 178 266 152 258 110C250 70 232 40 200 40Z" fill="url(#av-skin)"/>
    <path d="M200 40C168 40 150 70 142 110C134 152 112 178 92 214C66 260 56 300 58 350C62 440 126 500 200 500C274 500 338 440 342 350C344 300 334 260 308 214C288 178 266 152 258 110C250 70 232 40 200 40Z" fill="url(#av-tex)" style="mix-blend-mode:overlay"/>
    <path d="M200 40C168 40 150 70 142 110C134 152 112 178 92 214C66 260 56 300 58 350C62 440 126 500 200 500C274 500 338 440 342 350C344 300 334 260 308 214C288 178 266 152 258 110C250 70 232 40 200 40Z" fill="url(#av-volume)"/>
    <path d="M200 40C168 40 150 70 142 110C134 152 112 178 92 214C66 260 56 300 58 350C62 440 126 500 200 500C274 500 338 440 342 350C344 300 334 260 308 214C288 178 266 152 258 110C250 70 232 40 200 40Z" fill="url(#av-rim)"/>
    <ellipse cx="146" cy="262" rx="40" ry="84" transform="rotate(14 146 262)" fill="url(#av-spec)"/>
    <ellipse cx="136" cy="236" rx="9" ry="22" transform="rotate(14 136 236)" fill="#fff" opacity=".22"/>
  </g>
</svg>'''

def word_reveal(es, en, accent_from=None):
    T(es, en)
    return f'<h2 class="word-reveal" data-words data-es="{escape(es)}" data-accent="{accent_from or ""}">{escape(es)}</h2>'


# ---------------------------------------------------------------- mapa pre-dibujado
DEPARTMENTS = {
 'CO-AMA': ('Amazonas', 'Amazonía'), 'CO-ANT': ('Antioquia', 'Andina'), 'CO-ARA': ('Arauca', 'Orinoquía'),
 'CO-ATL': ('Atlántico', 'Caribe'), 'CO-BOY': ('Boyacá', 'Andina'), 'CO-BOL': ('Bolívar', 'Caribe'),
 'CO-CAL': ('Caldas', 'Andina'), 'CO-CAQ': ('Caquetá', 'Amazonía'), 'CO-CAS': ('Casanare', 'Orinoquía'),
 'CO-CAU': ('Cauca', 'Pacífica'), 'CO-CES': ('Cesar', 'Caribe'), 'CO-CHO': ('Chocó', 'Pacífica'),
 'CO-COR': ('Córdoba', 'Caribe'), 'CO-CUN': ('Cundinamarca', 'Andina'), 'CO-DC': ('Bogotá D. C.', 'Andina'),
 'CO-GUA': ('Guainía', 'Amazonía'), 'CO-GUV': ('Guaviare', 'Amazonía'), 'CO-HUI': ('Huila', 'Andina'),
 'CO-LAG': ('La Guajira', 'Caribe'), 'CO-MAG': ('Magdalena', 'Caribe'), 'CO-MET': ('Meta', 'Orinoquía'),
 'CO-NAR': ('Nariño', 'Pacífica'), 'CO-NSA': ('Norte de Santander', 'Andina'), 'CO-PUT': ('Putumayo', 'Amazonía'),
 'CO-QUI': ('Quindío', 'Andina'), 'CO-RIS': ('Risaralda', 'Andina'), 'CO-SAP': ('San Andrés, Providencia y Santa Catalina', 'Insular'),
 'CO-SAN': ('Santander', 'Andina'), 'CO-SUC': ('Sucre', 'Caribe'), 'CO-TOL': ('Tolima', 'Andina'),
 'CO-VAC': ('Valle del Cauca', 'Pacífica'), 'CO-VAU': ('Vaupés', 'Amazonía'), 'CO-VID': ('Vichada', 'Orinoquía'),
}
T('San Andrés, Providencia y Santa Catalina', 'San Andrés, Providencia and Santa Catalina')
HOME = {'CO-ANT', 'CO-DC'}

def _simplify(points, tolerance):
    if len(points) < 4:
        return points
    keep = [False] * len(points); keep[0] = keep[-1] = True
    stack = [(0, len(points) - 1)]
    while stack:
        a, z = stack.pop()
        ax, ay = points[a]; zx, zy = points[z]
        dx, dy = zx - ax, zy - ay; norm = (dx * dx + dy * dy) ** .5
        best, index = 0, None
        for i in range(a + 1, z):
            px, py = points[i]
            d = abs(dy * px - dx * py + zx * ay - zy * ax) / norm if norm > 1e-6 else ((px - ax) ** 2 + (py - ay) ** 2) ** .5
            if d > best: best, index = d, i
        if index is not None and best > tolerance:
            keep[index] = True; stack += [(a, index), (index, z)]
    return [p for p, k in zip(points, keep) if k]

def map_svg():
    import math
    data = json.loads((ROOT / 'assets/maps/colombia-adm1.geojson').read_text(encoding='utf-8'))
    width, height, padding = 640, 680, 22
    pts = []
    def walk(node):
        if isinstance(node[0], (int, float)): pts.append(node)
        else: [walk(n) for n in node]
    for f in data['features']: walk(f['geometry']['coordinates'])
    lats = [p[1] for p in pts]
    mid = (min(lats) + max(lats)) / 2 * math.pi / 180
    proj = lambda p: (p[0] * math.pi / 180 * math.cos(mid), math.log(math.tan(math.pi / 4 + max(-85, min(85, p[1])) * math.pi / 360)))
    xy = [proj(p) for p in pts]
    minx, maxx = min(x for x, _ in xy), max(x for x, _ in xy); miny, maxy = min(y for _, y in xy), max(y for _, y in xy)
    scale = min((width - padding * 2) / (maxx - minx), (height - padding * 2) / (maxy - miny))
    ox, oy = (width - (maxx - minx) * scale) / 2, (height - (maxy - miny) * scale) / 2
    def to_svg(p):
        x, y = proj(p); return (ox + (x - minx) * scale, height - oy - (y - miny) * scale)
    paths = []
    for f in sorted(data['features'], key=lambda f: DEPARTMENTS[f['properties']['shapeISO']][0]):
        code = f['properties']['shapeISO']; name = DEPARTMENTS[code][0]
        polygons = [f['geometry']['coordinates']] if f['geometry']['type'] == 'Polygon' else f['geometry']['coordinates']
        d = ''
        for polygon in polygons:
            for ring in polygon:
                r = _simplify([to_svg(p) for p in ring], .45)
                area = abs(sum(r[i][0] * r[i - 1][1] - r[i - 1][0] * r[i][1] for i in range(len(r)))) / 2
                if len(r) < 4 or (area < 1.5 and code != 'CO-SAP'): continue
                d += 'M' + 'L'.join(f'{x:.1f},{y:.1f}' for x, y in r) + 'Z'
        cls = ' class="is-home"' if code in HOME else ''
        paths.append(f'<path d="{d}" data-code="{code}" data-region="{DEPARTMENTS[code][1]}"{cls} role="button" tabindex="0" aria-pressed="false" aria-label="{escape(name)}"><title>{escape(name)}</title></path>')
    options = ''.join(f'<option value="{c}">{escape(n)}</option>' for c, (n, _) in sorted(DEPARTMENTS.items(), key=lambda kv: kv[1][0]))
    pins = ''
    for (lat, lon), label, side in (((5.7114, -75.3108), T('Sonsón', 'Sonsón'), 'start'), ((4.6275, -74.1545), 'Corabastos', 'start')):
        x, y = to_svg((lon, lat))
        pins += (f'<g class="map-pin" transform="translate({x:.1f} {y:.1f})" aria-hidden="true">'
                 f'<circle class="map-pin-pulse" r="9"/><circle class="map-pin-dot" r="8"/>'
                 f'<text x="16" y="7">{escape(label)}</text></g>')
    return ''.join(paths) + pins, options

# ---------------------------------------------------------------- INICIO
def build_index():
    TEASER = ''.join(f'<a class="teaser-card reveal" style="--d:{i}" href="nosotros.html#cultivo"><img src="assets/imgs/cultivo/{f}-sm.webp" alt="{escape(a)}" loading="lazy" /></a>' for i, (f, a, _) in enumerate([CROP_PHOTOS[i] for i in (2, 0, 3, 1, 5)]))
    X = 'assets/imgs/exportacion'
    chips = lambda items: ''.join(f'<li>{icon(ic)}{label}</li>' for ic, label in items)
    origin_chips = chips([('map-pin', T('Sonsón, Antioquia', 'Sonsón, Antioquia')), ('plant', T('Tierras fértiles', 'Fertile land')), ('leaf', T('Tradición agrícola', 'Farming tradition')), ('sun', T('Paisajes que inspiran', 'Inspiring landscapes'))])
    people_chips = chips([('plant', T('Agricultores locales', 'Local growers')), ('users-three', T('Familias del campo', 'Farming families')), ('medal', T('Conocimiento y experiencia', 'Knowledge and experience')), ('globe-simple', T('Regiones que avanzan', 'Regions moving forward'))])
    attrs = chips([('sparkle', T('Sabor característico', 'Distinctive flavor')), ('cooking-pot', T('Versatilidad gastronómica', 'Culinary versatility')), ('leaf', T('Textura cremosa', 'Creamy texture')), ('medal', T('Variedad apreciada', 'Prized variety')), ('globe-simple', T('Potencial en mercados internacionales', 'Strong international demand'))])
    stages = [
     ('flores', T('Cultivo', 'Growing'), T('Cuidado de los árboles en nuestras tierras de Sonsón, Antioquia, con condiciones ideales para un fruto de alta calidad.', 'Tree care on our land in Sonsón, Antioquia, with ideal conditions for high quality fruit.')),
     ('recogiendo', T('Cosecha', 'Harvest'), T('Recolección manual en el punto óptimo de maduración.', 'Hand picked at the optimal point of maturity.')),
     ('hass-caja', T('Recepción', 'Reception'), T('Recepción del fruto en nuestras instalaciones para su revisión inicial de calidad.', 'Fruit is received at our facilities for an initial quality check.')),
     ('manos-caja', T('Selección', 'Sorting'), T('Clasificación manual de acuerdo con el peso, tamaño, apariencia y calidad del fruto.', 'Hand sorted by weight, size, appearance and quality.')),
     ('cosecha-caja', T('Empaque', 'Packing'), T('Materiales diseñados para proteger el fruto y mantener su calidad durante el transporte internacional.', 'Packaging designed to protect the fruit and keep its quality during international transport.')),
    ]
    stage_cards = ''.join(f'<li class="step-card reveal" style="--d:{i}"><figure><img src="{X}/{img}.webp" alt="" loading="lazy" /></figure><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (img, t, d) in enumerate(stages))
    pillars = [
     ('map-pin', T('Origen colombiano', 'Colombian origin'), T('Producción agrícola en Sonsón, Antioquia, una región que forma parte de nuestra identidad y de nuestra historia.', 'Grown in Sonsón, Antioquia, a region that is part of our identity and our story.')),
     ('plant', T('Cercanía con el campo', 'Close to the farm'), T('Conocimiento del origen del producto y contacto directo con las actividades de cultivo, cosecha y selección.', 'First hand knowledge of the fruit and direct involvement in growing, harvest and sorting.')),
     ('headset', T('Atención comercial personalizada', 'Personal sales support'), T('Buscamos comprender los requerimientos de cada cliente para desarrollar propuestas acordes con sus necesidades.', 'We take time to understand each buyer’s requirements and shape proposals around them.')),
     ('handshake', T('Relaciones a largo plazo', 'Long term partnerships'), T('Creemos en las alianzas construidas sobre la transparencia, la responsabilidad y el crecimiento mutuo.', 'We believe in partnerships built on transparency, responsibility and shared growth.')),
    ]
    pillar_cards = ''.join(f'<article class="value-card reveal{" is-featured" if i == 0 else ""}" style="--d:{i}"><span class="value-icon">{icon(ic)}</span><span class="value-num">0{i + 1}</span><h3>{t}</h3><p>{d}</p></article>' for i, (ic, t, d) in enumerate(pillars))
    specs = [
     ('plant', T('Producto', 'Product'), T('Aguacate Hass fresco', 'Fresh Hass avocado')),
     ('map-pin', T('Origen', 'Origin'), T('Sonsón, Antioquia, Colombia', 'Sonsón, Antioquia, Colombia')),
     ('truck', T('Capacidad de suministro', 'Supply capacity'), T('50 toneladas, periodicidad por confirmar', '50 tons, frequency to be confirmed')),
     ('package', T('Presentaciones y empaques', 'Presentation and packaging'), T('Según requerimientos del mercado de destino', 'Based on destination market requirements')),
     ('clock', T('Frecuencia de abastecimiento', 'Supply frequency'), T('Según acuerdo comercial con el cliente', 'Agreed with each client')),
     ('leaf', T('Conservación', 'Post harvest handling'), T('Manejo poscosecha según los requerimientos técnicos del mercado de destino', 'Handled to the technical requirements of the destination market')),
     ('clipboard-text', T('Condiciones comerciales', 'Commercial terms'), T('Según negociación y acuerdo entre las partes', 'Subject to negotiation between the parties')),
     ('check-circle', T('Calibres', 'Sizes'), T('Del 12 (340 a 390 g) al 32 (100 a 122 g)', 'From 12 (340 to 390 g) to 32 (100 to 122 g)')),
    ]
    spec_cards = ''.join(f'<div class="spec-card reveal" style="--d:{i % 4}"><span class="value-icon">{icon(ic)}</span><div><small>{k}</small><strong>{v}</strong></div></div>' for i, (ic, k, v) in enumerate(specs))
    faqs = [
     (T('¿De dónde proviene su aguacate Hass?', 'Where do your Hass avocados come from?'), T('De nuestros cultivos en Sonsón, Antioquia, una región de montaña con tradición agrícola. Acompañamos el proceso desde el árbol hasta el empaque.', 'From our orchards in Sonsón, Antioquia, a mountain region with a long farming tradition. We follow the process from tree to packing.')),
     (T('¿Qué calibres manejan?', 'Which sizes do you supply?'), T('Del calibre 12 (340 a 390 g) al 32 (100 a 122 g). La tabla completa de pesos está en la sección Abastecimiento nacional.', 'From size 12 (340 to 390 g) to size 32 (100 to 122 g). The full weight table is in the National supply section.')),
     (T('¿Cuál es su capacidad de suministro?', 'What is your supply capacity?'), T('Contamos con una capacidad de suministro de 50 toneladas. La periodicidad se define según el acuerdo comercial con cada cliente.', 'We have a supply capacity of 50 tons. Frequency is defined in the commercial agreement with each client.')),
     (T('¿Qué certificaciones tienen?', 'Which certifications do you hold?'), T('Contamos con certificación Rainforest Alliance, certificación GLOBALG.A.P. y registro ante el ICA, Instituto Colombiano Agropecuario.', 'We are Rainforest Alliance and GLOBALG.A.P. certified and registered with ICA, the Colombian Agricultural Institute.')),
     (T('¿Cómo se empaca el producto?', 'How is the fruit packed?'), T('Las presentaciones y empaques se definen según los requerimientos del mercado de destino, con materiales que protegen el fruto durante el transporte internacional.', 'Presentation and packaging follow the destination market requirements, using materials that protect the fruit in international transport.')),
     (T('¿Cuáles son las condiciones comerciales?', 'What are the commercial terms?'), T('Se definen por negociación y acuerdo entre las partes. Cuéntanos tu mercado de destino y volumen para preparar una propuesta.', 'They are agreed between the parties. Tell us your destination market and volume and we will prepare a proposal.')),
     (T('¿También venden en Colombia?', 'Do you also sell in Colombia?'), T(f'Sí. Desde Corabastos, Bogotá, distribuimos {TOTAL} referencias de frutas, hortalizas, tubérculos y plátanos. Puedes verlas en la sección Abastecimiento nacional.', f'Yes. From Corabastos, Bogotá, we supply {TOTAL} fruits, vegetables, tubers and plantains. See the National supply section.')),
     (T('¿Cómo solicito una cotización de exportación?', 'How do I request an export quote?'), T('Escríbenos por WhatsApp, correo o el formulario de contacto con el mercado de destino, el volumen, los calibres y la frecuencia que necesitas.', 'Message us on WhatsApp, by email or through the contact form with your destination market, volume, sizes and frequency.')),
    ]
    faq_html = ''.join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(faqs))
    faq_ld = json.dumps({'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faqs]}, ensure_ascii=False)
    org_ld = json.dumps({'@context': 'https://schema.org', '@type': 'Organization', 'name': 'Agro Colombia Company', 'legalName': LEGAL_NAME, 'taxID': NIT,
        'url': SITE + '/', 'logo': SITE + '/assets/imgs/brand/logo-completo.png', 'email': EMAIL, 'telephone': WA_DISPLAY, 'sameAs': [IG, FB], 'slogan': 'Cultivando oportunidades',
        'address': {'@type': 'PostalAddress', 'addressLocality': 'Bogotá', 'addressRegion': 'Bogotá D. C.', 'addressCountry': 'CO'},
        'hasCredential': [{'@type': 'EducationalOccupationalCredential', 'name': n, 'url': u} for _, n, u, _ in CERTS],
        'description': 'Productor y exportador colombiano de aguacate Hass de Sonsón, Antioquia, con certificaciones Rainforest Alliance, GLOBALG.A.P. y registro ICA.'}, ensure_ascii=False)
    extra = f'  <script type="application/ld+json">{org_ld}</script>\n  <script type="application/ld+json">{faq_ld}</script>\n'
    body = f"""<main id="contenido">
    <section class="hero hero-scroll on-dark" data-hero-scroll aria-labelledby="hero-title">
      <div class="hero-sticky">
        <div class="hero-bg"><img src="assets/imgs/origen/cultivo-hass-montana.jpg" alt="" fetchpriority="high" /></div>
        <div class="hero-copy">
          <p class="eyebrow reveal">{T("Aguacate Hass colombiano de exportación", "Colombian Hass avocados for export")}</p>
          <h1 id="hero-title" class="reveal" style="--d:1">{T("De nuestras montañas", "From our mountains")} <em>{T("al mundo.", "to the world.")}</em></h1>
          <p class="hero-intro reveal" style="--d:2">{T("Producimos aguacate Hass fresco en Sonsón, Antioquia, con certificaciones internacionales y una propuesta comercial que se adapta a las necesidades de cada mercado.", "We grow fresh Hass avocados in Sonsón, Antioquia, with international certifications and a commercial approach tailored to each market.")}</p>
          <div class="hero-links reveal" style="--d:3">
            <a class="button button-gold" href="contacto.html?tipo=exportacion">{T("Cotiza tu exportación", "Request an export quote")} {ARROW}</a>
            <a class="text-link" href="#ficha">{T("Ver ficha técnica", "See technical sheet")} {icon("arrow-down")}</a>
          </div>
          <ul class="hero-stats reveal" style="--d:4">
            <li><strong data-count="50" data-suffix=" t">50 t</strong><span>{T("capacidad de suministro", "supply capacity")}</span></li>
            <li><strong data-count="11">11</strong><span>{T("calibres disponibles", "available sizes")}</span></li>
            <li><strong data-count="3">3</strong><span>{T("certificaciones y registros", "certifications")}</span></li>
          </ul>
        </div>
        <div class="avocado-stage" aria-hidden="true">
          <div class="avocado"><div class="avocado-glow"></div>{AVOCADO_SVG}</div>
          <ol class="avocado-steps">
            <li><b>01 · {T("Cultivo", "Growing")}</b>{T("Sonsón, Antioquia", "Sonsón, Antioquia")}</li>
            <li><b>02 · {T("Selección", "Sorting")}</b>{T("Por calibre y calidad", "By size and quality")}</li>
            <li><b>03 · {T("Exportación", "Export")}</b>{T("Al mercado de destino", "To your market")}</li>
          </ol>
        </div>
        <a class="scroll-cue" href="#historia"><span class="scroll-line"></span>{T("Desliza para abrir el aguacate", "Scroll to open the avocado")}</a>
      </div>
    </section>

    <section class="brand-pillars on-dark" aria-label="{T("Nuestros pilares", "Our pillars")}">
      <ul>
        <li class="reveal">{icon("map-pin")}<span>{T("Origen Sonsón, Antioquia", "Origin Sonsón, Antioquia")}</span></li>
        <li class="reveal" style="--d:1">{icon("plant")}<span>{T("Producción responsable", "Responsible production")}</span></li>
        <li class="reveal" style="--d:2">{icon("globe-simple")}<span>{T("Mercados internacionales", "International markets")}</span></li>
        <li class="reveal" style="--d:3">{icon("handshake")}<span>{T("Alianzas de largo plazo", "Long term partnerships")}</span></li>
      </ul>
    </section>

    <section class="manifesto on-deep on-dark" id="historia">
      <div class="manifesto-inner">
        <p class="eyebrow">{T("Nuestra tierra conecta al mundo", "Our land connects with the world")}</p>
        {word_reveal("Nuestro origen es Colombia. Nuestro horizonte es el mundo.", "Our origin is Colombia. Our horizon is the world.", "4")}
        <p class="reveal">{T("Cada cosecha representa el trabajo de nuestra tierra. Cada nuevo mercado es una oportunidad para llevar ese esfuerzo más lejos.", "Every harvest carries the work of our land. Every new market is a chance to take that effort further.")}</p>
        <a class="text-link reveal" href="nosotros.html">{T("Conoce nuestra historia", "Read our story")} {ARROW}</a>
      </div>
      <img class="manifesto-figure" src="assets/imgs/brand/aguacate-hass-rama.svg?v={VERSION}" alt="" aria-hidden="true" />
    </section>

    <section class="section editorial-split" id="origen">
      <figure class="editorial-media reveal"><img src="{X}/origen-sonson.webp" style="object-position: 18% 50%" alt="{T("Montañas y cultivos de Sonsón, Antioquia", "Mountains and farmland in Sonsón, Antioquia")}" loading="lazy" /><figcaption>{icon("map-pin")}{T("Sonsón, Antioquia", "Sonsón, Antioquia")}</figcaption></figure>
      <div class="editorial-copy">
        <p class="eyebrow reveal">{T("Nuestro origen", "Our origin")}</p>
        <h2 class="h-section reveal" style="--d:1">{T("Todo comienza", "It all begins")} <em>{T("en nuestra tierra.", "in our land.")}</em></h2>
        <p class="reveal" style="--d:2">{T("En el corazón de las montañas de Sonsón, Antioquia, donde la naturaleza y la tradición agrícola forman parte de nuestra identidad, comienza la historia de nuestro aguacate Hass.", "In the heart of the mountains of Sonsón, Antioquia, where nature and farming tradition are part of who we are, the story of our Hass avocados begins.")}</p>
        <p class="reveal" style="--d:3">{T("Entre paisajes verdes y tierras cultivadas con dedicación crece un fruto que representa mucho más que una cosecha: el esfuerzo de quienes trabajan el campo colombiano.", "Among green hills and carefully tended land grows a fruit that means far more than a harvest: the effort of the people who work Colombia’s countryside.")}</p>
<p class="pull-quote reveal" style="--d:4">{T("Y el nuestro comienza en Colombia.", "And ours begins in Colombia.")}</p>
        <ul class="values-row reveal" style="--d:4">{origin_chips}</ul>
      </div>
    </section>

    <section class="section editorial-split is-flipped on-dark">
      <figure class="editorial-media reveal"><img src="{X}/agricultor.webp" alt="{T("Agricultor cosechando aguacate Hass", "Farmer harvesting Hass avocados")}" loading="lazy" /></figure>
      <div class="editorial-copy">
        <p class="eyebrow reveal">{T("Las manos que hacen posible cada cosecha", "The hands behind every harvest")}</p>
        <h2 class="h-section reveal" style="--d:1">{T("Detrás de cada cosecha", "Behind every harvest")} <em>{T("hay una historia.", "there is a story.")}</em></h2>
        <p class="reveal" style="--d:2">{T("Desde el cuidado de los árboles hasta la recolección y selección de los frutos, las manos de nuestros agricultores colombianos son parte esencial del proceso. Personas que conocen la tierra y saben que la calidad comienza mucho antes de que el producto llegue al consumidor.", "From caring for the trees to picking and sorting the fruit, the hands of our Colombian growers are essential to the process. People who know the land and understand that quality starts long before the fruit reaches the consumer.")}</p>
<p class="pull-quote reveal" style="--d:3">{T("Porque detrás de cada aguacate hay manos que trabajan, familias que sueñan y una tierra que nos llena de orgullo.", "Because behind every avocado there are hands that work, families with dreams and a land that makes us proud.")}</p>
        <ul class="values-row reveal" style="--d:3">{people_chips}</ul>
      </div>
    </section>

    <section class="section editorial-split" id="producto">
      <figure class="editorial-media reveal"><img src="{X}/mitad-hass.webp" alt="{T("Aguacate Hass partido por la mitad", "Hass avocado cut in half")}" loading="lazy" /></figure>
      <div class="editorial-copy">
        <p class="eyebrow reveal">{T("Un fruto que representa nuestra tierra", "A fruit that represents our land")}</p>
        <h2 class="h-section reveal" style="--d:1">{T("Aguacate Hass:", "Hass avocado:")} <em>{T("la riqueza de nuestro origen.", "the richness of our origin.")}</em></h2>
        <p class="reveal" style="--d:2">{T("Reconocido internacionalmente por su textura cremosa, su sabor característico y su versatilidad gastronómica, el aguacate Hass se ha convertido en un producto apreciado en diferentes mercados.", "Known worldwide for its creamy texture, distinctive flavor and culinary versatility, the Hass avocado is valued in markets around the world.")}</p>
        <p class="reveal" style="--d:3">{T("Conectamos la producción colombiana con compradores que valoran el origen, la calidad y las relaciones comerciales de largo plazo.", "We connect Colombian production with buyers who value origin, quality and long term commercial relationships.")}</p>
<p class="pull-quote reveal" style="--d:4">{T("Un fruto colombiano con vocación internacional.", "A Colombian fruit made for the world.")}</p>
        <ul class="values-row reveal" style="--d:4">{attrs}</ul>
      </div>
    </section>

    <section class="section on-dark steps-section" id="proceso">
      <div class="section-head">
        <div><p class="eyebrow reveal">{T("Del árbol a la selección", "From tree to sorting")}</p><h2 class="h-section reveal" style="--d:1">{T("Cada etapa", "Every stage")} <em>{T("importa.", "matters.")}</em></h2></div>
        <p class="reveal" style="--d:2">{T("La calidad se construye desde el origen y requiere atención durante todo el recorrido. Así preparamos nuestro aguacate Hass para los mercados internacionales.", "Quality is built from the origin and needs care along the whole journey. This is how we prepare our Hass avocados for international markets.")}</p>
      </div>
      <ol class="steps steps-5">{stage_cards}</ol>
      <p class="pull-quote is-center reveal" style="--d:1">{T("Nuestro propósito es que el valor de nuestra tierra se refleje en cada entrega.", "Our purpose is for the value of our land to show in every delivery.")}</p>
    </section>

    <section class="section" id="ficha">
      <div class="section-head">
        <div><p class="eyebrow reveal">{T("Información técnica y comercial", "Technical and commercial information")}</p><h2 class="h-section reveal" style="--d:1">{T("Nuestro aguacate Hass", "Our Hass avocados")} <em>{T("para mercados internacionales.", "for international markets.")}</em></h2></div>
        <p class="reveal" style="--d:2">{T("Un producto colombiano con especificaciones que se adaptan a su mercado.", "A Colombian product with specifications that adapt to your market.")}</p>
      </div>
      <div class="spec-grid">{spec_cards}</div>
      <div class="section-cta reveal">
        <a class="button button-gold" href="contacto.html?tipo=exportacion">{T("Solicitar ficha y cotización", "Request sheet and quote")} {ARROW}</a>
        <a class="text-link" href="servicios.html#calibres">{T("Ver tabla de calibres", "See the size table")} {ARROW}</a>
      </div>
    </section>

    <section class="section section-alt" id="certificaciones">
      <div class="section-head">
        <div><p class="eyebrow reveal">{T("Certificaciones y registros", "Certifications and registrations")}</p><h2 class="h-section reveal" style="--d:1">{T("Calidad respaldada", "Quality backed")} <em>{T("por estándares internacionales.", "by international standards.")}</em></h2></div>
        <p class="reveal" style="--d:2">{T("Nuestro cultivo cumple con estándares de sostenibilidad, buenas prácticas agrícolas y requisitos fitosanitarios para la exportación. Toca cada certificación para ir a su sitio oficial.", "Our orchards meet sustainability, good agricultural practice and plant health requirements for export. Tap each certification to visit its official website.")}</p>
      </div>
      {cert_cards()}
    </section>

    <section class="section on-dark">
      <div class="section-head">
        <div><p class="eyebrow reveal">{T("Nuestra propuesta de valor", "Our value proposition")}</p><h2 class="h-section reveal" style="--d:1">{T("Más que un proveedor,", "More than a supplier,")} <em>{T("un aliado comercial.", "a business partner.")}</em></h2></div>
        <p class="reveal" style="--d:2">{T("Construir relaciones comerciales internacionales requiere confianza, comunicación, compromiso y la capacidad de comprender las necesidades de cada comprador.", "Building international trade relationships takes trust, communication, commitment and a real understanding of each buyer’s needs.")}</p>
      </div>
      <div class="value-grid is-4">{pillar_cards}</div>
      <p class="pull-quote is-center reveal" style="--d:1">{T("Construyamos juntos relaciones que generen valor, oportunidades y un impacto positivo en el largo plazo.", "Let’s build relationships together that create value, opportunity and a positive long term impact.")}</p>
    </section>

    <section class="section reel-section on-deep on-dark" aria-labelledby="reel-title">
      <div class="reel-layout">
        <div class="reel-frame reveal" data-reel>
          <video playsinline muted loop preload="none" poster="assets/imgs/origen/reel-poster.jpg" aria-label="{T("Video del cultivo de aguacate Hass de Agro Colombia Company", "Video of Agro Colombia Company’s Hass avocado farm")}"><source src="assets/videos/reel-web.mp4" type="video/mp4" /></video>
          <div class="reel-progress" aria-hidden="true"><span></span></div>
          <div class="reel-controls">
            <button class="reel-sound" type="button" data-reel-sound aria-pressed="false">{icon("speaker-slash", "is-muted")}{icon("speaker-high", "is-on")}<span data-sound-label>{T("Activar sonido", "Turn sound on")}</span></button>
            <button class="reel-toggle" type="button" data-reel-toggle aria-label="{T("Pausar video", "Pause video")}">{icon("pause", "is-playing")}{icon("play", "is-paused")}</button>
          </div>
        </div>
        <div class="reel-copy">
          <p class="eyebrow reveal">{T("Desde el origen", "From the source")}</p>
          <h2 class="h-section reveal" id="reel-title" style="--d:1">{T("Del campo nace", "Quality is born")} <em>{T("nuestra calidad.", "in the field.")}</em></h2>
          <p class="lead reveal" style="--d:2">{T("Mira el video con sonido y recorre con nosotros el camino del aguacate Hass, desde las montañas de Sonsón hasta la selección.", "Watch with sound and follow the Hass avocado’s journey with us, from the mountains of Sonsón to selection.")}</p>
          <ol class="reel-chapters reveal" style="--d:3">
            <li><button type="button" data-seek="0">{icon("map-pin")}<span><b>{T("Origen", "Origin")}</b>{T("Las montañas de Sonsón, Antioquia, donde nace nuestro aguacate Hass.", "The mountains of Sonsón, Antioquia, where our Hass avocados grow.")}</span><small>0:00</small></button></li>
            <li><button type="button" data-seek="10">{icon("plant")}<span><b>{T("Cuidado", "Care")}</b>{T("Acompañamos cada etapa del cultivo, desde la tierra hasta la cosecha.", "We look after every stage, from soil to harvest.")}</span><small>0:10</small></button></li>
            <li><button type="button" data-seek="17">{icon("check-circle")}<span><b>{T("Calidad", "Quality")}</b>{T("Seleccionamos el producto según los requerimientos de cada cliente.", "Produce is selected to each client’s requirements.")}</span><small>0:17</small></button></li>
          </ol>
        </div>
      </div>
    </section>

    <section class="section horizon-section">
      <div class="horizon-grid">
        <figure class="horizon-main reveal"><img src="{X}/puerto-cajas.webp" alt="{T("Cajas de aguacate Hass Agro Colombia en puerto", "Agro Colombia Hass avocado crates at port")}" loading="lazy" /></figure>
        <div class="horizon-copy">
          <p class="eyebrow reveal">{T("Cuando el campo crece, crecen las oportunidades", "When the countryside grows, opportunities grow")}</p>
          <h2 class="h-section reveal" style="--d:1">{T("El próximo capítulo", "The next chapter")} <em>{T("podemos escribirlo juntos.", "we can write together.")}</em></h2>
          <p class="reveal" style="--d:2">{T("Queremos conectar la riqueza agrícola colombiana con empresas que crean, como nosotros, en el valor de construir alianzas duraderas, y que nuestro crecimiento comercial represente nuevas posibilidades para las familias que hacen parte de esta cadena productiva.", "We want to connect Colombia’s farming wealth with companies that, like us, value lasting partnerships, so our commercial growth also creates new opportunities for the families in this supply chain.")}</p>
          <div class="horizon-thumbs reveal" style="--d:3"><img src="{X}/contenedor.webp" alt="{T("Carga lista para contenedor", "Cargo ready for container")}" loading="lazy" /><img src="{X}/carga-aerea.webp" alt="{T("Carga aérea", "Air cargo")}" loading="lazy" /></div>
        </div>
      </div>
    </section>

    <section class="section crop-teaser on-dark on-deep">
      <div class="section-head">
        <div><p class="eyebrow reveal">{T("Nuestro cultivo", "Our orchard")}</p><h2 class="h-section reveal" style="--d:1">{T("Fotos reales", "Real photos")} <em>{T("desde Sonsón.", "from Sonsón.")}</em></h2></div>
        <p class="reveal" style="--d:2">{T("Árboles en producción, frutos en la rama y cosecha en canastillas. Así trabajamos todos los días.", "Trees in production, fruit on the branch and harvest in crates. This is how we work every day.")}</p>
      </div>
      <div class="teaser-strip">{TEASER}</div>
      <div class="section-cta reveal"><a class="button button-gold" href="nosotros.html#cultivo">{T("Ver galería y videos del cultivo", "See the orchard gallery and videos")} {ARROW}</a></div>
    </section>

    <section class="section">
      <a class="national-band reveal" href="servicios.html">
        <img src="assets/imgs/escenas/cat-frutas.webp" alt="" loading="lazy" />
        <div><p class="eyebrow">{T("Abastecimiento nacional", "National supply")}</p><h3>{T(f"Soluciones integrales para el suministro de productos agrícolas frescos: {TOTAL} referencias desde Corabastos, Bogotá.", f"Complete supply solutions for fresh produce: {TOTAL} products from Corabastos, Bogotá.")}</h3></div>
        <span class="button button-gold">{T("Ver abastecimiento nacional", "See national supply")} {ARROW}</span>
      </a>
    </section>

    <section class="section faq-section section-alt" id="preguntas">
      <div class="faq-heading">
        <p class="eyebrow reveal">{T("Preguntas frecuentes", "FAQ")}</p>
        <h2 class="h-section reveal" style="--d:1">{T("Lo que preguntan", "What buyers ask")} <em>{T("nuestros compradores.", "before ordering.")}</em></h2>
        <p class="reveal" style="--d:2">{T("Si tu pregunta no está aquí, escríbenos y te respondemos con la información vigente.", "If your question is not here, write to us and we will reply with current details.")}</p>
        <a class="text-link reveal" style="--d:3" href="contacto.html?tipo=exportacion">{T("Hacer una pregunta", "Ask a question")} {ARROW}</a>
      </div>
      <div class="faq-list reveal" style="--d:1">{faq_html}</div>
    </section>
{closing(T("Cultivemos", "Let’s cultivate"), T("oportunidades juntos.", "opportunities together."), T("Conectemos el campo colombiano con nuevos mercados. Cuéntanos tu destino, volumen y calibres y te preparamos una propuesta.", "Let’s connect Colombian farms with new markets. Tell us your destination, volume and sizes and we will prepare a proposal."), cta=T("Cotiza tu exportación", "Request an export quote"), perks=[('check-circle', T('Calidad', 'Quality')), ('handshake', T('Confianza', 'Trust')), ('users-three', T('Alianzas', 'Partnerships')), ('plant', T('Crecimiento', 'Growth'))])}  </main>
"""
    body = body.replace('href="contacto.html"', 'href="contacto.html?tipo=exportacion"')
    return (head('Agro Colombia Company | Aguacate Hass y productos agrícolas frescos', 'Agro Colombia Company | Hass avocados and fresh produce',
                 'Aguacate Hass fresco de Sonsón, Antioquia, para mercados internacionales. Certificaciones Rainforest Alliance, GLOBALG.A.P. y registro ICA. Capacidad de 50 toneladas.',
                 'Fresh Hass avocados from Sonsón, Antioquia, for international markets. Rainforest Alliance and GLOBALG.A.P. certified, ICA registered. 50 ton supply capacity.',
                 'index.html', 'assets/imgs/exportacion/mitad-hass.webp', extra=extra) + header('index.html') + body + footer())

# ---------------------------------------------------------------- NOSOTROS
def build_nosotros():
    values = [('handshake', T('Compromiso', 'Commitment')), ('check-circle', T('Calidad', 'Quality')), ('shield-star', T('Responsabilidad', 'Responsibility')),
              ('hand-heart', T('Confianza', 'Trust')), ('users-three', T('Trabajo en equipo', 'Teamwork')), ('plant', T('Desarrollo del campo', 'Rural development'))]
    chips = ''.join(f'<li>{icon(ic)}{v}</li>' for ic, v in values)
    body = f'''<main id="contenido">
{page_hero(T("Nosotros", "About us"), T("Nuestra historia", "Our story"),
  f'{T("Una empresa colombiana,", "A Colombian company,")} <em>{T("conectada con su origen.", "connected to its roots.")}</em>',
  T("Producimos aguacate Hass para mercados internacionales y distribuimos productos agrícolas frescos en Colombia. Unimos el trabajo del campo con la operación comercial.", "We grow Hass avocados for international markets and distribute fresh produce across Colombia, connecting farm work with commercial operations."),
  bg_video('huerto'))}
    <section class="section editorial-split">
      <figure class="editorial-media reveal"><img src="assets/imgs/origen/paisaje-sonson.jpeg" alt="{T("Paisaje de la zona de cultivo en Sonsón, Antioquia", "Farmland in Sonsón, Antioquia")}" loading="lazy" /><figcaption>{icon("map-pin")}{T("Sonsón, Antioquia", "Sonsón, Antioquia")}</figcaption></figure>
      <div class="editorial-copy">
        <p class="eyebrow reveal">{T("Quiénes somos", "Who we are")}</p>
        <h2 class="h-section reveal" style="--d:1">{T("Del campo colombiano", "From Colombian farms")} <em>{T("a cada operación.", "to every operation.")}</em></h2>
        <p class="reveal" style="--d:2">{T("Somos una empresa colombiana especializada en la distribución de frutas, verduras y productos agrícolas frescos, directamente desde los cultivos y cosechas.", "We are a Colombian company specialized in distributing fresh fruit, vegetables and farm produce, straight from the crops and harvests.")}</p>
        <p class="reveal" style="--d:3">{T("Con más de 10 años de experiencia en el sector agrario y en centros de abastecimiento, hemos construido relaciones sólidas con más de 200 clientes en Bogotá y a nivel nacional, que confían en nuestro compromiso con la calidad, el servicio y la puntualidad.", "With more than 10 years in agriculture and wholesale markets, we have built solid relationships with more than 200 clients in Bogotá and nationwide who trust our commitment to quality, service and punctuality.")}</p>
      </div>
    </section>
    <section class="section on-dark">
      <ul class="stats-band">
        <li class="reveal"><strong data-count="10" data-prefix="+">+10</strong><span>{T("años de experiencia en el sector agrario", "years of experience in agriculture")}</span></li>
        <li class="reveal" style="--d:1"><strong data-count="200" data-prefix="+">+200</strong><span>{T("clientes en Bogotá y a nivel nacional", "clients in Bogotá and nationwide")}</span></li>
        <li class="reveal" style="--d:2"><strong data-count="{TOTAL}">{TOTAL}</strong><span>{T("referencias de frutas, hortalizas, tubérculos y plátanos", "fruits, vegetables, tubers and plantains")}</span></li>
      </ul>
    </section>
    <section class="section">
      <div class="section-head"><div><p class="eyebrow reveal">{T("Hacia dónde vamos", "Where we are going")}</p><h2 class="h-section reveal" style="--d:1">{T("Propósito con", "Purpose with")} <em>{T("raíces profundas.", "deep roots.")}</em></h2></div></div>
      <div class="mv-grid">
        <article class="mv-card reveal"><span class="value-icon">{icon("plant")}</span><p class="eyebrow">{T("Misión", "Mission")}</p><h3>{T("Abastecer con lo mejor del campo.", "Supplying the best of the field.")}</h3><p>{T("Abastecer con productos agrícolas frescos y de calidad a nuestros clientes, generando relaciones a largo plazo basadas en confianza, servicio y compromiso con el desarrollo del sector agrícola colombiano.", "To supply our clients with fresh, quality produce, building long term relationships based on trust, service and commitment to Colombian agriculture.")}</p></article>
        <article class="mv-card reveal" style="--d:1"><span class="value-icon">{icon("globe-simple")}</span><p class="eyebrow">{T("Visión", "Vision")}</p><h3>{T("Llevar el campo colombiano más lejos.", "Taking Colombian agriculture further.")}</h3><p>{T("Ser una empresa líder en distribución agrícola en Colombia, reconocida por su excelencia operativa e innovación, y avanzar hacia mercados internacionales con la calidad del campo colombiano.", "To be a leading agricultural distributor in Colombia, known for operational excellence and innovation, and to reach international markets with the quality of Colombian produce.")}</p></article>
      </div>
    </section>
    <section class="section on-dark on-deep">
      <p class="eyebrow reveal">{T("Lo que nos guía", "What guides us")}</p>
      <h2 class="h-display reveal" style="--d:1;max-width:880px;margin-top:24px">{T("Creemos en el potencial del campo colombiano", "We believe in the potential of Colombian agriculture")} <em>{T("y en las relaciones que generan valor.", "and in relationships that create value.")}</em></h2>
      <ul class="values-row reveal" style="--d:2">{chips}</ul>
    </section>
    <section class="section editorial-split is-flipped">
      <figure class="editorial-media reveal"><img src="assets/imgs/origen/cultivo-hass-montana.jpg" alt="{T("Cultivo de aguacate Hass en una zona montañosa", "Hass avocado orchard on a mountainside")}" loading="lazy" /><figcaption>{icon("plant")}{T("Cultivo de aguacate Hass", "Hass avocado orchard")}</figcaption></figure>
      <div class="editorial-copy">
        <p class="eyebrow reveal">{T("El territorio", "The land")}</p>
        <h2 class="h-section reveal" style="--d:1">{T("Todo comienza", "It all begins")} <em>{T("en la tierra.", "in the soil.")}</em></h2>
        <p class="reveal" style="--d:2">{T("Entre las montañas de Antioquia comienza nuestra historia. En Sonsón cultivamos aguacate Hass, en una región de tradición y vocación agrícola donde el territorio permite desarrollar un producto con potencial para distintos mercados.", "Our story begins in the mountains of Antioquia. In Sonsón we grow Hass avocados, in a region with a deep farming tradition where the land produces fruit with potential for many markets.")}</p>
        <p class="reveal" style="--d:3">{T("Para nosotros, la tierra no es solo el lugar donde nace el producto. Es donde comienzan las oportunidades.", "For us, the land is not only where the fruit grows. It is where opportunity begins.")}</p>
      </div>
    </section>
    <section class="section on-dark on-deep" id="cultivo">
      <div class="section-head"><div><p class="eyebrow reveal">{T("Nuestro cultivo", "Our orchard")}</p><h2 class="h-section reveal" style="--d:1">{T("Así luce el origen", "This is what the origin")} <em>{T("de nuestro aguacate.", "of our avocados looks like.")}</em></h2></div>
      <p class="reveal" style="--d:2">{T("Fotos y videos reales de nuestros lotes de aguacate Hass en Sonsón, Antioquia. Toca cualquier imagen para verla en grande.", "Real photos and videos of our Hass avocado plots in Sonsón, Antioquia. Tap any image to see it full size.")}</p></div>
      {crop_videos()}
      {crop_gallery()}
    </section>
    <section class="section section-alt">
      <div class="section-head"><div><p class="eyebrow reveal">{T("Una operación, dos puntos clave", "One operation, two key places")}</p><h2 class="h-section reveal" style="--d:1">{T("Origen en Antioquia.", "Grown in Antioquia.")} <em>{T("Conexión en Bogotá.", "Connected in Bogotá.")}</em></h2></div>
      <p class="reveal" style="--d:2">{T("Nuestra ubicación en Corabastos, uno de los principales centros de abastecimiento del país, nos conecta con compradores en distintas regiones.", "Our base at Corabastos, one of the country’s main wholesale markets, connects us with buyers across regions.")}</p></div>
      <div class="route-band reveal">
        <div><b>{T("Origen", "Origin")}</b><strong>{T("Sonsón, Antioquia", "Sonsón, Antioquia")}</strong><p>{T("Cultivo y cosecha de aguacate Hass", "Hass avocado growing and harvest")}</p></div>
        <span class="route-line" aria-hidden="true"></span>
        <div><b>{T("Operación", "Operations")}</b><strong>{T("Corabastos, Bogotá D. C.", "Corabastos, Bogotá D. C.")}</strong><p>{T("Comercialización y logística nacional", "National sales and logistics")}</p></div>
      </div>
    </section>
    <section class="section editorial-split">
      <figure class="editorial-media reveal"><img src="assets/imgs/referencias/marca-en-campo.jpeg" alt="{T("Agro Colombia Company sobre un paisaje agrícola", "Agro Colombia Company over farmland")}" loading="lazy" /></figure>
      <div class="editorial-copy">
        <p class="eyebrow reveal">{T("Nuestra historia sigue creciendo", "Our story keeps growing")}</p>
        <h2 class="h-section reveal" style="--d:1">{T("De Colombia", "From Colombia")} <em>{T("hacia nuevos mercados.", "to new markets.")}</em></h2>
        <p class="reveal" style="--d:2">{T("Lo que comienza en las montañas de Sonsón busca llegar cada vez más lejos. Con certificaciones Rainforest Alliance, GLOBALG.A.P. y registro ICA, llevamos nuestro aguacate Hass a compradores que valoran el origen y la calidad.", "What begins in the mountains of Sonsón aims to go further. With Rainforest Alliance and GLOBALG.A.P. certification and ICA registration, we take our Hass avocados to buyers who value origin and quality.")}</p>
        <a class="button button-gold reveal" style="--d:3" href="contacto.html">{T("Conversemos", "Let’s talk")} {ARROW}</a>
      </div>
    </section>
{closing(T("Cultivemos nuevas", "Let’s grow new"), T("oportunidades juntos.", "opportunities together."), T("Buscamos relaciones con clientes, distribuidores y aliados interesados en productos agrícolas colombianos.", "We are looking for clients, distributors and partners interested in Colombian produce."), 'huerto')}  </main>
'''
    return (head('Nosotros | Agro Colombia Company', 'About us | Agro Colombia Company',
                 'Más de 10 años en el sector agrario y más de 200 clientes. Conoce el origen de Agro Colombia Company en Sonsón, Antioquia, y su operación en Corabastos, Bogotá.',
                 'More than 10 years in agriculture and 200 clients. Discover Agro Colombia Company’s origin in Sonsón, Antioquia, and its operation at Corabastos, Bogotá.',
                 'nosotros.html', 'assets/imgs/origen/paisaje-sonson.jpeg') + header('nosotros.html') + body + footer())

# ---------------------------------------------------------------- PRODUCTOS
def build_productos():
    MAP_PATHS, MAP_OPTIONS = map_svg()
    chips = (f'<button class="chip" type="button" data-filter="all" aria-pressed="true">{T("Todos", "All")} <small>{TOTAL}</small></button>' +
             ''.join(f'<button class="chip" type="button" data-filter="{k}" aria-pressed="false">{name} <small>{COUNTS[k]}</small></button>' for k, name, _, _ in CATS))
    items = ''.join(f'<li data-cat="{k}">{tile(i)}</li>' for k in CATALOG for i in CATALOG[k])
    cat_cards = ''.join(f"""<a class="category-card reveal" style="--d:{n}" href="#{k}">
          <img src="assets/imgs/escenas/{img}" alt="" loading="lazy" />
          <div class="category-card-body"><span class="category-count" data-count="{COUNTS[k]}">{COUNTS[k]}</span><h3>{name}</h3><p>{desc}</p>
          <span class="card-link">{T("Ver referencias", "See products")} {icon("arrow-up-right")}</span></div></a>""" for n, (k, name, img, desc) in enumerate(CATS))
    values = [
     ('headset', T('Atención personalizada', 'Personal service'), T('Nos adaptamos a las necesidades de cada cliente para ofrecer soluciones a la medida.', 'We adapt to each client’s needs with tailored solutions.')),
     ('truck', T('Transporte y envío gratis', 'Own fleet, free delivery'), T('Transporte propio y envío gratuito en Bogotá, y según cobertura a nivel nacional.', 'Our own trucks and free delivery in Bogotá, and nationwide depending on coverage.')),
     ('leaf', T('Productos frescos y de calidad', 'Fresh, quality produce'), T('Seleccionamos directamente desde los cultivos para garantizar frescura y calidad.', 'Selected straight from the farms to guarantee freshness and quality.')),
     ('coins', T('Precio mayorista', 'Wholesale prices'), T('Precios competitivos que dejan un mayor beneficio para tu negocio.', 'Competitive prices that leave more margin for your business.')),
     ('hand-coins', T('Pago contra entrega', 'Cash on delivery'), T('Confianza y seguridad en cada compra: pagas cuando recibes.', 'Trust and security in every order: you pay when it arrives.')),
     ('clock', T('Puntualidad garantizada', 'On time, every time'), T('Cumplimos los tiempos de entrega para que tu operación nunca se detenga.', 'We meet delivery times so your operation never stops.')),
    ]
    value_cards = ''.join(f"""<article class="value-card reveal{" is-featured" if i == 1 else ""}" style="--d:{i % 3}"><span class="value-icon">{icon(ic)}</span><span class="value-num">0{i + 1}</span><h3>{t}</h3><p>{d}</p></article>""" for i, (ic, t, d) in enumerate(values))
    sectors = [('abastos', 'storefront', T('Centrales de abastos', 'Wholesale markets')), ('restaurantes', 'fork-knife', T('Restaurantes', 'Restaurants')),
               ('hoteles', 'bed', T('Hoteles', 'Hotels')), ('casinos', 'cooking-pot', T('Casinos y comedores', 'Cafeterias')),
               ('colegios', 'graduation-cap', T('Colegios', 'Schools')), ('hospitales', 'first-aid', T('Hospitales', 'Hospitals')),
               ('carceles', 'buildings', T('Centros penitenciarios', 'Correctional facilities')), ('ejercito', 'medal', T('Ejército', 'Army')),
               ('policia', 'shield-star', T('Policía', 'Police')), ('fundaciones', 'hand-heart', T('Fundaciones', 'Foundations'))]
    sector_cards = ''.join(f'<figure class="sector-card reveal" style="--d:{i % 5}"><img src="assets/imgs/escenas/sector-{k}.webp" alt="" loading="lazy" /><span>{icon(ic)}{label}</span></figure>' for i, (k, ic, label) in enumerate(sectors))
    steps = [('paso-1', T('Cuéntanos qué necesitas', 'Tell us what you need'), T('Productos, volumen y zona de entrega. Te asesoramos de forma personalizada.', 'Products, volume and delivery area. We advise you one on one.')),
             ('paso-3', T('Aprueba tu cotización', 'Approve your quote'), T('Te enviamos una propuesta según disponibilidad y confirmamos la fecha de entrega.', 'We send a proposal based on availability and confirm the delivery date.')),
             ('paso-6', T('Recibe y paga al llegar', 'Receive and pay on arrival'), T('Llevamos tu pedido con transporte propio y pagas contra entrega.', 'We deliver with our own fleet and you pay on delivery.'))]
    step_cards = ''.join(f'<li class="step-card reveal" style="--d:{i}"><figure><img src="assets/imgs/escenas/{img}.webp?v={VERSION}" alt="" loading="lazy" /></figure><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (img, t, d) in enumerate(steps))
    calibres = [(12, '340 – 390'), (14, '261 – 339'), (16, '240 – 260'), (18, '211 – 239'), (20, '197 – 210'), (22, '176 – 196'), (24, '152 – 175'), (26, '145 – 152'), (28, '135 – 144'), (30, '123 – 134'), (32, '100 – 122')]
    cal_rows = ''.join(f'<tr><th scope="row">{c}</th><td>{g} g</td></tr>' for c, g in calibres)
    faqs = [
     (T('¿El envío tiene costo?', 'Is delivery free?'), T('Contamos con transporte propio y el envío es gratis en Bogotá. Para otras ciudades lo confirmamos según la cobertura de tu zona.', 'We run our own fleet and delivery is free in Bogotá. For other cities we confirm it based on coverage in your area.')),
     (T('¿Cómo se paga el pedido?', 'How do I pay?'), T('Pagas contra entrega, cuando recibes tus productos en la fecha acordada.', 'You pay on delivery, when your products arrive on the agreed date.')),
     (T('¿Venden al por mayor?', 'Do you sell wholesale?'), T('Sí. Manejamos precios mayoristas para negocios e instituciones. Volúmenes y frecuencia se acuerdan en cada cotización.', 'Yes. We offer wholesale prices to businesses and institutions. Volumes and frequency are agreed in each quote.')),
     (T('¿A qué tipo de clientes atienden?', 'Who do you supply?'), T('Centrales de abastos, restaurantes, hoteles, casinos, colegios, hospitales, instituciones públicas y fundaciones, entre otros.', 'Wholesale markets, restaurants, hotels, cafeterias, schools, hospitals, public institutions and foundations, among others.')),
    ]
    faq_html = ''.join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(faqs))
    body = f"""<main id="contenido">
{page_hero(T("Abastecimiento nacional", "National supply"), T("Abastecimiento nacional", "National supply"),
  f'{T("Soluciones integrales para el suministro", "Complete supply solutions")} <em>{T("de productos agrícolas frescos.", "for fresh farm produce.")}</em>',
  T("En Agro Colombia Company conectamos el campo colombiano con las necesidades de nuestros clientes, ofreciendo un amplio portafolio de frutas, verduras, hortalizas, tubérculos, plátanos y otros productos agrícolas.", "At Agro Colombia Company we connect Colombian farms with our clients’ needs, offering a wide range of fruit, vegetables, greens, tubers, plantains and other farm produce."),
  bg_video('mercado'),
  f'<a class="button button-gold" href="contacto.html?tipo=nacional">{T("Solicita tu cotización", "Request a quote")} {ARROW}</a><a class="text-link" href="#catalogo">{T("Ver portafolio", "See our portfolio")} {icon("arrow-down")}</a>')}
    <section class="section">
      <div class="section-head">
        <div><p class="eyebrow reveal">{T("Nuestro portafolio", "Our portfolio")}</p><h2 class="h-section reveal" style="--d:1">{T("Seleccionado desde", "Selected straight")} <em>{T("los cultivos.", "from the farms.")}</em></h2></div>
        <p class="reveal" style="--d:2">{T("Atendemos hoteles, restaurantes, casinos, instituciones y establecimientos comerciales, con un servicio de abastecimiento confiable, eficiente y personalizado.", "We serve hotels, restaurants, cafeterias, institutions and retail businesses with reliable, efficient and personal supply service.")}</p>
      </div>
      <div class="category-grid">{cat_cards}</div>
    </section>
    <section class="section editorial-split section-alt" id="aguacate">
      <figure class="editorial-media reveal"><img src="assets/imgs/origen/cosecha-hass.webp" alt="{T("Cosecha de aguacate Hass", "Hass avocado harvest")}" loading="lazy" /><figcaption>{icon("map-pin")}{T("Origen: Sonsón, Antioquia", "Origin: Sonsón, Antioquia")}</figcaption></figure>
      <div class="editorial-copy" id="calibres">
        <p class="eyebrow reveal">{T("Producto de origen propio", "Grown by us")}</p>
        <h2 class="h-section reveal" style="--d:1">{T("Aguacate Hass", "Hass avocado")} <em>{T("por calibre.", "by size.")}</em></h2>
        <p class="reveal" style="--d:2">{T("Producción en Sonsón, Antioquia, clasificada por peso. Disponibilidad y presentaciones se confirman en cada pedido.", "Grown in Sonsón, Antioquia and sorted by weight. Availability and presentation are confirmed with each order.")}</p>
        <table class="calibre-table reveal" style="--d:3">
          <caption>{T("Tabla de calibres del productor", "Grower size table")}</caption>
          <thead><tr><th scope="col">{T("Calibre", "Size")}</th><th scope="col">{T("Peso en gramos", "Weight in grams")}</th></tr></thead>
          <tbody>{cal_rows}</tbody>
        </table>
        <a class="button button-gold reveal" style="--d:4" href="contacto.html?tipo=nacional">{T("Consultar disponibilidad", "Ask about availability")} {ARROW}</a>
      </div>
    </section>
    <section class="section" id="catalogo">
      <div class="section-head"><div><p class="eyebrow reveal">{T("Catálogo nacional", "National catalog")}</p><h2 class="h-section reveal" style="--d:1">{T(f"{TOTAL} referencias", f"{TOTAL} products")} <em>{T("del campo colombiano.", "from Colombian farms.")}</em></h2></div>
      <p class="reveal" style="--d:2">{T("Filtra por categoría y consulta la disponibilidad vigente con nuestro equipo.", "Filter by category and ask our team about current availability.")}</p></div>
      <div class="filter-bar" role="group" aria-label="{T("Filtrar por categoría", "Filter by category")}">{chips}</div>
      <ul class="catalog-grid" data-catalog>{items}</ul>
      <p class="catalog-count" data-catalog-count aria-live="polite"></p>
      <a class="catalog-download reveal" href="assets/docs/catalogo-nacional-agro-colombia.pdf" target="_blank" rel="noopener" style="margin-top:48px">
        <img src="assets/imgs/catalogo/portada-catalogo.jpg" alt="" loading="lazy" />
        <div><h3>{T("Catálogo nacional en PDF", "National catalog in PDF")}</h3><p>{T("Todo el portafolio con fotografías, listo para compartir con tu equipo de compras.", "The full portfolio with photos, ready to share with your purchasing team.")}</p></div>
        <span class="button button-gold">{T("Descargar", "Download")} {ARROW}</span>
      </a>
    </section>
    <section class="section on-dark">
      <div class="section-head">
        <div><p class="eyebrow reveal">{T("Por qué trabajar con nosotros", "Why work with us")}</p><h2 class="h-section reveal" style="--d:1">{T("Un servicio pensado para que tu operación", "Service designed so your operation")} <em>{T("no se detenga.", "never stops.")}</em></h2></div>
        <p class="reveal" style="--d:2">{T("Productos frescos, un servicio eficiente y atención personalizada para responder a cada cliente con compromiso.", "Fresh produce, efficient service and personal attention for every client.")}</p>
      </div>
      <div class="value-grid">{value_cards}</div>
    </section>
    <section class="section">
      <div class="section-head">
        <div><p class="eyebrow reveal">{T("A quiénes abastecemos", "Who we supply")}</p><h2 class="h-section reveal" style="--d:1">{T("Diferentes sectores,", "Different sectors,")} <em>{T("un mismo compromiso.", "one commitment.")}</em></h2></div>
        <p class="reveal" style="--d:2">{T("Llevamos lo mejor del campo colombiano a cada operación, con un servicio confiable y adaptado a cada cliente.", "We bring the best of Colombian farms to every operation, with reliable service tailored to each client.")}</p>
      </div>
      <div class="sector-grid">{sector_cards}</div>
    </section>
    <section class="section on-dark steps-section">
      <div class="section-head">
        <div><p class="eyebrow reveal">{T("Cómo funciona", "How it works")}</p><h2 class="h-section reveal" style="--d:1">{T("Del pedido a tu operación", "From order to operation")} <em>{T("en tres pasos.", "in three steps.")}</em></h2></div>
        <p class="reveal" style="--d:2">{T("Un proceso simple, seguro y eficiente para que recibas productos frescos y a tiempo.", "A simple, secure and efficient process so fresh produce arrives on time.")}</p>
      </div>
      <ol class="steps">{step_cards}</ol>
      <div class="section-cta reveal"><a class="text-link" href="contacto.html#proceso">{T("Ver el proceso completo", "See the full process")} {icon("arrow-right")}</a></div>
    </section>
    <section class="section section-alt map-section" id="cobertura" aria-labelledby="map-title">
      <div class="map-intro">
        <p class="eyebrow reveal">{T("Cobertura nacional", "National coverage")}</p>
        <h2 class="h-section reveal" id="map-title" style="--d:1">{T("Presencia en Bogotá", "Present in Bogotá")} <em>{T("y a nivel nacional.", "and nationwide.")}</em></h2>
        <p class="reveal" style="--d:2">{T("Explora los 32 departamentos y Bogotá D. C. Te confirmamos destinos y disponibilidad vigentes para tu zona.", "Explore Colombia’s 32 departments and Bogotá D. C. We confirm current destinations and availability for your area.")}</p>
        <ul class="map-legend reveal" style="--d:3">
          <li><span class="legend-dot is-home"></span><span><b>{T("Origen", "Origin")}</b>{T("Sonsón, Antioquia", "Sonsón, Antioquia")}</span></li>
          <li><span class="legend-dot is-home"></span><span><b>{T("Operación", "Operations")}</b>{T("Corabastos, Bogotá D. C.", "Corabastos, Bogotá D. C.")}</span></li>
          <li><span class="legend-dot"></span><span><b>{T("Cobertura", "Coverage")}</b>{T("Según destino y disponibilidad", "Depending on destination and availability")}</span></li>
        </ul>
      </div>
      <div class="map-card on-dark reveal" style="--d:1">
        <div class="map-canvas">
          <svg class="department-map" viewBox="0 0 640 680" role="group" aria-label="{T("Mapa interactivo de departamentos de Colombia", "Interactive map of Colombian departments")}"><g data-map-geometry>{MAP_PATHS}</g></svg>
        </div>
        <div class="map-details">
          <label for="department-select">{T("Explora el mapa", "Explore the map")}</label>
          <div class="select-wrap"><select id="department-select" data-map-select><option value="">{T("Selecciona un departamento", "Select a department")}</option>{MAP_OPTIONS}</select></div>
          <div class="map-selection" aria-live="polite"><span data-map-region>{T("Cobertura nacional", "National coverage")}</span><h3 data-map-name>Colombia</h3><p data-map-copy>{T("Antioquia es nuestro origen y Bogotá nuestra operación comercial. Selecciona un departamento para consultar destinos.", "Antioquia is our origin and Bogotá our commercial hub. Select a department to ask about destinations.")}</p></div>
          <a class="button button-gold" href="contacto.html?tipo=nacional">{T("Hablar con el equipo", "Talk to our team")} {ARROW}</a>
          <p class="map-attribution">{T("Límites administrativos:", "Administrative boundaries:")} <a href="https://www.geoboundaries.org/" target="_blank" rel="noopener">geoBoundaries</a>, OpenStreetMap / Wambacher, <a href="https://opendatacommons.org/licenses/odbl/1-0/" target="_blank" rel="noopener">ODbL 1.0</a>.</p>
        </div>
      </div>
    </section>
    <section class="section faq-section" id="preguntas">
      <div class="faq-heading">
        <p class="eyebrow reveal">{T("Preguntas frecuentes", "FAQ")}</p>
        <h2 class="h-section reveal" style="--d:1">{T("Lo que nos preguntan", "What clients ask")} <em>{T("antes de comprar.", "before ordering.")}</em></h2>
        <a class="text-link reveal" style="--d:2" href="contacto.html?tipo=nacional">{T("Hacer una pregunta", "Ask a question")} {ARROW}</a>
      </div>
      <div class="faq-list reveal" style="--d:1">{faq_html}</div>
    </section>
{closing(T("¿Listo para abastecer", "Ready to stock"), T("tu negocio?", "your business?"), T("Cuéntanos qué productos necesitas y a dónde deben llegar. Te respondemos con una cotización a la medida.", "Tell us which products you need and where they should go. We will reply with a tailored quote."), 'aguacate-corte', NATIONAL_PERKS)}  </main>
"""
    body = body.replace('href="contacto.html"', 'href="contacto.html?tipo=nacional"')
    return (head('Abastecimiento nacional | Agro Colombia Company', 'National supply | Agro Colombia Company',
                 f'Abastecimiento nacional desde Corabastos, Bogotá: aguacate Hass por calibre y {TOTAL} referencias de frutas, hortalizas, tubérculos y plátanos. Envío gratis en Bogotá y pago contra entrega.',
                 f'National supply from Corabastos, Bogotá: Hass avocados by size and {TOTAL} fruits, vegetables, tubers and plantains. Free delivery in Bogotá and cash on delivery.',
                 'servicios.html', 'assets/imgs/escenas/cat-frutas.webp') + header('servicios.html') + body + footer())

# ---------------------------------------------------------------- CONTACTO
def build_contacto():
    steps = [
     ('paso-1', T('Contáctanos', 'Contact us'), T('Cuéntanos tus necesidades, volumen y productos de interés. Te asesoramos de forma personalizada.', 'Tell us your needs, volume and products of interest. We advise you one on one.')),
     ('paso-2', T('Cotización', 'Quote'), T('Te enviamos una propuesta detallada según disponibilidad, cantidades y zona de entrega.', 'We send a detailed proposal based on availability, quantities and delivery area.')),
     ('paso-3', T('Confirmación', 'Confirmation'), T('Cuando apruebas la cotización, confirmamos tu pedido y coordinamos la fecha de entrega.', 'Once you approve the quote, we confirm your order and schedule delivery.')),
     ('paso-4', T('Preparación en el campo', 'Preparation at the farm'), T('Seleccionamos y preparamos los productos desde los cultivos, cuidando frescura y manejo.', 'We select and prepare produce at the farm, protecting freshness and handling.')),
     ('paso-5', T('Transporte seguro', 'Safe transport'), T('Transporte propio y logística eficiente para entregar en óptimas condiciones y sin costo adicional.', 'Our own fleet and efficient logistics deliver in top condition at no extra cost.')),
     ('paso-6', T('Entrega y pago', 'Delivery and payment'), T('Recibes tus productos en la fecha acordada y pagas contra entrega, de forma segura.', 'Your produce arrives on the agreed date and you pay securely on delivery.')),
    ]
    step_cards = ''.join(f'<li class="step-card reveal" style="--d:{i % 3}"><figure><img src="assets/imgs/escenas/{img}.webp?v={VERSION}" alt="" loading="lazy" /></figure><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (img, t, d) in enumerate(steps))
    def field(name, label, kind='text', required=False, auto='', full=False, optional=False, extra=''):
        opt = f' <span>({T("opcional", "optional")})</span>' if optional else ''
        tag = (f'<textarea id="f-{name}" name="{name}"{" required" if required else ""} aria-describedby="e-{name}"{extra}></textarea>' if kind == 'textarea' else
               f'<input id="f-{name}" name="{name}" type="{kind}"{f" autocomplete=\"{auto}\"" if auto else ""}{" required" if required else ""} aria-describedby="e-{name}"{extra} />')
        return f'<div class="field{" field-full" if full else ""}"><label for="f-{name}">{label}{opt}</label>{tag}<span class="field-error" id="e-{name}"></span></div>'
    kind = (f'<div class="field field-full"><label for="f-type">{T("Tipo de solicitud", "Request type")}</label>'
            f'<div class="select-wrap"><select id="f-type" name="type" required aria-describedby="e-type">'
            f'<option value="exportacion">{T("Exportación de aguacate Hass", "Hass avocado export")}</option>'
            f'<option value="nacional">{T("Abastecimiento nacional", "National supply")}</option></select></div>'
            f'<span class="field-error" id="e-type"></span></div>')
    form = (kind + field('name', T('Nombre', 'Name'), auto='name', required=True) +
            field('company', T('Empresa o negocio', 'Company or business'), auto='organization', optional=True) +
            field('email', T('Correo electrónico', 'Email'), 'email', True, 'email') +
            field('phone', T('Teléfono', 'Phone'), 'tel', False, 'tel', optional=True) +
            field('city', T('País y ciudad de destino', 'Destination country and city'), auto='address-level2', required=True) +
            field('interest', T('Productos de interés', 'Products of interest'), extra=f' placeholder="{T("Aguacate Hass, frutas, hortalizas...", "Hass avocados, fruit, vegetables...")}"') +
            field('message', T('Volumen, calibres, frecuencia y detalles', 'Volume, sizes, frequency and details'), 'textarea', True, full=True))
    body = f'''<main id="contenido">
{page_hero(T("Contacto", "Contact"), T("Hablemos", "Let’s talk"),
  f'{T("Conectemos el campo colombiano", "Let’s connect Colombian farms")} <em>{T("con nuevos mercados.", "with new markets.")}</em>',
  T("Cotiza aguacate Hass de exportación o abastecimiento nacional. Cuéntanos tu destino, volumen y calibres y te respondemos con una propuesta a la medida.", "Request a quote for export Hass avocados or national distribution. Tell us your destination, volume and sizes and we will reply with a tailored proposal."),
  '<img src="assets/imgs/escenas/crate-hero.webp" alt="" fetchpriority="high" />')}
    <section class="section contact-layout">
      <div>
        <p class="eyebrow reveal">{T("Canales directos", "Direct channels")}</p>
        <h2 class="h-section contact-heading reveal" style="--d:1">{T("Una conversación", "Every partnership")} <em>{T("abre el camino.", "starts with a chat.")}</em></h2>
        <div class="channel-list">
          <a class="channel is-whatsapp reveal" href="https://wa.me/{WA}" data-whatsapp-link target="_blank" rel="noopener">{icon("whatsapp-logo")}<div><small>{T("WhatsApp comercial", "Sales WhatsApp")}</small><strong>{WA_DISPLAY}</strong></div>{ARROW}</a>
          <a class="channel reveal" href="mailto:{EMAIL}">{icon("envelope-simple")}<div><small>{T("Correo", "Email")}</small><strong>{EMAIL}</strong></div>{ARROW}</a>
          <a class="channel reveal" style="--d:1" href="{IG}" target="_blank" rel="noopener">{icon("instagram-logo")}<div><small>Instagram</small><strong>@agrocolombiacompany</strong></div>{ARROW}</a>
          <a class="channel reveal" style="--d:2" href="{FB}" target="_blank" rel="noopener">{icon("facebook-logo")}<div><small>Facebook</small><strong>Agro Colombia Company</strong></div>{ARROW}</a>

          <div class="channel reveal" style="--d:3">{icon("map-pin")}<div><small>{T("Operación comercial", "Commercial operation")}</small><strong>{T("Corabastos, Bogotá D. C.", "Corabastos, Bogotá D. C.")}</strong></div></div>
          <div class="channel reveal" style="--d:4">{icon("plant")}<div><small>{T("Origen", "Origin")}</small><strong>{T("Sonsón, Antioquia", "Sonsón, Antioquia")}</strong></div></div>
          <div class="channel reveal" style="--d:5">{icon("buildings")}<div><small>{T("Razón social", "Legal name")}</small><strong>{LEGAL_NAME} · NIT {NIT}</strong></div></div>
        </div>
      </div>
      <form class="contact-form on-dark reveal" style="--d:1" data-contact-form novalidate>
        {form}
        <div class="form-foot"><small>{T("Al enviar aceptas nuestra", "By sending you accept our")} <a href="privacidad.html">{T("política de privacidad", "privacy policy")}</a>.</small><div class="form-actions"><button class="button button-whatsapp" type="submit" data-send="whatsapp">{icon("whatsapp-logo")} {T("Enviar por WhatsApp", "Send via WhatsApp")}</button><button class="button button-ghost" type="submit" data-send="email">{icon("envelope-simple")} {T("Enviar por correo", "Send by email")}</button></div></div>
        <p class="form-status" role="status" aria-live="polite"></p>
      </form>
    </section>
    <section class="section section-alt" id="proceso">
      <div class="section-head"><div><p class="eyebrow reveal">{T("Proceso de abastecimiento nacional", "National supply process")}</p><h2 class="h-section reveal" style="--d:1">{T("Del pedido", "From order")} <em>{T("a tu operación.", "to your operation.")}</em></h2></div>
      <p class="reveal" style="--d:2">{T("Te acompañamos en cada paso, desde el campo hasta tu negocio.", "We are with you at every step, from the farm to your business.")}</p></div>
      <ol class="steps">{step_cards}</ol>
    </section>
  </main>
'''
    return (head('Contacto | Agro Colombia Company', 'Contact | Agro Colombia Company',
                 'Cotiza aguacate Hass colombiano de exportación o abastecimiento nacional de frutas, hortalizas y tubérculos.',
                 'Request a quote for Colombian export Hass avocados or national supply of fruit, vegetables and tubers.',
                 'contacto.html', 'assets/imgs/escenas/crate-hero.webp') + header('contacto.html') + body + footer())

# ---------------------------------------------------------------- PRIVACIDAD
def build_privacidad():
    body = f'''<main id="contenido">
    <section class="page-hero on-dark" style="min-height:auto">
      <nav class="breadcrumb" aria-label="{T("Ruta", "Breadcrumb")}"><a href="index.html">{T("Inicio", "Home")}</a><span aria-hidden="true">/</span><span>{T("Privacidad", "Privacy")}</span></nav>
      <p class="eyebrow">{T("Información legal", "Legal information")}</p>
      <h1>{T("Privacidad y", "Privacy and")} <em>{T("términos de uso.", "terms of use.")}</em></h1>
    </section>
    <section class="section">
      <div class="legal-content">
        <h2>Política de tratamiento de datos personales</h2>
        <p>{LEGAL_NAME}, identificada con NIT {NIT} y domicilio en Bogotá D. C., Colombia, es responsable del tratamiento de los datos personales que nos compartes a través de este sitio, conforme a la Ley 1581 de 2012 y sus decretos reglamentarios.</p>
        <p>Este sitio no guarda en servidores la información del formulario de contacto. Al enviarlo se abre WhatsApp o tu aplicación de correo con el mensaje preparado y solo recibimos los datos que decidas enviarnos: nombre, empresa, correo, teléfono, ciudad y detalles de tu solicitud.</p>
        <h2>Finalidad</h2>
        <ul><li>Responder tus consultas y preparar cotizaciones.</li><li>Coordinar pedidos, entregas y pagos.</li><li>Enviarte información comercial cuando lo hayas autorizado.</li></ul>
        <h2>Tus derechos</h2>
        <p>Puedes conocer, actualizar, rectificar y solicitar la supresión de tus datos, así como revocar la autorización otorgada, escribiendo a <a href="mailto:{EMAIL}">{EMAIL}</a>. También puedes presentar quejas ante la Superintendencia de Industria y Comercio.</p>
        <h2>Almacenamiento local y servicios de terceros</h2>
        <p>Guardamos en tu navegador solo tus preferencias de idioma y tema. El sitio carga tipografías de Google Fonts y mapas de OpenStreetMap, servicios que pueden registrar tu dirección IP según sus propias políticas.</p>
        <h2 id="terminos">Términos de uso</h2>
        <p>La información de productos, disponibilidad, calibres, presentaciones, precios y cobertura es de referencia y se confirma en cada cotización. Las imágenes son ilustrativas.</p>
        <p>Los contenidos, la marca y el material gráfico de Agro Colombia Company no pueden reproducirse sin autorización. Algunos videos y fotografías provienen de bancos de imágenes de uso libre. Los logotipos de Rainforest Alliance, GLOBALG.A.P. e ICA pertenecen a sus respectivas organizaciones y se muestran para identificar las certificaciones y registros de la empresa.</p>
        <p class="legal-updated muted">Última actualización: octubre de 2026.</p>
      </div>
    </section>
  </main>
'''
    return (head('Privacidad y términos | Agro Colombia Company', 'Privacy and terms | Agro Colombia Company',
                 'Política de tratamiento de datos personales y términos de uso del sitio de Agro Colombia Company.',
                 'Personal data policy and terms of use for the Agro Colombia Company website.', 'privacidad.html') +
            header('') + body + footer())

def build_404():
    body = f'''<main id="contenido">
    <section class="page-hero on-dark not-found">
      <img src="assets/imgs/origen/paisaje-sonson.jpeg" alt="" />
      <span class="not-found-code">404</span>
      <h1>{T("Esta página", "This page")} <em>{T("no se cultivó aquí.", "was not grown here.")}</em></h1>
      <p class="lead">{T("La dirección que buscas no existe o cambió. Vuelve al inicio o explora nuestro portafolio.", "The address you are looking for does not exist or has moved. Go back home or browse our portfolio.")}</p>
      <div class="hero-links"><a class="button button-gold" href="index.html">{T("Volver al inicio", "Back to home")} {ARROW}</a><a class="text-link" href="servicios.html">{T("Ver portafolio", "See our portfolio")} {icon("arrow-right")}</a></div>
    </section>
  </main>
'''
    return (head('Página no encontrada | Agro Colombia Company', 'Page not found | Agro Colombia Company',
                 'La página que buscas no existe.', 'The page you are looking for does not exist.', '404.html') + header('') + body + footer())

pages = {'index.html': build_index, 'nosotros.html': build_nosotros, 'servicios.html': build_productos,
         'contacto.html': build_contacto, 'privacidad.html': build_privacidad, '404.html': build_404}
for name, fn in pages.items():
    (ROOT / name).write_text(fn(), encoding='utf-8')

# Textos que solo usa site.js
for es, en in [
    ('Cerrar menú', 'Close menu'), ('Cambiar a tema claro', 'Switch to light theme'), ('Cambiar a tema oscuro', 'Switch to dark theme'),
    ('No se pudo cargar el mapa. Recarga la página para intentarlo de nuevo.', 'The map could not be loaded. Reload the page to try again.'),
    ('Consulta con nuestro equipo la disponibilidad y los destinos vigentes.', 'Ask our team about current availability and destinations.'),
    ('Nuestro origen: aquí cultivamos el aguacate Hass en Sonsón.', 'Our origin: we grow Hass avocados here in Sonsón.'),
    ('Nuestra operación comercial en Corabastos atiende desde aquí.', 'Our commercial operation at Corabastos serves clients from here.'),
    ('Amazonía', 'Amazon'), ('Andina', 'Andean'), ('Caribe', 'Caribbean'), ('Insular', 'Insular'), ('Orinoquía', 'Orinoquía'), ('Pacífica', 'Pacific'),
    ('Este campo es obligatorio.', 'This field is required.'), ('Escribe un correo válido, por ejemplo nombre@empresa.com.', 'Enter a valid email, for example name@company.com.'),
    ('Revisa los campos marcados antes de continuar.', 'Check the highlighted fields and try again.'),
    ('Abrimos tu aplicación de correo con la consulta lista para enviar.', 'We opened your email app with the inquiry ready to send.'),
    ('Hola, Agro Colombia Company. Quisiera información y una cotización de sus productos.', 'Hello, Agro Colombia Company. I would like information and a quote for your products.'),
    ('Mostrando {n} referencias', 'Showing {n} products'), ('Abrimos WhatsApp con tu consulta lista para enviar.', 'We opened WhatsApp with your inquiry ready to send.'), ('Desactivar sonido', 'Turn sound off'), ('Reproducir video', 'Play video'), ('Consulta desde la web', 'Website inquiry'),
    ('Hola, quisiera información sobre sus productos.', 'Hello, I would like information about your products.')]:
    T(es, en)

(ROOT / 'assets/js/i18n.js').write_text(
    '/* Generado: diccionario español → inglés del sitio. */\nwindow.ACC_I18N = ' +
    json.dumps(DICT, ensure_ascii=False, indent=0) + ';\n', encoding='utf-8')
print('ok', len(DICT), 'textos;', {k: v for k, v in COUNTS.items()}, 'total', TOTAL)
