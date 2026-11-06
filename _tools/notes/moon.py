"""DRAFT, not built or linked: the moon and the menstrual cycle, what the research says.
To publish later: move MOON_SOURCES / MOON_BODY into _tools/build_notes.py, add
MOON_APPNOTE to APPNOTES and MOON_NOTE to NOTES (drop its appnote key before
passing it to page(), which doesn't take it). n() and STORE below mirror
build_notes.py so this file runs on its own. Research notes and what was
verified in full text: _drafts/moon-research.md. Current as of 2026-11-04.
Run `python3 _drafts/moon.py` for the self-test.

<!--
VISUAL SPECS

1. Explanatory diagram: "how a 28-day cycle drifts across the moon's month"
   Place: in "the arithmetic of coincidence", after the paragraph on drift.
   Drawn simply, in the site's serif, hairline rules, no colour coding alone.
   - A raster, the way the diary studies drew their records: each row is one
     moon's month, 29.5 days wide, left to right from new moon to new moon.
     Two pale outlined bands run down the whole raster: seven days centred
     on the full moon (the middle) and seven days centred on the new moon
     (split across the left and right edges). Band labels at the top, small:
     "within three days of the full moon", "of the new moon".
   - Twenty rows, one dot per row: the starts of a perfectly regular 28-day
     cycle, each 1.53 days earlier in the moon's month than the last. Exact
     positions, in days after the new moon, rows 1 to 20:
     17.5, 16.0, 14.4, 12.9, 11.4, 9.8, 8.3, 6.8, 5.3, 3.7,
     2.2, 0.7, 28.7, 27.1, 25.6, 24.1, 22.5, 21.0, 19.5, 17.9.
     Dots inside a band are filled; dots outside are hollow (shape, not
     colour). Rows 1-4 and 11-14 are filled: eight of twenty (rows 5 and 20 sit just outside, 3.4 and 3.1 days from the full moon).
   - A bracket at the right of rows 1-4, small italic: "four in a row near
     the full moon. no moon needed."
   - Foot line, small: "a cycle that never varies, drawn against a moon it
     ignores. 8 of 20 starts fall within three days of a full or new moon;
     chance gives about half (Clue)."
   - No body, no phases of the cycle, no arrows, no moon faces.
   - Alt text: "twenty starts of a regular 28-day cycle, each drawn a day and
     a half earlier in the moon's month than the one before. they drift
     through the bands around the full and new moon in runs of four or five,
     eight of twenty inside a band, near what chance gives."
   - Figures: the 29.53-day synodic month (Helfrich-Förster 2021); the drift
     and positions are arithmetic (28 - 29.53 = -1.53 days per row); the
     one-in-two chance line is Clue's.

2. App screen: the ledger's head, the month by the moon (needs a fresh
   capture from a real build with real fasts; none of /screenshots or
   /images shows it, and AppStore/mocks/v5-by-the-moon.png is a mock, not
   the app). Capture late in a month with eight to twelve fasts kept: the
   ring of the month with the fasts as beads (filled where kept, hollow
   where set down), the moon's four marks outside on the dotted track, the
   month's name and "by the moon" in the middle, and the one line under it
   ("the longest, ... hours, kept as the moon waned." or as it falls), then
   the first ledger rows with a moon's mark beside a fast that crossed a
   night. Use a phone with "track a cycle" off, so the ledger's first line
   reads the season, not a phase.
   Caption: "the month by the moon, at the head of the ledger. the fasts
   where they began, the moon where it was. nothing grouped, nothing read."

3. OG image, 1200x630, the site's cream ground and serif:
   line 1 (large): "the moon and the menstrual cycle"
   line 2: "what the research says, and what chance says"
   foot, small: "hæl · hael.app"
-->
"""

STORE = "https://apps.apple.com/app/id6778956802"


def n(i):
    return f'<sup><a href="#s{i}">{i}</a></sup>'


# "verified": "full text" = read in full; "abstract" = PubMed abstract only;
# "full page" = the web page itself read; "secondary" = a summary of another
# source. build_notes.page() reads only "html" and "cite", so the extra key
# is safe to keep.
MOON_SOURCES = [
    # 1
    {"cite": "Science Writers at Clue. The myth of moon phases and menstruation. Clue (helloclue.com). Published November 20, 2017; updated April 17, 2019.",
     "html": 'Science Writers at Clue. <a href="https://helloclue.com/articles/cycle-a-z/myth-moon-phases-menstruation">The myth of moon phases and menstruation</a>. <i>Clue</i>, 2017, updated 2019.',
     "verified": "full page, read 2026-11-04 (7.5 million cycles, 1.5 million users, the one-in-two chance line, the mensis/mene etymology, Wheeler's quote)"},
    # 2
    {"cite": "Helfrich-Förster C, Monecke S, Spiousas I, Hovestadt T, Mitesser O, Wehr TA. Women temporarily synchronize their menstrual cycles with the luminance and gravimetric cycles of the Moon. Science Advances. 2021;7(5):eabe1358.",
     "html": 'Helfrich-Förster C, et al. <a href="https://doi.org/10.1126/sciadv.abe1358">Women temporarily synchronize their menstrual cycles with the luminance and gravimetric cycles of the Moon</a>. <i>Science Advances</i>, 2021.',
     "verified": "full text (PMC7840133)"},
    # 3
    {"cite": "Helfrich-Förster C, Domenie ED, Mitesser O, Hovestadt T, Ferlin A, Wehr TA, Costa R, Montagnese S. Synchronization of women's menstruation with the Moon has decreased but remains detectable when gravitational pull is strong. Science Advances. 2025;11(39):eadw4096.",
     "html": 'Helfrich-Förster C, et al. <a href="https://doi.org/10.1126/sciadv.adw4096">Synchronization of women\'s menstruation with the Moon has decreased but remains detectable when gravitational pull is strong</a>. <i>Science Advances</i>, 2025.',
     "verified": "full text (PMC13141897)"},
    # 4
    {"cite": "Bull JR, Rowland SP, Scherwitzl EB, Scherwitzl R, Danielsson KG, Harper J. Real-world menstrual cycle characteristics of more than 600,000 menstrual cycles. npj Digital Medicine. 2019;2:83.",
     "html": 'Bull JR, et al. <a href="https://doi.org/10.1038/s41746-019-0152-7">Real-world menstrual cycle characteristics of more than 600,000 menstrual cycles</a>. <i>npj Digital Medicine</i>, 2019.',
     "verified": "full text (PMC6710244)"},
    # 5
    {"cite": "Li H, Gibson EA, Jukic AMZ, et al. Menstrual cycle length variation by demographic characteristics from the Apple Women's Health Study. npj Digital Medicine. 2023;6:100.",
     "html": 'Li H, et al. <a href="https://doi.org/10.1038/s41746-023-00848-1">Menstrual cycle length variation by demographic characteristics from the Apple Women\'s Health Study</a>. <i>npj Digital Medicine</i>, 2023.',
     "verified": "full text (PMC10226714)"},
    # 6
    {"cite": "Komada Y, Sato M, Ikeda Y, Kami A, Masuda C, Shibata S. The relationship between the lunar phase, menstrual cycle onset and subjective sleep quality among women of reproductive age. International Journal of Environmental Research and Public Health. 2021;18(6):3245.",
     "html": 'Komada Y, et al. <a href="https://doi.org/10.3390/ijerph18063245">The relationship between the lunar phase, menstrual cycle onset and subjective sleep quality among women of reproductive age</a>. <i>International Journal of Environmental Research and Public Health</i>, 2021.',
     "verified": "full text (PMC8003924)"},
    # 7
    {"cite": "Ecochard R, Stanford JB, Fehring RJ, Schneider M, Najmabadi S, Gronfier C. Evidence that the woman's ovarian cycle is driven by an internal circamonthly timing system. Science Advances. 2024;10(15):eadg9646.",
     "html": 'Ecochard R, et al. <a href="https://doi.org/10.1126/sciadv.adg9646">Evidence that the woman\'s ovarian cycle is driven by an internal circamonthly timing system</a>. <i>Science Advances</i>, 2024.',
     "verified": "full text (PMC11006216)"},
    # 8
    {"cite": "Ecochard R, Leiva R, Bouchard TP, Van Lamsweerde A, Pearson JT, Stanford JB, Gronfier C. The menstrual cycle is influenced by weekly and lunar rhythms. Fertility and Sterility. 2024;121(4):651-659.",
     "html": 'Ecochard R, et al. <a href="https://doi.org/10.1016/j.fertnstert.2023.12.009">The menstrual cycle is influenced by weekly and lunar rhythms</a>. <i>Fertility and Sterility</i>, 2024.',
     "verified": "abstract (PMID 38206269; full text not reachable)"},
    # 9
    {"cite": "Eriksson F. Does the moon affect the menstrual cycle? Natural Cycles research library.",
     "html": 'Natural Cycles. <a href="https://www.naturalcycles.com/research-library/does-the-moon-affect-the-menstrual-cycle">Does the moon affect the menstrual cycle?</a> <i>Natural Cycles research library</i>.',
     "verified": "full page, read 2026-11-04 (a company summary of source 8)"},
    # 10
    {"cite": "Science Media Centre. Expert reaction to study looking at the correlation between menstruation, the moon and artificial light. September 24, 2025.",
     "html": 'Science Media Centre. <a href="https://www.sciencemediacentre.org/expert-reaction-to-study-looking-at-the-correlation-between-menstruation-the-moon-and-artificial-light/">Expert reaction to study looking at the correlation between menstruation, the moon and artificial light</a>, 2025.',
     "verified": "full page, read 2026-11-04 (Gronfier's comment)"},
    # 11
    {"cite": "Science Media Centre Spain. Increasing use of smartphones and LED lights prevents synchronisation between menstrual and lunar cycles. September 24, 2025.",
     "html": 'Science Media Centre Spain. <a href="https://sciencemediacentre.es/en/increasing-use-smartphones-and-led-lights-prevents-synchronisation-between-menstrual-and-lunar">Increasing use of smartphones and LED lights prevents synchronisation between menstrual and lunar cycles</a>, 2025.',
     "verified": "full page, read 2026-11-04 (Carrasco Romero's comment)"},
    # 12
    {"cite": "Stice E, Davis K, Miller NP, Marti CN. Fasting increases risk for onset of binge eating and bulimic pathology: a 5-year prospective study. Journal of Abnormal Psychology. 2008;117(4):941-946.",
     "html": 'Stice E, et al. <a href="https://doi.org/10.1037/a0013644">Fasting increases risk for onset of binge eating and bulimic pathology: a 5-year prospective study</a>. <i>Journal of Abnormal Psychology</i>, 2008.',
     "verified": "abstract (PMID 19025239)"},
    # 13
    {"cite": "Grajower MM, Horne BD. Clinical management of intermittent fasting in patients with diabetes mellitus. Nutrients. 2019;11(4):873.",
     "html": 'Grajower MM, Horne BD. <a href="https://doi.org/10.3390/nu11040873">Clinical management of intermittent fasting in patients with diabetes mellitus</a>. <i>Nutrients</i>, 2019.',
     "verified": "abstract (PMID 31003482)"},
]

MOON_BODY = f"""
            <h2>where the belief comes from</h2>
            <p>it is in the words. "menstruation" and "menses" come from Latin and Greek words for month, mensis, and moon, mene.{n(1)} the usual version of the belief, in the words of a data scientist at the period app Clue, is that "you ovulate around the full moon and get your period around the new moon".{n(1)}</p>
            <p>there are reasons it has lasted. in many sea creatures, and some on land, breeding is timed to a phase of the moon, and the human cycle runs close to the moon's month. a few older studies that kept only women whose cycles were near 29.5 days found periods gathering at the full moon; studies that didn't select by cycle length found no link. the authors of the 2021 study below, who take the idea seriously, still write that "the scientific community generally remains skeptical".{n(2)} the older studies don't even agree on which moon: a 1986 study of 826 young women in China found 28.3% of periods around the new moon.{n(3)}</p>

            <h2>two months of nearly the same length</h2>
            <p>the moon's month, from one new moon to the next, averages 29.53 days.{n(2)} the cycle is close to it on average and rarely equal to it. in 612,613 cycles from 124,648 users of one fertility app, the mean was 29.3 days, and only 13% of cycles were exactly 28 days long.{n(4)} in the Apple Women's Health Study, 165,668 cycles from 12,608 people in the US, the mean was 28.7 days and the median 28.{n(5)}</p>
            <p>so the two months sit within a day or so of each other, and that small gap does most of the work in everything below.</p>

            <h2>what the large datasets found</h2>
            <ul>
                <li>Clue looked at 7.5 million cycles from 1.5 million users not using hormonal birth control and "found no correlation between the lunar phases and the menstrual cycle or period start date".{n(1)} it is the largest look so far, but the method isn't published and it wasn't peer reviewed.</li>
                <li>in Japan, 529 women aged 25 to 39 gave the starts of six cycles from a period app. there was no association between the start of a period and the moon's phase (p = 0.99).{n(6)}</li>
                <li>a 2024 study used old fertility records: 26,912 cycles from 2,303 European women, first recorded between 1960 and 1997, and 4,786 cycles from 721 women in North America. in Europe, the most common moon phase for a period to start was the waxing crescent, with 3,533 of 26,912 starts, 13.1%. if starts were spread evenly over the eight phases, each would hold 12.5%. the gap was significant counted cycle by cycle, but not when each woman's cycles were averaged (P = 0.0986). in North America the most common phase was the full moon instead.{n(7)}</li>
                <li>the same team's second 2024 paper looked at 311,064 cycles from 35,940 women aged 18 to 40, recorded from 2019 to 2021. periods began most often on Thursdays and Fridays. a lunar rhythm was also statistically significant, but "less pronounced than the weekly rhythm".{n(8)} two of its authors work at Natural Cycles, the fertility app, whose own summary says periods most often start "in the phases around the full moon".{n(9)} only the abstract could be read, so its effect sizes aren't given here.</li>
            </ul>
            <p>the authors of the European study call the link "weak and inconsistent in terms of phase relationship". they think a direct effect of moonlight "unlikely", since nearly everyone now lives with artificial light at night, and they call the moon's gravitational pull on a person "negligible".{n(7)} the weekly finding is worth keeping in mind too: in the same data, the day of the week stood out more than the moon did, and nobody suggests Thursday is astronomical.</p>
            <p>so "there is no link" goes further than the evidence. the fairer summary is a small statistical signal in some large datasets, pointing to different phases in different places, with no known cause.</p>

            <h2>what the long diaries found</h2>
            <p>the studies most often quoted for the moon come from one research group in Germany, and they read records one person at a time.</p>
            <p>in 2021 they looked at 22 women who had written down the start of every period, out of personal interest, for 5 to 32 years: 4,112 periods in all. a stretch of a record counted as in step with the moon only when at least three starts in a row fell at a full or new moon, judged by eye on plots of the record. by that measure, women aged 35 or under were in step for an average of 23.6% of their recorded time, and women over 35 for 9.5%.{n(2)} that is a share of time, not of periods, and it hides a wide spread: from 0% for some women to 65% for one.{n(2)}</p>
            <p>the authors write that their findings "do not prove causality". they also report that the three young women exposed to the most light at night showed no such stretches, but that light was judged from where each one lived and how, not measured.{n(2)}</p>
            <p>in 2025 the same group looked at 176 women and 11,565 periods, with records of 2 to 37 years, 6 on average, and now asked for at least four months in a row before counting a stretch. in records kept before 2010, starts pooled across women lined up with the full and new moon. after 2010, they write, the link "was completely lost on the population level". they suggest the cause is light at night, from LED lighting and screens, and add that this "remains hypothetical", because nobody measured the women's light. a smaller pattern was left in December and January, which they put down to the moon's pull, while noting "there may be other seasonal factors (both environmental and social)".{n(3)}</p>

            <h2>the limits of the diaries</h2>
            <ul>
                <li>they are small, and the women chose themselves. in 2021 they included a mother and two daughters, and another mother and two daughters.{n(2)}</li>
                <li>being in step was decided by looking at plots, with a rule of three, later four, in a row.{n(2)}{n(3)} the next section shows how easily runs like that appear by arithmetic alone.</li>
                <li>the way records were kept changed at about the time the link faded. in 2025, the older records were on paper or from a fertility database, and most from this century came from phone apps.{n(3)} records from the same Italian database also appear in the 2024 European study, so the studies that seem to confirm each other may partly share data.{n(3)}{n(7)}</li>
                <li>no study measured light, and no one has shown how the moon's pull could act on a body. the European authors call that pull "negligible".{n(7)}</li>
            </ul>
            <p>researchers close to the work still disagree about how much it means. Claude Gronfier, an author of both 2024 papers, said the association "is not due to chance. The level of evidence is high", and called the evidence for light, gravity and search trends "modest".{n(10)} Cristina Carrasco Romero, a physiology researcher at the University of Extremadura in Spain, said of the 2025 study that "these are correlations, not a proven causal relationship".{n(11)}</p>

            <h2>the arithmetic of coincidence</h2>
            <p>start with chance. if periods started at random, about one in two would still start within three days of a full or new moon. seven days around each of two points is 14 of the moon's 29.53 days, about 47%.{n(1)} half of anyone's periods will seem to keep company with the moon, whatever the moon is doing.</p>
            <p>then add drift. a perfectly regular 28-day cycle starts 1.53 days earlier in the moon's month each time. it takes four or five starts to cross the week around a full or new moon, then crosses the week around the other one about nine or ten cycles later, and comes all the way round the moon in about nineteen cycles, a year and a half. so a cycle that never varies, against a moon it ignores, still gives runs of four or five starts "at" the full or new moon, more than enough to pass the diaries' rule of three or four in a row. a cycle of 29.3 days slips only about a quarter of a day each month, so a regular one could stay within three days of the same phase for two years or more.</p>
            <p>real cycles vary by a few days, which breaks those runs up and starts new ones, without changing the share: still about half. even if every start fell at random, a year of twelve periods would hold a run of three or more near a full or new moon about half the time. that last figure is a simple calculation of ours, from Clue's one in two, not a study.</p>

            <figure class="fig" style="margin:2em 0"><div style="overflow-x:auto;-webkit-overflow-scrolling:touch"><svg viewBox="0 0 580 320" role="img" aria-labelledby="fig-moon-t" style="width:100%;min-width:560px;height:auto;font-family:var(--serif)"><title id="fig-moon-t">twenty starts of a regular 28-day cycle, each drawn a day and a half earlier in the moon's month than the one before. they drift through the bands around the full and new moon in runs of four, eight of twenty inside a band, near what chance gives.</title><rect x="207.3" y="34" width="85.3" height="264" fill="var(--rose)" fill-opacity=".08" stroke="var(--rose)" stroke-opacity=".35" stroke-width=".8"/><rect x="40.0" y="34" width="42.7" height="264" fill="var(--rose)" fill-opacity=".08" stroke="var(--rose)" stroke-opacity=".35" stroke-width=".8"/><rect x="417.3" y="34" width="42.7" height="264" fill="var(--rose)" fill-opacity=".08" stroke="var(--rose)" stroke-opacity=".35" stroke-width=".8"/><text x="250.0" y="26" text-anchor="middle" font-size="10" font-style="italic" fill="var(--soft)">within three days of the full moon</text><text x="61.3" y="26" text-anchor="start" font-size="10" font-style="italic" fill="var(--soft)">of the new moon</text><line x1="40" y1="42.5" x2="460" y2="42.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="288.9" cy="42.5" r="3.6" fill="var(--rose)"/><text x="32" y="46.0" text-anchor="end" font-size="9" fill="var(--muted)">1</text><line x1="40" y1="55.5" x2="460" y2="55.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="267.6" cy="55.5" r="3.6" fill="var(--rose)"/><line x1="40" y1="68.5" x2="460" y2="68.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="244.8" cy="68.5" r="3.6" fill="var(--rose)"/><line x1="40" y1="81.5" x2="460" y2="81.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="223.5" cy="81.5" r="3.6" fill="var(--rose)"/><line x1="40" y1="94.5" x2="460" y2="94.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="202.1" cy="94.5" r="3.6" fill="var(--paper)" stroke="var(--rose)" stroke-width="1.2"/><text x="32" y="98.0" text-anchor="end" font-size="9" fill="var(--muted)">5</text><line x1="40" y1="107.5" x2="460" y2="107.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="179.4" cy="107.5" r="3.6" fill="var(--paper)" stroke="var(--rose)" stroke-width="1.2"/><line x1="40" y1="120.5" x2="460" y2="120.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="158.0" cy="120.5" r="3.6" fill="var(--paper)" stroke="var(--rose)" stroke-width="1.2"/><line x1="40" y1="133.5" x2="460" y2="133.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="136.7" cy="133.5" r="3.6" fill="var(--paper)" stroke="var(--rose)" stroke-width="1.2"/><line x1="40" y1="146.5" x2="460" y2="146.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="115.4" cy="146.5" r="3.6" fill="var(--paper)" stroke="var(--rose)" stroke-width="1.2"/><line x1="40" y1="159.5" x2="460" y2="159.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="92.6" cy="159.5" r="3.6" fill="var(--paper)" stroke="var(--rose)" stroke-width="1.2"/><text x="32" y="163.0" text-anchor="end" font-size="9" fill="var(--muted)">10</text><line x1="40" y1="172.5" x2="460" y2="172.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="71.3" cy="172.5" r="3.6" fill="var(--rose)"/><line x1="40" y1="185.5" x2="460" y2="185.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="50.0" cy="185.5" r="3.6" fill="var(--rose)"/><line x1="40" y1="198.5" x2="460" y2="198.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="448.2" cy="198.5" r="3.6" fill="var(--rose)"/><line x1="40" y1="211.5" x2="460" y2="211.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="425.4" cy="211.5" r="3.6" fill="var(--rose)"/><line x1="40" y1="224.5" x2="460" y2="224.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="404.1" cy="224.5" r="3.6" fill="var(--paper)" stroke="var(--rose)" stroke-width="1.2"/><text x="32" y="228.0" text-anchor="end" font-size="9" fill="var(--muted)">15</text><line x1="40" y1="237.5" x2="460" y2="237.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="382.8" cy="237.5" r="3.6" fill="var(--paper)" stroke="var(--rose)" stroke-width="1.2"/><line x1="40" y1="250.5" x2="460" y2="250.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="360.0" cy="250.5" r="3.6" fill="var(--paper)" stroke="var(--rose)" stroke-width="1.2"/><line x1="40" y1="263.5" x2="460" y2="263.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="338.7" cy="263.5" r="3.6" fill="var(--paper)" stroke="var(--rose)" stroke-width="1.2"/><line x1="40" y1="276.5" x2="460" y2="276.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="317.3" cy="276.5" r="3.6" fill="var(--paper)" stroke="var(--rose)" stroke-width="1.2"/><line x1="40" y1="289.5" x2="460" y2="289.5" stroke="var(--rule)" stroke-width=".6"/><circle cx="294.6" cy="289.5" r="3.6" fill="var(--paper)" stroke="var(--rose)" stroke-width="1.2"/><text x="32" y="293.0" text-anchor="end" font-size="9" fill="var(--muted)">20</text><path d="M468 36 h4 V81.5 h-4" fill="none" stroke="var(--muted)" stroke-width=".8"/><text x="478" y="56.8" font-size="10" font-style="italic" fill="var(--soft)">four in a row</text><text x="478" y="69.8" font-size="10" font-style="italic" fill="var(--soft)">near the full moon.</text><text x="478" y="82.8" font-size="10" font-style="italic" fill="var(--soft)">no moon needed.</text><text x="40.0" y="312" text-anchor="middle" font-size="9" fill="var(--muted)">new</text><text x="250.0" y="312" text-anchor="middle" font-size="9" fill="var(--muted)">full</text><text x="460.0" y="312" text-anchor="middle" font-size="9" fill="var(--muted)">new</text></svg></div><figcaption style="margin-top:.8em;font-size:.88em;font-style:italic;color:var(--soft)">a cycle that never varies, drawn against a moon it ignores. 8 of 20 starts fall within three days of a full or new moon; chance gives about half.</figcaption></figure>
            <h2>how to read your own record honestly</h2>
            <p>if you keep the dates and want to look, these keep the arithmetic on your side:</p>
            <ul>
                <li>decide what counts before you look. "within three days of a full or new moon" is fair, and then about half your starts should land there by chance.</li>
                <li>count every start, not the stretches that look striking. a run of four is expected now and then; it isn't the moon showing itself.</li>
                <li>look over years, not months. a cycle a day or two shorter than the moon's will drift through every phase in time.</li>
                <li>count the misses as well as the hits. a link would show as clearly more than half, cycle after cycle, and across tens of thousands of cycles the most common phase held only slightly more starts than chance would give.{n(7)}</li>
                <li>don't plan by it. no study shows that the moon can tell you when a period will come, and none supports timing a fast, a meal or anything else to it.</li>
                <li>a period that stops, or cycles that change sharply, are worth taking to a doctor. that is a question about the body, not the sky.</li>
            </ul>

            <h2>who shouldn't fast</h2>
            <p>the moon is no reason to begin a fast, to lengthen one or to time one. and some people should not fast without a doctor's advice, whatever the sky is doing:</p>
            <ul>
                <li>anyone with a current or past eating disorder. in a five-year study of 496 adolescent girls, going without food for a day to control weight predicted the start of binge eating and bulimia more strongly than dieting did.{n(12)}</li>
                <li>anyone with diabetes, or on medicines that lower blood sugar. the evidence on fasting with diabetes is almost nonexistent; an expert review says it can be done safely only under the supervision of a doctor, with blood sugar checked.{n(13)}</li>
                <li>during pregnancy or breastfeeding, or while trying to conceive.</li>
                <li>under 18.</li>
                <li>with a missed or irregular period that hasn't been looked into.</li>
            </ul>

            <h2>how hæl draws the moon</h2>
            <p>hæl draws the moon as the sky's calendar over the nights your fasts cross, because that is plainly true: if a fast ran through the night, the moon was in the sky above it. it is worked out on your phone from the time zone alone, with no location asked and nothing sent.</p>
            <p>it is never drawn round the cycle's ring or set against your periods, and it is never a reading of the body. hæl doesn't group fasts or anything else by the moon's phase, because a chart sorted that way would show patterns that chance alone makes. the moon never changes the hours hæl suggests, and nothing in hæl asks you to fast by it.</p>

            <h2>where the moon appears in hæl</h2>
            <ol>
                <li>the ledger opens with the month by the moon. it is a ring of the month, with your fasts as beads where they began, filled where kept to the goal and hollow where set down, and the moon's four phases marked outside, where each fell. one line under it names the night of the longest fast, such as "the longest, thirty-six hours, kept as the moon waned."</li>
                <li>in the ledger, each fast that crossed a night has a small mark of that night's moon beside it. VoiceOver reads it in words: "through the night, a waning moon."</li>
                <li>if you don't keep a cycle, home shows the moon's four marks under the suggestion, new, waxing, full and waning, with tonight's drawn deepest, and one line beneath, such as "the return. a waning moon, thinning toward the new." choose "I don't keep one" on the first page, or turn off "track a cycle" in settings. if you keep a cycle, the cycle comes first and the marks aren't shown.</li>
                <li>with the full witness, the film at the end of a fast draws the night's moon in its sky.</li>
            </ol>
            <p>the timer, the ledger, the moon's marks, the month by the moon and rest days are free. <a href="/how-to-use-hael/">how to use hæl, step by step</a>.</p>

            <div class="aside">
                <p>hæl keeps the moon where it belongs, in the sky over the nights you fasted. it makes no claim that the moon moves the body, suggests no fast by it, and keeps a day of rest as rest. there are no badges and no coaching.</p>
                <a class="download" href="{STORE}">hæl on the App Store</a>
            </div>
"""

# for APPNOTES in build_notes.py: (campaign token, one true sentence)
MOON_APPNOTE = ("article-moon", "hæl, a fasting timer for iPhone, draws the moon over the nights your fasts cross, as the sky's calendar, never as a reading of the body.")

MOON_NOTE = dict(
    slug="menstrual-cycle-moon",
    title="The Moon and the Menstrual Cycle: What the Research Says | hæl",
    description="does the moon affect your period? what large datasets and long diaries found, why chance makes a link look real, and how to read your own record.",
    kicker="the moon",
    h1="the moon and the menstrual cycle",
    headline="The moon and the menstrual cycle: what the research says",
    short="the moon's month is 29.53 days and the average cycle is a day or so shorter, so the two have long been linked. in the large studies, periods start at every phase: in 27,000 European cycles the most common phase held 13.1% of starts, against 12.5% by chance. small diary studies found runs near the full or new moon, mostly before 2010. no cause is known, and chance alone puts about half of starts within three days of one.",
    body=MOON_BODY, sources=MOON_SOURCES,
    published="2026-11-09", published_text="november 9, 2026",
    appnote=MOON_APPNOTE,
)

if __name__ == "__main__":
    # quick self-checks only; builds nothing
    import re
    text = MOON_BODY + MOON_NOTE["short"] + MOON_NOTE["description"] + MOON_NOTE["title"] + MOON_NOTE["headline"] + MOON_APPNOTE[1]
    assert "—" not in text and "–" not in text, "dash found"
    assert "!" not in text, "exclamation found"
    assert not re.search(r"\b(she|her|hers|herself)\b", text, re.I), "she/her found"
    assert len(MOON_NOTE["description"]) < 160, len(MOON_NOTE["description"])
    # never "sync" as advice: the word appears only inside a source title
    assert not re.search(r"\bsync", text, re.I), "sync found"
    used = sorted({int(x) for x in re.findall(r'href="#s(\d+)"', MOON_BODY)})
    assert used == list(range(1, len(MOON_SOURCES) + 1)), used
    # footnotes appear in order of first use
    first = []
    for x in re.findall(r'href="#s(\d+)"', MOON_BODY):
        if int(x) not in first:
            first.append(int(x))
    assert first == list(range(1, len(MOON_SOURCES) + 1)), first
    assert all(k in s for s in MOON_SOURCES for k in ("html", "cite", "verified"))
    print("ok:", len(MOON_SOURCES), "sources, description", len(MOON_NOTE["description"]), "chars")
