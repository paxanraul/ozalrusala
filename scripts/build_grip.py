"""Build the registered, layered envelope scene from one imagegen composition.

All paths use the original 1536 x 1024 image coordinates. No bitmap is cut or
resampled here: SVG masks select the original photo pixels in the browser.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LEFT_THUMB = (
    "M326 246 C350 247 370 257 393 265 "
    "C437 273 500 273 520 295 C535 311 538 338 522 354 "
    "C507 372 483 379 460 375 C417 372 372 363 341 358 "
    "L314 352 L310 267Z"
)
RIGHT_THUMB = (
    "M1210 654 C1155 652 1114 666 1077 680 "
    "C1036 694 976 691 934 703 C900 709 881 722 886 746 "
    "C889 771 913 784 949 785 L1118 782 "
    "C1152 786 1182 798 1216 810 L1300 745Z"
)
ENVELOPE = "M342 230H1158Q1174 230 1174 246V767Q1174 783 1158 783H342Q326 783 326 767V246Q326 230 342 230Z"
FLAP = "M326 230H1163Q1178 230 1168 242L770 607Q756 621 742 608L326 246Z"
POCKET = "M326 230L742 608Q756 621 770 607L1174 230V767Q1174 783 1158 783H342Q326 783 326 767Z"


def svg(content):
    return f'<svg viewBox="0 0 1536 1024" width="1536" height="1024" aria-hidden="true" focusable="false">{content}</svg>'


def photo(name, extra=""):
    return f'<image href="assets/grip/{name}.webp" width="1536" height="1024" {extra}/>'


defs = f'''<svg class="grip-defs" width="0" height="0" aria-hidden="true" focusable="false"><defs>
  <clipPath id="grip-envelope" clipPathUnits="userSpaceOnUse"><path d="{ENVELOPE}"/></clipPath>
  <clipPath id="grip-flap" clipPathUnits="userSpaceOnUse"><path d="{FLAP}"/></clipPath>
  <clipPath id="grip-pocket" clipPathUnits="userSpaceOnUse"><path d="{POCKET}"/></clipPath>
  <clipPath id="grip-left-thumb" clipPathUnits="userSpaceOnUse"><path d="{LEFT_THUMB}"/></clipPath>
  <clipPath id="grip-right-thumb" clipPathUnits="userSpaceOnUse"><path d="{RIGHT_THUMB}"/></clipPath>
  <mask id="grip-left-rear" maskUnits="userSpaceOnUse" x="0" y="0" width="1536" height="1024" style="mask-type:luminance">
    <rect width="1536" height="1024" fill="white"/><path d="{LEFT_THUMB}" fill="black"/>
    <path d="M512 293L716 290" stroke="black" stroke-width="8"/>
  </mask>
  <mask id="grip-right-rear" maskUnits="userSpaceOnUse" x="0" y="0" width="1536" height="1024" style="mask-type:luminance">
    <rect width="1536" height="1024" fill="white"/><path d="{RIGHT_THUMB}" fill="black"/>
  </mask>
  <filter id="grip-shadow-soften" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="4"/></filter>
  <mask id="grip-left-contact" maskUnits="userSpaceOnUse" x="0" y="0" width="1536" height="1024" style="mask-type:luminance">
    <path d="{LEFT_THUMB}" fill="white" stroke="white" stroke-width="32" filter="url(#grip-shadow-soften)"/><path d="{LEFT_THUMB}" fill="black"/>
  </mask>
  <mask id="grip-right-contact" maskUnits="userSpaceOnUse" x="0" y="0" width="1536" height="1024" style="mask-type:luminance">
    <path d="{RIGHT_THUMB}" fill="white" stroke="white" stroke-width="32" filter="url(#grip-shadow-soften)"/><path d="{RIGHT_THUMB}" fill="black"/>
  </mask>
</defs></svg>'''

parts = [defs]
for side in ["left", "right"]:
    parts.append(f'<div class="grip-frame grip-hand grip-hand-{side} grip-hand-rear" aria-hidden="true">' + svg(photo(f"{side}-hand", f'mask="url(#grip-{side}-rear)"')) + '</div>')

parts.append('<div class="grip-frame grip-lining" aria-hidden="true">' + svg(
    f'<g clip-path="url(#grip-envelope)">{photo("envelope")}<path d="{ENVELOPE}" fill="#062d22" opacity=".68"/></g>'
) + '</div>')

parts.append('<div class="grip-frame grip-flap grip-flap-back" aria-hidden="true">' + svg(
    f'<g clip-path="url(#grip-flap)">{photo("envelope")}<path d="{FLAP}" fill="#1b513c" opacity=".35"/></g>'
) + '</div>')

parts.append('''<div class="card-track"><div class="heart-card">
  <img class="heart-lace" src="assets/ornaments/heart-lace.svg" width="420" height="410" alt="" aria-hidden="true">
  <div class="heart-lettering"><p class="card-initials">O<span>&amp;</span>R</p><div class="heart-rule" aria-hidden="true"></div><p class="heart-date">14.11.2026</p></div>
</div></div>''')

parts.append('<div class="grip-frame grip-pocket" aria-hidden="true">' + svg(photo("envelope", 'clip-path="url(#grip-pocket)"')) + '</div>')
parts.append('<div class="grip-frame grip-flap grip-flap-front" aria-hidden="true">' + svg(photo("envelope", 'clip-path="url(#grip-flap)"')) + '</div>')

for side in ["left", "right"]:
    parts.append(f'<div class="grip-frame grip-contact grip-contact-{side}" aria-hidden="true">' + svg(
        f'<g clip-path="url(#grip-envelope)">{photo("composition", f"mask=\"url(#grip-{side}-contact)\"")}</g>'
    ) + '</div>')

parts.append('''<div class="wax-seal" aria-hidden="true"><img src="assets/velvet/wax-seal.svg" width="120" height="120" alt=""><span class="wax-monogram">O<span>&amp;</span>R</span></div>''')

for side in ["left", "right"]:
    parts.append(f'<div class="grip-frame grip-hand grip-hand-{side} grip-hand-front" aria-hidden="true">' + svg(photo(f"{side}-hand", f'clip-path="url(#grip-{side}-thumb)"')) + '</div>')

scene = '<div class="envelope-scene grip-scene" aria-label="Свадебное приглашение Ozal и Rusala">\n' + '\n'.join(parts) + '\n</div>\n        '
path = ROOT / 'index.html'
html = path.read_text()
html, count = re.subn(r'<div class="envelope-scene[^>]*>.*?(?=<div class="hero-signature">)', scene, html, count=1, flags=re.S)
assert count == 1, "Envelope scene not found"
path.write_text(html)
print('Registered grip scene rebuilt.')
