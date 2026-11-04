"""Tin Roof carousels from the road shoot data. 1080x1350, brand dark/orange, Inter."""
import os
from playwright.sync_api import sync_playwright
F = 'file:///usr/share/fonts/opentype/inter/'
CSS = f"""@font-face{{font-family:I;src:url({F}Inter-Black.otf);font-weight:900}}
@font-face{{font-family:I;src:url({F}Inter-Bold.otf);font-weight:700}}
@font-face{{font-family:I;src:url({F}Inter-Medium.otf);font-weight:500}}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;background:#1f1f1d;font-family:I;color:#fff;position:relative;overflow:hidden}}
.bg{{position:absolute;inset:0;background:radial-gradient(1100px 900px at 30% 25%,#3a2416 0%,#1f1f1d 68%)}}
.wrap{{position:absolute;left:90px;right:90px;top:120px;bottom:230px;display:flex;flex-direction:column;justify-content:center;gap:44px}}
.k{{font:800 36px I;letter-spacing:6px;color:#ff7a1f}}
.big{{font:900 116px/1.0 I;letter-spacing:-3px}}
.mid{{font:900 90px/1.04 I;letter-spacing:-2.5px}}
.body{{font:700 52px/1.3 I;color:#f3e6d6}}
em{{font-style:normal;color:#ffd166}}
.num{{font:900 260px/0.9 I;color:#ff7a1f;letter-spacing:-9px}}
.foot{{position:absolute;left:90px;right:90px;bottom:80px;display:flex;justify-content:space-between;align-items:center}}
.br{{font:900 34px I;color:#ff7a1f}} .br span{{color:#f3e6d6;font-size:24px;letter-spacing:6px;margin-left:10px}}
.pg{{font:700 28px I;color:#8f8579}}
.sw{{position:absolute;right:90px;bottom:150px;font:800 30px I;color:#ffd166;letter-spacing:2px}}
.bar{{position:absolute;left:90px;width:120px;height:10px;background:#ff7a1f}}"""
def page(inner, i, n, swipe=False):
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=bg></div><div class=wrap>{inner}</div>
{'<div class=sw>SWIPE &rarr;</div>' if swipe else ''}
<div class=foot><div class=br>TIN ROOF <span>DIGITAL</span></div><div class=pg>{i}/{n}</div></div></body></html>"""
END = ('<div class=k>REAL ESTATE AGENTS</div><div class=mid>Follow for <em>free tips</em> for agents.</div>'
       '<div class=body>One fix at a time. No fluff.<br><br>Save this for later, or send it to an agent who needs it.</div>')
C = {
 'C1-most-reviews-10th': [
  '<div class=k>I GRADED THE TOP 10 ON GOOGLE MAPS</div><div class=big>The most reviews in Chicago came in <em>10th.</em></div><div class=body>Here\'s what that tells you about the map.</div>',
  '<div class=k>HOW I CHECKED</div><div class=mid>Oct 20. Google Maps. "Real estate agent" plus the city.</div><div class=body>First 10 profiles in Indianapolis and the first 10 in Chicago. Offices, teams and solo agents. No names.</div>',
  '<div class=k>CHICAGO, SPOT 10</div><div class=num>756</div><div class=body>Google reviews. The most of any profile in Chicago\'s top 10.<br><br>And it sat <em>last.</em></div>',
  '<div class=k>SPOTS 7 TO 10 WEREN\'T WEAK</div><div class=mid>Two got <em>60+</em> new reviews this year.</div><div class=body>All four replied to almost every recent review.</div>',
  '<div class=k>CHICAGO, SPOT 1</div><div class=mid>About <em>2 years</em> without a new review.</div><div class=body>Summer 2024 to summer 2026. Still number one.</div>',
  '<div class=k>WHAT IT MEANS</div><div class=mid>Past a certain point, the map isn\'t a scoreboard.</div><div class=body>Google says it weighs how well you match the search, how far you are, and how well known you are. One day, two cities, a snapshot.</div>',
  END],
 'C2-stars': [
  '<div class=k>TOP 20 ON GOOGLE MAPS, INDY AND CHICAGO</div><div class=big>Your star rating isn\'t <em>holding you back.</em></div>',
  '<div class=k>THE NUMBERS</div><div class=num>18/20</div><div class=body>of the top real estate profiles in Indianapolis and Chicago had <em>4.8 stars or better.</em><br><br>Stars barely separate anybody.</div>',
  '<div class=k>EXHIBIT A</div><div class=mid>A Chicago office with a <em>4.2</em> still made the top 10.</div>',
  '<div class=k>EXHIBIT B</div><div class=mid>Another had a <em>4.7</em> and sat at number 3.</div>',
  '<div class=k>SO WHAT</div><div class=mid>A perfect 5 isn\'t the ticket.</div><div class=body>A 4.7 won\'t knock you off the map. Put the energy into getting more reviews and replying to every one.</div>',
  END],
 'C3-top3': [
  '<div class=k>INDY AND CHICAGO, OCT 20</div><div class=big>What the top 3 on Google Maps <em>all had.</em></div><div class=body>Six profiles. Three things in common.</div>',
  '<div class=k>1. REAL PROOF</div><div class=num>121+</div><div class=body>Google reviews each, at minimum.</div>',
  '<div class=k>2. THEY ANSWER REVIEWS</div><div class=mid>All six replied to at least <em>8 of 10</em> recent reviews.</div><div class=body>Two replied to every one of their last 60.</div>',
  '<div class=k>3. A STEADY STREAM</div><div class=mid><em>5 of the 6</em> got 18+ new reviews this year.</div><div class=body>Not a burst. A habit.</div>',
  '<div class=k>THE HONEST PART</div><div class=mid>Four profiles lower on the list had all three too.</div><div class=body>In a big city, that\'s the <em>ticket in,</em> not the trophy. Win where you actually sell first.</div>',
  END],
 'C4-one-week': [
  '<div class=k>FOR REAL ESTATE AGENTS</div><div class=big>Fix your Google profile in <em>one week.</em></div><div class=body>No money. One small fix a day.</div>',
  '<div class=k>MONDAY</div><div class=mid>Fix your category and your location.</div><div class=body>Real estate agent, not agency. Right address, or a service area with the towns you actually work.</div>',
  '<div class=k>TUESDAY</div><div class=mid>One phone number everywhere.</div><div class=body>Then tap it and make sure your phone rings. Tap your website link and make sure it loads.</div>',
  '<div class=k>WEDNESDAY</div><div class=mid>Text your last 10 clients for a Google review.</div><div class=body>Same words for everybody. No gifts tied to it.</div>',
  '<div class=k>EVERY DAY AFTER</div><div class=mid>Reply to every review that comes in.</div><div class=body>Keep replies about the home and the work. Check with your broker before you change your profile or your wording.</div>',
  END],
}
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width':1080,'height':1350})
    for name, slides in C.items():
        os.makedirs(name, exist_ok=True)
        for i, s in enumerate(slides, 1):
            open('t.html','w').write(page(s, i, len(slides), swipe=(i==1)))
            pg.goto('file:///home/claude/carousels/t.html'); pg.wait_for_timeout(150)
            pg.screenshot(path=f'{name}/{i:02d}.jpg', type='jpeg', quality=90)
    b.close()
print('ok')
