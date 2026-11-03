"""Builds /press/: what has been written about hæl, labelled as what it is,
and what a writer needs (a description, the icon, a contact). Shares the
notes' frame (shell.py). Run: python3 _tools/build_press.py

A piece made with hæl is labelled a collaboration, in its own words; only
independent coverage would go in unlabelled. Quotes are verbatim and only
of lines that describe the app accurately."""
import pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import shell

ROOT = pathlib.Path(__file__).resolve().parent.parent

COVERAGE = [
    dict(publication="angels for aid", date="october 27, 2026", label="a collaboration",
         title="the body keeps seasons. so should your practice.",
         url="https://angelsforaid.substack.com/p/the-body-keeps-seasons-so-should",
         quote="It is closer to a journal that happens to keep time than a tracker with opinions on your body."),
]


def item(c):
    return (f'<div class="short"><span>{c["publication"]} · {c["date"]} · {c["label"]}</span>'
            f'<p>“{c["quote"]}”</p></div>\n'
            f'<p><a href="{c["url"]}">{c["title"]}</a>, {c["publication"]}.</p>')


BODY = f"""{shell.title_block("press", "press", "hæl · KI-GEN Studios")}
<article class="text">
<h2>written about hæl</h2>
{"".join(item(c) for c in COVERAGE)}

<h2>about hæl</h2>
<p>hæl is a fasting timer for iPhone, iPad and Apple Watch that observes instead of coaching. it suggests the hours of a fast for each phase of the menstrual cycle, reads weight against the cycle rather than against yesterday, and writes a new page for each stretch of the fast. there is no account, no ads and no server of its own: the record stays on the phone, in the user's own iCloud and in Apple Health.</p>
<p>in one line: a fasting timer that observes instead of coaching.</p>

<h2>for writers</h2>
<ul>
    <li>the icon: <a href="/images/app/icon-day.png">day</a> and <a href="/images/app/icon-night.png">night</a></li>
    <li>the preview image: <a href="/og-image.png">og-image.png</a></li>
    <li>how it works: <a href="/how-to-use-hael/">how to use hæl</a> and <a href="/cycle-syncing-fasting/">cycle syncing in hæl</a></li>
    <li>screenshots, questions, or anything else: <a href="mailto:hello@hael.app">hello@hael.app</a></li>
</ul>
</article>
{shell.closing("hæl is a cycle-aware intermittent fasting timer for iPhone. no account, no ads, nothing asked of you.")}
{shell.more([("/", "← hæl, the fasting timer"), ("/intermittent-fasting-for-beginners/", "intermittent fasting for beginners")])}"""

html = shell.page(
    head_html=shell.head(title="Press | hæl",
                         description="press for hæl, the cycle-aware fasting timer for iPhone: what has been written about it, a short description, the icon, and how to get in touch.",
                         path="/press/"),
    body=BODY, current="/press/")
d = ROOT / "press"; d.mkdir(exist_ok=True)
(d / "index.html").write_text(html, encoding="utf-8")
print("built", d / "index.html")
