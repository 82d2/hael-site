"""DRAFT, not built or linked: PCOS and intermittent fasting, what the research shows.
To publish later: move PCOS_SOURCES / PCOS_BODY into _tools/build_notes.py, add
PCOS_APPNOTE to APPNOTES and PCOS_NOTE to NOTES. Research notes and what was
verified in full text: _drafts/pcos-research.md. Current as of 2026-11-04.

<!--
VISUAL SPECS

1. Explanatory diagram: "what the comparison was"
   Place: after the trials list, before "what about androgens and periods?".
   Drawn simply: two columns of rows, hairline rules, the site's serif, no
   colour coding alone (use a filled dot for "lost more weight", a hollow
   dot for "about the same").
   Left column head: "against eating as usual"
     - 6 weeks, 75 women, 10-hour window: lost more weight, lower insulin  (filled)
     - 6 months, 76 women, 6-hour window: lost more weight (-4.32%)        (filled)
     - 12-week crossover, 11 women, 6-hour window: lost more weight,
       exploratory only                                                   (filled)
   Right column head: "against cutting calories"
     - 8 weeks, 90 women, 10-hour window: about the same (2 to 3 kg each)  (hollow)
     - 6 months, 76 women, 6-hour window: about the same
       (-4.32% vs -4.66%)                                                 (hollow)
     - 16 weeks, 93 women, 8-hour window on the same calorie target:
       about 3 kg more (-7.47 vs -4.38 kg)                                (filled)
   Footer line, small: "periods: no clear change in the two trials that
   compared them (8 weeks; 6 months)."
   Alt text: "in five randomised trials in PCOS, eating within a window led to
   more weight loss than eating as usual, and about the same as cutting
   calories, except where it was added to a calorie target. periods did not
   clearly change."
   Sources for every figure: Talebi 2024, Aminian 2026, Zheng 2025,
   Corapi 2026, Floyd 2026, Hamsho 2026 (see PCOS_SOURCES).

2. App screen: home with no cycle kept (needs a fresh capture; none of
   /screenshots or /images shows it). Settings > the cycle > "track a cycle"
   off, dial turned to 12, before begin. Shows the ring at 12 hours, the
   moon's four marks and the night's line under the suggestion, begin and
   rest. Do not use screenshots/ledger.png (it shows "1 day in a row" and
   cycle phases) or ring.png (it shows "day 14" of a cycle).
   Caption: "without a cycle, hæl keeps the hours alone. twelve is a fair
   place to start, and rest is one press away."

3. OG image, 1200x630, the site's cream ground and serif:
   line 1 (large): "PCOS and intermittent fasting"
   line 2: "what the research shows, and what it doesn't"
   foot, small: "hæl · hael.app"
-->
"""

STORE = "https://apps.apple.com/app/id6778956802"


def n(i):
    return f'<sup><a href="#s{i}">{i}</a></sup>'


# "verified": "full text" = read in full; "abstract" = PubMed abstract only;
# "secondary" = press release or summary. build_notes.page() reads only
# "html" and "cite", so the extra key is safe to keep.
PCOS_SOURCES = [
    {"cite": "Teede HJ, Tay CT, Laven JJE, et al. Recommendations from the 2023 International Evidence-based Guideline for the Assessment and Management of Polycystic Ovary Syndrome. Human Reproduction. 2023;38(9):1655-1679.",
     "html": 'Teede HJ, et al. <a href="https://doi.org/10.1093/humrep/dead156">Recommendations from the 2023 International Evidence-based Guideline for the Assessment and Management of Polycystic Ovary Syndrome</a>. <i>Human Reproduction</i>, 2023.',
     "verified": "full text (PMC10477934)"},
    {"cite": "Bozdag G, Mumusoglu S, Zengin D, Karabulut E, Yildiz BO. The prevalence and phenotypic features of polycystic ovary syndrome: a systematic review and meta-analysis. Human Reproduction. 2016;31(12):2841-2855.",
     "html": 'Bozdag G, et al. <a href="https://doi.org/10.1093/humrep/dew218">The prevalence and phenotypic features of polycystic ovary syndrome: a systematic review and meta-analysis</a>. <i>Human Reproduction</i>, 2016.',
     "verified": "abstract"},
    {"cite": "Teede HJ, Khomami MB, Morman R, et al. Polyendocrine metabolic ovarian syndrome, the new name for polycystic ovary syndrome: a multistep global consensus process. Lancet. 2026;407(10545):2329-2339.",
     "html": 'Teede HJ, et al. <a href="https://doi.org/10.1016/S0140-6736(26)00717-8">Polyendocrine metabolic ovarian syndrome, the new name for polycystic ovary syndrome: a multistep global consensus process</a>. <i>The Lancet</i>, 2026;407(10545):2329-39 (epub May 12, 2026).',
     "verified": "abstract read on PubMed (PMID 42119588), 2026-11-04: the name, the reasons, the 56 organisations, the 14,360 survey responses, one in eight, the transition"},
    {"cite": "Cassar S, Misso ML, Hopkins WG, Shaw CS, Teede HJ, Stepto NK. Insulin resistance in polycystic ovary syndrome: a systematic review and meta-analysis of euglycaemic-hyperinsulinaemic clamp studies. Human Reproduction. 2016;31(11):2619-2631.",
     "html": 'Cassar S, et al. <a href="https://doi.org/10.1093/humrep/dew243">Insulin resistance in polycystic ovary syndrome: a systematic review and meta-analysis of euglycaemic-hyperinsulinaemic clamp studies</a>. <i>Human Reproduction</i>, 2016.',
     "verified": "abstract"},
    {"cite": "Endocrine Society. Polycystic ovary syndrome (PCOS). Endocrine Library. 2022.",
     "html": 'Endocrine Society. <a href="https://www.endocrine.org/patient-engagement/endocrine-library/pcos">Polycystic ovary syndrome (PCOS)</a>.',
     "verified": "full page"},
    {"cite": "Li C, Xing C, Zhang J, Zhao H, Shi W, He B. Eight-hour time-restricted feeding improves endocrine and metabolic profiles in women with anovulatory polycystic ovary syndrome. Journal of Translational Medicine. 2021;19:148.",
     "html": 'Li C, et al. <a href="https://doi.org/10.1186/s12967-021-02817-2">Eight-hour time-restricted feeding improves endocrine and metabolic profiles in women with anovulatory polycystic ovary syndrome</a>. <i>Journal of Translational Medicine</i>, 2021.',
     "verified": "full text (PMC8045367)"},
    {"cite": "Feyzioglu BS, Güven CM, Avul Z. Eight-hour time-restricted feeding: a strong candidate diet protocol for first-line therapy in polycystic ovary syndrome. Nutrients. 2023;15(10):2260.",
     "html": 'Feyzioglu BS, et al. <a href="https://doi.org/10.3390/nu15102260">Eight-hour time-restricted feeding: a strong candidate diet protocol for first-line therapy in polycystic ovary syndrome</a>. <i>Nutrients</i>, 2023.',
     "verified": "abstract"},
    {"cite": "Talebi S, Shab-Bidar S, Moini A, Mohammadi H, Djafarian K. The effects of time-restricted eating alone or in combination with probiotic supplementation in comparison with a calorie-restricted diet on endocrine and metabolic profiles in women with polycystic ovary syndrome: a randomized clinical trial. Diabetes, Obesity and Metabolism. 2024;26(10):4468-4479.",
     "html": 'Talebi S, et al. <a href="https://doi.org/10.1111/dom.15801">The effects of time-restricted eating alone or in combination with probiotic supplementation in comparison with a calorie-restricted diet on endocrine and metabolic profiles in women with polycystic ovary syndrome: a randomized clinical trial</a>. <i>Diabetes, Obesity and Metabolism</i>, 2024.',
     "verified": "abstract"},
    {"cite": "Aminian M, Hajshafiha M, Heidari M, Daneghian S. Effect of two types of time-restricted eating on glycemic, lipid indices, and weight in women with polycystic ovary syndrome: a randomized controlled trial. European Journal of Nutrition. 2026;65(5):173.",
     "html": 'Aminian M, et al. <a href="https://doi.org/10.1007/s00394-026-04034-3">Effect of two types of time-restricted eating on glycemic, lipid indices, and weight in women with polycystic ovary syndrome: a randomized controlled trial</a>. <i>European Journal of Nutrition</i>, 2026.',
     "verified": "abstract"},
    {"cite": "Zheng S, Chen Y, Zheng X, et al. Time-restricted eating plus calorie-restricted diet versus calorie-restricted diet in women with polycystic ovary syndrome. iScience. 2025;28(11):113654.",
     "html": 'Zheng S, et al. <a href="https://doi.org/10.1016/j.isci.2025.113654">Time-restricted eating plus calorie-restricted diet versus calorie-restricted diet in women with polycystic ovary syndrome</a>. <i>iScience</i>, 2025.',
     "verified": "abstract"},
    {"cite": "Corapi S, Runchey MC, Lyons J, et al. Time-restricted eating for body weight management in women with polycystic ovary syndrome: a randomized controlled trial. Nature Medicine. 2026;32(6):2155-2163.",
     "html": 'Corapi S, et al. <a href="https://doi.org/10.1038/s41591-026-04316-7">Time-restricted eating for body weight management in women with polycystic ovary syndrome: a randomized controlled trial</a>. <i>Nature Medicine</i>, 2026.',
     "verified": "abstract (full text paywalled)"},
    {"cite": "Floyd R, Dyer A, Gibney J, et al. Time-restricted eating to improve metabolic abnormalities in polycystic ovarian syndrome (TimeMAP). Clinical Endocrinology. 2026;104(4):327-342.",
     "html": 'Floyd R, et al. <a href="https://doi.org/10.1111/cen.70094">Time-restricted eating to improve metabolic abnormalities in polycystic ovarian syndrome (TimeMAP)</a>. <i>Clinical Endocrinology</i>, 2026.',
     "verified": "abstract"},
    {"cite": "University of Illinois Chicago. Study: intermittent fasting positively affects female hormones in PCOS. UIC Today. March 27, 2026.",
     "html": 'University of Illinois Chicago. <a href="https://today.uic.edu/study-intermittent-fasting-positively-affects-female-hormones-in-pcos/">Study: intermittent fasting positively affects female hormones in PCOS</a>. <i>UIC Today</i>, 2026.',
     "verified": "secondary (press release)"},
    {"cite": "Hamsho M, Bensaoua M, Shkorfu W, Ranneh Y, Kalam F. The effects of time-restricted eating in women with polyendocrine metabolic ovarian syndrome: a systematic review and meta-analysis. Nutrients. 2026;18(13):2096.",
     "html": 'Hamsho M, et al. <a href="https://doi.org/10.3390/nu18132096">The effects of time-restricted eating in women with polyendocrine metabolic ovarian syndrome: a systematic review and meta-analysis</a>. <i>Nutrients</i>, 2026.',
     "verified": "full text (PMC13363535), read through a summarising fetch"},
    {"cite": "American College of Obstetricians and Gynecologists. Polycystic ovary syndrome (PCOS). Frequently asked questions.",
     "html": 'American College of Obstetricians and Gynecologists. <a href="https://www.acog.org/womens-health/faqs/polycystic-ovary-syndrome-pcos">Polycystic ovary syndrome (PCOS)</a>.',
     "verified": "full page"},
    {"cite": "Ranneh Y, Hamsho M, Shkorfu W, Terzi M, Fadel A. Effect of intermittent fasting on anthropometric measurements, metabolic profile, and hormones in women with polycystic ovary syndrome: a systematic review and meta-analysis. Nutrients. 2025;17(15):2436.",
     "html": 'Ranneh Y, et al. <a href="https://doi.org/10.3390/nu17152436">Effect of intermittent fasting on anthropometric measurements, metabolic profile, and hormones in women with polycystic ovary syndrome: a systematic review and meta-analysis</a>. <i>Nutrients</i>, 2025.',
     "verified": "abstract"},
    {"cite": "Aolymat I, Abumweis S, Al-Momani H, et al. The impact of intermittent fasting on metabolic and hormonal profile in patients with polycystic ovary syndrome: a systematic review and meta-analysis. Metabolites. 2025;15(10):654.",
     "html": 'Aolymat I, et al. <a href="https://doi.org/10.3390/metabo15100654">The impact of intermittent fasting on metabolic and hormonal profile in patients with polycystic ovary syndrome: a systematic review and meta-analysis</a>. <i>Metabolites</i>, 2025.',
     "verified": "abstract"},
    {"cite": "Gibson-Helm M, Teede H, Dunaif A, Dokras A. Delayed diagnosis and a lack of information associated with dissatisfaction in women with polycystic ovary syndrome. Journal of Clinical Endocrinology and Metabolism. 2017;102(2):604-612.",
     "html": 'Gibson-Helm M, et al. <a href="https://doi.org/10.1210/jc.2016-2963">Delayed diagnosis and a lack of information associated with dissatisfaction in women with polycystic ovary syndrome</a>. <i>Journal of Clinical Endocrinology and Metabolism</i>, 2017.',
     "verified": "abstract"},
    {"cite": "Lim S, Smith CA, Costello MF, MacMillan F, Moran L, Ee C. Barriers and facilitators to weight management in overweight and obese women living in Australia with PCOS: a qualitative study. BMC Endocrine Disorders. 2019;19:106.",
     "html": 'Lim S, et al. <a href="https://doi.org/10.1186/s12902-019-0434-8">Barriers and facilitators to weight management in overweight and obese women living in Australia with PCOS: a qualitative study</a>. <i>BMC Endocrine Disorders</i>, 2019.',
     "verified": "abstract"},
    {"cite": "Ee C, Smith C, Moran L, et al. \"The whole package deal\": experiences of overweight/obese women living with polycystic ovary syndrome. BMC Women's Health. 2020;20:221.",
     "html": 'Ee C, et al. <a href="https://doi.org/10.1186/s12905-020-01090-7">"The whole package deal": experiences of overweight/obese women living with polycystic ovary syndrome</a>. <i>BMC Women\'s Health</i>, 2020.',
     "verified": "abstract"},
    {"cite": "Cooney LG, Gyorfi K, Sanneh A, et al. Increased prevalence of binge eating disorder and bulimia nervosa in women with polycystic ovary syndrome: a systematic review and meta-analysis. Journal of Clinical Endocrinology and Metabolism. 2024;109(12):3293-3305.",
     "html": 'Cooney LG, et al. <a href="https://doi.org/10.1210/clinem/dgae462">Increased prevalence of binge eating disorder and bulimia nervosa in women with polycystic ovary syndrome: a systematic review and meta-analysis</a>. <i>Journal of Clinical Endocrinology and Metabolism</i>, 2024.',
     "verified": "abstract"},
    {"cite": "Grajower MM, Horne BD. Clinical management of intermittent fasting in patients with diabetes mellitus. Nutrients. 2019;11(4):873.",
     "html": 'Grajower MM, Horne BD. <a href="https://doi.org/10.3390/nu11040873">Clinical management of intermittent fasting in patients with diabetes mellitus</a>. <i>Nutrients</i>, 2019.',
     "verified": "full text (PMC6521152), read through a summarising fetch"},
]

PCOS_BODY = f"""
            <h2>what is PCOS?</h2>
            <p>polycystic ovary syndrome is a condition of hormones and metabolism, not only of the ovaries. by the Rotterdam criteria it affects 10 to 13% of women worldwide, according to the 2023 international guideline,{n(1)} and a meta-analysis of prevalence studies put it at 10% by the same criteria.{n(2)} it is one of the most common hormonal conditions of the reproductive years.</p>
            <h2>a new name: PMOS</h2>
            <p>in May 2026 the condition was given a new name: polyendocrine metabolic ovarian syndrome, or PMOS. the name came from a global consensus process led from Monash University and published in the Lancet, with 56 academic, clinical and patient organisations taking part and survey responses from 14,360 people with PCOS and health professionals across every world region.{n(3)}</p>
            <p>the reasons are in the paper itself. the old name implies pathological ovarian cysts, which are not what the condition is, and it hides the endocrine and metabolic sides of it, which the authors link to delayed diagnosis, fragmented care and stigma. the new name drops the cysts and names the three things it involves: several hormones, metabolism, and the ovaries. the consensus puts the condition at one in eight women.{n(3)}</p>
            <p>the change is happening gradually, with a transition period, education, and work to bring health systems and disease classification in line.{n(3)} the trials on this page were all run and published under the old name, and most people still search for it, so this page says PCOS throughout. it means the same condition.</p>

            <h2>how is it diagnosed?</h2>
            <p>in adults, by two of three features, once other causes are ruled out: signs of high androgens, such as excess hair growth or high testosterone on a blood test; ovulation that is irregular or absent; and polycystic ovaries on an ultrasound, or, since 2023, a high AMH blood level instead of the scan. in adolescents, the first two are both needed.{n(1)}</p>
            <p>"irregular" has a definition. from three years after a first period until perimenopause, the guideline counts cycles shorter than 21 days or longer than 35, fewer than eight cycles a year, or any one cycle longer than 90 days.{n(1)} for many people with PCOS, periods come late, rarely, or not at all. that matters for anything built on the cycle, hæl included.</p>

            <h2>where does insulin come in?</h2>
            <p>the guideline calls insulin resistance part of how PCOS works.{n(1)} across 28 studies that measured it with the most exact method, the insulin clamp, women with PCOS were about 27% less sensitive to insulin than women without it, and a higher BMI lowered sensitivity a further 15% in PCOS compared with controls.{n(4)} when the body answers insulin less, it makes more of it, and high insulin may worsen androgen excess.{n(5)}</p>
            <p>the guideline also notes a higher risk of prediabetes and type 2 diabetes in PCOS, at any age and any weight. it doesn't recommend routine insulin blood tests, because they say little in practice.{n(1)}</p>

            <h2>what does the guideline say about diet?</h2>
            <p>that no one type of diet has been shown to work better than another in PCOS, for weight, metabolism, hormones, fertility or mood. any way of eating that fits ordinary healthy-eating advice has benefits, and it should suit the person, avoiding diets that are unduly restrictive or unbalanced. where weight loss is the goal, it suggests a tailored energy deficit, eating a little less than the body uses, and it says a healthy lifestyle has benefits even when weight doesn't change.{n(1)} its published recommendations don't mention intermittent fasting by name.</p>
            <p>in that light, fasting is one way of arranging an energy deficit, not a treatment of its own. the trials below mostly test whether the arrangement helps.</p>

            <h2>what have fasting trials in PCOS found?</h2>
            <p>the study cited most is from 2021. 18 women with PCOS who weren't ovulating ate only between 8 am and 4 pm for five weeks, and 15 finished. their weight fell a little, from a median of 74.7 to 73.4 kg, and insulin and the free androgen index, a measure of active testosterone, fell too.{n(6)} there was no comparison group, so it can't say how much came from the window. a 2023 study of 30 women on an eight-hour window for six weeks found similar changes, also without one.{n(7)}</p>
            <p>randomised trials are newer:</p>
            <ul>
                <li>eight weeks, 90 women: a ten-hour window from 8 am to 6 pm, with or without a probiotic, against three meals a day on a calorie-restricted diet. every group lost about 2 to 3 kg, and the window made no difference to weight, metabolism, periods or hormones.{n(8)}</li>
                <li>six weeks, 75 women: a ten-hour window, early (8 am to 6 pm) or mid-day (11 am to 9 pm), against eating as usual. both windows lowered fasting insulin, insulin resistance, weight and waist compared with eating as usual.{n(9)}</li>
                <li>sixteen weeks, 93 women: everyone was given 1,200 to 1,500 calories a day, and half ate them within eight hours. the window group lost 7.47 kg and the others 4.38 kg, about 3 kg more.{n(10)}</li>
                <li>six months, 76 women, the largest trial so far: eating between 1 pm and 7 pm without counting calories, against cutting calories by a quarter, against no change. compared with no change, weight fell 4.32% with the window and 4.66% with calorie cutting, and the two diets didn't differ.{n(11)}</li>
                <li>twelve weeks each way, in a crossover study in Ireland: of 70 women eligible, 15 joined and 11 finished. those who finished kept an 18:6 window on about 95% of days, and weight and HbA1c, a three-month measure of blood sugar, fell compared with eating as usual, in an analysis the study wasn't designed to test.{n(12)}</li>
            </ul>
            <p>read together: against eating as usual, a window helped with weight and insulin. against an equal effort at eating less, it mostly did about as well, not better. in the one trial where it did better, the window was added to a calorie target, not used instead of one.</p>

            <figure class="fig" style="margin:2em 0"><div role="img" aria-label="in randomised trials in PCOS, eating within a window led to more weight loss than eating as usual, and about the same as cutting calories, except where it was added to a calorie target. periods did not clearly change." style="display:flex;flex-wrap:wrap;gap:20px 32px;font-size:.92em;line-height:1.45"><div style="flex:1 1 240px;min-width:0"><p style="margin:0 0 6px;font-style:italic;color:var(--rose)">against eating as usual</p><ul style="list-style:none;margin:0;padding:0"><li style="display:flex;gap:10px;padding:8px 0;border-top:1px solid var(--rule)"><span aria-hidden="true" style="flex:none;width:9px;height:9px;margin-top:.45em;border-radius:50%;background:var(--rose)"></span><span>6 weeks, 75 women, a 10-hour window: lost more weight, lower insulin.</span></li><li style="display:flex;gap:10px;padding:8px 0;border-top:1px solid var(--rule)"><span aria-hidden="true" style="flex:none;width:9px;height:9px;margin-top:.45em;border-radius:50%;background:var(--rose)"></span><span>6 months, 76 women, a 6-hour window: lost more weight, 4.32%.</span></li><li style="display:flex;gap:10px;padding:8px 0;border-top:1px solid var(--rule)"><span aria-hidden="true" style="flex:none;width:9px;height:9px;margin-top:.45em;border-radius:50%;background:var(--rose)"></span><span>12 weeks, 11 women, a 6-hour window: lost more weight. exploratory only.</span></li></ul></div><div style="flex:1 1 240px;min-width:0"><p style="margin:0 0 6px;font-style:italic;color:var(--rose)">against cutting calories</p><ul style="list-style:none;margin:0;padding:0"><li style="display:flex;gap:10px;padding:8px 0;border-top:1px solid var(--rule)"><span aria-hidden="true" style="flex:none;width:9px;height:9px;margin-top:.45em;border-radius:50%;border:1.2px solid var(--rose)"></span><span>8 weeks, 90 women, a 10-hour window: about the same, 2 to 3 kg each.</span></li><li style="display:flex;gap:10px;padding:8px 0;border-top:1px solid var(--rule)"><span aria-hidden="true" style="flex:none;width:9px;height:9px;margin-top:.45em;border-radius:50%;border:1.2px solid var(--rose)"></span><span>6 months, 76 women, a 6-hour window: about the same, 4.32% against 4.66%.</span></li><li style="display:flex;gap:10px;padding:8px 0;border-top:1px solid var(--rule)"><span aria-hidden="true" style="flex:none;width:9px;height:9px;margin-top:.45em;border-radius:50%;background:var(--rose)"></span><span>16 weeks, 93 women, an 8-hour window added to the same calorie target: about 3 kg more.</span></li></ul></div><p style="flex-basis:100%;margin:4px 0 0;font-size:.9em;color:var(--muted)"><span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--rose)"></span> lost more weight &nbsp; <span style="display:inline-block;width:8px;height:8px;border-radius:50%;border:1.2px solid var(--rose)"></span> about the same. periods: no clear change in the two trials that compared them.</p></div><figcaption style="margin-top:.8em;font-size:.88em;font-style:italic;color:var(--soft)">what the trials compared, and what they found for weight.</figcaption></figure>
            <h2>what about androgens and periods?</h2>
            <p>this is where hopes run ahead of the data. in the six-month trial, testosterone fell with both the window and calorie cutting; the free androgen index fell only with the window, and HbA1c improved, according to the university's summary.{n(13)} cycle length and bleeding didn't change significantly.{n(14)} in the eight-week trial, periods and androgens did no better with the window than with calorie restriction.{n(8)} the 2021 study reported that cycles improved for 11 of 15 women, but it had no comparison group and didn't clearly define improvement.{n(6)}</p>
            <p>outside the fasting trials, weight loss on its own may make periods more regular for some women with higher weight.{n(15)} if a window helps, that is the likely route, rather than anything about the clock.</p>

            <h2>what do the reviews say?</h2>
            <p>they disagree, because each pools a different handful of studies. a 2025 review of five studies found that fasting lowered weight by about 4 kg, along with insulin resistance and the free androgen index, with no change in total testosterone.{n(16)} another 2025 review, of four studies, found no significant effect on BMI, blood sugar or insulin resistance.{n(17)} a 2026 review of four randomised trials, 216 women in all, found better insulin resistance with a window, and no significant difference in weight, testosterone, the free androgen index or SHBG compared with the other diets. its authors called the evidence preliminary.{n(14)}</p>
            <p>the honest summary: the trials are few, small and mostly short. eating within a window seems to work about as well as other ways of eating less, and may help insulin a little. no trial shows that it treats PCOS, and none shows that it brings periods back.</p>

            <h2>what women with PCOS have told researchers</h2>
            <p>in a survey of 1,385 women with PCOS, the most common concern was difficulty losing weight, named by 53.6%, then irregular periods, 50.8%, and infertility, 44.5%. a third had waited more than two years for a diagnosis, and nearly half had seen three or more health professionals before getting one.{n(18)}</p>
            <p>in interviews in Australia, ten women with PCOS described trying many ways to lose weight and finding it hard to lose and to keep off. structure helped, they said, such as balanced meals and support from health professionals, friends or family; time, cost, tiredness, low mood and unsupportive partners got in the way.{n(19)} in another set of focus groups and interviews, ten women spoke of frustration that there is no cure, of little information after diagnosis, and of worry about the future.{n(20)}</p>
            <p>the fasting trials asked too. in the 2021 study, 7 of 15 women found the eight-hour window easy or very easy and 2 found it difficult, and all said they wanted to continue.{n(6)} in the Irish study, 10 of 11 were keen to continue,{n(12)} and in the six-month trial about 80% of the window group said they would.{n(13)} these are small groups of volunteers who chose to try fasting. they don't speak for everyone.</p>

            <h2>who shouldn't fast, or should ask first</h2>
            <ul>
                <li>anyone with a current or past eating disorder. eating disorders are more common in PCOS: across 20 studies, the odds of any eating disorder were about 1.5 times higher, with bulimia and binge eating raised and anorexia not.{n(21)} the guideline asks clinicians to keep this in mind at any weight, especially when advising weight loss.{n(1)} a fast that turns into a rule you can't break is a reason to stop.</li>
                <li>during pregnancy, or while trying to conceive. none of the trials here tested fasting then. eating around a pregnancy or a fertility treatment is worth planning with a doctor or midwife, not a timer.</li>
                <li>anyone with diabetes on insulin or a sulfonylurea, such as glipizide, glimepiride or glyburide. these can cause low blood sugar when you don't eat, and an expert review advises lower doses on fasting days, with a doctor's guidance and more frequent glucose checks.{n(22)} don't change a dose on your own.</li>
                <li>anyone on metformin, which many people with PCOS take. on its own it rarely causes low blood sugar, and the same review says it can usually be continued as usual.{n(22)} its common side effects are in the stomach and gut, mild and dose-related,{n(1)} so ask whoever prescribes it how to time it around an eating window.</li>
                <li>anyone under 18, or with a missed period that hasn't been looked into.</li>
            </ul>

            <h2>what if your cycle is irregular, or absent?</h2>
            <p>then hours suggested for each phase of the cycle may not fit you. the phases assume that ovulation happens and the next period follows on time. with PCOS ovulation often doesn't happen, or not on a schedule, so a "luteal phase" counted from the calendar may not be one at all. no trial has tested fasting by phase in anyone, and in PCOS there is even less to go on.</p>
            <p>hæl counts the phase from the day your last period began and the cycle length it knows, which it keeps between 21 and 45 days. if a period comes later than that, it counts on as though a new cycle had begun, so until you enter the next period, the phase on screen is a guess. when cycles are far apart, the guess is often wrong, and turning the cycle off is the more honest choice. either way the suggestions stay suggestions: the dial turns to any length.</p>

            <h2>setting up hæl with an irregular cycle</h2>
            <ol>
                <li>on the first page, hæl asks when your last cycle began. give the day, or choose "I don't keep one". you can change either later, in settings, under the cycle.</li>
                <li>if you keep a cycle, enter each period when it comes. in settings, change the date of your last period, or log it in Apple Health and hæl reads it from there.</li>
                <li>if you don't, turn off "track a cycle" in settings. the ring keeps the hours alone, and the ledger draws the month by the moon, with your fasts round it. the moon is only a calendar there; hæl makes no claim that it moves the body.</li>
                <li>start at twelve hours. turn the dial to twelve and press begin. lengthen slowly, if at all.</li>
                <li>keep rest days. under begin is rest. press it on a day you won't fast, and the ledger keeps the day as rest rather than a gap.</li>
                <li>read the scale slowly. with a cycle, the body ledger reads each morning against the same point of the cycle; without one, against the same time last month. when periods are far apart, the trend over weeks says more than any morning.</li>
            </ol>
            <p>the timer, the ledger and rest days are free. the hours for each phase and the readings against the cycle are part of the full witness. <a href="/cycle-syncing-fasting/">how hæl reads the cycle</a>.</p>

            <div class="aside">
                <p>hæl doesn't treat PCOS, and neither does fasting. it keeps the hours you choose, suggests without insisting, and works just as well without a cycle. there are no badges and no coaching, and it says plainly when a fast runs long enough to need a doctor.</p>
                <a class="download" href="{STORE}">hæl on the App Store</a>
            </div>
"""

# for APPNOTES in build_notes.py: (campaign token, one true sentence)
PCOS_APPNOTE = ("article-pcos", "hæl, a fasting timer for iPhone, works with a cycle or without one, and every hour it suggests stays a suggestion, never a rule.")

PCOS_NOTE = dict(
    slug="pcos-intermittent-fasting",
    title="PCOS and Intermittent Fasting: What the Research Shows | hæl",
    description="what trials of intermittent fasting in PCOS, now named PMOS, found for weight, insulin, androgens and periods, and who shouldn't fast.",
    kicker="the syndrome",
    h1="PCOS and intermittent fasting",
    headline="PCOS and intermittent fasting: what the research shows",
    short="in small trials, eating within a window helped women with PCOS lose weight about as well as cutting calories, and may help insulin a little. it hasn't been shown to lower androgens reliably or bring periods back, and the international guideline favours no one diet. with an eating disorder history, on insulin or sulfonylureas, or pregnant or trying to conceive, ask a doctor first.",
    body=PCOS_BODY, sources=PCOS_SOURCES,
    published="2026-11-04", published_text="november 4, 2026",
    appnote=PCOS_APPNOTE,
)

if __name__ == "__main__":
    # quick self-checks only; builds nothing
    import re
    text = PCOS_BODY + PCOS_NOTE["short"] + PCOS_NOTE["description"] + PCOS_APPNOTE[1]
    assert "—" not in text and "–" not in text, "dash found"
    assert "!" not in text, "exclamation found"
    assert not re.search(r"\b(she|her|hers)\b", text, re.I), "she/her found"
    assert len(PCOS_NOTE["description"]) < 160, len(PCOS_NOTE["description"])
    used = sorted({int(x) for x in re.findall(r'href="#s(\d+)"', PCOS_BODY)})
    assert used == list(range(1, len(PCOS_SOURCES) + 1)), used
    print("ok:", len(PCOS_SOURCES), "sources, description", len(PCOS_NOTE["description"]), "chars")
