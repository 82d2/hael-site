"""DRAFT, not built or linked: endometriosis and intermittent fasting, what the research shows.
To publish later: move ENDO_SOURCES / ENDO_BODY into _tools/build_notes.py, add
ENDO_APPNOTE to APPNOTES and ENDO_NOTE to NOTES (drop the appnote key before
passing it to page(), which doesn't take it). n() and STORE below mirror
build_notes.py so this file runs on its own. Research notes and what was
verified: _drafts/endometriosis-research.md. Current as of 2026-11-06.
Run `python3 _drafts/endometriosis.py` to run the self-test.

<!--
VISUAL SPECS

1. Explanatory diagram: "where the pain can sit, and where hæl's hours sit"
   Place: after "pain, fatigue and nausea", before "who shouldn't fast".
   Drawn simply: hairline rules, the site's serif, lowercase labels, no
   symptom icons, no faces, no arrows suggesting relief.
   - a horizontal strip of 28 squares, days 1 to 28 of a 28-day cycle, day
     numbers under every seventh square.
   - top row, the phases as hæl counts them for a 28-day cycle (CycleTracker:
     menstruation 1-5, follicular 6-13, ovulation 14-15, luteal 16-28), in
     the app's phase colours (periodRose, follicularGlow, ovulationGold,
     lutealLavender).
   - second row, "hæl's suggested hours" (full witness): 12-14 under
     menstruation, 16-18 under follicular, 16-20 under ovulation, 14-16 under
     luteal. a small open square marked "rest" over day 2, labelled "rest,
     any day you choose".
   - third row, "pain in endometriosis, as the WHO lists it", two bands only,
     no gradient of intensity: a solid band over days 1-5 labelled "severe
     pain during menstruation", and a thin dotted line along all 28 days
     labelled "chronic pelvic pain (pain that does not go away when the
     menstrual cycle ends)". nothing else is drawn: no claim about which days
     hurt most for any one person.
   - one note under the strip, small: "hæl counts the period as days 1 to 5,
     whatever its length. no trial has tested fasting in endometriosis."
   - alt text: "a 28-day cycle strip. hæl suggests 12 to 14 hours on days 1
     to 5 and 14 to 16 in the luteal phase. in endometriosis, pain can come
     with the period and, for some, on any day of the cycle."
   Sources for every label: WHO fact sheet (ENDO_SOURCES 1); app code
   (CycleTracker.swift phase(for:) and typicalHours).

2. App screen: home on day 2 of a cycle, full witness on, after rest has been
   pressed: the ring in the period colour, the line "resting today." and
   "the practice keeps no score against it." under the dial. needs a fresh
   capture from a real build with real data; none of the current screenshots
   shows a rest day or the menstrual phase (ring.png is day 14, ledger.png
   shows follicular days and "1 day in a row"). do not mock it up.
   Caption: "on the hardest days, rest is one press under begin. hæl keeps
   the day as rest, not as a gap."

3. OG image, 1200x630, the site's paper ground and book type:
   line 1 (large): "endometriosis and intermittent fasting"
   line 2 (smaller): "what the research shows, and what it doesn't."
   foot, small: "hæl · hael.app"
-->
"""

STORE = "https://apps.apple.com/app/id6778956802"


def n(i):
    return f'<sup><a href="#s{i}">{i}</a></sup>'


# "verified": "full text" = read in full; "abstract" = PubMed abstract only;
# "full page" = the web page itself; "secondary" = a summary of a page.
# build_notes.page() reads only "html" and "cite", so the extra key is safe.
ENDO_SOURCES = [
    # 1
    {"cite": "World Health Organization. Endometriosis. Fact sheet, 15 October 2025.",
     "html": 'World Health Organization. <a href="https://www.who.int/news-room/fact-sheets/detail/endometriosis">Endometriosis</a>. Fact sheet, 2025.',
     "verified": "full page, read 2026-11-04"},
    # 2
    {"cite": "Nnoaham KE, Hummelshoj L, Webster P, et al. Impact of endometriosis on quality of life and work productivity: a multicenter study across ten countries. Fertility and Sterility. 2011;96(2):366-373.e8.",
     "html": 'Nnoaham KE, et al. <a href="https://doi.org/10.1016/j.fertnstert.2011.05.090">Impact of endometriosis on quality of life and work productivity: a multicenter study across ten countries</a>. <i>Fertility and Sterility</i>, 2011.',
     "verified": "abstract (PMID 21718982)"},
    # 3
    {"cite": "Endometriosis UK. What is endometriosis?",
     "html": 'Endometriosis UK. <a href="https://www.endometriosis-uk.org/what-is-endometriosis">What is endometriosis?</a>',
     "verified": "full page, read 2026-11-04"},
    # 4
    {"cite": "Becker CM, Bokor A, Heikinheimo O, et al. ESHRE guideline: endometriosis. Human Reproduction Open. 2022;2022(2):hoac009.",
     "html": 'Becker CM, et al. <a href="https://doi.org/10.1093/hropen/hoac009">ESHRE guideline: endometriosis</a>. <i>Human Reproduction Open</i>, 2022.',
     "verified": "full text (PMC8951218)"},
    # 5
    {"cite": "National Institute for Health and Care Excellence. Endometriosis: diagnosis and management. NICE guideline NG73. Published 2017, last updated 11 November 2024.",
     "html": 'National Institute for Health and Care Excellence. <a href="https://www.nice.org.uk/guidance/ng73/chapter/Recommendations">Endometriosis: diagnosis and management</a>. NICE guideline NG73, 2017, updated 2024.',
     "verified": "full page (recommendations), read 2026-11-04"},
    # 6
    {"cite": "Missmer SA, Chavarro JE, Malspeis S, et al. A prospective study of dietary fat consumption and endometriosis risk. Human Reproduction. 2010;25(6):1528-1535.",
     "html": 'Missmer SA, et al. <a href="https://doi.org/10.1093/humrep/deq044">A prospective study of dietary fat consumption and endometriosis risk</a>. <i>Human Reproduction</i>, 2010.',
     "verified": "abstract (PMID 20332166)"},
    # 7
    {"cite": "Nirgianakis K, Egger K, Kalaitzopoulos DR, Lanz S, Bally L, Mueller MD. Effectiveness of dietary interventions in the treatment of endometriosis: a systematic review. Reproductive Sciences. 2022;29(1):26-42.",
     "html": 'Nirgianakis K, et al. <a href="https://doi.org/10.1007/s43032-020-00418-w">Effectiveness of dietary interventions in the treatment of endometriosis: a systematic review</a>. <i>Reproductive Sciences</i>, 2022.',
     "verified": "abstract (PMID 33761124)"},
    # 8
    {"cite": "Armour M, Sinclair J, Chalmers KJ, Smith CA. Self-management strategies amongst Australian women with endometriosis: a national online survey. BMC Complementary and Alternative Medicine. 2019;19:17.",
     "html": 'Armour M, et al. <a href="https://doi.org/10.1186/s12906-019-2431-x">Self-management strategies amongst Australian women with endometriosis: a national online survey</a>. <i>BMC Complementary and Alternative Medicine</i>, 2019.',
     "verified": "full text (PMC6332532)"},
    # 9
    {"cite": "Armour M, Middleton A, Lim S, Sinclair J, Varjabedian D, Smith CA. Dietary practices of women with endometriosis: a cross-sectional survey. Journal of Alternative and Complementary Medicine. 2021;27(9):771-777.",
     "html": 'Armour M, et al. <a href="https://doi.org/10.1089/acm.2021.0068">Dietary practices of women with endometriosis: a cross-sectional survey</a>. <i>Journal of Alternative and Complementary Medicine</i>, 2021.',
     "verified": "abstract (PMID 34161144)"},
    # 10
    {"cite": "Moore JS, Gibson PR, Perry RE, Burgell RE. Endometriosis in patients with irritable bowel syndrome: specific symptomatic and demographic profile, and response to the low FODMAP diet. Australian and New Zealand Journal of Obstetrics and Gynaecology. 2017;57(2):201-205.",
     "html": 'Moore JS, et al. <a href="https://doi.org/10.1111/ajo.12594">Endometriosis in patients with irritable bowel syndrome: specific symptomatic and demographic profile, and response to the low FODMAP diet</a>. <i>Australian and New Zealand Journal of Obstetrics and Gynaecology</i>, 2017.',
     "verified": "abstract (PMID 28303579)"},
    # 11
    {"cite": "Varney JE, So D, Gibson PR, et al. Clinical trial: effect of a 28-day low FODMAP diet on gastrointestinal symptoms associated with endometriosis (EndoFOD), a randomised, controlled crossover feeding study. Alimentary Pharmacology and Therapeutics. 2025;61(12):1889-1903.",
     "html": 'Varney JE, et al. <a href="https://doi.org/10.1111/apt.70161">Clinical trial: effect of a 28-day low FODMAP diet on gastrointestinal symptoms associated with endometriosis (EndoFOD)</a>. <i>Alimentary Pharmacology and Therapeutics</i>, 2025.',
     "verified": "full text (PMC12107219)"},
    # 12
    {"cite": "Endometriosis UK. Diet and complementary therapies for endometriosis. Booklet, 2025.",
     "html": 'Endometriosis UK. <a href="https://www.endometriosis-uk.org/sites/default/files/2025-11/Endometriosis-CompTherapy-16pp-v4.pdf">Diet and complementary therapies for endometriosis</a>. Booklet, 2025.',
     "verified": "full text (PDF), read 2026-11-04"},
    # 13
    {"cite": "Endometriosis Australia. Endometriosis and FODMAPs. 27 March 2021.",
     "html": 'Endometriosis Australia. <a href="https://endometriosisaustralia.org/endometriosis-and-fodmaps/">Endometriosis and FODMAPs</a>. 2021.',
     "verified": "secondary (page read through a summarising fetch; direct download blocked)"},
    # 14
    {"cite": "Deepak Kumar K, Appleby-Gunnill B, Maslin K. Nutritional practices and dietetic provision in the endometriosis population, with a focus on functional gut symptoms. Journal of Human Nutrition and Dietetics. 2023;36(4):1529-1538.",
     "html": 'Deepak Kumar K, et al. <a href="https://doi.org/10.1111/jhn.13158">Nutritional practices and dietetic provision in the endometriosis population, with a focus on functional gut symptoms</a>. <i>Journal of Human Nutrition and Dietetics</i>, 2023.',
     "verified": "abstract (PMID 36794746)"},
    # 15
    {"cite": "Vennberg Karlsson J, Patel H, Premberg A. Experiences of health after dietary changes in endometriosis: a qualitative interview study. BMJ Open. 2020;10(2):e032321.",
     "html": 'Vennberg Karlsson J, Patel H, Premberg A. <a href="https://doi.org/10.1136/bmjopen-2019-032321">Experiences of health after dietary changes in endometriosis: a qualitative interview study</a>. <i>BMJ Open</i>, 2020.',
     "verified": "full text (PMC7044830); quotations copied from it"},
    # 16
    {"cite": "Yin B, Liu X, Guo SW. Caloric restriction dramatically stalls lesion growth in mice with induced endometriosis. Reproductive Sciences. 2018;25(7):1024-1036.",
     "html": 'Yin B, Liu X, Guo SW. <a href="https://doi.org/10.1177/1933719118756755">Caloric restriction dramatically stalls lesion growth in mice with induced endometriosis</a>. <i>Reproductive Sciences</i>, 2018.',
     "verified": "abstract (PMID 29439622)"},
    # 17
    {"cite": "Hosseinirad H, An H, Jeong EM, et al. Dietary caloric restriction suppresses endometriosis by inhibiting STAT3/ERK pathways. FASEB Journal. 2026;40(4):e71555.",
     "html": 'Hosseinirad H, et al. <a href="https://doi.org/10.1096/fj.202503269R">Dietary caloric restriction suppresses endometriosis by inhibiting STAT3/ERK pathways</a>. <i>FASEB Journal</i>, 2026.',
     "verified": "abstract (PMID 41665220)"},
    # 18
    {"cite": "Ramin-Wright A, Schwartz ASK, Geraedts K, et al. Fatigue: a symptom in endometriosis. Human Reproduction. 2018;33(8):1459-1465.",
     "html": 'Ramin-Wright A, et al. <a href="https://doi.org/10.1093/humrep/dey115">Fatigue: a symptom in endometriosis</a>. <i>Human Reproduction</i>, 2018.',
     "verified": "abstract (PMID 29947766)"},
    # 19
    {"cite": "NHS. How and when to take ibuprofen (adults).",
     "html": 'NHS. <a href="https://www.nhs.uk/medicines/ibuprofen-for-adults/how-and-when-to-take-ibuprofen/">How and when to take ibuprofen</a>.',
     "verified": "secondary (page read through a summarising fetch)"},
    # 20
    {"cite": "Di Michele S, Camoglio C, Chieppa P, et al. Endometriosis and eating disorders: epidemiology, shared neurobiology, and clinical implications. Archives of Gynecology and Obstetrics. 2026;313(1):58.",
     "html": 'Di Michele S, et al. <a href="https://doi.org/10.1007/s00404-026-08325-2">Endometriosis and eating disorders: epidemiology, shared neurobiology, and clinical implications</a>. <i>Archives of Gynecology and Obstetrics</i>, 2026.',
     "verified": "abstract (PMID 41563503)"},
    # 21
    {"cite": "NHS (Healthy London Partnership). Intermittent fasting. MyHealth London.",
     "html": 'NHS, MyHealth London. <a href="https://www.myhealthlondon.nhs.uk/be-healthier/lose-weight/which-diet-is-right-for-me/intermittent-fasting/">Intermittent fasting</a>.',
     "verified": "secondary (page read through a summarising fetch)"},
    # 22
    {"cite": "Cleveland Clinic. Why intermittent fasting may be less effective for some women. 17 July 2023.",
     "html": 'Cleveland Clinic. <a href="https://health.clevelandclinic.org/intermittent-fasting-for-women">Why intermittent fasting may be less effective for some women</a>. 2023.',
     "verified": "secondary (page read through a summarising fetch)"},
    # 23
    {"cite": "Grajower MM, Horne BD. Clinical management of intermittent fasting in patients with diabetes mellitus. Nutrients. 2019;11(4):873.",
     "html": 'Grajower MM, Horne BD. <a href="https://doi.org/10.3390/nu11040873">Clinical management of intermittent fasting in patients with diabetes mellitus</a>. <i>Nutrients</i>, 2019.',
     "verified": "full text (PMC6521152)"},
]

ENDO_BODY = f"""
            <h2>what is endometriosis?</h2>
            <p>endometriosis is a long-term condition in which tissue like the lining of the womb grows outside it, causing inflammation and scar tissue. the World Health Organization estimates that it affects about 10% of women of reproductive age worldwide, some 190 million. it lists severe period pain, heavy bleeding, chronic pelvic pain that doesn't go away when the period ends, infertility, and bloating and nausea among the symptoms. there is no cure; treatment aims to control symptoms.{n(1)}</p>
            <p>diagnosis is slow. the WHO puts the average wait at between 4 and 12 years.{n(1)} in a study of 1,418 women having laparoscopy in ten countries, the delay from first symptoms to a surgical diagnosis was 6.7 years, mostly in primary care, and women with endometriosis lost on average 10.8 hours of work a week, mainly from working less well while in pain.{n(2)} in the UK, Endometriosis UK gives the average time from a first GP visit to diagnosis as 9 years and 4 months.{n(3)}</p>

            <h2>what do doctors recommend?</h2>
            <p>the European guideline, from ESHRE in 2022, and the UK's NICE guideline agree on the outline.{n(4)}{n(5)}</p>
            <ul>
                <li>pain relief. NICE suggests a short trial, for example three months, of paracetamol or an anti-inflammatory such as ibuprofen, alone or together, as a first step.{n(5)} ESHRE says these may be offered, as a weak recommendation.{n(4)}</li>
                <li>hormonal treatment, such as the combined pill, a progestogen, a hormonal coil or implant, or medicines that pause the cycle. both guidelines recommend it as an option for pain.{n(4)}{n(5)}</li>
                <li>surgery, as one of the options for pain, with NICE asking doctors to be guided by a person's symptoms, priorities and wishes about fertility.{n(4)}{n(5)}</li>
            </ul>
            <p>NICE also advises that keeping a pain and symptom diary can help conversations with a doctor.{n(5)} these are things to talk through with a doctor; nothing on this page replaces them.</p>

            <h2>what do the guidelines say about diet?</h2>
            <p>very little, because the evidence is thin. ESHRE asks doctors to discuss non-medical ways of coping, and then says that no recommendation can be made for any specific one, nutrition included, to reduce pain or improve quality of life, "as the potential benefits and harms are unclear".{n(4)} it suggests a healthy lifestyle and diet in general terms, not as a treatment.{n(4)} NICE makes no recommendation on diet at all; its one non-drug recommendation is that the evidence does not support Chinese medicine or supplements for treating endometriosis.{n(5)} neither guideline mentions fasting.</p>

            <h2>what is known about diet and endometriosis?</h2>
            <p>mostly observational studies, a few small trials, and surveys.</p>
            <ul>
                <li>in the Nurses' Health Study II, which followed women for 12 years, those who ate the most long-chain omega-3 fats were 22% less likely to be diagnosed with endometriosis than those who ate the least, and those who ate the most trans fats were 48% more likely.{n(6)} that is about risk of diagnosis, not about symptoms, and it can't show cause.</li>
                <li>a 2022 systematic review found nine human studies of a dietary change in endometriosis, each testing a different one. most reported a benefit, but all had a moderate or high risk of bias.{n(7)}</li>
                <li>in an Australian survey of 484 women with surgically confirmed endometriosis, 76% used some form of self-management. the commonest were heat, 70%, and rest, 68%; 44% had changed their diet, and they rated it 6.4 out of 10 for pain relief, with no one diet doing better than another.{n(8)} a second paper from the same survey found that cutting gluten, cutting dairy and the low-FODMAP diet were the commonest changes.{n(9)}</li>
            </ul>
            <p>the best-studied diet is low-FODMAP, which cuts certain fermentable carbohydrates for a few weeks and then brings them back one by one. among 160 women with irritable bowel syndrome at a New Zealand clinic, 36% also had endometriosis, and 72% of them reported bowel symptoms more than halved after four weeks on the diet, against 49% of those with IBS alone.{n(10)} in 2025 a randomised crossover trial fed 35 women with endometriosis and gut symptoms a low-FODMAP diet and a control diet for 28 days each: 60% responded to the low-FODMAP diet and 26% to the control. pain in the abdomen, bloating and quality of life improved; tiredness and nausea did not.{n(11)} it is a gut treatment, tested on gut symptoms.</p>
            <p>the charities are careful. Endometriosis UK says there is little high-quality evidence that particular diets help, that low-FODMAP may offer some relief alongside IBS-like symptoms, and that it should be done with a registered dietitian.{n(12)} Endometriosis Australia says the same diet may help those with IBS or IBS-like symptoms, works best short term, and is worth doing with professional support.{n(13)}</p>
            <p>restriction is already common. in a UK survey of 1,385 people with endometriosis, 36.7% were eating a restricted diet, 29.8% had a decreased appetite, and 13.5% had recently lost weight without meaning to.{n(14)}</p>

            <h2>what people with endometriosis have told researchers</h2>
            <p>in a Swedish study, twelve people with endometriosis who had changed their diet were interviewed. most had cut or reduced gluten, dairy or carbohydrates, and they described less pain and more energy; one said a general low-FODMAP diet hadn't helped and changed course. they were recruited from online forums linked to diet, so they speak for people for whom a change seemed to work. one said, in the published translation, "…everybody reacts differently to diet…I think that you need to know your body and sense whether something makes you feel good or bad…". another described raising it with health services: "It’s just like meeting a brick wall, you just get a: ‘Nah, it’s meaningless, just eat what you want’."{n(15)} none of them described fasting.</p>

            <h2>has intermittent fasting been studied in endometriosis?</h2>
            <p>no. as of november 2026, searches of PubMed, Europe PMC and ClinicalTrials.gov found no trial of intermittent fasting, time-restricted eating or meal timing in people with endometriosis, and no registered one. there is no evidence that fasting helps endometriosis, and none that it harms it. there is simply no study.</p>
            <p>the nearest work is in mice, and it isn't fasting. in one study, mice fed 30% fewer calories than mice eating freely grew much smaller endometriosis lesions.{n(16)} in another, mice on a calorie-restricted diet for 90 days weighed 24.5% less and had fewer, lighter lesions.{n(17)} both tested eating less every day, not eating within a window, in animals with endometriosis induced by surgery or injection. they say nothing about what a fast does to pain in a person.</p>

            <h2>pain, fatigue and nausea</h2>
            <p>these are the reasons a fast may not suit some days.</p>
            <ul>
                <li>pain. in endometriosis it often comes with the period, and for some it is there on other days too.{n(1)} on a day of bad pain, a long fast adds a hard thing to a hard day.</li>
                <li>fatigue. in a study of 560 women with endometriosis and 560 without, frequent fatigue was reported by 50.7% of those with it and 22.4% of those without; it went with insomnia, depression and pain.{n(18)} in the UK survey, tiredness was the commonest symptom, reported by 85.5%, ahead of bloating, 75.3%, and abdominal pain, 67.3%.{n(14)}</li>
                <li>nausea. the WHO lists it among the symptoms.{n(1)} in the Australian survey, some who changed their diet reported less nausea and vomiting,{n(9)} but in the low-FODMAP trial nausea didn't improve.{n(11)}</li>
                <li>pain relief. the NHS advises taking ibuprofen with or after food, and lists indigestion and stomach ulcers among its side effects.{n(19)} if you take an anti-inflammatory on painful days, a fast that leaves you taking it on an empty stomach is worth asking a pharmacist about.</li>
            </ul>
            <p>rest, in the Australian survey, meant physical rest, and women rated it 5.3 out of 10 for pain.{n(8)} it is not the same as a day without a fast, and no study has measured that.</p>

            <figure class="fig" style="margin:2em 0"><div style="overflow-x:auto;-webkit-overflow-scrolling:touch"><svg viewBox="0 0 620 196" role="img" aria-labelledby="fig-endo-t" style="width:100%;min-width:600px;height:auto;font-family:var(--serif)"><title id="fig-endo-t">a 28-day cycle strip. hæl suggests 12 to 14 hours on days 1 to 5 and 14 to 16 in the luteal phase. in endometriosis, pain can come with the period and, for some, on any day of the cycle.</title><rect x="118" y="24" width="16" height="16" rx="2" fill="#D6A9A9"/><rect x="136" y="24" width="16" height="16" rx="2" fill="#D6A9A9"/><rect x="154" y="24" width="16" height="16" rx="2" fill="#D6A9A9"/><rect x="172" y="24" width="16" height="16" rx="2" fill="#D6A9A9"/><rect x="190" y="24" width="16" height="16" rx="2" fill="#D6A9A9"/><text x="162" y="16" text-anchor="middle" font-size="11" font-style="italic" fill="var(--soft)">menstrual</text><rect x="208" y="24" width="16" height="16" rx="2" fill="#DEC1AF"/><rect x="226" y="24" width="16" height="16" rx="2" fill="#DEC1AF"/><rect x="244" y="24" width="16" height="16" rx="2" fill="#DEC1AF"/><rect x="262" y="24" width="16" height="16" rx="2" fill="#DEC1AF"/><rect x="280" y="24" width="16" height="16" rx="2" fill="#DEC1AF"/><rect x="298" y="24" width="16" height="16" rx="2" fill="#DEC1AF"/><rect x="316" y="24" width="16" height="16" rx="2" fill="#DEC1AF"/><rect x="334" y="24" width="16" height="16" rx="2" fill="#DEC1AF"/><text x="279" y="16" text-anchor="middle" font-size="11" font-style="italic" fill="var(--soft)">follicular</text><rect x="352" y="24" width="16" height="16" rx="2" fill="#D9C49B"/><rect x="370" y="24" width="16" height="16" rx="2" fill="#D9C49B"/><text x="369" y="16" text-anchor="middle" font-size="11" font-style="italic" fill="var(--soft)">ovulation</text><rect x="388" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="406" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="424" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="442" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="460" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="478" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="496" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="514" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="532" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="550" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="568" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="586" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="604" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><text x="504" y="16" text-anchor="middle" font-size="11" font-style="italic" fill="var(--soft)">luteal</text><text x="126" y="54" text-anchor="middle" font-size="10" fill="var(--muted)">1</text><text x="234" y="54" text-anchor="middle" font-size="10" fill="var(--muted)">7</text><text x="360" y="54" text-anchor="middle" font-size="10" fill="var(--muted)">14</text><text x="486" y="54" text-anchor="middle" font-size="10" fill="var(--muted)">21</text><text x="612" y="54" text-anchor="middle" font-size="10" fill="var(--muted)">28</text><text x="162" y="84" text-anchor="middle" font-size="11" fill="var(--ink)">12 to 14h</text><text x="279" y="84" text-anchor="middle" font-size="11" fill="var(--ink)">16 to 18h</text><text x="369" y="84" text-anchor="middle" font-size="11" fill="var(--ink)">16 to 20h</text><text x="504" y="84" text-anchor="middle" font-size="11" fill="var(--ink)">14 to 16h</text><rect x="136" y="94" width="16" height="12" rx="2" fill="none" stroke="var(--muted)" stroke-dasharray="2 2"/><text x="158" y="104" font-size="9" font-style="italic" fill="var(--muted)">rest, any day you choose</text><rect x="118" y="128" width="88" height="10" rx="5" fill="var(--rose)" opacity=".85"/><text x="118" y="154" font-size="11" fill="var(--ink)">severe pain during menstruation</text><line x1="118" y1="170" x2="620" y2="170" stroke="var(--rose)" stroke-width="1.2" stroke-dasharray="1 3"/><text x="118" y="186" font-size="11" fill="var(--ink)">and, for some, chronic pelvic pain that does not go away when the period ends</text><text x="0" y="32" font-size="12" font-style="italic" fill="var(--rose)">the cycle</text><text x="0" y="84" font-size="12" font-style="italic" fill="var(--rose)">hæl suggests</text><text x="0" y="136" font-size="12" font-style="italic" fill="var(--rose)">the pain</text></svg></div><figcaption style="margin-top:.8em;font-size:.88em;font-style:italic;color:var(--soft)">where hæl's hours sit, and where the pain can. hæl counts the period as days 1 to 5, whatever its length.</figcaption></figure>
            <h2>who shouldn't fast</h2>
            <ul>
                <li>anyone with a current or past eating disorder. a 2026 review reports a large genetic study finding nearly three times the odds of eating disorders in women with endometriosis, and says disordered eating, including restrictive dieting, is common and tied to pain.{n(20)} NHS guidance says people with a history of eating disorders shouldn't try intermittent fasting.{n(21)}</li>
                <li>during pregnancy or breastfeeding, or while trying to conceive.{n(21)}{n(22)} infertility is part of endometriosis for many,{n(1)} and eating around fertility treatment is for a doctor or midwife, not a timer.</li>
                <li>anyone with diabetes on insulin or a sulfonylurea, which can cause low blood sugar without food; doses need a doctor's guidance on fasting days.{n(23)}</li>
                <li>anyone under 18, or with weight loss, a poor appetite or a missed period that hasn't been looked into.</li>
                <li>when fasting starts to feel like a way to control pain by eating less, or like something you can't stop.</li>
            </ul>
            <p>if you are being treated for endometriosis, mention fasting to whoever prescribes for you.</p>

            <h2>where hæl fits</h2>
            <p>hæl doesn't treat endometriosis, and no study shows that fasting does. what it can do is keep the hours from asking for more on the days you have less. with the full witness, it suggests twelve to fourteen hours while you bleed, the shortest of the cycle, and fourteen to sixteen in the luteal phase, from ovulation to the period. its line for the period reads, "a rest day counts as part of the practice." that isn't a finding about endometriosis. it's a way of making the hard days easy to step back from.</p>
            <p>two honest limits. hæl counts the period as the first five days of the cycle, whatever its real length, so pain that starts before bleeding, or lasts beyond it, falls under the luteal or follicular hours. and if hormonal treatment has stopped your periods, the phases don't describe you, and turning the cycle off is the truer choice.</p>

            <h2>setting hæl up around painful days</h2>
            <ol>
                <li>tell hæl about your cycle, or don't. on the first page, give the day your last period began, read it from Apple Health, or choose "I don't keep one". if your periods have stopped with treatment, turn off "track a cycle" in settings: the ring keeps the hours alone, and the ledger draws the month by the moon, as a calendar only.</li>
                <li>let the dial sit lower. with the full witness, hæl suggests thirteen hours during the period, written under the dial; tap it to set the dial there. on any day, turn the dial lower, down to eight hours. if you'd rather the cycle didn't shape the suggestion, turn off "let the cycle shape the suggestion" in settings.</li>
                <li>press rest. on a day you won't fast, press rest under begin. the screen says "resting today." and "the practice keeps no score against it." rest days are free, and they don't break your days in a row; with "cycle-aware streaks" on, neither do period days. you can mark today only, so decide on the morning, not the week before.</li>
                <li>end a fast when you need to. press end fast, then end. the fast is kept as it was, at whatever length it reached. if you'd rather it weren't kept, choose discard this fast.</li>
                <li>keep your pain diary elsewhere. NICE suggests one for talking to a doctor;{n(5)} hæl observes fasts, not symptoms, so keep it on paper or in an app made for it.</li>
            </ol>
            <p>the timer, the ledger and rest days are free. the hours for each phase are part of the full witness. <a href="/cycle-syncing-fasting/">how hæl reads the cycle</a>.</p>

            <div class="aside">
                <p>hæl doesn't treat endometriosis, and neither does fasting. it suggests shorter hours while you bleed, keeps a day of rest as rest, and lets you end any fast without a word against it. for endometriosis itself, see a doctor; <a href="https://www.endometriosis-uk.org/what-is-endometriosis">Endometriosis UK</a> is a good place to start.</p>
                <a class="download" href="{STORE}">hæl on the App Store</a>
            </div>
"""

# for APPNOTES in build_notes.py: (campaign token, one true sentence)
ENDO_APPNOTE = ("article-endometriosis", "hæl, a fasting timer for iPhone, suggests its shortest hours while you bleed and keeps a day of rest as rest, never as a gap.")

ENDO_NOTE = dict(
    slug="endometriosis-intermittent-fasting",
    title="Endometriosis and Intermittent Fasting: What the Research Shows | hæl",
    description="no trial has tested intermittent fasting in endometriosis. what guidelines and studies say about diet, pain, fatigue, and who shouldn't fast.",
    kicker="the hard days",
    h1="endometriosis and intermittent fasting",
    headline="endometriosis and intermittent fasting: what the research shows",
    short="endometriosis affects about 1 in 10 women of reproductive age, and diagnosis often takes years. no trial has tested intermittent fasting in it; the only related studies cut calories in mice. the European guideline makes no recommendation on diet because the evidence is unclear. on days of pain, fatigue or nausea, a shorter fast or none is a reasonable choice; treatment is for a doctor.",
    body=ENDO_BODY, sources=ENDO_SOURCES,
    published="2026-11-09", published_text="november 9, 2026",
    appnote=ENDO_APPNOTE,
)

if __name__ == "__main__":
    # quick self-checks only; builds nothing
    import re
    text = ENDO_BODY + ENDO_NOTE["short"] + ENDO_NOTE["description"] + ENDO_APPNOTE[1]
    assert "—" not in text and "–" not in text, "dash found"
    assert "!" not in text, "exclamation found"
    assert not re.search(r"\b(she|her|hers)\b", text, re.I), "she/her found"
    assert len(ENDO_NOTE["description"]) < 160, len(ENDO_NOTE["description"])
    used = sorted({int(x) for x in re.findall(r'href="#s(\d+)"', ENDO_BODY)})
    assert used == list(range(1, len(ENDO_SOURCES) + 1)), used
    assert all({"html", "cite", "verified"} <= set(s) for s in ENDO_SOURCES), "source keys"
    print("ok:", len(ENDO_SOURCES), "sources, description", len(ENDO_NOTE["description"]), "chars")
