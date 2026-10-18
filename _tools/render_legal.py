"""Render the policy pages from 82d2/hael-legal into this site.

hael-legal is the source of truth for privacy, terms, and consumer health
data text. Edit the Markdown there and merge it to main, then run from this
repo's root:

    python3 _tools/render_legal.py ../hael-legal

The text is always read from hael-legal's main branch (through git, whatever
branch the checkout is on), so wording waiting on a branch for a release
can't reach the site early. Each page is written whole, in the shared frame
from shell.py. Headings are lowercased to match the site.
(Jekyll skips folders starting with "_", so this isn't published.)
"""
import os, re, html, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shell

PAGES = [
    dict(name="privacy", h1="privacy policy", title="Privacy Policy | hæl",
         description="how hæl handles your data: no account, no server of ours, no advertising. what stays on your phone and in iCloud, and the anonymous counts kept."),
    dict(name="terms", h1="terms of use", title="Terms of Use | hæl",
         description="the terms of use for hæl, a cycle-aware intermittent fasting app for iPhone: the free timer, the one-time full witness, and what the app is not."),
    dict(name="consumer-health-data", h1="consumer health data", title="Consumer Health Data Privacy Policy | hæl",
         description="how hæl handles consumer health data under Washington, Nevada, and Connecticut law."),
]

LINKS = {'telemetrydeck.com/privacy': 'https://telemetrydeck.com/privacy', 'revenuecat.com/privacy': 'https://revenuecat.com/privacy',
         'apple.com/legal/internet-services/itunes/dev/stdeula': 'https://www.apple.com/legal/internet-services/itunes/dev/stdeula/',
         'hael.app/consumer-health-data': '/consumer-health-data/', 'hael.app/privacy': '/privacy/', 'atg.wa.gov/file-complaint': 'https://www.atg.wa.gov/file-complaint'}


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'`(.+?)`', r'<code>\1</code>', t)
    for k, v in LINKS.items():
        t = re.sub(r'(?<![/\w.])' + re.escape(k) + r'(?![\w/-])', f'<a href="{v}">{k}</a>', t)
    t = re.sub(r'\bhello@hael\.app\b', '<a href="mailto:hello@hael.app">hello@hael.app</a>', t)
    return t


def markdown(md):
    """The policy Markdown as HTML, and its 'last updated' date."""
    out, inlist, updated = [], False, ''
    for line in md.split('\n'):
        if line.startswith('# ') or line.strip() == '---':
            continue
        if line.startswith('**hæl** — last updated'):
            updated = line.split('last updated ')[1].strip()
            continue
        if line.startswith('- '):
            if not inlist:
                out.append('<ul>'); inlist = True
            out.append(f'  <li>{inline(line[2:])}</li>'); continue
        if inlist:
            out.append('</ul>'); inlist = False
        if line.startswith('## '):
            out += ['', f'<h2>{inline(line[3:].lower())}</h2>']
        elif line.strip():
            out.append(f'<p>{inline(line)}</p>')
    if inlist:
        out.append('</ul>')
    if not updated:
        raise SystemExit('no "last updated" line found')
    return '\n'.join(out).strip('\n'), updated


def from_main(legal, name):
    try:
        return subprocess.run(['git', '-C', legal, 'show', f'main:{name}.md'], check=True,
                              capture_output=True, text=True).stdout
    except subprocess.CalledProcessError as e:
        raise SystemExit(f'could not read {name}.md from hael-legal main: {e.stderr.strip()}')


def render(legal, site, p):
    text, updated = markdown(from_main(legal, p['name']))
    path = f"/{p['name']}/"
    body = f"""{shell.title_block('legal', p['h1'], f'last updated {updated}')}
<div class="text">
{text}
</div>
{shell.closing()}
{shell.more([('/', '← hæl, the fasting timer')])}"""
    out = shell.page(head_html=shell.head(title=p['title'], description=p['description'], path=path),
                     body=body, current=path)
    open(os.path.join(site, p['name'], 'index.html'), 'w', encoding='utf-8').write(out)
    print('rendered', p['name'], 'from main, last updated', updated)


if __name__ == '__main__':
    legal = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '../hael-legal')
    site = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    commit = subprocess.run(['git', '-C', legal, 'log', '-1', '--format=%h %s', 'main'], capture_output=True, text=True).stdout.strip()
    print('hael-legal main:', commit)
    for p in PAGES:
        render(legal, site, p)
