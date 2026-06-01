#!/usr/bin/env python3
"""Generate MagicForge Studio developer-profile assets: 512x512 logo + 4096x2304 cover."""
import math, random, subprocess, os
random.seed(7)
HERE = os.path.dirname(os.path.abspath(__file__))

GRAD = ('<linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#22d3ee"/>'
        '<stop offset=".5" stop-color="#8b5cf6"/>'
        '<stop offset="1" stop-color="#d946ef"/></linearGradient>')

# 8-point spark/star path on a 48 viewBox (matches site logo)
STAR = ('M24 3l4.2 12.6L41 19l-9.5 8.4L34 41 24 33.5 14 41l2.5-13.6L7 19l12.8-3.4L24 3z')

def star_group(cx, cy, scale, glow=True):
    """Return an SVG group of the filled-gradient star centered at cx,cy scaled from the 48-grid."""
    s = scale / 48.0
    tx = cx - 24 * s
    ty = cy - 22 * s   # 22 = optical center of star
    g = ''
    if glow:
        g += (f'<g transform="translate({tx},{ty}) scale({s})" filter="url(#blur)" opacity=".75">'
              f'<path d="{STAR}" fill="url(#g)"/></g>')
    g += (f'<g transform="translate({tx},{ty}) scale({s})">'
          f'<path d="{STAR}" fill="url(#g)"/>'
          f'<circle cx="24" cy="22" r="5.4" fill="#fff" opacity=".92"/>'
          f'<circle cx="24" cy="22" r="2.6" fill="#fff"/></g>')
    return g

# ---------------- LOGO 512x512 ----------------
logo = f'''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
<defs>{GRAD}
<radialGradient id="bg" cx="50%" cy="42%" r="70%">
  <stop offset="0" stop-color="#160d2e"/><stop offset="1" stop-color="#07040f"/></radialGradient>
<filter id="blur" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="9"/></filter>
</defs>
<rect width="512" height="512" fill="url(#bg)"/>
<circle cx="256" cy="232" r="180" fill="none" stroke="url(#g)" stroke-width="2" opacity=".25"/>
<circle cx="256" cy="232" r="150" fill="url(#g)" opacity=".10" filter="url(#blur)"/>
{star_group(256, 232, 270)}
<text x="256" y="452" text-anchor="middle" font-family="Helvetica Neue,Helvetica,Arial,sans-serif"
      font-weight="700" font-size="54" letter-spacing="1" fill="#f4f0ff">MagicForge</text>
</svg>'''

# ---------------- COVER 4096x2304 ----------------
W, H = 4096, 2304
# starfield
stars = ''
for _ in range(260):
    x = random.uniform(0, W); y = random.uniform(0, H)
    r = random.uniform(1.2, 4.2); o = random.uniform(0.15, 0.85)
    stars += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="#cbd5ff" opacity="{o:.2f}"/>'
# a few colored ember dots
COL = ['#22d3ee', '#8b5cf6', '#d946ef', '#ff7a3d', '#fbbf24']
for _ in range(40):
    x = random.uniform(0, W); y = random.uniform(0, H)
    r = random.uniform(2.5, 6); c = random.choice(COL)
    stars += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="{c}" opacity=".55"/>'
# grid lines
grid = ''
for gx in range(0, W + 1, 160):
    grid += f'<line x1="{gx}" y1="0" x2="{gx}" y2="{H}" stroke="#a89dc4" stroke-width="1" opacity=".05"/>'
for gy in range(0, H + 1, 160):
    grid += f'<line x1="0" y1="{gy}" x2="{W}" y2="{gy}" stroke="#a89dc4" stroke-width="1" opacity=".05"/>'

cover = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>{GRAD}
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="#0a0618"/><stop offset=".5" stop-color="#07040f"/><stop offset="1" stop-color="#0c0818"/></linearGradient>
<radialGradient id="v1" cx="20%" cy="28%" r="55%"><stop offset="0" stop-color="#8b5cf6" stop-opacity=".42"/><stop offset="1" stop-color="#8b5cf6" stop-opacity="0"/></radialGradient>
<radialGradient id="v2" cx="86%" cy="22%" r="50%"><stop offset="0" stop-color="#22d3ee" stop-opacity=".30"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
<radialGradient id="v3" cx="72%" cy="92%" r="55%"><stop offset="0" stop-color="#d946ef" stop-opacity=".30"/><stop offset="1" stop-color="#d946ef" stop-opacity="0"/></radialGradient>
<radialGradient id="v4" cx="10%" cy="92%" r="45%"><stop offset="0" stop-color="#ff7a3d" stop-opacity=".22"/><stop offset="1" stop-color="#ff7a3d" stop-opacity="0"/></radialGradient>
<filter id="blur" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="22"/></filter>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#07040f" stop-opacity="0"/><stop offset="1" stop-color="#07040f" stop-opacity=".55"/></linearGradient>
</defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/>
{grid}
{stars}
<rect width="{W}" height="{H}" fill="url(#v1)"/>
<rect width="{W}" height="{H}" fill="url(#v2)"/>
<rect width="{W}" height="{H}" fill="url(#v3)"/>
<rect width="{W}" height="{H}" fill="url(#v4)"/>
<rect width="{W}" height="{H}" fill="url(#fade)"/>

<!-- big soft glow ring behind logo -->
<circle cx="980" cy="1080" r="560" fill="none" stroke="url(#g)" stroke-width="3" opacity=".18"/>
<circle cx="980" cy="1080" r="430" fill="url(#g)" opacity=".10" filter="url(#blur)"/>
{star_group(980, 1080, 760)}

<!-- wordmark -->
<text x="1640" y="1010" font-family="Helvetica Neue,Helvetica,Arial,sans-serif" font-weight="800"
      font-size="290" letter-spacing="-4" fill="#f4f0ff">MagicForge</text>
<text x="1648" y="1310" font-family="Helvetica Neue,Helvetica,Arial,sans-serif" font-weight="300"
      font-size="220" letter-spacing="34" fill="#a89dc4">STUDIO</text>
<text x="1656" y="1500" font-family="Helvetica Neue,Helvetica,Arial,sans-serif" font-weight="400"
      font-size="92" fill="#cbbfe6" opacity=".9">We forge worlds worth getting lost in.</text>

<!-- game chips -->
<g font-family="Helvetica Neue,Helvetica,Arial,sans-serif" font-weight="600" font-size="62" fill="#a89dc4">
  <rect x="1656" y="1610" width="520" height="120" rx="60" fill="none" stroke="#a89dc4" stroke-opacity=".25" stroke-width="2"/>
  <text x="1916" y="1690" text-anchor="middle">★ Star Saviors</text>
  <rect x="2216" y="1610" width="470" height="120" rx="60" fill="none" stroke="#a89dc4" stroke-opacity=".25" stroke-width="2"/>
  <text x="2451" y="1690" text-anchor="middle">✦ MagicMath</text>
</g>
</svg>'''

open(f'{HERE}/_logo.svg', 'w').write(logo)
open(f'{HERE}/_cover.svg', 'w').write(cover)
print('SVGs written')

def render(svg, png, w, h):
    subprocess.run(['rsvg-convert', '-w', str(w), '-h', str(h),
                    '-b', '#07040f', f'{HERE}/{svg}', '-o', f'{HERE}/{png}'], check=True)

render('_logo.svg', '_logo_raw.png', 512, 512)
render('_cover.svg', '_cover_raw.png', W, H)
print('PNGs rendered')

# flatten to 24-bit RGB (non-transparent) + keep <1MB
from PIL import Image
def finalize(src, dst, maxbytes=1_000_000):
    im = Image.open(f'{HERE}/{src}').convert('RGB')
    im.save(f'{HERE}/{dst}', 'PNG', optimize=True)
    size = os.path.getsize(f'{HERE}/{dst}')
    if size > maxbytes:
        jpg = dst.rsplit('.', 1)[0] + '.jpg'
        q = 92
        while q >= 60:
            im.save(f'{HERE}/{jpg}', 'JPEG', quality=q, optimize=True, progressive=True)
            size = os.path.getsize(f'{HERE}/{jpg}')
            if size <= maxbytes:
                break
            q -= 6
        os.remove(f'{HERE}/{dst}')
        return jpg, size
    return dst, size

l = finalize('_logo_raw.png', 'dev-logo-512.png')
c = finalize('_cover_raw.png', 'dev-cover-4096x2304.png')
print('LOGO ->', l[0], f'{l[1]/1024:.0f} KB')
print('COVER ->', c[0], f'{c[1]/1024:.0f} KB')

# cleanup intermediates
for f in ['_logo.svg', '_cover.svg', '_logo_raw.png', '_cover_raw.png']:
    p = f'{HERE}/{f}'
    if os.path.exists(p):
        os.remove(p)
print('done')
