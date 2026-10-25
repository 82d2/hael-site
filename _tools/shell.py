"""The frame every page but the home page shares: the head, the menu bar,
the title block, the reading column, the closing line with the App Store
badge, and the footer. build_notes.py and render_legal.py both use it, so
the notes, the policy pages and the 404 page look like the home page and
like each other. (Jekyll skips folders starting with "_", so this isn't
published.)"""

STORE = "https://apps.apple.com/app/id6778956802"
SITE = "https://hael.app"
# App Store campaign links: pt is KI-GEN's provider token, ct names where the tap came from
CAMPAIGN = {"/weight-gain-before-period/": "article-water", "/intermittent-fasting-menstrual-cycle/": "article-cycle", None: "site-404"}
def store_link(current):
    ct = CAMPAIGN.get(current, "site-legal")
    return f"https://apps.apple.com/app/apple-store/id6778956802?pt=129001731&amp;ct={ct}&amp;mt=8"

CSS = """*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{--paper:#FBF7EE;--band:#F4EDE0;--ink:#2F2A27;--soft:#5F5853;--muted:#6E6965;--rule:#DED5C7;--rose:#925B62;--serif:ui-serif,'New York','Newsreader',Georgia,serif}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--paper:#1E1B19;--band:#26221F;--ink:#ECE4DC;--soft:#BDB3AB;--muted:#9C928B;--rule:#3B3531;--rose:#D29EA5}}
html{background:var(--paper)}
body{font-family:var(--serif);background:var(--paper);color:var(--ink);-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;font-size:19px;line-height:1.6}
a{color:inherit}
.wrap{max-width:980px;margin:0 auto;padding:0 24px}
.label{display:inline-flex;align-items:center;gap:8px;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--soft)}
.enso{width:13px;height:13px;flex:none;color:var(--rose)}
nav.top{position:sticky;top:0;z-index:10;background:color-mix(in srgb,var(--paper) 82%,transparent);backdrop-filter:saturate(1.4) blur(18px);-webkit-backdrop-filter:saturate(1.4) blur(18px);border-bottom:1px solid var(--rule)}
nav.top .wrap{display:flex;align-items:center;gap:26px;height:52px}
nav.top .mark{font-size:19px;color:var(--ink);text-decoration:none;margin-right:auto}
nav.top a.link{font-size:14px;font-style:italic;color:var(--soft);text-decoration:none}
nav.top a.link:hover{color:var(--ink)}
.bracket{font-size:12px;letter-spacing:.16em;text-transform:uppercase;text-decoration:none;white-space:nowrap}
.bracket::before{content:"[\\2009\\2009"}.bracket::after{content:"\\2009\\2009]"}
.title{text-align:center;padding:88px 0 0}
.title h1{font-size:clamp(40px,6.4vw,68px);font-weight:300;line-height:1.06;letter-spacing:-.015em;margin:18px auto 0;max-width:15em;text-wrap:balance}
.title .meta{margin-top:18px;font-size:16px;font-style:italic;color:var(--muted)}
.text{max-width:640px;margin:64px auto 0;padding:0 24px}
.text h2{font-size:26px;font-weight:300;line-height:1.25;margin:52px 0 0;color:var(--ink)}
.text p,.text li{margin-top:16px;color:var(--soft)}
.text ul,.text ol{padding-left:22px}.text li{margin-top:10px}
.text strong{color:var(--ink);font-weight:500}
.text a{color:var(--rose);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px}.text a:hover{text-decoration-thickness:2px}.appnote{display:grid;grid-template-columns:56px 1fr;gap:16px;align-items:start;margin:28px 0 8px;padding:18px 0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}.appnote .ai{border-radius:13px;display:block}.appnote p{margin:0;font-size:16px;font-style:italic;color:var(--soft);line-height:1.5}.appnote .ab{display:inline-block;margin-top:12px;text-decoration:none}.appnote .ab img{display:block;height:40px;width:auto}@media (prefers-color-scheme:dark){.appnote .ai{content:url(/images/app/icon-night.png)}}
.text code{font-size:.9em}
.text sup a{font-style:italic;font-size:14px;padding-left:1px}
.short{margin-top:8px;padding:26px 28px;background:var(--band);border-radius:22px}
.short span{display:block;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--soft)}
.short p{margin-top:10px;font-size:21px;font-weight:300;line-height:1.45;color:var(--ink)}
.sources{margin-top:56px;font-size:15px;line-height:1.5}
.sources h2{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--soft);font-weight:400;margin-top:0}
.sources li{color:var(--muted);margin-top:8px}
.text p.note{margin-top:30px;font-size:15px;font-style:italic;color:var(--muted)}
.closing{max-width:640px;margin:64px auto 0;padding:34px 24px 0;border-top:1px solid var(--rule);text-align:center}
.closing p{font-style:italic;color:var(--soft);text-wrap:balance}
.closing img{height:46px;width:auto;margin:22px auto 0;display:block}
.text .closing{margin:56px 0 0;padding:34px 0 30px;border-bottom:1px solid var(--rule)}
.text .closing p{margin-top:0}
.more{max-width:640px;margin:40px auto 0;padding:0 24px 80px;display:flex;flex-wrap:wrap;justify-content:center;gap:10px 28px;font-size:16px;font-style:italic}
.more a{color:var(--rose);text-decoration:none}.more a:hover{text-decoration:underline}
footer{border-top:1px solid var(--rule)}
footer .wrap{padding:22px 24px 40px;display:flex;flex-wrap:wrap;gap:6px 18px;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
footer nav{display:flex;flex-wrap:wrap;gap:6px 18px}footer a{text-decoration:none}footer a:hover,footer a[aria-current]{color:var(--ink)}
footer span{margin-right:auto;letter-spacing:0;text-transform:none;font-style:italic;font-size:14px}
@media (max-width:760px){nav.top a.link{display:none}.title{padding-top:60px}.text{margin-top:44px}}"""

FOOTER_LINKS = [
    ("/weight-gain-before-period/", "weight before a period"),
    ("/intermittent-fasting-menstrual-cycle/", "fasting and the cycle"),
    ("/privacy/", "privacy"),
    ("/terms/", "terms"),
    ("/consumer-health-data/", "health data"),
    ("mailto:hello@hael.app", "contact"),
]

BADGE = (f'<a href="{STORE}"><img src="/images/app-store-badge.svg" width="138" height="46" '
         'alt="Download hæl on the App Store"></a>')

PITCH = "hæl is a cycle-aware intermittent fasting timer for iPhone. no account, no subscription, nothing asked of you."


def head(*, title, description, path, og_type="website", og_title=None, extra=""):
    """Everything inside <head>. `path` is the page's address on the site,
    e.g. "/privacy/"; `extra` is page-specific markup such as structured data."""
    url = SITE + path
    og_title = og_title or title
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url}">
<meta name="apple-itunes-app" content="app-id=6778956802">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:image:alt" content="hæl · a fasting timer that observes instead of coaching.">
<meta property="og:site_name" content="hæl">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE}/og-image.png">{extra}
<!-- New York (the app's serif) on Apple devices; Newsreader, self-hosted, elsewhere -->
<link rel="stylesheet" href="/fonts/newsreader.css">
<style>
{CSS}
</style>"""


NAV = f"""<svg width="0" height="0" style="position:absolute" aria-hidden="true"><symbol id="enso" viewBox="0 0 20 20"><path d="M10 2.2a7.8 7.8 0 1 1-6.9 4.2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></symbol></svg>
<nav class="top" aria-label="Main"><div class="wrap">
  <a class="mark" href="/">hæl</a>
  <a class="link" href="/#hours">the hours</a><a class="link" href="/#water">the water</a><a class="link" href="/#cycle">the cycle</a><a class="link" href="/#questions">questions</a>
  <a class="bracket" href="{STORE}">download</a>
</div></nav>"""


def title_block(label, h1, meta):
    return f"""<header class="title"><div class="wrap">
  <span class="label"><svg class="enso" aria-hidden="true"><use href="#enso"/></svg>{label}</span>
  <h1>{h1}</h1>
  <p class="meta">{meta}</p>
</div></header>"""


def closing(line=PITCH):
    return f"""<div class="closing">
  <p>{line}</p>
  {BADGE}
</div>"""


def more(links):
    """A row of onward links under the closing line."""
    return '<nav class="more" aria-label="Keep reading">' + "".join(f'<a href="{h}">{t}</a>' for h, t in links) + "</nav>"


def footer(current):
    cur = ' aria-current="page"'
    links = "".join(f'<a href="{h}"{cur if h == current else ""}>{t}</a>' for h, t in FOOTER_LINKS)
    return f'<footer><div class="wrap"><span>&copy; 2026 KI-GEN Studios LLC</span><nav aria-label="Footer">{links}</nav></div></footer>'


def page(*, head_html, body, current):
    return _page(head_html=head_html, body=body, current=current).replace(f'href="{STORE}"', f'href="{store_link(current)}"')


def _page(*, head_html, body, current):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{head_html}
</head>
<body>
{NAV}
<main>
{body}
</main>
{footer(current)}
</body>
</html>
"""
