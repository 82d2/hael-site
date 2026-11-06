"""DRAFT, not built, not linked, not published: intermittent fasting when
trying to conceive, pregnant or breastfeeding.

To publish later: move PREG_SOURCES / PREG_BODY into _tools/build_notes.py,
add PREG_APPNOTE to APPNOTES and PREG_NOTE (with body= and sources=) to NOTES.
n() and STORE below mirror build_notes.py so this file runs on its own.
PREG_NOTE carries appnote= for the APPNOTES dict; drop that key before
passing it to page(), which doesn't take it.
Run `python3 _drafts/pregnancy.py` for the self-test. Research notes and
what was verified: _drafts/pregnancy-research.md. Current as of 2026-11-06.

APP NOTE FOR THE EDITOR (checked in /home/user/hael, v5, commit a878611):
the "track a cycle" switch in settings is drawn only while the cycle is
off (SettingsView.swift shows SettingsCycleOverrideCard only when
isCycleApplicable is false). once a cycle is kept, settings has no switch to
turn it off, and the phase keeps counting from the last period entered. the
tutorial below says so plainly. if the app gains an off switch before this
is published, rewrite step 3 to use it.

<!--
VISUAL SPECS

1. explanatory diagram: "how much more energy, and when"
   - a single row of six columns on a hairline baseline, the site's serif,
     no colour coding alone. each column is a plain bar whose height is the
     extra daily energy, with the figure written above it:
       before pregnancy        0
       pregnancy, 1st trimester  + 0
       pregnancy, 2nd trimester  + 340
       pregnancy, 3rd trimester  + 452
       breastfeeding, first 6 months   + 330
       breastfeeding, next 6 months    + 400
     unit under the row, small: "extra calories a day, compared with before
     pregnancy, for a healthy pre-pregnancy weight".
   - a thin bracket over the first column only, labelled "the only time
     the guidance leaves room for a fasting app is before trying to conceive,
     and even then with care". (if this reads as advice, drop it and keep
     the bars alone.)
   - footer, small: "US estimates from the Institute of Medicine (Dietary
     Guidelines for Americans 2020-2025, table 5-2). NICE: no need to 'eat
     for two'. La Leche League: time-restricted eating is not recommended
     while breastfeeding."
   - no baby or bump drawings, no food icons, no clocks.
   - alt text: "extra energy needed each day: none in the first trimester,
     about 340 calories in the second, 452 in the third, 330 in the first six
     months of breastfeeding and 400 in the next six."
   - every figure: DGA 2020-2025 table 5-2 (PREG_SOURCES 12); CDC (21)
     gives 330 to 400 for breastfeeding.

2. app screen to capture: home in the resting state. on a day with no
   fast running, press rest under begin, and capture the screen that reads
   "resting today." with "the practice keeps no score against it." under it
   (ContentViewInactive.swift, restingView). capture fresh from a real build
   with the cycle off ("I don't keep one" at onboarding), so no phase,
   phase colour or "day 14" shows anywhere on screen. do not use
   screenshots/ring.png or ledger.png (both show cycle days). do not mock it
   up. no phase, no ovulation label, no cycle day may be visible.
   caption: "a rest day in hæl. for as long as you are trying to conceive,
   pregnant or breastfeeding, rest is the whole of it."

3. OG image, 1200x630, the site's paper ground and book type:
   line 1 (large): "fasting when pregnant or breastfeeding"
   line 2 (smaller): "what the guidance says, plainly, and how to pause hæl"
   foot, small: "hæl · hael.app"
-->
"""

STORE = "https://apps.apple.com/app/id6778956802"


def n(i):
    return f'<sup><a href="#s{i}">{i}</a></sup>'


# "verified": "full text" = read in full; "full page" = guideline or
# organisation page read directly; "abstract" = PubMed abstract only;
# "secondary" = summary. build_notes.page() reads only "html" and "cite".
PREG_SOURCES = [
    # 1
    {"cite": "NHS. Weight gain in pregnancy. Page last reviewed 6 July 2022.",
     "html": 'NHS. <a href="https://www.nhs.uk/pregnancy/keeping-well/weight-gain/">Weight gain in pregnancy</a>.',
     "verified": "full page, read 2026-11-04 (last reviewed 6 July 2022; its review date has passed)"},
    # 2
    {"cite": "National Institute for Health and Care Excellence. Maternal and child nutrition: nutrition and weight management in pregnancy, and nutrition in children up to 5 years. NICE guideline NG247. 15 January 2025.",
     "html": 'National Institute for Health and Care Excellence. <a href="https://www.nice.org.uk/guidance/ng247/chapter/Recommendations">Maternal and child nutrition: nutrition and weight management in pregnancy, and nutrition in children up to 5 years</a> (NG247), 2025.',
     "verified": "full page (recommendations chapter), read 2026-11-04"},
    # 3
    {"cite": "La Leche League International. Weight loss for mothers. Updated November 2024.",
     "html": 'La Leche League International. <a href="https://llli.org/breastfeeding-info/weight-loss-mothers/">Weight loss for mothers</a>, 2024.',
     "verified": "full page, read 2026-11-06"},
    # 4
    {"cite": "Velissariou M, Athanasiadou CR, Diamanti A, Lykeridou A, Sarantaki A. The impact of intermittent fasting on fertility: a focus on polycystic ovary syndrome and reproductive outcomes in women. A systematic review. Metabolism Open. 2025;25:100341.",
     "html": 'Velissariou M, et al. <a href="https://doi.org/10.1016/j.metop.2024.100341">The impact of intermittent fasting on fertility: a focus on polycystic ovary syndrome and reproductive outcomes in women</a>. <i>Metabolism Open</i>, 2025.',
     "verified": "abstract"},
    # 5
    {"cite": "Loucks AB, Thuma JR. Luteinizing hormone pulsatility is disrupted at a threshold of energy availability in regularly menstruating women. Journal of Clinical Endocrinology and Metabolism. 2003;88(1):297-311.",
     "html": 'Loucks AB, Thuma JR. <a href="https://doi.org/10.1210/jc.2002-020369">Luteinizing hormone pulsatility is disrupted at a threshold of energy availability in regularly menstruating women</a>. <i>Journal of Clinical Endocrinology and Metabolism</i>, 2003.',
     "verified": "abstract"},
    # 6
    {"cite": "National Institute for Health and Care Excellence. Fertility problems: assessment and treatment. NICE guideline NG257. 31 March 2026. Advice about factors that can affect fertility.",
     "html": 'National Institute for Health and Care Excellence. <a href="https://www.nice.org.uk/guidance/ng257/chapter/Advice-about-factors-that-can-affect-fertility">Fertility problems: assessment and treatment</a> (NG257), 2026.',
     "verified": "full page (advice chapter), read 2026-11-06"},
    # 7
    {"cite": "Daley A, Pallan M, Clifford S, et al. Are babies conceived during Ramadan born smaller and sooner than babies conceived at other times of the year? A Born in Bradford cohort study. Journal of Epidemiology and Community Health. 2017;71(7):722-728.",
     "html": 'Daley A, et al. <a href="https://doi.org/10.1136/jech-2016-208800">Are babies conceived during Ramadan born smaller and sooner than babies conceived at other times of the year? A Born in Bradford cohort study</a>. <i>Journal of Epidemiology and Community Health</i>, 2017.',
     "verified": "abstract"},
    # 8
    {"cite": "Glazier JD, Hayes DJL, Hussain S, et al. The effect of Ramadan fasting during pregnancy on perinatal outcomes: a systematic review and meta-analysis. BMC Pregnancy and Childbirth. 2018;18:421.",
     "html": 'Glazier JD, et al. <a href="https://doi.org/10.1186/s12884-018-2048-y">The effect of Ramadan fasting during pregnancy on perinatal outcomes: a systematic review and meta-analysis</a>. <i>BMC Pregnancy and Childbirth</i>, 2018.',
     "verified": "full text (PMC6202808)"},
    # 9
    {"cite": "Pradella F, Witte P, van Ewijk R. Ramadan during pregnancy and offspring health outcomes over the life course: a systematic review and meta-analysis. Human Reproduction Update. 2024;30(6):789-812.",
     "html": 'Pradella F, Witte P, van Ewijk R. <a href="https://doi.org/10.1093/humupd/dmae026">Ramadan during pregnancy and offspring health outcomes over the life course: a systematic review and meta-analysis</a>. <i>Human Reproduction Update</i>, 2024.',
     "verified": "abstract"},
    # 10
    {"cite": "NHS. Vitamins, supplements and nutrition in pregnancy. Page last reviewed 3 June 2026.",
     "html": 'NHS. <a href="https://www.nhs.uk/pregnancy/keeping-well/pregnancy-vitamins-and-supplements/">Vitamins, supplements and nutrition in pregnancy</a>.',
     "verified": "full page, read 2026-11-04"},
    # 11
    {"cite": "American College of Obstetricians and Gynecologists. ACOG Committee Opinion No. 762 summary: Prepregnancy counseling. Obstetrics and Gynecology. 2019;133(1):228-230.",
     "html": 'American College of Obstetricians and Gynecologists. <a href="https://doi.org/10.1097/AOG.0000000000003014">Prepregnancy counseling</a>. Committee Opinion No. 762, summary. <i>Obstetrics and Gynecology</i>, 2019.',
     "verified": "abstract (the published summary, PMID 30575672); ACOG's own pages could not be read"},
    # 12
    {"cite": "US Department of Agriculture and US Department of Health and Human Services. Dietary Guidelines for Americans, 2020-2025. 9th edition. December 2020. Chapter 5, table 5-2.",
     "html": 'US Department of Agriculture and US Department of Health and Human Services. <a href="https://www.dietaryguidelines.gov/sites/default/files/2020-12/Dietary_Guidelines_for_Americans_2020-2025.pdf">Dietary Guidelines for Americans, 2020-2025</a>, chapter 5, table 5-2 (from the Institute of Medicine\'s estimated energy requirements, 2005).',
     "verified": "full text (PDF, page 111)"},
    # 13
    {"cite": "NHS. Have a healthy diet in pregnancy. Page last reviewed 21 April 2023.",
     "html": 'NHS. <a href="https://www.nhs.uk/pregnancy/keeping-well/have-a-healthy-diet/">Have a healthy diet in pregnancy</a>.',
     "verified": "full page, read 2026-11-04"},
    # 14
    {"cite": "Metzger BE, Ravnikar V, Vileisis RA, Freinkel N. \"Accelerated starvation\" and the skipped breakfast in late normal pregnancy. Lancet. 1982;1(8272):588-592.",
     "html": 'Metzger BE, et al. <a href="https://doi.org/10.1016/s0140-6736(82)91750-0">"Accelerated starvation" and the skipped breakfast in late normal pregnancy</a>. <i>The Lancet</i>, 1982.',
     "verified": "abstract"},
    # 15
    {"cite": "Rizzo T, Metzger BE, Burns WJ, Burns K. Correlations between antepartum maternal metabolism and intelligence of offspring. New England Journal of Medicine. 1991;325(13):911-916.",
     "html": 'Rizzo T, et al. <a href="https://doi.org/10.1056/NEJM199109263251303">Correlations between antepartum maternal metabolism and intelligence of offspring</a>. <i>New England Journal of Medicine</i>, 1991.',
     "verified": "abstract"},
    # 16
    {"cite": "Giorno A, De Simone C, Lopez G, et al. Intermittent fasting during pregnancy and neonatal birth weight: a systematic review and meta-analysis. Nutrients. 2025;17(22):3546.",
     "html": 'Giorno A, et al. <a href="https://doi.org/10.3390/nu17223546">Intermittent fasting during pregnancy and neonatal birth weight: a systematic review and meta-analysis</a>. <i>Nutrients</i>, 2025.',
     "verified": "full text (PMC12655342), searched for the figures used"},
    # 17
    {"cite": "Al-Taiar A, Rahman ME, Salama M, Ziyab AH, Karmaus W. Impacts of Ramadan fasting during pregnancy on pregnancy and birth outcomes: an umbrella review. International Journal of Gynecology and Obstetrics. 2025;169(3):968-978.",
     "html": 'Al-Taiar A, et al. <a href="https://doi.org/10.1002/ijgo.16127">Impacts of Ramadan fasting during pregnancy on pregnancy and birth outcomes: an umbrella review</a>. <i>International Journal of Gynecology and Obstetrics</i>, 2025.',
     "verified": "full text (PMC12093917), searched for the figures used"},
    # 18
    {"cite": "DiPiazza B, Patel B, Li Y, et al. Trial design: evaluating the safety, feasibility, and acceptability of time-restricted eating in pregnant women with obesity. Contemporary Clinical Trials. 2026;163:108257.",
     "html": 'DiPiazza B, et al. <a href="https://doi.org/10.1016/j.cct.2026.108257">Trial design: evaluating the safety, feasibility, and acceptability of time-restricted eating in pregnant women with obesity</a>. <i>Contemporary Clinical Trials</i>, 2026.',
     "verified": "abstract"},
    # 19
    {"cite": "NHS. Gestational diabetes: treatment. Page last reviewed 8 December 2022.",
     "html": 'NHS. <a href="https://www.nhs.uk/conditions/gestational-diabetes/treatment/">Gestational diabetes: treatment</a>.',
     "verified": "full page, read 2026-11-06"},
    # 20
    {"cite": "Carrasco M, Vlacho B, Franch-Nadal J, et al. Overdiagnosis of gestational diabetes mellitus during Ramadan: a retrospective population-based study in Catalonia, Spain. BMC Medicine. 2026;24(1):95.",
     "html": 'Carrasco M, et al. <a href="https://doi.org/10.1186/s12916-026-04638-w">Overdiagnosis of gestational diabetes mellitus during Ramadan: a retrospective population-based study in Catalonia, Spain</a>. <i>BMC Medicine</i>, 2026.',
     "verified": "abstract"},
    # 21
    {"cite": "Centers for Disease Control and Prevention. Maternal diet and breastfeeding. Last reviewed August 25, 2026.",
     "html": 'Centers for Disease Control and Prevention. <a href="https://www.cdc.gov/breastfeeding-special-circumstances/hcp/diet-micronutrients/maternal-diet.html">Maternal diet and breastfeeding</a>.',
     "verified": "full page, read through a summarising fetch, 2026-11-06"},
    # 22
    {"cite": "La Leche League International. Fasting (religious or dietary) and breastfeeding.",
     "html": 'La Leche League International. <a href="https://llli.org/fasting/">Fasting (religious or dietary) and breastfeeding</a>.',
     "verified": "full page, read 2026-11-06"},
    # 23
    {"cite": "NHS. Breastfeeding and diet. Page last reviewed 15 May 2026.",
     "html": 'NHS. <a href="https://www.nhs.uk/baby/breastfeeding-and-bottle-feeding/breastfeeding-and-lifestyle/diet/">Breastfeeding and diet</a>.',
     "verified": "full page, read 2026-11-04"},
    # 24
    {"cite": "Rakicioğlu N, Samur G, Topçu A, Topçu AA. The effect of Ramadan on maternal nutrition and composition of breast milk. Pediatrics International. 2006;48(3):278-283.",
     "html": 'Rakicioğlu N, et al. <a href="https://doi.org/10.1111/j.1442-200X.2006.02204.x">The effect of Ramadan on maternal nutrition and composition of breast milk</a>. <i>Pediatrics International</i>, 2006.',
     "verified": "abstract"},
    # 25
    {"cite": "Başıbüyük M, Aktaç Ş, Kundakçı S, Büke Ö, Karabayır N. Effect of Ramadan fasting on breast milk. Breastfeeding Medicine. 2023;18(8):596-601.",
     "html": 'Başıbüyük M, et al. <a href="https://doi.org/10.1089/bfm.2023.0144">Effect of Ramadan fasting on breast milk</a>. <i>Breastfeeding Medicine</i>, 2023.',
     "verified": "abstract"},
    # 26
    {"cite": "Allegaert K, Smits A. Acute maternal fasting or fluid abstention does not significantly affect the macronutrient composition of human milk: clinical and clinical research relevance. Children. 2020;7(6):60.",
     "html": 'Allegaert K, Smits A. <a href="https://doi.org/10.3390/children7060060">Acute maternal fasting or fluid abstention does not significantly affect the macronutrient composition of human milk</a>. <i>Children</i>, 2020.',
     "verified": "abstract"},
    # 27
    {"cite": "Al Alawi AM, Al Flaiti A, Falhammar H. Lactation ketoacidosis: a systematic review of case reports. Medicina (Kaunas). 2020;56(6):299.",
     "html": 'Al Alawi AM, Al Flaiti A, Falhammar H. <a href="https://doi.org/10.3390/medicina56060299">Lactation ketoacidosis: a systematic review of case reports</a>. <i>Medicina</i>, 2020.',
     "verified": "abstract"},
    # 28
    {"cite": "Ertem IO, Kaynak G, Kaynak C, Ulukol B, Gulnar SB. Attitudes and practices of breastfeeding mothers regarding fasting in Ramadan. Child: Care, Health and Development. 2001;27(6):545-554.",
     "html": 'Ertem IO, et al. <a href="https://doi.org/10.1046/j.1365-2214.2001.00226.x">Attitudes and practices of breastfeeding mothers regarding fasting in Ramadan</a>. <i>Child: Care, Health and Development</i>, 2001.',
     "verified": "abstract"},
    # 29
    {"cite": "El-Kurdy R, Abozed HW, El-Gilany AH, Mohamed Abdu SM. The effect of Ramadan fasting on breastfeeding practices of Muslim women. Breastfeeding Medicine. 2025;20(5):303-309.",
     "html": 'El-Kurdy R, et al. <a href="https://doi.org/10.1089/bfm.2024.0325">The effect of Ramadan fasting on breastfeeding practices of Muslim women</a>. <i>Breastfeeding Medicine</i>, 2025.',
     "verified": "abstract"},
    # 30
    {"cite": "Safari K, Piro TJ, Ahmad HM. Perspectives and pregnancy outcomes of maternal Ramadan fasting in the second trimester of pregnancy. BMC Pregnancy and Childbirth. 2019;19:128.",
     "html": 'Safari K, Piro TJ, Ahmad HM. <a href="https://doi.org/10.1186/s12884-019-2275-x">Perspectives and pregnancy outcomes of maternal Ramadan fasting in the second trimester of pregnancy</a>. <i>BMC Pregnancy and Childbirth</i>, 2019.',
     "verified": "abstract"},
    # 31
    {"cite": "Uludağ E, Göral Türkcü S. Ramadan fasting as a religious obligation: a qualitative study on opinions and experiences of Muslim pregnant women about fasting in Turkey. Journal of Religion and Health. 2022;61(4):2960-2974.",
     "html": 'Uludağ E, Göral Türkcü S. <a href="https://doi.org/10.1007/s10943-022-01588-4">Ramadan fasting as a religious obligation: a qualitative study on opinions and experiences of Muslim pregnant women about fasting in Turkey</a>. <i>Journal of Religion and Health</i>, 2022.',
     "verified": "abstract"},
]

PREG_BODY = f"""
            <h2>what does the guidance say?</h2>
            <p>during pregnancy, don't diet. the NHS puts it in one line: "pregnancy isn't the time to go on a diet, as it may harm the health of the unborn child."{n(1)} NICE, which writes the guidance for doctors and midwives in England, says pregnant people don't need to "eat for two", and don't need a special diet beyond avoiding certain foods, but should eat a variety of foods every day.{n(2)}</p>
            <p>while breastfeeding, La Leche League International, the breastfeeding support charity, is just as plain: "time-restricted eating is not recommended during breastfeeding," because there isn't enough information to know whether it is safe.{n(3)}</p>
            <p>while trying to conceive, there is no guidance on intermittent fasting either way, because there are no trials to base it on. what is known is set out below.</p>
            <p>so: if you are pregnant or breastfeeding, intermittent fasting isn't advised, and hæl isn't for you right now. if you are trying to conceive, talk to a doctor before you fast at all.</p>

            <h2>trying to conceive: what is known</h2>
            <p>very little, about fasting itself. no trial we found tested intermittent fasting in people trying to conceive and counted pregnancies or births. a 2025 review of fasting and fertility found only three studies, all in polycystic ovary syndrome; the outcomes in its summary are cycles, hormones and weight, and pregnancies aren't among them.{n(4)}</p>
            <p>what is better known is energy. ovulation depends on signals from the brain, and those signals slow when the body runs short of fuel. in a careful 2003 study, 29 women with regular cycles were fed set amounts for five days while they exercised. the pulses of LH, the hormone that triggers ovulation, held steady down to 30 calories a day for each kilogram of lean body mass, and slowed below it. the authors placed that threshold "deep into negative energy balance".{n(5)} a fast followed by enough food is not the same thing. a fast that becomes a way of eating less and less can be.</p>
            <p>weight matters in both directions. NICE advises that with a BMI under 18.5 and periods that are irregular or absent, gaining weight is likely to improve the chance of conceiving; with a BMI of 30 or more, conceiving is likely to take longer, and if ovulation isn't happening, losing weight is likely to help.{n(6)} that is a plan for a doctor, and nothing in it is specific to fasting.</p>
            <p>a few studies have looked at Ramadan fasting around conception. in Bradford, babies whose estimated conception fell during Ramadan (479) were born no lighter than those conceived at other times (4,677): an adjusted difference of 24.3 g, and 5.2% against 4.9% born early.{n(7)} the largest review of Ramadan in pregnancy didn't look at fasting around conception at all,{n(8)} and a 2024 review of long-term outcomes found the first trimester to be the most sensitive time, with effects that appeared later in childhood and adulthood rather than at birth.{n(9)} the first weeks of a pregnancy often pass before anyone knows it has begun.</p>
            <p>what the guidance does ask of everyone trying to conceive is folic acid. the NHS advises 400 micrograms a day, ideally from three months before trying, and for the first 12 weeks of pregnancy.{n(10)} NICE advises a higher dose, 5 mg a day, for some people, including anyone with type 1 or type 2 diabetes or a personal or family history of a neural tube defect, and that is prescribed.{n(2)} ACOG, the American college of obstetricians, also encourages folic acid before pregnancy, as part of seeing a doctor before trying.{n(11)}</p>

            <h2>pregnancy: how much more energy, and when?</h2>
            <p>none at first, then more. US estimates, from the Institute of Medicine, for someone of healthy weight before pregnancy: no extra calories in the first trimester, about 340 a day more in the second, and about 452 a day more in the third. with overweight or obesity before pregnancy, the advice is to ask your own doctor or midwife.{n(12)} the NHS adds that you will probably be hungrier than usual, and that you still don't need to eat for two, even with twins or triplets.{n(13)}</p>
            <p>weight is meant to rise. most people gain between 10 and 12.5 kg (22 to 28 lb), most of it after week 20, and gaining too little can cause problems such as early birth and low birth weight.{n(1)} NICE says there is too little evidence to set an ideal gain for each trimester, and advises against routine weighing in pregnancy unless there is a clinical reason.{n(2)}</p>
            <p>nutrients matter as much as calories: folic acid in the first 12 weeks, and in the UK, 10 micrograms of vitamin D a day from early October to late March.{n(10)}</p>

            <figure class="fig" style="margin:2em 0"><div role="img" aria-label="extra energy needed each day: none in the first trimester, about 340 calories in the second, 452 in the third, 330 in the first six months of breastfeeding and 400 in the next six." style="font-size:.95em"><div style="display:flex;gap:3px;align-items:flex-end;height:220px;padding-top:12px;border-bottom:1px solid var(--rule)"><div style="flex:1 1 0;min-width:0;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;text-align:center"><div style="font-size:.85em;color:var(--ink);margin-bottom:4px">0</div><div style="width:60%;height:2px;background:var(--rose);opacity:0.35"></div><div style="font-size:.64em;color:var(--soft);margin-top:6px;line-height:1.25;min-height:3.8em">before</div></div><div style="flex:1 1 0;min-width:0;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;text-align:center"><div style="font-size:.85em;color:var(--ink);margin-bottom:4px">0</div><div style="width:60%;height:2px;background:var(--rose);opacity:0.35"></div><div style="font-size:.64em;color:var(--soft);margin-top:6px;line-height:1.25;min-height:3.8em">trimester 1</div></div><div style="flex:1 1 0;min-width:0;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;text-align:center"><div style="font-size:.85em;color:var(--ink);margin-bottom:4px">+ 340</div><div style="width:60%;height:83px;background:var(--rose);opacity:0.85"></div><div style="font-size:.64em;color:var(--soft);margin-top:6px;line-height:1.25;min-height:3.8em">trimester 2</div></div><div style="flex:1 1 0;min-width:0;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;text-align:center"><div style="font-size:.85em;color:var(--ink);margin-bottom:4px">+ 452</div><div style="width:60%;height:110px;background:var(--rose);opacity:0.85"></div><div style="font-size:.64em;color:var(--soft);margin-top:6px;line-height:1.25;min-height:3.8em">trimester 3</div></div><div style="flex:1 1 0;min-width:0;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;text-align:center"><div style="font-size:.85em;color:var(--ink);margin-bottom:4px">+ 330</div><div style="width:60%;height:80px;background:var(--rose);opacity:0.85"></div><div style="font-size:.64em;color:var(--soft);margin-top:6px;line-height:1.25;min-height:3.8em">nursing, months 1 to 6</div></div><div style="flex:1 1 0;min-width:0;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;text-align:center"><div style="font-size:.85em;color:var(--ink);margin-bottom:4px">+ 400</div><div style="width:60%;height:97px;background:var(--rose);opacity:0.85"></div><div style="font-size:.64em;color:var(--soft);margin-top:6px;line-height:1.25;min-height:3.8em">nursing, months 7 to 12</div></div></div><p style="margin:8px 0 0;font-size:.85em;color:var(--muted)">extra calories a day, compared with before pregnancy, for a healthy pre-pregnancy weight. US estimates from the Institute of Medicine (Dietary Guidelines for Americans 2020 to 2025).</p></div><figcaption style="margin-top:.8em;font-size:.88em;font-style:italic;color:var(--soft)">how much more energy, and when.</figcaption></figure>
            <h2>what happens when a pregnant body goes without food?</h2>
            <p>it switches to stored fuel sooner than it otherwise would. in a 1982 study, women in the third trimester and women who weren't pregnant ate dinner at 6 pm and then nothing until noon the next day. in the women who weren't pregnant, blood sugar and fuel levels barely moved between the 12th and 18th hour. in the pregnant women, blood sugar was already lower at 6 am and fell further, insulin fell, and fatty acids and ketones rose. the authors called this "accelerated starvation", and concluded that pregnant women should avoid skipping breakfast.{n(14)}</p>
            <p>ketones are the reason for caution. in a 1991 study of 223 pregnant women, 188 of them with diabetes, higher ketone levels in the third trimester went with lower scores on their children's tests of development at two and intelligence at three to five.{n(15)} that is a correlation, a weak one (about 0.2), and mostly in diabetes; it can't show that ketones caused anything. the authors still urged efforts to avoid accelerated starvation in all pregnant women, and nothing since has shown that a daily fast in pregnancy is safe.</p>

            <h2>what the Ramadan studies show</h2>
            <p>nearly everything known about fasting in pregnancy comes from Ramadan. pregnant Muslim women are exempt, yet many fast for at least some of the month; one review cites estimates of up to 90%.{n(8)} these are studies of what happened, not trials, and Ramadan, with no food or drink from sunrise to sunset and meals at night, is not the same as a daily sixteen-hour fast kept for months.</p>
            <p>the 2018 meta-analysis by Glazier and colleagues pooled 22 studies of 31,374 pregnancies, 18,920 of them exposed to Ramadan fasting.{n(8)}</p>
            <ul>
                <li>birth weight, in 21 studies: no effect (standardised mean difference 0.03, 95% CI 0.00 to 0.05).</li>
                <li>low birth weight, under 2.5 kg, in 8 studies and 11,080 births: no significant difference (odds ratio 1.05, 0.87 to 1.26).</li>
                <li>preterm birth, in 5,600 pregnancies: no effect (odds ratio 0.99, 0.72 to 1.37).</li>
                <li>placental weight: lower with fasting, but one study supplied 17,626 of the 17,986 births, and one of the other two found the opposite.</li>
                <li>stillbirth, newborn death, gestational diabetes, high blood pressure and birth defects: too few data to pool. there were no data at all on perinatal death.</li>
            </ul>
            <p>its own limits are worth reading: English-language papers only, birth weight as the only measure of growth, nothing on growth before birth or after it, and the authors called for further studies before anyone could say whether fasting is linked with harm to mother or baby.{n(8)}</p>
            <p>later reviews add to it. a 2025 meta-analysis found no randomised trials at all; across six studies it could pool, babies born after fasting weighed about 94 g less (95% CI 176 to 12 g less), which its authors judged unlikely to matter clinically, with no rise in low birth weight.{n(16)} a 2024 review that followed children and adults found no difference at birth, but slightly lower scores on cognitive tests in childhood (by about 3% of a standard deviation), slightly shorter height, and in adults a higher chance of hearing disability (odds ratio 1.26), with the quality of evidence low to moderate.{n(9)} a 2025 review of 13 earlier reviews found that none reported on stillbirth, miscarriage, birth defects or newborn deaths, and that the studies underneath had significant flaws.{n(17)}</p>
            <p>the honest summary: Ramadan fasting doesn't clearly change birth weight or early birth, the rare serious outcomes have hardly been studied, and some long-term findings give reason for care. none of it tests a daily eating window. the first trial of one in pregnancy, in women with a BMI of 35 to 60, under supervision, with an eight-hour window in the second trimester and ten hours in the third, had its design published in 2026; we found no results yet.{n(18)}</p>

            <h2>gestational diabetes and fasting</h2>
            <p>with gestational diabetes, fasting works against the treatment. the NHS advice is to eat regularly, usually three meals a day, and avoid skipping meals, and it warns that insulin can make blood sugar fall too low.{n(19)} don't fast, and don't change a meal plan or a dose, without your diabetes team.</p>
            <p>fasting can also muddle the test. in a 2026 study of 35,054 pregnancies in Catalonia, women from Muslim-majority countries were diagnosed with gestational diabetes more often when tested during Ramadan, 12.8% against 8.84% at other times, while other women showed no difference (5.57% against 5.52%). the authors suggest fasting or other Ramadan habits may affect glucose testing.{n(20)} if you have been fasting, say so before a glucose test.</p>

            <h2>breastfeeding: energy and milk</h2>
            <p>making milk takes fuel. the CDC recommends an extra 330 to 400 calories a day for a well-nourished breastfeeding mother, more or less with age, size, activity and how much the baby feeds;{n(21)} the US estimates are about 330 a day more in the first six months and 400 in the next six.{n(12)} La Leche League advises eating at least 1,800 calories a day while losing weight, and notes that "sometimes eating fewer calories can affect milk supply."{n(3)}</p>
            <p>its page on fasting adds the other side: the main nutrients in milk don't seem to be much affected by fasting, and babies grow normally, because the body puts the baby first, so it is the parent's own wellbeing that is likely to suffer first. it suggests seeking an exemption or adapting a religious fast when feeding a very young baby or more than one child, during pregnancy, or with diabetes or another condition, and watching the baby's weight and your own wellbeing if you do fast.{n(22)} the NHS says no special diet is needed while breastfeeding, and suggests 10 micrograms of vitamin D a day in autumn and winter.{n(23)}</p>
            <p>the studies are small, and nearly all are of Ramadan:</p>
            <ul>
                <li>21 breastfeeding mothers in Ankara: the milk's protein, fat and sugar held steady, but zinc, magnesium and potassium in the milk fell during Ramadan, and the mothers' own energy and most nutrients fell below what is recommended in lactation. the authors thought it prudent to excuse breastfeeding mothers from the fast.{n(24)}</li>
                <li>21 fasting and 27 non-fasting mothers in Istanbul, all exclusively breastfeeding: no difference in the milk's energy, protein, fat or carbohydrate, and no difference in the babies' weight gain over the month.{n(25)}</li>
                <li>a 2020 review of seven reports: short fasts of 18 to 25 hours didn't meaningfully change the milk's main nutrients; the changes found were mostly in salts, and mostly over a month of daily fasting.{n(26)}</li>
            </ul>
            <p>no trial has tested a daily eating window while breastfeeding. one rare danger is clear: lactation ketoacidosis, a build-up of acid from ketones. a review found 18 reported cases between 1970 and 2019, and dieting and exercise to lose weight came before 14 of them; with treatment, none died.{n(27)} nausea, vomiting, stomach pain, breathlessness or headache while breastfeeding and eating little need medical help straight away.{n(22)}</p>

            <h2>what women have told researchers</h2>
            <ul>
                <li>of 164 breastfeeding mothers surveyed in Ankara, about half fasted in Ramadan. among the 129 with babies of six months or younger, 22% felt their milk had decreased and 23% said their baby was being given more solid food. mothers who believed fasting doesn't reduce milk were more likely to fast.{n(28)}</li>
                <li>of 1,130 breastfeeding mothers surveyed in Egypt, 83.7% fasted during Ramadan, despite the exemption.{n(29)}</li>
                <li>in Erbil, Iraq, 60% of the women who fasted in the second trimester said they saw fasting in pregnancy as compulsory for healthy and unhealthy women alike. the authors concluded that most didn't fully recognise their right to an exemption.{n(30)}</li>
                <li>17 pregnant women interviewed in Turkey described religious belief, past experience, family and society all pressing them to fast; some didn't, out of worry for their own physical and mental health and for their babies.{n(31)}</li>
            </ul>
            <p>these are small groups, and all are about a religious fast, chosen for reasons a timer can't weigh. none is about fasting for weight.</p>

            <h2>who shouldn't fast</h2>
            <ul>
                <li>anyone who is pregnant. pregnancy isn't the time to diet,{n(1)} skipping breakfast late in pregnancy brings on ketones within hours,{n(14)} and no trial shows a daily fast to be safe.</li>
                <li>anyone who is breastfeeding, especially a young baby, or more than one child. time-restricted eating is not recommended.{n(3)}</li>
                <li>anyone with gestational diabetes, or diabetes of any kind in pregnancy.{n(19)}</li>
                <li>anyone trying to conceive with a BMI under 18.5 and periods that are irregular or have stopped. gaining weight, not fasting, is what NICE advises.{n(6)}</li>
                <li>anyone with a current or past eating disorder, at any time. hæl's own first pages ask the same.</li>
                <li>anyone trying to conceive, without a word with a doctor first. there is no evidence that fasting helps, and the first weeks of a pregnancy can pass unnoticed.</li>
                <li>anyone whose period is late. stop fasting, take a test, and see a doctor if a period has stopped.</li>
            </ul>

            <h2>hæl isn't for these times</h2>
            <p>hæl is a fasting timer. it is built for months when fasting is a reasonable choice, and pregnancy and breastfeeding aren't those months. its first pages say so before the timer appears: "speak to a doctor before you begin, especially if you are pregnant or nursing." hæl doesn't track pregnancy, and it isn't a fertility app.</p>
            <p>hæl makes no fertility or contraception claim, and must never be used to plan or to prevent a pregnancy. if you keep a cycle in hæl, the phase it shows, ovulation included, is arithmetic: two days placed about fourteen days before the next expected period, from the last period and the cycle length hæl holds. it measures nothing, and it doesn't know whether or when you ovulate. its hours are a suggestion for a fast, and nothing more.</p>

            <h2>how to pause hæl, or keep only the ledger</h2>
            <ol>
                <li>end any fast that is running. press end, or "discard this fast" if you'd rather it left no page.</li>
                <li>stop beginning new ones. hæl needs nothing from you to pause, and nothing is lost by stopping. on a day you open it, you can press rest under begin, and the screen reads "resting today. the practice keeps no score against it." rest marks one day at a time; there is no switch that pauses hæl for months.</li>
                <li>quiet the cycle. if you chose "I don't keep one" at the start, there is nothing to change. if you keep a cycle, hæl goes on counting phases from the last period you entered, through a pregnancy and through the months before periods return after birth, as if cycles were still coming. that count means nothing now. from hæl 5, out on november 17, turn off "track a cycle" on the cycle card in settings: the phases stop, and the record you kept stays for later. in earlier versions a kept cycle can't be switched off, so with the full witness turn off "let the cycle shape the suggestion" under the cycle, and read any phase on screen as blank.</li>
                <li>quiet the notes. in settings, under the practice, turn off the daily check-in, and with it turn off the two notes. then hæl sends no morning nudge and no phase notes.</li>
                <li>set the scale aside. weight is meant to rise in pregnancy, and the body ledger's readings are built for ordinary months, not for these. in settings, under the form, turn on "keep the numbers out of sight", or turn off "sync weight data" under Apple Health, so hæl stops syncing weight with it.</li>
                <li>keep the ledger. everything you have already recorded stays on your device and in your private iCloud. under the record, you can export it as a spreadsheet, a full backup, or a page to read. when you are ready to fast again, with a doctor's word, the ledger is still there.</li>
            </ol>
            <p>if you would rather it were gone, "delete all data" is under about and privacy. either way, hæl has no account and no server of its own: its records stay on your device and in your private iCloud.</p>

            <div class="aside">
                <p>hæl isn't for pregnancy, for breastfeeding, or for trying to conceive, and it makes no fertility or contraception claim. it keeps what you have already written, asks nothing while you are away, and will be there, unchanged, for a later year.</p>
                <a class="download" href="{STORE}">hæl on the App Store</a>
            </div>
"""

# for APPNOTES in build_notes.py: (campaign token, one true sentence)
PREG_APPNOTE = ("article-pregnancy", "hæl is a fasting timer for iPhone, not for pregnancy or breastfeeding; it makes no fertility claim, and rest days are free.")

PREG_NOTE = dict(
    slug="intermittent-fasting-pregnancy-breastfeeding",
    title="Intermittent Fasting When Pregnant or Breastfeeding | hæl",
    description="is intermittent fasting safe while trying to conceive, pregnant or breastfeeding? what guidance and research say, and how to pause hæl.",
    kicker="the pause",
    h1="intermittent fasting, pregnancy and breastfeeding",
    headline="intermittent fasting when trying to conceive, pregnant or breastfeeding: what the guidance says",
    short="during pregnancy, intermittent fasting isn't advised: the NHS says pregnancy isn't the time to diet, energy needs rise from the second trimester, and no trial shows a daily fast to be safe. while breastfeeding, La Leche League says time-restricted eating is not recommended. while trying to conceive there is no evidence for fasting either way; see a doctor first, and take folic acid. hæl isn't for these times.",
    body=PREG_BODY, sources=PREG_SOURCES,
    published="2026-11-09", published_text="november 9, 2026",
    appnote=PREG_APPNOTE,
)

if __name__ == "__main__":
    # quick self-checks only; builds nothing
    import re
    text = (PREG_BODY + PREG_NOTE["short"] + PREG_NOTE["description"] + PREG_NOTE["h1"]
            + PREG_NOTE["headline"] + PREG_NOTE["kicker"] + PREG_APPNOTE[1])
    assert "—" not in text and "–" not in text, "dash found"
    assert "!" not in text, "exclamation found"
    assert not re.search(r"\b(she|her|hers|herself)\b", text, re.I), "she/her found"
    for banned in ("fertile", "safe days", "safe day", "fertility window", "fertile window",
                   "ovulation window", "best time to conceive", "rhythm method"):
        assert banned not in text.lower(), banned
    assert len(PREG_NOTE["description"]) < 160, len(PREG_NOTE["description"])
    used = sorted({int(x) for x in re.findall(r'href="#s(\d+)"', PREG_BODY)})
    assert used == list(range(1, len(PREG_SOURCES) + 1)), used
    assert all(s.get("verified") for s in PREG_SOURCES), "verified key missing"
    print("ok:", len(PREG_SOURCES), "sources, description", len(PREG_NOTE["description"]), "chars")
