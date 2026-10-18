"""Builds 404.html in the shared frame. Run: python3 _tools/build_404.py
(Jekyll skips folders starting with "_", so this isn't published.)"""
import pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import shell

head = shell.head(title="page not found · hæl", description="this page isn't written. hæl is a cycle-aware intermittent fasting timer for iPhone.",
                  path="/404.html").replace('<link rel="canonical" href="https://hael.app/404.html">', '<meta name="robots" content="noindex">')
body = f"""{shell.title_block('page not found', 'a blank page.', 'nothing is written here.')}
{shell.closing()}
{shell.more([('/', '← hæl, the fasting timer'), ('/weight-gain-before-period/', 'why weight goes up before a period'), ('/intermittent-fasting-menstrual-cycle/', 'fasting and the cycle')])}"""
(pathlib.Path(__file__).resolve().parent.parent / "404.html").write_text(shell.page(head_html=head, body=body, current=None), encoding="utf-8")
print("built 404.html")
