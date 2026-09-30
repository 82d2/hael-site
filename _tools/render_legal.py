"""Render the policy pages from 82d2/hael-legal into this site.

hael-legal is the source of truth for privacy, terms, and consumer health
data text. Edit the Markdown there, then run from this repo's root:

    python3 _tools/render_legal.py ../hael-legal

It replaces the content between <p class="updated"> and <footer> in
privacy/, terms/, and consumer-health-data/ index.html, keeping each
page's head and styles. Headings are lowercased to match the site.
(Jekyll skips folders starting with "_", so this isn't published.)
"""
import os
import re,html,sys
def inline(t):
    t=html.escape(t,quote=False)
    t=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',t)
    t=re.sub(r'`(.+?)`',r'<code>\1</code>',t)
    links={'telemetrydeck.com/privacy':'https://telemetrydeck.com/privacy','revenuecat.com/privacy':'https://revenuecat.com/privacy',
      'apple.com/legal/internet-services/itunes/dev/stdeula':'https://www.apple.com/legal/internet-services/itunes/dev/stdeula/',
      'hael.app/consumer-health-data':'/consumer-health-data','hael.app/privacy':'/privacy','atg.wa.gov/file-complaint':'https://www.atg.wa.gov/file-complaint'}
    for k,v in links.items():
        t=re.sub(r'(?<![/\w.])'+re.escape(k)+r'(?![\w/-])',f'<a href="{v}">{k}</a>',t)
    t=re.sub(r'\bhello@hael\.app\b','<a href="mailto:hello@hael.app">hello@hael.app</a>',t)
    return t
def render(mdpath,htmlpath):
    md=open(mdpath,encoding='utf-8').read().split('\n'); out=[];inlist=False;updated=''
    for line in md:
        if line.startswith('# ') or line.strip()=='---': continue
        if line.startswith('**hæl** — last updated'): updated=line.split('last updated ')[1]; continue
        if line.startswith('- '):
            if not inlist: out.append('        <ul>'); inlist=True
            out.append(f'            <li>{inline(line[2:])}</li>'); continue
        if inlist: out.append('        </ul>'); inlist=False
        if line.startswith('## '): out+=['',f'        <h2>{inline(line[3:].lower())}</h2>']
        elif line.strip(): out.append(f'        <p>{inline(line)}</p>')
    if inlist: out.append('        </ul>')
    s=open(htmlpath,encoding='utf-8').read(); a=s.index('        <p class="updated">'); b=s.index('        <footer>')
    open(htmlpath,'w',encoding='utf-8').write(s[:a]+f'        <p class="updated">last updated {updated}</p>\n\n'+'\n'.join(out).strip('\n')+'\n\n'+s[b:])
legal=os.path.abspath(sys.argv[1] if len(sys.argv)>1 else '../hael-legal')
site=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
for name,page in [('privacy','privacy'),('terms','terms'),('consumer-health-data','consumer-health-data')]:
    render(os.path.join(legal,name+'.md'),os.path.join(site,page,'index.html'))
