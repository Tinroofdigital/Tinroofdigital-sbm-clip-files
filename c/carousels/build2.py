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
.src{{font:600 28px I;color:#8f8579;letter-spacing:1px}}
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
 'C5-five-fixes': [
  '<div class=k>FOR REAL ESTATE AGENTS</div><div class=big>5 Google profile fixes <em>sellers notice.</em></div><div class=body>Found on real agent profiles in October. Names left off.</div>',
  '<div class=k>FIX 1. AGENT, NOT AGENCY</div><div class=mid>Your main category should be <em>real estate agent.</em></div><div class=body>One agent\'s own profile was set up as an agency. Your brokerage\'s office is the agency. Your profile is you.</div>',
  '<div class=k>FIX 2. BE WHERE YOU SELL</div><div class=mid>One profile sat about <em>20 miles</em> from where she sells.</div><div class=body>If clients don\'t meet you at an office, hide the address and set a service area with your real towns.</div>',
  '<div class=k>FIX 3. ONE NUMBER, ONE STORY</div><div class=mid>Same phone number <em>everywhere.</em></div><div class=body>Google, Zillow, Realtor.com, Homes.com and your site. Then call it from another phone and make sure it rings you.</div>',
  '<div class=k>FIX 4. ONLY WHAT YOU OFFER</div><div class=mid>Home loans and insurance <em>don\'t belong</em> there.</div><div class=body>Unless you actually do them. Keep buying, selling and the kinds of homes you work with.</div>',
  '<div class=k>FIX 5. A LINK THAT WORKS</div><div class=mid>Send sellers to a page about <em>you.</em></div><div class=body>Your photo, a short bio, your reviews and a way to reach you. Tap it on your phone once a month.</div>',
  '<div class=k>TONIGHT, ABOUT 5 MINUTES</div><div class=mid>Search your name. Read the gray line under it.</div><div class=body>Check your pin, call your number, scroll your services, tap your link. Check with your broker before you change anything.</div>',
  END],
 'C6-closing-day-ask': [
  '<div class=k>FOR REAL ESTATE AGENTS</div><div class=big>The closing day review ask, <em>word for word.</em></div><div class=body>Save this. Put it in your phone tonight.</div>',
  '<div class=k>WHEN TO ASK</div><div class=mid>The day it <em>closes.</em></div><div class=body>They\'re relieved, grateful and already telling everybody. That\'s the easiest ask you\'ll ever make.</div>',
  '<div class=k>BUYERS, THE DAY THEY GET THE KEYS</div><div class=body style="font-size:56px;line-height:1.32;color:#fff">"Hi, it\'s [name]. Congratulations on the new place. It was a joy helping you find it. If you have thirty seconds, would you share your experience on Google? It helps the next client find me."</div><div class=body><em>+ your review link</em></div>',
  '<div class=k>SELLERS, THE DAY IT CLOSES</div><div class=body style="font-size:56px;line-height:1.32;color:#fff">"Hi, it\'s [name]. It\'s officially closed. Thank you for trusting me with your home. If you have a minute, would you share how it went on Google? It means a lot."</div><div class=body><em>+ your review link</em></div>',
  '<div class=k>PAST CLIENTS</div><div class=body style="font-size:56px;line-height:1.32;color:#fff">"Hi, it\'s [name]. I was thinking about your move and hope the house is treating you well. I\'m building up my Google reviews. If you have thirty seconds, I\'d be grateful if you\'d share your experience."</div><div class=body><em>+ your review link</em></div>',
  '<div class=k>NOTICE WHAT\'S NOT IN THERE</div><div class=mid>No stars. No gifts tied to it.</div><div class=body>Same words for every client, not just the happy ones. Google doesn\'t allow anything in exchange for a review. Run the wording past your broker.</div>',
  END],
 'C7-first-time-buyers': [
  '<div class=k>NAR 2025 PROFILE OF HOME BUYERS AND SELLERS</div><div class=big>Your first time buyer isn\'t who you <em>think.</em></div>',
  '<div class=k>MEDIAN AGE</div><div class=num>40</div><div class=body>The median first time buyer was 40 years old.</div><div class=src>Source: NAR 2025 Profile of Home Buyers and Sellers</div>',
  '<div class=k>SHARE OF ALL BUYERS</div><div class=num>21%</div><div class=body>First time buyers were 21% of buyers, the lowest NAR has ever recorded.</div><div class=src>Source: NAR 2025 Profile of Home Buyers and Sellers</div>',
  '<div class=k>MEDIAN DOWN PAYMENT</div><div class=num>10%</div><div class=body>Not 20. Renters waiting years to save 20% may be waiting longer than they need to.</div><div class=src>Source: NAR 2025 Profile of Home Buyers and Sellers</div>',
  '<div class=k>WHAT TO DO WITH THAT</div><div class=mid>Talk to the person with a career and years of <em>rent receipts.</em></div><div class=body>Make a one minute video with your lender on down payments. Pin it and send it to every renter who asks.</div>',
  END],
 'C8-search-your-name': [
  '<div class=k>FOR REAL ESTATE AGENTS</div><div class=big>Search your own name on <em>Google Maps</em> tonight.</div>',
  '<div class=k>A REAL PROFILE I GRADED</div><div class=mid>Google said this agent was <em>permanently closed.</em></div><div class=body>His only listing had an old office address, and nobody had claimed it.</div>',
  '<div class=k>WHAT A SELLER THINKS</div><div class=big><em>"He quit."</em></div><div class=body>Anyone who found him there figured he was out of the business.</div>',
  '<div class=k>CHECK 3 THINGS</div><div class=mid>1. Does it say closed?<br>2. An old brokerage or address?<br>3. Is it claimed by you?</div>',
  '<div class=k>IF ANYTHING\'S OFF</div><div class=mid>Claim it and fix it <em>this week.</em></div><div class=body>If your brokerage manages your profile, start with your broker.</div>',
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
