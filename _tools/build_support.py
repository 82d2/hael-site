"""Builds support/index.html in the shared frame: how to write, and the
answers people write for most (restore, the plan, refunds, the data).
Run: python3 _tools/build_support.py"""
import pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import shell

ROOT = pathlib.Path(__file__).resolve().parent.parent
head = shell.head(title="support · hæl",
                  description="write to hæl, and the answers to what is asked most: restoring a purchase, the plan, refunds, Apple Health and the data.",
                  path="/support/")

QA = [
    ("to write", 'write to <a href="mailto:hello@hael.app">hello@hael.app</a>. a person reads every letter, usually within two days. for anything about a purchase, the support ID in settings → iv the full witness helps: it is a random code, not your name, and it lets us find the purchase without anything else.'),
    ("a purchase that didn't arrive, or a new phone", 'in hæl, settings → iv the full witness → restore a previous purchase. it asks Apple for what this Apple Account has bought; nothing is needed from us. use the same Apple Account the purchase was made with.'),
    ("the plan: changing or cancelling", 'the year and the month are managed by Apple: settings → iv the full witness → manage the plan, or the App Store app → your account → subscriptions. cancelling at least a day before a period ends means nothing more is charged; the full witness stays open until then, and everything kept stays after.'),
    ("the fourteen days", 'the year begins with fourteen days at no cost for new subscribers. cancel in the App Store at least a day before they end and nothing is charged.'),
    ("refunds", 'refunds are made by Apple, not by us: <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>, sign in, choose hæl, and say what happened.'),
    ("Apple Health", 'connecting is a choice, in the first entry or in settings → ii the form. hæl reads and writes period starts and weight, and can record each fast as a mind and body session. to change what it may read or write: the Health app → your profile → apps → hæl.'),
    ("the data, and deleting it", 'everything lives on the phone, in your own iCloud, and in Apple Health; there is no account and no server of ours. settings → iii the record exports it; settings → v about and privacy deletes all of it. what is counted, anonymously, is set out in <a href="/privacy/">the privacy policy</a>.'),
]

body = shell.title_block("support", "write to us.", "hello@hael.app · a person reads every letter") + """
<article class="text">
""" + "\n".join(f"            <h2>{q}</h2>\n            <p>{a}</p>\n" for q, a in QA) + """
</article>
""" + shell.closing() + "\n" + shell.more([("/", "← hæl, the fasting timer"), ("/how-to-use-hael/", "how to use hæl"), ("/terms/", "terms"), ("/privacy/", "privacy")])

out = ROOT / "support"; out.mkdir(exist_ok=True)
(out / "index.html").write_text(shell.page(head_html=head, body=body, current="/support/"), encoding="utf-8")
print("built support/index.html")
