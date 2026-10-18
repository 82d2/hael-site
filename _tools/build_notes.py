"""Builds the two sourced notes from the text below into their own folders.
Shared page: the home page's book styling, a running head back home, the
question as the title, the short answer first, sources and a not-medical-
advice line at the foot. Run: python3 _tools/build_notes.py"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
STORE = "https://apps.apple.com/app/id6778956802"
BYLINE = "the maker of hæl"
PUBLISHED = "2026-10-12"
PUBLISHED_TEXT = "october 12, 2026"

STYLE = """
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
:root { --paper:#FDFBF9; --ink:#2E2B2A; --soft:#6E6864; --muted:#8A8480; --rule:#DCD8D2; --rose:#A8737A;
        --button:#2E2B2A; --button-ink:#FDFBF9; --serif: ui-serif, 'New York', 'Newsreader', Georgia, serif; }
@media (prefers-color-scheme: dark) { :root { --paper:#1C1A19; --ink:#EDE7E3; --soft:#B5ADA8; --muted:#8F8783;
        --rule:#3A3634; --rose:#D29EA5; --button:#EDE7E3; --button-ink:#1C1A19; } }
html { background: var(--paper); }
body { font-family: var(--serif); background: var(--paper); color: var(--ink); -webkit-font-smoothing: antialiased;
       text-rendering: optimizeLegibility; font-size: 19px; line-height: 1.6; }
.page { max-width: 680px; margin: 0 auto; padding: 0 24px; }
.head { display: flex; justify-content: space-between; align-items: baseline; padding: 28px 0 12px;
        border-bottom: 1px solid var(--rule); font-style: italic; color: var(--muted); font-size: 17px; }
.head a { color: var(--muted); text-decoration: none; } .head a:hover { color: var(--ink); }
article { padding: 64px 0 24px; }
.kicker { font-style: italic; color: var(--rose); font-size: 17px; }
h1 { margin-top: 10px; font-size: clamp(36px, 6.6vw, 52px); font-weight: 300; line-height: 1.1; letter-spacing: -0.015em; }
.byline { margin-top: 18px; font-style: italic; color: var(--muted); font-size: 16px; }
.short { margin-top: 34px; padding: 22px 0; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule); }
.short span { display: block; font-style: italic; color: var(--muted); font-size: 16px; margin-bottom: 6px; }
.short p { font-size: 21px; font-weight: 300; line-height: 1.5; }
h2 { margin-top: 52px; font-size: clamp(25px, 4.4vw, 31px); font-weight: 300; line-height: 1.2; letter-spacing: -0.01em; }
article p, article li { color: var(--soft); }
article p { margin-top: 16px; }
article ul { margin: 16px 0 0 1.1em; display: grid; gap: 8px; }
article a { color: var(--ink); text-decoration-color: var(--rule); text-underline-offset: 3px; }
article a:hover { text-decoration-color: var(--rose); }
sup a { text-decoration: none; color: var(--rose); font-style: italic; font-size: 14px; padding-left: 1px; }
.aside { margin-top: 52px; padding-top: 22px; border-top: 1px solid var(--rule); }
.aside p:first-child { margin-top: 0; }
.download { display: inline-flex; margin-top: 22px; padding: 13px 26px; border-radius: 999px; background: var(--button);
            color: var(--button-ink) !important; text-decoration: none; font-size: 17px; }
.sources { margin-top: 52px; font-size: 15px; line-height: 1.5; color: var(--muted); }
.sources h2 { font-size: 21px; margin-top: 0; margin-bottom: 12px; }
.sources ol { margin-left: 1.3em; display: grid; gap: 8px; }
.sources li { color: var(--muted); }
.note { margin-top: 32px; font-size: 15px; font-style: italic; color: var(--muted); }
footer { margin-top: 56px; border-top: 1px solid var(--rule); padding: 28px 0 48px; display: flex; flex-wrap: wrap;
         justify-content: space-between; gap: 12px 28px; font-size: 16px; color: var(--muted); }
footer nav { display: flex; flex-wrap: wrap; gap: 10px 26px; }
footer a { color: var(--muted); text-decoration: none; } footer a:hover { color: var(--ink); }
@media (max-width: 520px) { body { font-size: 18px; } article { padding-top: 48px; } }
"""

FOOTER = """<footer>
        <span>&copy; 2026 KI-GEN Studios LLC</span>
        <nav aria-label="Footer">
            <a href="/weight-gain-before-period/">weight before a period</a>
            <a href="/intermittent-fasting-menstrual-cycle/">fasting and the cycle</a>
            <a href="/privacy/">privacy</a>
            <a href="/terms/">terms</a>
            <a href="mailto:hello@hael.app">contact</a>
        </nav>
    </footer>"""

def page(slug, title, description, kicker, h1, short, body, sources, headline):
    url = f"https://hael.app/{slug}/"
    ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "@id": url + "#article",
        "headline": headline,
        "description": description,
        "url": url,
        "mainEntityOfPage": url,
        "datePublished": PUBLISHED,
        "dateModified": PUBLISHED,
        "inLanguage": "en",
        "author": {"@type": "Organization", "@id": "https://hael.app/#org", "name": "KI-GEN Studios LLC"},
        "publisher": {"@type": "Organization", "@id": "https://hael.app/#org", "name": "KI-GEN Studios LLC",
                      "logo": "https://hael.app/icon-192x192.png"},
        "image": "https://hael.app/og-image.png",
        "citation": [s["cite"] for s in sources],
    }
    src = "\n".join(f'                <li id="s{i}">{s["html"]}</li>' for i, s in enumerate(sources, 1))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{url}">
    <meta name="apple-itunes-app" content="app-id=6778956802">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <meta property="og:title" content="{headline}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="https://hael.app/og-image.png">
    <meta property="og:site_name" content="hæl">
    <meta property="article:published_time" content="{PUBLISHED}">
    <meta name="twitter:card" content="summary_large_image">
    <script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=4)}
    </script>
    <link rel="stylesheet" href="/fonts/newsreader.css">
    <style>{STYLE}</style>
</head>
<body>
<div class="page">
    <header class="head"><a href="/">hæl</a><a href="{STORE}">download</a></header>
    <main>
        <article>
            <p class="kicker">{kicker}</p>
            <h1>{h1}</h1>
            <p class="byline">by {BYLINE} · {PUBLISHED_TEXT}</p>
            <div class="short"><span>the short answer</span><p>{short}</p></div>
{body}
            <section class="sources" aria-labelledby="sources">
            <h2 id="sources">sources</h2>
            <ol>
{src}
            </ol>
            </section>
            <p class="note">this page explains what research says; it is not medical advice, and hæl does not diagnose or treat anything. if something about your body worries you, see a doctor.</p>
        </article>
    </main>
    {FOOTER}
</div>
</body>
</html>
"""

def n(i):
    return f'<sup><a href="#s{i}">{i}</a></sup>'

# ---------------------------------------------------------------- the water
WEIGHT_SOURCES = [
    {"cite": "Kanellakis S, et al. Changes in body weight and body composition during the menstrual cycle. American Journal of Human Biology. 2023;35(11):e23951.",
     "html": 'Kanellakis S, et al. <a href="https://doi.org/10.1002/ajhb.23951">Changes in body weight and body composition during the menstrual cycle</a>. <i>American Journal of Human Biology</i>, 2023.'},
    {"cite": "White CP, Hitchcock CL, Vigna YM, Prior JC. Fluid retention over the menstrual cycle: 1-year data from the Prospective Ovulation Cohort. Obstetrics and Gynecology International. 2011;2011:138451.",
     "html": 'White CP, Hitchcock CL, Vigna YM, Prior JC. <a href="https://doi.org/10.1155/2011/138451">Fluid retention over the menstrual cycle: 1-year data from the Prospective Ovulation Cohort</a>. <i>Obstetrics and Gynecology International</i>, 2011.'},
    {"cite": "Benton MJ, Hutchins AM, Dawes JJ. Effect of menstrual cycle on resting metabolism: a systematic review and meta-analysis. PLoS ONE. 2020;15(7):e0236025.",
     "html": 'Benton MJ, Hutchins AM, Dawes JJ. <a href="https://doi.org/10.1371/journal.pone.0236025">Effect of menstrual cycle on resting metabolism: a systematic review and meta-analysis</a>. <i>PLoS ONE</i>, 2020.'},
    {"cite": "Cleveland Clinic. Do you gain weight when on your period?",
     "html": 'Cleveland Clinic. <a href="https://health.clevelandclinic.org/do-you-gain-weight-when-on-your-period">Do you gain weight when on your period?</a>'},
]

WEIGHT_BODY = f"""
            <h2>how much weight do you gain before your period?</h2>
            <p>less than it feels like, on average. a 2023 study that weighed women through a cycle found them about 0.45 kg (one pound) heavier during their period than at a point earlier in the cycle, and the whole difference was water held outside the cells. fat and muscle didn't change.{n(1)}</p>
            <p>an average hides a lot. some women see almost nothing on the scale; others see a few pounds that come and go on the same days every month. your own pattern says more than any study can, which is why it's worth watching across two or three cycles before reading anything into a single morning.</p>

            <h2>why does it happen?</h2>
            <p>the main explanation is water. estrogen and progesterone both affect how the kidneys hold on to salt, and where salt stays, water stays with it. as the hormones shift late in the cycle, many women carry extra fluid, which shows up as bloating, tender breasts, puffy fingers, and a higher number on the scale.{n(4)}</p>
            <p>appetite plays a part too. resting metabolism may run slightly higher in the luteal phase, the two weeks after ovulation, though the effect is small and newer studies find it smaller still.{n(3)} many women notice more hunger in those days, and a fuller gut also weighs something.</p>

            <h2>when does it peak, and when does it go?</h2>
            <p>later than most people think. a year-long study of 62 women and 765 cycles found that fluid retention climbed through the second half of the cycle and peaked on the first day of the period, not in the days before it. it was lowest in the middle of the follicular phase, roughly a week after the period ends.{n(2)}</p>
            <p>so the number often keeps rising for a day or two after bleeding starts, and settles over the following week. if you weigh yourself on day one of your period, you are likely weighing yourself at the wettest point of the month.</p>

            <h2>is it fat?</h2>
            <p>no. putting on a pound of fat takes days of eating well beyond what the body uses. a pound that appears over three days and leaves over five is water. in the 2023 study, body fat stayed flat across the cycle while the water came and went.{n(1)}</p>

            <h2>what about birth control, or no period?</h2>
            <p>hormonal birth control that stops ovulation flattens the natural rise and fall of estrogen and progesterone, so the pattern may be smaller, different, or tied to the pill-free week instead. not every study finds a cycle effect even in women with natural cycles. if you don't have a cycle, or it isn't regular, comparing a morning with the same point last month is fairer than comparing it with yesterday.</p>

            <h2>how to read the scale across a cycle</h2>
            <ul>
                <li>weigh at the same time, ideally in the morning before eating, so the only thing changing is you.</li>
                <li>compare a morning with the same day of your last cycle, not with yesterday. day 24 against day 24 tells you something; day 24 against day 10 mostly tells you about water.</li>
                <li>look at the trend over weeks. a single morning is noise.</li>
                <li>expect the highest number around the first day of your period and the lowest about a week after it ends.</li>
            </ul>
            <p>swelling that comes on suddenly, swelling in only one leg, or swelling with breathlessness or chest pain is not cycle water. see a doctor, urgently for the last two.</p>

            <div class="aside">
                <p>this is what the body ledger in hæl is built on. it learns where your body carries water across the cycle and reads each morning against that, with last cycle beside it for comparison. it doesn't call a luteal morning a setback, because it isn't one.</p>
                <a class="download" href="{STORE}">hæl on the App Store</a>
            </div>
"""

# ---------------------------------------------------------------- the cycle
FAST_SOURCES = [
    {"cite": "Cienfuegos S, Corapi S, Gabel K, et al. Effect of intermittent fasting on reproductive hormone levels in females and males: a review of human trials. Nutrients. 2022;14(11):2343.",
     "html": 'Cienfuegos S, et al. <a href="https://doi.org/10.3390/nu14112343">Effect of intermittent fasting on reproductive hormone levels in females and males: a review of human trials</a>. <i>Nutrients</i>, 2022.'},
    {"cite": "Kalam F, Akasheh RT, Cienfuegos S, et al. Effect of time-restricted eating on sex hormone levels in premenopausal and postmenopausal females. Obesity. 2023;31(Suppl 1):57-62.",
     "html": 'Kalam F, et al. <a href="https://pubmed.ncbi.nlm.nih.gov/?term=Kalam+time-restricted+eating+sex+hormone+premenopausal+postmenopausal">Effect of time-restricted eating on sex hormone levels in premenopausal and postmenopausal females</a>. <i>Obesity</i>, 2023.'},
    {"cite": "Gordon CM, Ackerman KE, Berga SL, et al. Functional hypothalamic amenorrhea: an Endocrine Society clinical practice guideline. Journal of Clinical Endocrinology and Metabolism. 2017;102(5):1413-1439.",
     "html": 'Gordon CM, et al. <a href="https://www.endocrine.org/guidelines-and-clinical-practice/clinical-practice-guidelines/hypothalamic-amenorrhea">Functional hypothalamic amenorrhea: an Endocrine Society clinical practice guideline</a>. <i>Journal of Clinical Endocrinology and Metabolism</i>, 2017.'},
    {"cite": "Benton MJ, Hutchins AM, Dawes JJ. Effect of menstrual cycle on resting metabolism: a systematic review and meta-analysis. PLoS ONE. 2020;15(7):e0236025.",
     "html": 'Benton MJ, Hutchins AM, Dawes JJ. <a href="https://doi.org/10.1371/journal.pone.0236025">Effect of menstrual cycle on resting metabolism: a systematic review and meta-analysis</a>. <i>PLoS ONE</i>, 2020.'},
]

FAST_BODY = f"""
            <h2>does intermittent fasting affect your period?</h2>
            <p>in the trials so far, mostly not in the ways people fear. a 2022 review of human studies found that fasting didn't clearly change estrogen or the pituitary hormones that drive ovulation. androgens such as testosterone fell in premenopausal women with obesity, which may help in polycystic ovary syndrome.{n(1)} in an eight-week trial of eating within four to six hours a day, most sex hormones held steady; DHEA, an adrenal hormone, fell by about a seventh and stayed within the normal range.{n(2)}</p>
            <p>the honest caveat is how thin this is. the trials are small, short, and mostly in women with obesity. almost none followed lean women with regular cycles through several months, and none tested fasting timed to the phases of the cycle.</p>

            <h2>can fasting stop your period?</h2>
            <p>yes, if it adds up to too little food. the body treats a long shortfall of energy, especially with heavy exercise, stress, or weight loss, as a reason to pause ovulation. doctors call this functional hypothalamic amenorrhea.{n(3)} the risk comes from eating too little overall, not from the clock: a fast followed by enough food is a different thing from a fast that becomes a way of eating less and less.</p>
            <p>a missed period, cycles getting much longer, or bleeding stopping for three months or more is a reason to stop fasting and see a doctor. so is a fast that starts to feel like something you can't stop.</p>

            <h2>can you fast during your period?</h2>
            <p>there's no evidence that a fast is harmful during a period for a healthy woman. what changes is how it feels. cramps, low energy, and poor sleep make any fast harder, and a heavy period is a good reason to eat enough iron. a shorter fast, or none, on the first heavy days is a reasonable choice; so is your usual one, if it feels fine.</p>

            <h2>should you fast less in the luteal phase?</h2>
            <p>this is the core of "cycle syncing", and no trial has tested it. what is known: resting metabolism may rise a little after ovulation, though newer studies find the effect small,{n(4)} and many women feel hungrier and less patient in the week before a period. a long fast in those days is likely to feel harder.</p>
            <p>so shortening a fast in the late luteal phase is a sensible way to keep the practice easy to live with. it isn't a medical rule, and anyone selling it as one, in either direction, is overstating the evidence.</p>

            <h2>what is cycle syncing, for fasting?</h2>
            <p>it means matching the length of a fast to the phase of the cycle: longer in the follicular phase, between the period and ovulation, when many women find fasting easier; shorter in the days before a period. it is a practical idea built on how the cycle feels, not on proven hormonal effects. treat it as a way to listen, not a prescription.</p>

            <h2>is intermittent fasting safe for women?</h2>
            <p>for most healthy adult women, shorter daily fasts such as 12 to 16 hours appear to be well tolerated in studies so far. some women should not fast without a doctor's advice:</p>
            <ul>
                <li>during pregnancy or breastfeeding, or while trying to conceive</li>
                <li>with a current or past eating disorder</li>
                <li>with diabetes, or on medicines that lower blood sugar</li>
                <li>under 18</li>
                <li>with a missed or irregular period that hasn't been looked into</li>
            </ul>

            <h2>does any of this apply on birth control?</h2>
            <p>hormonal birth control that stops ovulation also flattens the phases, so there is no luteal phase to time a fast around. fasting by the hours alone, and by how you feel, makes more sense than following a cycle chart.</p>

            <div class="aside">
                <p>hæl takes this approach. connect Apple Health or enter your last period, and it suggests the hours of a fast for the phase you are in, shorter late in the cycle, longer after it. it suggests; it doesn't insist, and if a cycle doesn't apply to you, it keeps the hours alone. it also stops at forty-eight hours to say a longer fast needs a doctor.</p>
                <a class="download" href="{STORE}">hæl on the App Store</a>
            </div>
"""

NOTES = [
    dict(slug="weight-gain-before-period",
         title="Why Does Weight Go Up Before Your Period? | hæl",
         description="weight often rises a pound or so before a period, and it is water, not fat. what studies show: how much, why, when it peaks, and how to read the scale.",
         kicker="the water",
         h1="why does weight go up before a period?",
         headline="Why does weight go up before a period?",
         short="it is mostly water. hormones late in the cycle make the body hold extra fluid, adding about a pound on average, sometimes more. it peaks around the first day of the period and is gone about a week later. it isn't fat, and it isn't a setback.",
         body=WEIGHT_BODY, sources=WEIGHT_SOURCES),
    dict(slug="intermittent-fasting-menstrual-cycle",
         title="Intermittent Fasting and the Menstrual Cycle | hæl",
         description="does intermittent fasting affect your period? can you fast on your period or in the luteal phase? honest answers, with what the research does and doesn't show.",
         kicker="the cycle",
         h1="intermittent fasting and the menstrual cycle",
         headline="Intermittent fasting and the menstrual cycle: what the evidence shows",
         short="small trials of daily fasting in women have mostly not found harm to reproductive hormones, but they are short and few. the real risk to the cycle is eating too little overall, which can stop periods. shorter fasts late in the cycle are a sensible choice; no study proves they're required.",
         body=FAST_BODY, sources=FAST_SOURCES),
]

for note in NOTES:
    d = ROOT / note["slug"]; d.mkdir(exist_ok=True)
    (d / "index.html").write_text(page(**note), encoding="utf-8")
    print("built", d / "index.html")
