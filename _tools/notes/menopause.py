"""DRAFT, not built or linked: intermittent fasting in perimenopause and menopause,
what the research shows. To publish later: move MENO_SOURCES / MENO_BODY into
_tools/build_notes.py, add MENO_APPNOTE to APPNOTES and MENO_NOTE to NOTES
(drop the appnote key before passing it to page(), which doesn't take it).
n() and STORE below mirror build_notes.py so this file runs on its own.
Run `python3 _drafts/menopause.py` for the self-test. Research notes and what
was verified: _drafts/menopause-research.md. Current as of 2026-11-06.

<!--
VISUAL SPECS

1. Explanatory diagram: "where the trials sit in the transition"
   Place: after the trials list, before "what about muscle?".
   A single horizontal strip of the STRAW+10 stages, left to right, hairline
   rules, the site's serif, lowercase labels, no colour coding alone:
     -2 "early transition" (cycles vary by 7 days or more)
     -1 "late transition" (60 days or more without a period; 1 to 3 years)
      0 a vertical line, "final period" (known only after 12 months)
     +1a, +1b "first two years after"
     +1c "3 to 6 more years"
     +2 "late postmenopause"
   A bracket over -2 to +1a labelled "perimenopause" (STRAW+10: from stage
   -2 to 12 months after the final period). A second, thinner bracket over
   -1 to +1b labelled "fat gain doubles, lean mass falls, most bone loss"
   (SWAN: Greendale 2019, Greendale 2012).
   Under the strip, two rows of small marks:
     row "studied after menopause only" (hollow squares over +1 and +2):
       "8 weeks, 4 to 6 hour window, 19 women" (Cienfuegos 2021)
       "12 weeks, alternate days, 22 women" (Lin 2021)
       "12 weeks, 10 hour window, 100 women" (Yang 2026)
       "8 weeks, 8 hour window, 142 women" (Wang 2025)
     row "perimenopause included" (filled squares spanning -2 to +2):
       "12 weeks, 8 hour window, 104 women aged 40 to 60" (Dai 2025)
       "12 weeks, 16:8 with exercise, 54 to 62 women" (Jozwiak 2024, 2025)
   Footer line, small: "perimenopausal women were excluded from the
   Chicago trials. no fasting trial has tested hot flushes as its main
   outcome."
   Alt text: "the stages of reproductive ageing, from cycles that start to
   vary, through gaps of two months or more, to the final period and the
   years after it. most fasting trials studied women after menopause; two
   included women in perimenopause. none tested hot flushes as the main
   outcome."
   Sources for every figure: Harlow 2012, Greendale 2019, Greendale 2012,
   Cienfuegos 2021, Lin 2021, Yang 2026, Wang 2025, Dai 2025, Jozwiak 2024
   and 2025 (see MENO_SOURCES).

2. App screen: home with no cycle kept (capture fresh from a real build; none
   of /screenshots or /images shows it). Settings > the cycle > "track a
   cycle" off, dial turned to 12, before begin. Shows the ring at 12 hours,
   the moon's four marks and the night's line under the suggestion
   (ContentViewInactive, phase unknown), begin and rest. Do not use
   screenshots/ring.png (it shows "day 14" of a cycle) or ledger.png (it
   shows cycle phases). Do not mock it up.
   Caption: "when periods stop, hæl keeps the hours alone. the moon under
   the dial is a calendar, and nothing more."

3. OG image, 1200x630, the site's cream ground and serif:
   line 1 (large): "intermittent fasting and menopause"
   line 2: "what the research shows, and what it doesn't"
   foot, small: "hæl · hael.app"
-->
"""

STORE = "https://apps.apple.com/app/id6778956802"


def n(i):
    return f'<sup><a href="#s{i}">{i}</a></sup>'


# "verified": "full text" = read in full; "abstract" = PubMed abstract only;
# "secondary" = a summary by another body, not the source itself.
# build_notes.page() reads only "html" and "cite", so the extra key is safe.
MENO_SOURCES = [
    # 1
    {"cite": "Harlow SD, Gass M, Hall JE, et al. Executive summary of the Stages of Reproductive Aging Workshop + 10: addressing the unfinished agenda of staging reproductive aging. Journal of Clinical Endocrinology and Metabolism. 2012;97(4):1159-1168.",
     "html": 'Harlow SD, et al. <a href="https://doi.org/10.1210/jc.2011-3362">Executive summary of the Stages of Reproductive Aging Workshop + 10: addressing the unfinished agenda of staging reproductive aging</a>. <i>Journal of Clinical Endocrinology and Metabolism</i>, 2012.',
     "verified": "full text (PMC3319184), read through a summarising fetch"},
    # 2
    {"cite": "Gold EB, Crawford SL, Avis NE, et al. Factors related to age at natural menopause: longitudinal analyses from SWAN. American Journal of Epidemiology. 2013;178(1):70-83.",
     "html": 'Gold EB, et al. <a href="https://doi.org/10.1093/aje/kws421">Factors related to age at natural menopause: longitudinal analyses from SWAN</a>. <i>American Journal of Epidemiology</i>, 2013.',
     "verified": "abstract"},
    # 3
    {"cite": "British Menopause Society. Menopause: identification and management, from NICE guideline to practice (NICE NG23, last updated 7 November 2024). Tool for clinicians, updated September 2026.",
     "html": 'British Menopause Society. <a href="https://thebms.org.uk/wp-content/uploads/2026/09/09-NEW-BMS-TfC-NICE-Menopause-Menopause-identification-and-management-%E2%80%93-from-guideline-to-practice-SEPT2026-D.pdf">Menopause: identification and management, from NICE guideline to practice</a>, 2026. A summary of <a href="https://www.nice.org.uk/guidance/ng23">NICE guideline NG23</a>.',
     "verified": "secondary (BMS summary of NICE NG23, read in full; the NICE site returned 403)"},
    # 4
    {"cite": "Greendale GA, Sternfeld B, Huang M, et al. Changes in body composition and weight during the menopause transition. JCI Insight. 2019;4(5):e124865.",
     "html": 'Greendale GA, et al. <a href="https://doi.org/10.1172/jci.insight.124865">Changes in body composition and weight during the menopause transition</a>. <i>JCI Insight</i>, 2019.',
     "verified": "full text (PMC6483504), read through a summarising fetch"},
    # 5
    {"cite": "Greendale GA, Sowers M, Han W, et al. Bone mineral density loss in relation to the final menstrual period in a multiethnic cohort: results from the Study of Women's Health Across the Nation (SWAN). Journal of Bone and Mineral Research. 2012;27(1):111-118.",
     "html": 'Greendale GA, et al. <a href="https://doi.org/10.1002/jbmr.534">Bone mineral density loss in relation to the final menstrual period in a multiethnic cohort: results from the Study of Women\'s Health Across the Nation</a>. <i>Journal of Bone and Mineral Research</i>, 2012.',
     "verified": "full text (PMC3378821)"},
    # 6
    {"cite": "Avis NE, Crawford SL, Greendale G, et al. Duration of menopausal vasomotor symptoms over the menopause transition. JAMA Internal Medicine. 2015;175(4):531-539.",
     "html": 'Avis NE, et al. <a href="https://doi.org/10.1001/jamainternmed.2014.8063">Duration of menopausal vasomotor symptoms over the menopause transition</a>. <i>JAMA Internal Medicine</i>, 2015.',
     "verified": "abstract"},
    # 7
    {"cite": "Kravitz HM, Ganz PA, Bromberger J, et al. Sleep difficulty in women at midlife: a community survey of sleep and the menopausal transition. Menopause. 2003;10(1):19-28.",
     "html": 'Kravitz HM, et al. <a href="https://doi.org/10.1097/00042192-200310010-00005">Sleep difficulty in women at midlife: a community survey of sleep and the menopausal transition</a>. <i>Menopause</i>, 2003.',
     "verified": "abstract"},
    # 8
    {"cite": "Cienfuegos S, Gabel K, Kalam F, Ezpeleta M, Lin S, Varady KA. Changes in body weight and metabolic risk during time restricted feeding in premenopausal versus postmenopausal women. Experimental Gerontology. 2021;154:111545.",
     "html": 'Cienfuegos S, et al. <a href="https://doi.org/10.1016/j.exger.2021.111545">Changes in body weight and metabolic risk during time restricted feeding in premenopausal versus postmenopausal women</a>. <i>Experimental Gerontology</i>, 2021.',
     "verified": "full text (PMC8464526)"},
    # 9
    {"cite": "Lin S, Lima Oliveira M, Gabel K, et al. Does the weight loss efficacy of alternate day fasting differ according to sex and menopausal status? Nutrition, Metabolism and Cardiovascular Diseases. 2021;31(2):641-649.",
     "html": 'Lin S, et al. <a href="https://doi.org/10.1016/j.numecd.2020.10.018">Does the weight loss efficacy of alternate day fasting differ according to sex and menopausal status?</a> <i>Nutrition, Metabolism and Cardiovascular Diseases</i>, 2021.',
     "verified": "full text (PMC7887029)"},
    # 10
    {"cite": "Kalam F, Akasheh RT, Cienfuegos S, et al. Effect of time-restricted eating on sex hormone levels in premenopausal and postmenopausal females. Obesity. 2023;31(Suppl 1):57-62.",
     "html": 'Kalam F, et al. <a href="https://doi.org/10.1002/oby.23562">Effect of time-restricted eating on sex hormone levels in premenopausal and postmenopausal females</a>. <i>Obesity</i>, 2023.',
     "verified": "abstract (full text PMC9877115 checked for the exclusion of perimenopausal women)"},
    # 11
    {"cite": "Lin S, Cienfuegos S, Ezpeleta M, et al. Effect of time restricted eating versus daily calorie restriction on sex hormones in males and females with obesity. European Journal of Clinical Nutrition. 2024;78(9):814-817.",
     "html": 'Lin S, et al. <a href="https://doi.org/10.1038/s41430-024-01461-5">Effect of time restricted eating versus daily calorie restriction on sex hormones in males and females with obesity</a>. <i>European Journal of Clinical Nutrition</i>, 2024.',
     "verified": "abstract"},
    # 12
    {"cite": "Dai Z, Miyashita M, Poon ET, et al. Flexible time-restricted eating combined with exercise in a free-living setting for middle-aged women with overweight/obesity: a randomized controlled trial. Nature Communications. 2025;16(1):10659.",
     "html": 'Dai Z, et al. <a href="https://doi.org/10.1038/s41467-025-65678-z">Flexible time-restricted eating combined with exercise in a free-living setting for middle-aged women with overweight/obesity: a randomized controlled trial</a>. <i>Nature Communications</i>, 2025.',
     "verified": "full text (PMC12660762)"},
    # 13
    {"cite": "Jóźwiak B, Domin R, Krzywicka M, Laudańska-Krzemińska I. Effect of exercise alone and in combination with time-restricted eating on cardiometabolic health in menopausal women. Journal of Translational Medicine. 2024;22(1):957.",
     "html": 'Jóźwiak B, et al. <a href="https://doi.org/10.1186/s12967-024-05738-y">Effect of exercise alone and in combination with time-restricted eating on cardiometabolic health in menopausal women</a>. <i>Journal of Translational Medicine</i>, 2024.',
     "verified": "full text (PMC11494798)"},
    # 14
    {"cite": "Wang XY, Chen J, Li H. The effects of time-restricted eating combined with Tai Chi on glycolipid metabolism and endothelial function in postmenopausal women. Journal of the International Society of Sports Nutrition. 2025;22(1):2581148.",
     "html": 'Wang XY, et al. <a href="https://doi.org/10.1080/15502783.2025.2581148">The effects of time-restricted eating combined with Tai Chi on glycolipid metabolism and endothelial function in postmenopausal women</a>. <i>Journal of the International Society of Sports Nutrition</i>, 2025.',
     "verified": "abstract"},
    # 15
    {"cite": "Jóźwiak B, Kleka P, Laudańska-Krzemińska I. Effect of exercise alone and in combination with time-restricted eating on cognitive health in menopausal women. Frontiers in Public Health. 2025;13:1640512.",
     "html": 'Jóźwiak B, et al. <a href="https://doi.org/10.3389/fpubh.2025.1640512">Effect of exercise alone and in combination with time-restricted eating on cognitive health in menopausal women</a>. <i>Frontiers in Public Health</i>, 2025.',
     "verified": "abstract"},
    # 16
    {"cite": "Yang Y, Zhu Y, Ossowski Z. Effects of Nordic walking combined with high-protein intake and time-restricted eating on muscle-related outcomes in postmenopausal women: a three-arm randomized controlled trial. Nutrients. 2026;18(15):2470.",
     "html": 'Yang Y, et al. <a href="https://doi.org/10.3390/nu18152470">Effects of Nordic walking combined with high-protein intake and time-restricted eating on muscle-related outcomes in postmenopausal women: a three-arm randomized controlled trial</a>. <i>Nutrients</i>, 2026.',
     "verified": "full text (PMC13467998)"},
    # 17
    {"cite": "Bauer J, Biolo G, Cederholm T, et al. Evidence-based recommendations for optimal dietary protein intake in older people: a position paper from the PROT-AGE Study Group. Journal of the American Medical Directors Association. 2013;14(8):542-559.",
     "html": 'Bauer J, et al. <a href="https://doi.org/10.1016/j.jamda.2013.05.021">Evidence-based recommendations for optimal dietary protein intake in older people: a position paper from the PROT-AGE Study Group</a>. <i>Journal of the American Medical Directors Association</i>, 2013.',
     "verified": "abstract"},
    # 18
    {"cite": "Barnosky A, Kroeger CM, Trepanowski JF, et al. Effect of alternate day fasting on markers of bone metabolism: an exploratory analysis of a 6-month randomized controlled trial. Nutrition and Healthy Aging. 2017;4(3):255-263.",
     "html": 'Barnosky A, et al. <a href="https://doi.org/10.3233/NHA-170031">Effect of alternate day fasting on markers of bone metabolism: an exploratory analysis of a 6-month randomized controlled trial</a>. <i>Nutrition and Healthy Aging</i>, 2017.',
     "verified": "full text (PMC5734119)"},
    # 19
    {"cite": "Villareal DT, Chode S, Parimi N, et al. Weight loss, exercise, or both and physical function in obese older adults. New England Journal of Medicine. 2011;364(13):1218-1229.",
     "html": 'Villareal DT, et al. <a href="https://doi.org/10.1056/NEJMoa1008234">Weight loss, exercise, or both and physical function in obese older adults</a>. <i>New England Journal of Medicine</i>, 2011.',
     "verified": "abstract"},
    # 20
    {"cite": "Watson SL, Weeks BK, Weis LJ, et al. High-intensity resistance and impact training improves bone mineral density and physical function in postmenopausal women with osteopenia and osteoporosis: the LIFTMOR randomized controlled trial. Journal of Bone and Mineral Research. 2018;33(2):211-220.",
     "html": 'Watson SL, et al. <a href="https://doi.org/10.1002/jbmr.3284">High-intensity resistance and impact training improves bone mineral density and physical function in postmenopausal women with osteopenia and osteoporosis: the LIFTMOR randomized controlled trial</a>. <i>Journal of Bone and Mineral Research</i>, 2018.',
     "verified": "abstract"},
    # 21
    {"cite": "Jóźwiak B, Szulc A, Laudańska-Krzemińska I. Time-restricted eating combined with exercise reduces menopausal symptoms and improves quality of life more than exercise alone in menopausal women: a quasi-randomized controlled trial. Nutrients. 2025;17(20):3274.",
     "html": 'Jóźwiak B, et al. <a href="https://doi.org/10.3390/nu17203274">Time-restricted eating combined with exercise reduces menopausal symptoms and improves quality of life more than exercise alone in menopausal women: a quasi-randomized controlled trial</a>. <i>Nutrients</i>, 2025.',
     "verified": "full text (PMC12567392)"},
    # 22
    {"cite": "O'Neill HM, English CJ, Polley M, et al. Dietary interventions for menopausal symptoms: a systematic review. American Journal of Clinical Nutrition. 2026;124(5):101539.",
     "html": 'O\'Neill HM, et al. <a href="https://doi.org/10.1016/j.ajcnut.2026.101539">Dietary interventions for menopausal symptoms: a systematic review</a>. <i>American Journal of Clinical Nutrition</i>, 2026.',
     "verified": "abstract"},
    # 23
    {"cite": "The 2023 nonhormone therapy position statement of The North American Menopause Society. Menopause. 2023;30(6):573-590.",
     "html": 'The North American Menopause Society. <a href="https://doi.org/10.1097/GME.0000000000002200">The 2023 nonhormone therapy position statement of The North American Menopause Society</a>. <i>Menopause</i>, 2023.',
     "verified": "abstract (full text paywalled)"},
    # 24
    {"cite": "The 2022 hormone therapy position statement of The North American Menopause Society. Menopause. 2022;29(7):767-794.",
     "html": 'The North American Menopause Society. <a href="https://doi.org/10.1097/GME.0000000000002028">The 2022 hormone therapy position statement of The North American Menopause Society</a>. <i>Menopause</i>, 2022.',
     "verified": "abstract"},
    # 25
    {"cite": "Mangweth-Matzek B, Hoek HW, Rupp CI, et al. Prevalence of eating disorders in middle-aged women. International Journal of Eating Disorders. 2014;47(3):320-324.",
     "html": 'Mangweth-Matzek B, et al. <a href="https://doi.org/10.1002/eat.22232">Prevalence of eating disorders in middle-aged women</a>. <i>International Journal of Eating Disorders</i>, 2014.',
     "verified": "abstract"},
    # 26
    {"cite": "Grajower MM, Horne BD. Clinical management of intermittent fasting in patients with diabetes mellitus. Nutrients. 2019;11(4):873.",
     "html": 'Grajower MM, Horne BD. <a href="https://doi.org/10.3390/nu11040873">Clinical management of intermittent fasting in patients with diabetes mellitus</a>. <i>Nutrients</i>, 2019.',
     "verified": "full text (PMC6521152), read through a summarising fetch"},
    # 27
    {"cite": "NHS. Post-menopausal bleeding. Page last reviewed 24 September 2026.",
     "html": 'NHS. <a href="https://www.nhs.uk/conditions/post-menopausal-bleeding/">Post-menopausal bleeding</a>.',
     "verified": "full page, read through a summarising fetch"},
]

MENO_BODY = f"""
            <h2>what are perimenopause and menopause?</h2>
            <p>menopause is the last period, and it can only be named looking back: it counts once there have been twelve months without one. the researchers who wrote the standard staging system, STRAW+10, set out the years around it in stages. the early transition begins when cycles start to vary, with a persistent difference of seven days or more between one cycle and the next. the late transition begins with a gap of 60 days or more without a period, and lasts on average one to three years. after the final period, early postmenopause begins with two stages of about a year each, then a further three to six years, roughly five to eight years in all.{n(1)}</p>
            <p>perimenopause, the word most people use, runs in that system from the early transition to twelve months after the final period.{n(1)} in the Study of Women's Health Across the Nation (SWAN), which followed 3,302 women in the United States, the median age at the final period was 52.54 years.{n(2)} the British Menopause Society's summary of the NICE guideline gives the average age as 51.{n(3)}</p>
            <p>NICE advises that blood tests are rarely needed, and should not be used, to diagnose perimenopause or menopause from 45 onwards; FSH, the hormone most often tested, swings too much in these years to say much.{n(3)} the staging system doesn't apply to everyone: after a hysterectomy or endometrial ablation there are no periods to stage by, and STRAW+10 says its bleeding criteria don't apply in polycystic ovary syndrome.{n(1)}</p>

            <h2>what changes in the body?</h2>
            <p>SWAN measured 1,246 women by DXA scan, year after year. before the transition, fat mass rose by about 0.25 kg a year. during it, the rate nearly doubled, to 0.45 kg a year, and lean mass began to fall, by about 0.06 kg a year. across the 3.5 years of the transition that came to about 1.6 kg more fat and 0.2 kg less lean mass. weight itself climbed at much the same pace as before, about 0.25 kg a year, so the scale hid most of the change. the shifts settled about two years after the final period.{n(4)}</p>
            <p>bone changes on the same clock. in SWAN, bone loss began a year before the final period and was fastest from then until two years after it. over ten years, the lower spine lost 10.6% of its density, 7.38% of it in those three years, and the hip's femoral neck lost 9.1%.{n(5)}</p>
            <p>hot flushes and night sweats, when frequent, lasted a median of 7.4 years in SWAN, and went on for a median of 4.5 years after the final period.{n(6)} in a SWAN survey of 12,603 women aged 40 to 55, 38% reported trouble sleeping in the past two weeks, rising to 45.4% in the late transition.{n(7)}</p>

            <h2>what have fasting trials found?</h2>
            <p>the first studies came from a group in Chicago that compared women before and after menopause within the same trials. all were in adults with obesity, and all left out women in perimenopause, because those years bring metabolic changes of their own.{n(8)}{n(9)}</p>
            <ul>
                <li>eight weeks, eating within four to six hours a day: 13 premenopausal and 19 postmenopausal women both lost 3.3% of their weight, and kept to the window about 6.2 days a week. the postmenopausal women lost about 2.1 kg of fat and 1.0 kg of lean mass. there was no comparison group that didn't fast.{n(8)}</li>
                <li>twelve weeks of alternate day fasting, 500 calories on fasting days: 43 premenopausal and 22 postmenopausal women lost 4.6% and 6.5% of their weight, with no significant difference between them. everyone ate 400 to 500 calories more than planned on fasting days.{n(9)}</li>
                <li>hormones in the same eight-week trial: estradiol, estrone and progesterone, measured only after menopause, didn't change. DHEA, an adrenal hormone, fell by about 13%.{n(10)} over twelve months, in 90 adults, an eight-hour window from noon to 8 pm left testosterone, DHEA, SHBG and, after menopause, the estrogens and progesterone unchanged, while weight fell compared with a control group.{n(11)}</li>
            </ul>
            <p>newer trials take in a wider span of midlife:</p>
            <ul>
                <li>twelve weeks, 104 women aged 40 to 60 in Hong Kong, including women before, during and after the transition: an eight-hour window, aerobic exercise, both, or neither. against no change, the window alone lowered fat mass by 1.29 kg, and the window with exercise by 2.85 kg. the authors note that the mix of menopausal stages, and small numbers in each, limit what the subgroups can say.{n(12)}</li>
                <li>twelve weeks, 62 women aged about 51 in Poland: a 16:8 window with circuit training, against the training alone. BMI and systolic blood pressure fell more with the window. groups were not randomised: some women were allocated in turn, others chose their group.{n(13)}</li>
                <li>eight weeks, 142 postmenopausal women aged 50 to 60 in China: an eight-hour window with or without Tai Chi, against usual life. cholesterol and a measure of blood vessel function improved most with both together.{n(14)}</li>
                <li>in the Polish trial, adding the window to exercise brought no extra benefit on tests of memory and attention.{n(15)}</li>
            </ul>
            <p>read together: after menopause, eating within a window led to weight loss about as large as it did before menopause, over weeks to a few months. some of what was lost was lean mass. the trials are small and short, most are in women with higher weight, and the longest ran a year. none was designed to show what happens across the whole transition.</p>

            <figure class="fig" style="margin:2em 0"><div role="img" aria-label="the stages of reproductive ageing, from cycles that start to vary, through gaps of two months or more, to the final period and the years after it. most fasting trials studied women after menopause; two included women in perimenopause. none tested hot flushes as the main outcome." style="font-size:.9em;line-height:1.4"><div style="overflow-x:auto;-webkit-overflow-scrolling:touch;margin-bottom:6px"><div style="display:flex;min-width:480px;border:1px solid var(--rule);border-left:0"><div style="flex:1 1 0;min-width:0;padding:8px 6px;border-left:1px solid var(--rule)"><div style="font-size:.8em;color:var(--muted)">-2</div><div>early transition</div><div style="font-size:.8em;color:var(--soft);font-style:italic">cycles vary by 7 days or more</div></div><div style="flex:1 1 0;min-width:0;padding:8px 6px;border-left:1px solid var(--rule)"><div style="font-size:.8em;color:var(--muted)">-1</div><div>late transition</div><div style="font-size:.8em;color:var(--soft);font-style:italic">60 days or more without a period</div></div><div style="flex:1 1 0;min-width:0;padding:8px 6px;border-left:1px solid var(--rule)"><div style="font-size:.8em;color:var(--muted)">0</div><div>the final period</div><div style="font-size:.8em;color:var(--soft);font-style:italic">known after 12 months</div></div><div style="flex:1 1 0;min-width:0;padding:8px 6px;border-left:1px solid var(--rule)"><div style="font-size:.8em;color:var(--muted)">+1</div><div>the first years after</div><div style="font-size:.8em;color:var(--soft);font-style:italic"></div></div><div style="flex:1 1 0;min-width:0;padding:8px 6px;border-left:1px solid var(--rule)"><div style="font-size:.8em;color:var(--muted)">+2</div><div>late postmenopause</div><div style="font-size:.8em;color:var(--soft);font-style:italic"></div></div></div></div><p style="margin:0 0 18px;font-size:.88em;color:var(--soft)">perimenopause runs from stage −2 to a year after the final period. fat gain doubles, lean mass falls and most bone is lost from the late transition into the first years after.</p><div style="display:flex;flex-wrap:wrap;gap:16px 32px"><div style="flex:1 1 240px;min-width:0"><p style="margin:0 0 4px;font-style:italic;color:var(--rose)">studied after menopause only</p><ul style="list-style:none;margin:0;padding:0"><li style="display:flex;gap:10px;padding:6px 0;border-top:1px solid var(--rule)"><span aria-hidden="true" style="flex:none;width:9px;height:9px;margin-top:.45em;border:1.2px solid var(--rose)"></span><span>8 weeks, a 4 to 6 hour window, 19 women</span></li><li style="display:flex;gap:10px;padding:6px 0;border-top:1px solid var(--rule)"><span aria-hidden="true" style="flex:none;width:9px;height:9px;margin-top:.45em;border:1.2px solid var(--rose)"></span><span>12 weeks, alternate days, 22 women</span></li><li style="display:flex;gap:10px;padding:6px 0;border-top:1px solid var(--rule)"><span aria-hidden="true" style="flex:none;width:9px;height:9px;margin-top:.45em;border:1.2px solid var(--rose)"></span><span>12 weeks, a 10 hour window, 100 women</span></li><li style="display:flex;gap:10px;padding:6px 0;border-top:1px solid var(--rule)"><span aria-hidden="true" style="flex:none;width:9px;height:9px;margin-top:.45em;border:1.2px solid var(--rose)"></span><span>8 weeks, an 8 hour window, 142 women</span></li></ul></div><div style="flex:1 1 240px;min-width:0"><p style="margin:0 0 4px;font-style:italic;color:var(--rose)">perimenopause included</p><ul style="list-style:none;margin:0;padding:0"><li style="display:flex;gap:10px;padding:6px 0;border-top:1px solid var(--rule)"><span aria-hidden="true" style="flex:none;width:9px;height:9px;margin-top:.45em;background:var(--rose)"></span><span>12 weeks, an 8 hour window, 104 women aged 40 to 60</span></li><li style="display:flex;gap:10px;padding:6px 0;border-top:1px solid var(--rule)"><span aria-hidden="true" style="flex:none;width:9px;height:9px;margin-top:.45em;background:var(--rose)"></span><span>12 weeks, 16:8 with exercise, 54 to 62 women</span></li></ul></div></div><p style="margin:12px 0 0;font-size:.88em;color:var(--muted)">no fasting trial has tested hot flushes as its main outcome.</p></div><figcaption style="margin-top:.8em;font-size:.88em;font-style:italic;color:var(--soft)">where the trials sit in the transition.</figcaption></figure>
            <h2>what about muscle?</h2>
            <p>any way of eating less tends to take some muscle with the fat, and in the Chicago trials about a third of the weight lost after menopause was lean mass.{n(8)}{n(9)} in a 2026 trial of 100 postmenopausal women, every group did Nordic walking. those who also kept a ten-hour window and ate about 1.4 g of protein per kilogram of body weight a day gained 1.19 kg of lean mass in the arms and legs over twelve weeks. those who kept the window without the protein target gained 0.04 kg, about none, and lost a little in the legs.{n(16)} the authors say the result compares packages, not single parts.</p>
            <p>for people over 65, an expert group recommends at least 1.0 to 1.2 g of protein per kilogram a day, and 1.2 g or more for those who exercise.{n(17)} that was written for older adults, not for menopause in particular, but it points the same way: a shorter eating window still needs enough protein inside it.</p>

            <h2>and bone?</h2>
            <p>the fasting evidence on bone is thin. in a six-month trial of alternate day fasting in 100 adults, bone density and markers of bone turnover didn't change, and they didn't differ between women before and after menopause.{n(18)} we found no fasting trial in women with osteoporosis, and none that followed bone after menopause for longer than six months.</p>
            <p>what is better known is that losing weight can cost bone. in a year-long trial in adults over 65 with obesity, those who lost weight by diet alone lost 3% of their hip bone density and 5% of their lean mass. those who also exercised lost 1% and 3%.{n(19)} that trial wasn't about fasting, or only about women, but the lesson carries: eating less without moving more asks more of the skeleton.</p>
            <p>exercise has the stronger evidence. in the LIFTMOR trial, 101 postmenopausal women with low bone mass did eight months of supervised heavy resistance and impact training, twice a week for 30 minutes. their lower spine density rose 2.9%, against a fall of 1.2% in the low-intensity group, and one adverse event was reported.{n(20)} that was under close supervision; heavy lifting with low bone density is something to start with a professional.</p>

            <h2>hot flushes and sleep</h2>
            <p>no trial has tested fasting with hot flushes as its main outcome. the nearest is the Polish trial: 54 women finished twelve weeks of training, with or without a 16:8 window. total menopause symptom scores fell more in the window group, but there was no difference in the vasomotor part, the hot flushes and night sweats, and no change in sleep quality. groups were partly chosen by the women themselves, a third dropped out, and the authors list selection bias among the limits.{n(21)}</p>
            <p>in the Hong Kong trial, sleep quality didn't change in any group. six women in the two window groups reported hunger that may have affected their sleep in the first two weeks, which eased as they adapted.{n(12)} a 2026 systematic review of diets for menopausal symptoms found the evidence for intermittent fasting limited.{n(22)}</p>
            <p>so there is no evidence that fasting eases hot flushes or helps sleep in menopause. the Menopause Society's 2023 statement on treatments other than hormones recommends cognitive behavioural therapy, clinical hypnosis, some prescription medicines and, at a lower level of evidence, weight loss, and does not recommend dietary modification for hot flushes.{n(23)}</p>

            <h2>hormone therapy is a conversation for a doctor</h2>
            <p>the Menopause Society (then the North American Menopause Society) says in its 2022 statement that hormone therapy remains the most effective treatment for hot flushes and night sweats, and has been shown to prevent bone loss and fracture. for those under 60, or within ten years of menopause, without reasons not to take it, it judges the balance of benefit and risk favourable. the risks depend on the type, dose, route, timing and length of use.{n(24)}</p>
            <p>NICE, in England, says hormone replacement therapy should be offered for hot flushes and sweats after the benefits and risks have been weighed, and that menopause-specific cognitive behavioural therapy can be considered alongside it, or instead of it, including for sleep broken by night sweats. it also suggests advice on diet and lifestyle, such as stopping smoking, weight loss, less alcohol and more exercise.{n(3)}</p>
            <p>none of that is something a timer can decide. if symptoms are wearing you down, a doctor can go through the options with you, and fasting is no substitute for that conversation.</p>

            <h2>who shouldn't fast, or should ask first</h2>
            <ul>
                <li>anyone with a current or past eating disorder. they don't stop at 40: in a survey of 715 Austrian women aged 40 to 60, 4.6% met full criteria for an eating disorder, mostly binge eating disorder and related forms.{n(25)} a fast that turns into a rule you can't break is a reason to stop.</li>
                <li>anyone with diabetes on insulin or a sulfonylurea, such as glipizide, glimepiride or glyburide. these can cause low blood sugar when you don't eat, and an expert review advises lower doses on fasting days, with a doctor's guidance; metformin can usually be continued.{n(26)} don't change a dose on your own.</li>
                <li>anyone with osteoporosis, low bone density or a past fracture from a small fall. there is no fasting trial to go on, and weight loss can cost bone.{n(19)}</li>
                <li>anyone on or starting hormone therapy who has bleeding they didn't expect. NICE advises seeking help promptly for unscheduled bleeding after the first three months.{n(3)}</li>
                <li>anyone who bleeds after menopause, even a small amount or only once. the NHS advises seeing a GP.{n(27)} it isn't a new cycle to log; it's a reason to be checked.</li>
            </ul>

            <h2>what if your periods are irregular, or have stopped?</h2>
            <p>then hours suggested for each phase of the cycle may not fit you. in the late transition, gaps of two months or more are part of the definition,{n(1)} and ovulation doesn't follow a calendar. no trial has tested fasting by phase in anyone, and in perimenopause there is nothing at all to go on. after menopause there is no cycle to follow.</p>
            <p>hæl counts the phase from the day your last period began and the cycle length it knows, which it keeps between 21 and 45 days. if a period comes later than that, it counts on as though a new cycle had begun, so until you enter the next period, the phase on screen is a guess. when gaps grow long, the guess is often wrong, and turning the cycle off is the more honest choice.</p>
            <p>without a cycle, hæl doesn't invent one. the ledger draws the month by the moon, with your fasts round it, and home shows the moon's phase under the dial. the moon is only a calendar there, a way to see a month at a glance; hæl makes no claim that it moves the body, or that it has anything to do with menopause.</p>

            <h2>setting up hæl in perimenopause or after menopause</h2>
            <ol>
                <li>on the first page, hæl asks when your last cycle began. if periods still come, give the day. if they've stopped, or come too rarely to count, choose "I don't keep one". you can change either later, in settings, under the cycle.</li>
                <li>if you keep a cycle through perimenopause, enter each period when it comes: in settings, change the date of your last period, or log it in Apple Health and hæl reads it from there.</li>
                <li>when the gaps grow long, or a year has passed without a period, turn off "track a cycle" in settings, under the cycle. the ring keeps the hours alone.</li>
                <li>start at twelve hours. turn the dial to twelve and press begin. lengthen slowly, if at all, and keep enough protein in the hours you eat.</li>
                <li>keep rest days. under begin is rest. press it on a day you won't fast, and the ledger keeps the day as rest rather than a gap.</li>
                <li>read the scale slowly. without a cycle, the body ledger draws the last 28 days against your usual weight over the last 90, with the month before beside it. in these years the scale can stay flat while fat and muscle shift underneath,{n(4)} so the trend over months says more than any morning.</li>
            </ol>
            <p>the timer, the ledger and rest days are free. the hours for each phase and the readings are part of the full witness. <a href="/cycle-syncing-fasting/">how hæl reads the cycle</a>.</p>

            <div class="aside">
                <p>hæl doesn't treat menopause or its symptoms, and neither does fasting. it keeps the hours you choose, works just as well without a cycle, and keeps the month by the moon only as a calendar. there are no badges and no coaching.</p>
                <a class="download" href="{STORE}">hæl on the App Store</a>
            </div>
"""

# for APPNOTES in build_notes.py: (campaign token, one true sentence)
MENO_APPNOTE = ("article-menopause", "hæl, a fasting timer for iPhone, works without a cycle: when periods stop, the ledger keeps the month by the moon, as a calendar and nothing more.")

MENO_NOTE = dict(
    slug="intermittent-fasting-menopause",
    title="Intermittent Fasting in Perimenopause and Menopause: What the Research Shows | hæl",
    description="what trials of intermittent fasting in perimenopause and after menopause found for weight, muscle, bone, hot flushes and sleep, and who shouldn't fast.",
    kicker="the transition",
    h1="intermittent fasting in perimenopause and menopause",
    headline="intermittent fasting in perimenopause and menopause: what the research shows",
    short="in small, short trials, eating within a window led to weight loss after menopause much as it did before it, and some of the loss was muscle. no trial shows that fasting eases hot flushes or helps sleep; hormone therapy remains the most effective treatment for hot flushes, and that is a conversation for a doctor. keep protein up, keep lifting, and with an eating disorder history, on insulin or sulfonylureas, or with low bone density, ask first.",
    body=MENO_BODY, sources=MENO_SOURCES,
    published="2026-11-09", published_text="november 9, 2026",
    appnote=MENO_APPNOTE,
)

if __name__ == "__main__":
    # quick self-checks only; builds nothing
    import re
    text = MENO_BODY + MENO_NOTE["short"] + MENO_NOTE["description"] + MENO_APPNOTE[1] + MENO_NOTE["h1"] + MENO_NOTE["headline"]
    assert "—" not in text and "–" not in text, "dash found"
    assert "!" not in text, "exclamation found"
    assert not re.search(r"\b(she|her|hers|herself)\b", text, re.I), "she/her found"
    assert len(MENO_NOTE["description"]) < 160, len(MENO_NOTE["description"])
    used = sorted({int(x) for x in re.findall(r'href="#s(\d+)"', MENO_BODY)})
    assert used == list(range(1, len(MENO_SOURCES) + 1)), used
    assert all(set(s) == {"cite", "html", "verified"} for s in MENO_SOURCES), "source keys"
    print("ok:", len(MENO_SOURCES), "sources, description", len(MENO_NOTE["description"]), "chars")
