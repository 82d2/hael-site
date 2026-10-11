# hæl web traffic plan

*Written October 11, 2026, with 4.3 in review. Owner: Joy. Privacy-first throughout: no web analytics, no tracking pixels, no ad networks.*

## Where things stand

hael.app is a one-screen page: a headline, a download button and a price, about fifteen words. Google has almost nothing to rank it for. The technical base is now sound (fixed and live in `25eb398`): canonical URLs, a sitemap of the final addresses, structured data describing the app, store links that open the visitor's own country, and "hael" (plain spelling) in the title.

## The goal

Be found by the people already looking for something like hæl, in three places: Google and Bing, the App Store, and the communities they read. Measure it without tracking anyone.

## Phase 1: this week (about an hour, mostly yours)

| # | Task | Who | Why |
|---|------|-----|-----|
| 1 | Google Search Console: add hael.app, verify by DNS, submit `https://hael.app/sitemap.xml` | Joy | Shows the searches that find you, with no tracking on the site |
| 2 | Bing Webmaster Tools: import from Search Console | Joy | Bing also feeds ChatGPT search and DuckDuckGo |
| 3 | App Store campaign link: App Analytics → Campaigns, send Claude the `pt=` value | Joy, then Claude | Downloads from the website show in App Store Connect, counted by Apple in aggregate |
| 4 | Featuring nomination for 4.3 in App Store Connect (Featuring → Nominations) | Joy | The single best chance of real traffic; free |
| 5 | Approve the home page redesign (mock on branch `claude/gifted-turing-8rg1hy` of hael-site) | Joy | Gives Google words to rank |

## Phase 2: the next month

1. **Home page live.** Five sections in the book's order (the hours, the page, the water, the cycle, the colophon) and six questions with FAQ structured data. Each question is a real search:
   - does it work without a period or on birth control
   - is it a subscription
   - does it work with Apple Health
   - where does my data go
   - Apple Watch and iPad
   - is it medical advice
2. **Two articles, no more until they prove themselves.** Written together, sourced, marked not medical advice, in the voice but plainer than the app:
   - *why weight rises before your period*: the body ring's subject; a common, anxious search; hæl's answer is honest and specific.
   - *intermittent fasting and the menstrual cycle*: the category's biggest search. Say what the evidence does and doesn't show.
   Google ranks health pages on accuracy and sources. A thin or overclaiming article hurts the whole site.
3. **A press page (`/press`).** The icon, the v3 screenshots, the header, a one-paragraph description, the one-line pitch, a contact. Journalists and newsletter writers need this before they write.
4. **App Store search.** Review the 100-character keyword field against what Search Console shows people typing.

## Phase 3: ongoing, a few hours a month

**Who hæl is for, and where they are**

| Who | What they want | Where | The approach |
|-----|----------------|-------|--------------|
| Women tired of coaching apps (Zero, Simple, Flo) | No streaks, no nagging, no subscription | App Store search, Reddit, Threads | "no coaching. no celebration. no subscription." |
| Cycle-syncing readers | Fasting that respects the luteal phase | Substack newsletters, podcasts on hormonal health, slow living | Ask to be reviewed, never pay for placement |
| Design and literary people | Software that feels made | Product Hunt, indie app newsletters, design Threads and Bluesky | The book-like screenshots and the hour lines |
| The privacy-minded | Women's health without a data trade | Privacy newsletters, r/privacy | No account, no server, the policy itself |

**How to show up**
- **Product Hunt:** one launch day, timed to a quiet week. Prepare the press page first.
- **Reddit** (r/intermittentfasting, r/xxfitness, r/PCOS): only as the maker answering questions. Most of these forums ban promotion; read each one's rules first.
- **Newsletters:** a short personal note to five writers a month, with the press page link.
- **Your own voice:** one post a week on Threads or Bluesky with an hour line and a screenshot. The prose is the marketing.

## Measuring it

- **Search Console:** impressions, clicks, and the queries behind them. Check monthly.
- **App Store Connect:** downloads from the website campaign link, plus impressions and page views.
- **No Google Analytics, no pixels.** hæl's promise is that nothing watches you. The website keeps it too.

## Not doing

- Paid ads. They burn money before the organic baseline is known.
- Many thin articles. Two good pages beat twenty quick ones.
- Health claims the app doesn't make. hæl observes; the site does too.
