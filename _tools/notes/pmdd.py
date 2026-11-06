"""DRAFT, not built, not linked, not published: PMDD and intermittent fasting.

To publish later, move PMDD_SOURCES and PMDD_BODY into _tools/build_notes.py,
add PMDD_APPNOTE to APPNOTES and PMDD_NOTE (with body= and sources=) to NOTES.
n() and STORE below mirror build_notes.py so this file runs on its own.
PMDD_NOTE carries APPNOTES/appnote for the APPNOTES dict; drop those two keys
before passing it to page(), which doesn't take them.
Run `python3 _drafts/pmdd.py` to check footnotes, description length, dashes.
Research notes and what was verified: _drafts/pmdd-research.md.

<!--
VISUAL SPECS

1. explanatory diagram: "where PMDD sits in the cycle"
   - a horizontal strip of 28 squares, days 1 to 28 of a 28-day cycle, then
     days 1 to 7 of the next cycle in a paler tint, so the strip reads across
     one period into the next. day numbers under every seventh square.
   - top row, the phases as hæl counts them for a 28-day cycle (CycleTracker:
     menstrual 1-5, follicular 6-13, ovulation 14-15, luteal 16-28), in the
     app's phase colours (periodRose, follicularGlow, ovulationGold,
     lutealLavender), each labelled in lowercase.
   - second row, "PMDD's symptom window": a solid band over days 22-28 (the
     final week before the period, DSM-5 criterion A), fading out across days
     1-3 of the next cycle ("begins to improve within a few days"), and a
     plain outlined band over days 6-12 of the next cycle labelled "minimal or
     absent in the week after the period".
   - third row, "hæl's suggested hours": 12-14 under menstrual, 16-18 under
     follicular, 16-20 under ovulation, 14-16 under luteal. a small open
     square marked "rest" sits on days 26-28 to show a rest day can go
     anywhere, labelled "rest days, any day you choose".
   - one note under the strip, small: "energy intake is about 168 kcal a day
     higher in the luteal phase on average (Tucker 2024). no trial has tested
     fasting in PMDD."
   - no symptom icons, no faces, no arrows suggesting treatment.
   - alt text: "a 28-day cycle strip. the luteal phase runs from day 16 to
     the period. PMDD symptoms sit in the final week before the period and
     ease within a few days of it starting. hæl suggests 14 to 16 hours in the
     luteal phase and 12 to 14 while bleeding."

2. app screen to show: home, on a real late-luteal day (day 25 or 26 of a
   28-day cycle), full witness open: the ring in the luteal colour, the dial
   set at the cycle suggestion (15 hours, the middle of 14-16), the rest
   button visible under begin. capture it fresh from a real build with real
   data; none of the current screenshots (ring.png is day 14, ledger.png
   shows follicular days) shows the luteal phase. do not mock it up.
   caption: "late in the cycle, hæl suggests fourteen to sixteen hours. the
   dial turns lower, and rest is always there."

3. OG image, 1200x630, the site's paper ground and book type:
   line 1 (large): "PMDD and intermittent fasting"
   line 2 (smaller): "what the research shows, and what it doesn't."
   foot, small: "hæl · hael.app"
-->
"""

STORE = "https://apps.apple.com/app/id6778956802"


def n(i):
    return f'<sup><a href="#s{i}">{i}</a></sup>'


# ---------------------------------------------------------------- PMDD (draft, 2026-11-04)
PMDD_SOURCES = [
    # 1
    {"cite": "Schmidt PJ, Nieman LK, Danaceau MA, Adams LF, Rubinow DR. Differential behavioral effects of gonadal steroids in women with and in those without premenstrual syndrome. New England Journal of Medicine. 1998;338(4):209-216.",
     "html": 'Schmidt PJ, et al. <a href="https://doi.org/10.1056/NEJM199801223380401">Differential behavioral effects of gonadal steroids in women with and in those without premenstrual syndrome</a>. <i>New England Journal of Medicine</i>, 1998.'},
    # 2
    {"cite": "International Association for Premenstrual Disorders (IAPMD). What is PMDD?",
     "html": 'International Association for Premenstrual Disorders. <a href="https://www.iapmd.org/pmdd">What is PMDD?</a>'},
    # 3
    {"cite": "Dahlgren CL, Qvigstad E. Eating disorders in premenstrual dysphoric disorder: a neuroendocrinological pathway to the pathogenesis and treatment of binge eating. Journal of Eating Disorders. 2018;6:35.",
     "html": 'Dahlgren CL, Qvigstad E. <a href="https://doi.org/10.1186/s40337-018-0222-2">Eating disorders in premenstrual dysphoric disorder: a neuroendocrinological pathway to the pathogenesis and treatment of binge eating</a>. <i>Journal of Eating Disorders</i>, 2018. (table 1 sets out the DSM-5 criteria.)'},
    # 4
    {"cite": "Reilly TJ, Patel S, Unachukwu IC, et al. The prevalence of premenstrual dysphoric disorder: systematic review and meta-analysis. Journal of Affective Disorders. 2024;349:534-540.",
     "html": 'Reilly TJ, et al. <a href="https://doi.org/10.1016/j.jad.2024.01.066">The prevalence of premenstrual dysphoric disorder: systematic review and meta-analysis</a>. <i>Journal of Affective Disorders</i>, 2024.'},
    # 5
    {"cite": "Eisenlohr-Moul T, Divine M, Schmalenberger K, et al. Prevalence of lifetime self-injurious thoughts and behaviors in a global sample of 599 patients reporting prospectively confirmed diagnosis with premenstrual dysphoric disorder. BMC Psychiatry. 2022;22(1):199.",
     "html": 'Eisenlohr-Moul T, et al. <a href="https://doi.org/10.1186/s12888-022-03851-0">Prevalence of lifetime self-injurious thoughts and behaviors in a global sample of 599 patients reporting prospectively confirmed diagnosis with premenstrual dysphoric disorder</a>. <i>BMC Psychiatry</i>, 2022.'},
    # 6
    {"cite": "American College of Obstetricians and Gynecologists. Management of premenstrual disorders: ACOG Clinical Practice Guideline No. 7. Obstetrics and Gynecology. 2023;142(6):1516-1533.",
     "html": 'American College of Obstetricians and Gynecologists. <a href="https://doi.org/10.1097/AOG.0000000000005426">Management of premenstrual disorders: Clinical Practice Guideline No. 7</a>. <i>Obstetrics and Gynecology</i>, 2023.'},
    # 7
    {"cite": "Royal College of Obstetricians and Gynaecologists. Management of premenstrual syndrome: Green-top Guideline No. 48. BJOG. 2017;124(3):e73-e105.",
     "html": 'Royal College of Obstetricians and Gynaecologists. <a href="https://doi.org/10.1111/1471-0528.14260">Management of premenstrual syndrome: Green-top Guideline No. 48</a>. <i>BJOG</i>, 2017.'},
    # 8
    {"cite": "Tidy C. Premenstrual syndrome. Patient.info Professional, updated 23 November 2022 (drawing on NICE Clinical Knowledge Summaries).",
     "html": 'Tidy C. <a href="https://patient.info/doctor/premenstrual-syndrome-pro">Premenstrual syndrome</a>. <i>Patient.info Professional</i>, 2022, drawing on the NICE Clinical Knowledge Summary on <a href="https://cks.nice.org.uk/topics/premenstrual-syndrome/">premenstrual syndrome</a>.'},
    # 9
    {"cite": "Jespersen C, Lauritsen MP, Frokjaer VG, Schroll JB. Selective serotonin reuptake inhibitors for premenstrual syndrome and premenstrual dysphoric disorder. Cochrane Database of Systematic Reviews. 2024;8:CD001396.",
     "html": 'Jespersen C, et al. <a href="https://doi.org/10.1002/14651858.CD001396.pub4">Selective serotonin reuptake inhibitors for premenstrual syndrome and premenstrual dysphoric disorder</a>. <i>Cochrane Database of Systematic Reviews</i>, 2024.'},
    # 10
    {"cite": "Hooshiar SH, Yazdani A, Jafarnejad S. Does an alternate-day modified fasting diet improve premenstrual syndrome symptoms and health-related quality of life in obese or overweight women with premenstrual syndrome? A randomized, controlled trial. Frontiers in Nutrition. 2024;10:1298831.",
     "html": 'Hooshiar SH, Yazdani A, Jafarnejad S. <a href="https://doi.org/10.3389/fnut.2023.1298831">Does an alternate-day modified fasting diet improve premenstrual syndrome symptoms and health-related quality of life in obese or overweight women with premenstrual syndrome? A randomized, controlled trial</a>. <i>Frontiers in Nutrition</i>, 2024.'},
    # 11
    {"cite": "Harvie M, Haiba M. The impact of intermittent energy restriction on women's health. Proceedings of the Nutrition Society. 2026;85(1):23-32.",
     "html": 'Harvie M, Haiba M. <a href="https://doi.org/10.1017/S0029665125000059">The impact of intermittent energy restriction on women\'s health</a>. <i>Proceedings of the Nutrition Society</i>, 2026.'},
    # 12
    {"cite": "Tucker JAL, McCarthy SF, Bornath DPD, Khoja JS, Hazell TJ. The effect of the menstrual cycle on energy intake: a systematic review and meta-analysis. Nutrition Reviews. 2025;83(3):e866-e876.",
     "html": 'Tucker JAL, et al. <a href="https://doi.org/10.1093/nutrit/nuae093">The effect of the menstrual cycle on energy intake: a systematic review and meta-analysis</a>. <i>Nutrition Reviews</i>, 2025.'},
    # 13
    {"cite": "Reed SC, Levin FR, Evans SM. Changes in mood, cognitive performance and appetite in the late luteal and follicular phases of the menstrual cycle in women with and without PMDD (premenstrual dysphoric disorder). Hormones and Behavior. 2008;54(1):185-193.",
     "html": 'Reed SC, Levin FR, Evans SM. <a href="https://doi.org/10.1016/j.yhbeh.2008.02.018">Changes in mood, cognitive performance and appetite in the late luteal and follicular phases of the menstrual cycle in women with and without PMDD</a>. <i>Hormones and Behavior</i>, 2008.'},
    # 14
    {"cite": "Ko CH, Yen CF, Long CY, Kuo YT, Chen CS, Yen JY. The late-luteal leptin level, caloric intake and eating behaviors among women with premenstrual dysphoric disorder. Psychoneuroendocrinology. 2015;56:52-61.",
     "html": 'Ko CH, et al. <a href="https://doi.org/10.1016/j.psyneuen.2015.03.002">The late-luteal leptin level, caloric intake and eating behaviors among women with premenstrual dysphoric disorder</a>. <i>Psychoneuroendocrinology</i>, 2015.'},
    # 15
    {"cite": "Yen JY, Liu TL, Chen IJ, Chen SY, Ko CH. Premenstrual appetite and emotional responses to foods among women with premenstrual dysphoric disorder. Appetite. 2018;125:18-23.",
     "html": 'Yen JY, et al. <a href="https://doi.org/10.1016/j.appet.2018.01.029">Premenstrual appetite and emotional responses to foods among women with premenstrual dysphoric disorder</a>. <i>Appetite</i>, 2018.'},
    # 16
    {"cite": "Lin G, Siddiqui R, Lin Z, et al. Blood glucose variance measured by continuous glucose monitors across the menstrual cycle. npj Digital Medicine. 2023;6:140.",
     "html": 'Lin G, et al. <a href="https://doi.org/10.1038/s41746-023-00884-x">Blood glucose variance measured by continuous glucose monitors across the menstrual cycle</a>. <i>npj Digital Medicine</i>, 2023.'},
    # 17
    {"cite": "Reid RL, Greenaway-Coates A, Hahn PM. Oral glucose tolerance during the menstrual cycle in normal women and women with alleged premenstrual \"hypoglycemic\" attacks: effects of naloxone. Journal of Clinical Endocrinology and Metabolism. 1986;62(6):1167-1172.",
     "html": 'Reid RL, Greenaway-Coates A, Hahn PM. <a href="https://doi.org/10.1210/jcem-62-6-1167">Oral glucose tolerance during the menstrual cycle in normal women and women with alleged premenstrual "hypoglycemic" attacks</a>. <i>Journal of Clinical Endocrinology and Metabolism</i>, 1986.'},
    # 18
    {"cite": "Denicoff KD, Hoban C, Grover GN, Rubinow DR. Glucose tolerance testing in women with premenstrual syndrome. American Journal of Psychiatry. 1990;147(4):477-480.",
     "html": 'Denicoff KD, et al. <a href="https://doi.org/10.1176/ajp.147.4.477">Glucose tolerance testing in women with premenstrual syndrome</a>. <i>American Journal of Psychiatry</i>, 1990.'},
    # 19
    {"cite": "Nobles CJ, Thomas JJ, Valentine SE, Gerber MW, Vaewsorn AS, Marques L. Association of premenstrual syndrome and premenstrual dysphoric disorder with bulimia nervosa and binge-eating disorder in a nationally representative epidemiological sample. International Journal of Eating Disorders. 2016;49(7):641-650.",
     "html": 'Nobles CJ, et al. <a href="https://doi.org/10.1002/eat.22539">Association of premenstrual syndrome and premenstrual dysphoric disorder with bulimia nervosa and binge-eating disorder in a nationally representative epidemiological sample</a>. <i>International Journal of Eating Disorders</i>, 2016.'},
    # 20
    {"cite": "Klump KL, Keel PK, Racine SE, et al. The interactive effects of estrogen and progesterone on changes in emotional eating across the menstrual cycle. Journal of Abnormal Psychology. 2013;122(1):131-137.",
     "html": 'Klump KL, et al. <a href="https://doi.org/10.1037/a0029524">The interactive effects of estrogen and progesterone on changes in emotional eating across the menstrual cycle</a>. <i>Journal of Abnormal Psychology</i>, 2013.'},
    # 21
    {"cite": "Stice E, Davis K, Miller NP, Marti CN. Fasting increases risk for onset of binge eating and bulimic pathology: a 5-year prospective study. Journal of Abnormal Psychology. 2008;117(4):941-946.",
     "html": 'Stice E, et al. <a href="https://doi.org/10.1037/a0013644">Fasting increases risk for onset of binge eating and bulimic pathology: a 5-year prospective study</a>. <i>Journal of Abnormal Psychology</i>, 2008.'},
    # 22
    {"cite": "Ryan S, Ussher JM, Hawkey A. Managing the premenstrual body: a body mapping study of women's negotiation of premenstrual food cravings and exercise. Journal of Eating Disorders. 2021;9:125.",
     "html": 'Ryan S, Ussher JM, Hawkey A. <a href="https://doi.org/10.1186/s40337-021-00478-6">Managing the premenstrual body: a body mapping study of women\'s negotiation of premenstrual food cravings and exercise</a>. <i>Journal of Eating Disorders</i>, 2021.'},
    # 23
    {"cite": "Osborn E, Wittkowski A, Brooks J, Briggs PE, O'Brien PMS. Women's experiences of receiving a diagnosis of premenstrual dysphoric disorder: a qualitative investigation. BMC Women's Health. 2020;20:242.",
     "html": 'Osborn E, et al. <a href="https://doi.org/10.1186/s12905-020-01100-8">Women\'s experiences of receiving a diagnosis of premenstrual dysphoric disorder: a qualitative investigation</a>. <i>BMC Women\'s Health</i>, 2020.'},
    # 24
]

PMDD_BODY = f"""
            <h2>what is PMDD?</h2>
            <p>premenstrual dysphoric disorder is a severe, recurring change in mood that comes in the days before a period and lifts soon after it starts. it isn't a hormone imbalance. hormone levels in PMDD are normal; what differs is the brain's response to their ordinary rise and fall. in a well-known trial, switching the ovaries off eased symptoms in women with premenstrual syndrome, and adding back normal doses of estrogen or progesterone brought the symptoms back, while the same hormones changed nothing in women without it.{n(1)} the International Association for Premenstrual Disorders describes PMDD in the same terms, as a sensitivity to normal hormonal change.{n(2)}</p>

            <h2>how is it diagnosed?</h2>
            <p>in outline, the DSM-5, the psychiatric manual most doctors use, asks for all of these:{n(3)}</p>
            <ul>
                <li>at least five symptoms in the final week before the period, in most cycles of the past year, improving within a few days of the period starting and minimal or absent in the week after it.</li>
                <li>at least one of them a mood symptom: sudden swings of mood, marked irritability or anger, low mood or hopelessness, or marked anxiety or tension.</li>
                <li>the rest from a list that includes losing interest in usual things, poor concentration, low energy, a marked change in appetite, overeating or food cravings, sleeping too much or too little, feeling overwhelmed, and physical symptoms such as tender breasts or bloating.</li>
                <li>real distress, or interference with work, study, relationships or daily life.</li>
                <li>symptoms confirmed by daily ratings over at least two cycles. until then, the diagnosis is called provisional.</li>
                <li>not simply another condition, such as depression, getting worse before a period, and not caused by a medicine or another illness.</li>
            </ul>
            <p>appetite is written into the definition. that matters for anyone who fasts.</p>

            <figure class="fig" style="margin:2em 0"><div style="overflow-x:auto;-webkit-overflow-scrolling:touch"><svg viewBox="0 0 746 168" role="img" aria-labelledby="fig-pmdd-t" style="width:100%;min-width:600px;height:auto;font-family:var(--serif)"><title id="fig-pmdd-t">a 28-day cycle strip. the luteal phase runs from day 16 to the period. PMDD symptoms sit in the final week before the period and ease within a few days of it starting. hæl suggests 14 to 16 hours in the luteal phase and 12 to 14 while bleeding, and a rest day can go anywhere.</title><rect x="118" y="24" width="16" height="16" rx="2" fill="#D6A9A9"/><rect x="136" y="24" width="16" height="16" rx="2" fill="#D6A9A9"/><rect x="154" y="24" width="16" height="16" rx="2" fill="#D6A9A9"/><rect x="172" y="24" width="16" height="16" rx="2" fill="#D6A9A9"/><rect x="190" y="24" width="16" height="16" rx="2" fill="#D6A9A9"/><text x="162" y="16" text-anchor="middle" font-size="11" font-style="italic" fill="var(--soft)">menstrual</text><rect x="208" y="24" width="16" height="16" rx="2" fill="#DEC1AF"/><rect x="226" y="24" width="16" height="16" rx="2" fill="#DEC1AF"/><rect x="244" y="24" width="16" height="16" rx="2" fill="#DEC1AF"/><rect x="262" y="24" width="16" height="16" rx="2" fill="#DEC1AF"/><rect x="280" y="24" width="16" height="16" rx="2" fill="#DEC1AF"/><rect x="298" y="24" width="16" height="16" rx="2" fill="#DEC1AF"/><rect x="316" y="24" width="16" height="16" rx="2" fill="#DEC1AF"/><rect x="334" y="24" width="16" height="16" rx="2" fill="#DEC1AF"/><text x="279" y="16" text-anchor="middle" font-size="11" font-style="italic" fill="var(--soft)">follicular</text><rect x="352" y="24" width="16" height="16" rx="2" fill="#D9C49B"/><rect x="370" y="24" width="16" height="16" rx="2" fill="#D9C49B"/><text x="369" y="16" text-anchor="middle" font-size="11" font-style="italic" fill="var(--soft)">ovulation</text><rect x="388" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="406" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="424" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="442" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="460" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="478" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="496" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="514" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="532" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="550" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="568" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="586" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><rect x="604" y="24" width="16" height="16" rx="2" fill="#BEB0D3"/><text x="504" y="16" text-anchor="middle" font-size="11" font-style="italic" fill="var(--soft)">luteal</text><rect x="622" y="24" width="16" height="16" rx="2" fill="#D6A9A9" opacity=".4"/><rect x="640" y="24" width="16" height="16" rx="2" fill="#D6A9A9" opacity=".4"/><rect x="658" y="24" width="16" height="16" rx="2" fill="#D6A9A9" opacity=".4"/><rect x="676" y="24" width="16" height="16" rx="2" fill="#D6A9A9" opacity=".4"/><rect x="694" y="24" width="16" height="16" rx="2" fill="#D6A9A9" opacity=".4"/><rect x="712" y="24" width="16" height="16" rx="2" fill="#DEC1AF" opacity=".4"/><rect x="730" y="24" width="16" height="16" rx="2" fill="#DEC1AF" opacity=".4"/><text x="126" y="54" text-anchor="middle" font-size="10" fill="var(--muted)">1</text><text x="234" y="54" text-anchor="middle" font-size="10" fill="var(--muted)">7</text><text x="360" y="54" text-anchor="middle" font-size="10" fill="var(--muted)">14</text><text x="486" y="54" text-anchor="middle" font-size="10" fill="var(--muted)">21</text><text x="612" y="54" text-anchor="middle" font-size="10" fill="var(--muted)">28</text><text x="630" y="54" text-anchor="middle" font-size="10" fill="var(--muted)">1</text><text x="738" y="54" text-anchor="middle" font-size="10" fill="var(--muted)">7</text><defs><linearGradient id="ease" x1="0" x2="1"><stop offset="0" stop-color="var(--rose)" stop-opacity=".85"/><stop offset="1" stop-color="var(--rose)" stop-opacity="0"/></linearGradient></defs><rect x="496" y="76" width="124" height="10" rx="5" fill="var(--rose)" opacity=".85"/><rect x="622" y="76" width="54" height="10" fill="url(#ease)"/><rect x="712" y="76" width="34" height="10" rx="5" fill="none" stroke="var(--rose)" stroke-width="1"/><text x="496" y="102" font-size="11" fill="var(--ink)">the final week before the period</text><text x="728" y="70" text-anchor="end" font-size="10" font-style="italic" fill="var(--soft)">minimal after</text><text x="162" y="136" text-anchor="middle" font-size="11" fill="var(--ink)">12 to 14h</text><text x="279" y="136" text-anchor="middle" font-size="11" fill="var(--ink)">16 to 18h</text><text x="369" y="136" text-anchor="middle" font-size="11" fill="var(--ink)">16 to 20h</text><text x="504" y="136" text-anchor="middle" font-size="11" fill="var(--ink)">14 to 16h</text><rect x="568" y="146" width="52" height="12" rx="2" fill="none" stroke="var(--muted)" stroke-dasharray="2 2"/><text x="594" y="155" text-anchor="middle" font-size="9" font-style="italic" fill="var(--muted)">rest</text><text x="0" y="32" font-size="12" font-style="italic" fill="var(--rose)">the cycle</text><text x="0" y="84" font-size="12" font-style="italic" fill="var(--rose)">PMDD</text><text x="0" y="136" font-size="12" font-style="italic" fill="var(--rose)">hæl suggests</text></svg></div><figcaption style="margin-top:.8em;font-size:.88em;font-style:italic;color:var(--soft)">where PMDD sits in the cycle, and the hours hæl suggests around it.</figcaption></figure>
            <h2>how common is PMDD?</h2>
            <p>less common than headlines suggest, and the number depends on how it is counted. a 2024 meta-analysis of 44 studies and 50,659 participants found 3.2% when the diagnosis was confirmed by daily ratings, and 7.7% when it was provisional. in community samples with confirmed diagnosis, it was 1.6%.{n(4)} the authors conclude that studies without daily ratings overstate it.</p>
            <p>it is serious. in a global survey of 599 people with PMDD confirmed by daily ratings, 72% reported having had active thoughts of suicide at some point in their lives, and 34% a suicide attempt.{n(5)} that survey recruited through PMDD support groups, so it may lean toward the most affected, but the figures are why PMDD is treated as a medical condition, not a bad week.</p>
            <p>if PMDD brings thoughts of suicide or self-harm, that is an emergency. call your local emergency number, or 988 in the US, or Samaritans on 116 123 in the UK.</p>

            <h2>what do doctors recommend?</h2>
            <p>the American College of Obstetricians and Gynecologists, the Royal College of Obstetricians and Gynaecologists and the UK's primary care guidance agree on the main treatments.{n(6)}{n(7)}{n(8)}</p>
            <ul>
                <li>SSRIs, a kind of antidepressant, taken every day or only in the second half of the cycle. a 2024 Cochrane review of 34 trials found they probably reduce premenstrual symptoms, more so when taken every day, with nausea, tiredness and sleepiness the commonest side effects.{n(9)}</li>
                <li>cognitive behavioural therapy. ACOG recommends it for the mood symptoms, and the RCOG says it should be considered routinely in severe PMS.{n(6)}{n(7)}</li>
                <li>hormonal options, such as some combined contraceptive pills, and, for severe symptoms under a specialist, medicines that pause the cycle altogether.{n(6)}{n(8)}</li>
            </ul>
            <p>these are things to talk through with a doctor. no diet or fasting schedule is among them.</p>

            <h2>has intermittent fasting been studied in PMDD?</h2>
            <p>no. as of november 2026, searches of PubMed and ClinicalTrials.gov found no trial of intermittent fasting, time-restricted eating or meal timing in people with PMDD. there is no evidence that fasting helps PMDD, and none that it harms it. there is simply no study.</p>
            <p>the nearest is a trial in premenstrual syndrome, which is milder and more common. sixty women with overweight or obesity ate very little every other day, or cut calories daily, for eight weeks. the fasting group improved more on some measures, mood swings and expressed anger among them, but they also lost weight, the trial was open-label, and almost a fifth dropped out.{n(10)} a 2026 review of intermittent eating in women noted that weight loss on these diets has improved premenstrual symptoms, and found no evidence of an effect apart from the weight loss.{n(11)} neither tells us anything about PMDD in someone who isn't trying to lose weight.</p>

            <h2>what happens to appetite before a period?</h2>
            <p>it rises, a little, for most women. a 2024 meta-analysis of 15 datasets found energy intake higher in the luteal phase, the two weeks after ovulation, than in the follicular phase, by about 168 kcal a day on average.{n(12)} the studies were in women of healthy weight with no history of disordered eating, and the range between women was wide.</p>
            <p>in PMDD the rise is larger. in a laboratory study, women with PMDD, but not women without it, wanted more high-fat food in the late luteal days and ate more calories then.{n(13)} in a study of 62 women with PMDD and 69 without, those with PMDD had bigger late-luteal increases in calories, in sweet calories, and in eating that felt out of control.{n(14)} in another, women with PMDD, but not the others, wanted sweet food more in the late luteal phase, and that desire tracked their irritability and impulsivity.{n(15)}</p>

            <h2>and blood sugar?</h2>
            <p>it shifts slightly. in 49 young women without diabetes who wore glucose monitors for about eleven weeks, daily glucose was lowest in the late follicular phase, about 5.8 mmol/L, and highest in the luteal phase, about 6.1 mmol/L, peaking around day 24. days with more food cravings had slightly higher glucose.{n(16)} these are small changes inside the normal range.</p>
            <p>the old idea that premenstrual symptoms are low blood sugar has not held up. two small studies gave glucose tolerance tests at both ends of the cycle in women with premenstrual syndrome and found no cycle-related difference in how they handled glucose, and symptoms during the tests did not match their premenstrual symptoms.{n(17)}{n(18)} no study has measured blood sugar during a fast in PMDD.</p>
            <p>one more thing worth knowing: UK guidance for premenstrual syndrome advises regular, frequent, small meals, every two to three hours, rich in complex carbohydrates.{n(8)} it is general lifestyle advice, not tested against fasting, but it points the other way from long gaps between meals.</p>

            <h2>PMDD, binge eating and fasting</h2>
            <p>the links are real and worth taking seriously. in a nationally representative US sample of 8,694 women, PMDD was linked with about seven times the odds of bulimia nervosa, after accounting for other mental health conditions. a link with binge-eating disorder was seen too, but it did not hold once those conditions were accounted for.{n(19)} the study was cross-sectional, so it can't say which comes first.</p>
            <p>in women in general, emotional eating rises and falls with the cycle and is highest in the middle of the luteal phase, when progesterone peaks.{n(20)} and going without food matters: in 496 adolescent girls followed for five years, fasting for a day to control weight predicted later binge eating and bulimia more strongly than ordinary dieting did.{n(21)} that was full-day fasting for weight control, in teenagers, not a daily overnight window in adults, but the lesson carries: restriction and bingeing tend to feed each other.</p>
            <p>put together: in the very days when PMDD raises hunger and cravings, a long fast asks for the most restraint. for someone with a history of disordered eating, that is a reason not to fast at all. for everyone else, it is a reason to make the late luteal days the easiest of the month, not the hardest.</p>

            <h2>what women have told researchers</h2>
            <p>only a few studies have asked. in an Australian study of women who felt worse about their bodies before a period, many described strict eating the rest of the month, broken premenstrually by hunger and cravings. one said she would "crave food all night and that's not normally me". another said, "I'm eating more than I should and I know that I shouldn't eat so much, but I do it anyway". some gave themselves permission, "I say it could be my hormones and that's the reason, it's okay", while others described guilt; one said, "I feel disgusted with my lack of self-control."{n(22)} the study was about premenstrual body dissatisfaction, not PMDD diagnosed by daily ratings.</p>
            <p>in a UK study of 17 women diagnosed with PMDD by a specialist, symptoms had begun at a median age of 15 and diagnosis came at a median age of 35. one woman said of the diagnosis, "It made everything make sense and everything just clicked into place". another described her untreated years as "self-destruction and anxiety and eating disorders".{n(23)}</p>

            <h2>who shouldn't fast</h2>
            <p>with or without PMDD, some people should not fast without a doctor's advice:</p>
            <ul>
                <li>with a current or past eating disorder, including bingeing or purging</li>
                <li>during pregnancy or breastfeeding, or while trying to conceive</li>
                <li>with diabetes, or on medicines that lower blood sugar</li>
                <li>under 18</li>
                <li>with a missed or irregular period that hasn't been looked into</li>
                <li>when fasting starts to feel like a way to punish or control yourself, or like something you can't stop</li>
            </ul>
            <p>if you are being treated for PMDD, mention fasting to whoever prescribes for you.</p>

            <h2>a shorter fast, or none, in the late luteal days</h2>
            <p>if you fast and live with PMDD or strong premenstrual symptoms, shortening the fast, or not fasting, in the last week before a period is a reasonable personal choice. it follows from what is known: hunger and cravings rise then, more so in PMDD, and restraint is hardest when mood is lowest. it isn't a treatment. no study shows that a shorter fast, or any fast, eases PMDD, and nothing here should replace the treatments above.</p>
            <p>a rest day in those days isn't a lapse. it is the practice working as it should.</p>

            <h2>setting hæl up for the late luteal days</h2>
            <ol>
                <li>tell hæl about your cycle. connect Apple Health, and hæl reads your period starts from it; or enter the day your last period began. check the cycle length in settings, or let hæl learn it from the periods in Apple Health.</li>
                <li>let the hours shorten. with the full witness, hæl suggests fourteen to sixteen hours through the luteal phase and twelve to fourteen while bleeding, against sixteen to eighteen after the period. it counts the luteal phase as a whole and doesn't single out its last days, so if those days ask for less, turn the dial lower. the dial turns to any length.</li>
                <li>mark rest days. on a day you won't fast, press rest under begin, and the ledger keeps the day as rest, not a gap. rest days are free.</li>
                <li>keep your symptom record elsewhere. a diagnosis rests on daily ratings over two cycles; keep them on paper or in a tracker made for it, and take them to a doctor. hæl observes the fasts, not the symptoms.</li>
            </ol>

            <div class="aside">
                <p>hæl suggests, and never insists. it reads the phase from Apple Health or your last period, shortens its suggestion late in the cycle, and treats a day of rest as part of the practice. it doesn't diagnose or treat PMDD; for that, see a doctor, and <a href="https://www.iapmd.org/pmdd">IAPMD</a> is a good place to start. <a href="/cycle-syncing-fasting/">how hæl reads the cycle</a>.</p>
                <a class="download" href="{STORE}">hæl on the App Store</a>
            </div>
"""

# the quiet App Store note after the short answer (same shape as APPNOTES entries)
PMDD_APPNOTE = ("article-pmdd", "hæl, a fasting timer for iPhone, suggests shorter fasts late in the cycle and keeps a day of rest as rest, never as a gap.")

PMDD_NOTE = dict(
    slug="pmdd-intermittent-fasting",
    title="PMDD and Intermittent Fasting: What the Research Shows | hæl",
    description="no trial has tested intermittent fasting in PMDD. what research shows on appetite, cravings, blood sugar and binge eating before a period.",
    kicker="the late days",
    h1="PMDD and intermittent fasting",
    headline="PMDD and intermittent fasting: what the research shows",
    short="PMDD is a severe sensitivity to the normal hormone changes before a period, confirmed in about 3 in 100 people who menstruate. no trial has tested intermittent fasting in PMDD. appetite and cravings rise in those days, more so with PMDD, and PMDD is linked with binge eating. a shorter fast, or rest, then is a reasonable choice; treatment is for a doctor.",
    APPNOTES=PMDD_APPNOTE[1],
    appnote=PMDD_APPNOTE,
    published="2026-11-04",
    published_text="november 4, 2026",
)

if __name__ == "__main__":
    import re
    assert len(PMDD_NOTE["description"]) < 160, len(PMDD_NOTE["description"])
    used = sorted({int(m) for m in re.findall(r'href="#s(\d+)"', PMDD_BODY)})
    assert used == list(range(1, len(PMDD_SOURCES) + 1)), used
    for bad in ("—", "–", "!"):
        assert bad not in PMDD_BODY + PMDD_NOTE["short"] + PMDD_NOTE["description"], bad
    print("ok:", len(PMDD_SOURCES), "sources, description", len(PMDD_NOTE["description"]), "chars")
