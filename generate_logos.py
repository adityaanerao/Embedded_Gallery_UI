import base64

with open('assets/embedgallery-badge.png', 'rb') as f:
    b64_badge = base64.b64encode(f.read()).decode('utf-8')

with open('assets/embedgallery-badge-transparent.png', 'rb') as f:
    b64_badge_trans = base64.b64encode(f.read()).decode('utf-8')

with open('assets/embedgallery-emblem-transparent.png', 'rb') as f:
    b64_emblem = base64.b64encode(f.read()).decode('utf-8')

# 1. embedgallery-logo.svg (Horizontal brand logo with emblem + title)
svg_horizontal = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 74" width="100%" height="100%">
  <defs>
    <filter id="egShadow" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="rgba(11, 59, 149, 0.25)" />
    </filter>
  </defs>
  <g filter="url(#egShadow)">
    <image href="data:image/png;base64,{b64_emblem}" x="2" y="3" width="68" height="68" />
  </g>
  <text x="80" y="41" fill="#0B3B95" font-family="'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="25" font-weight="900" letter-spacing="0.2px">
    Embed<tspan fill="#1E40AF">Gallery</tspan>
  </text>
  <text x="81" y="58" fill="#64748B" font-family="'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9.5" font-weight="700" letter-spacing="1.5px">
    ELECTRONICS PVT LTD
  </text>
</svg>'''

with open('assets/embedgallery-logo.svg', 'w', encoding='utf-8') as f:
    f.write(svg_horizontal)

# 2. embedgallery-white.svg (For dark blue / gradient headers)
svg_white = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 74" width="100%" height="100%">
  <defs>
    <filter id="egGlow" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="rgba(0, 0, 0, 0.35)" />
    </filter>
  </defs>
  <g filter="url(#egGlow)">
    <image href="data:image/png;base64,{b64_emblem}" x="2" y="3" width="68" height="68" />
  </g>
  <text x="80" y="41" fill="#FFFFFF" font-family="'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="25" font-weight="900" letter-spacing="0.2px">
    Embed<tspan fill="#93C5FD">Gallery</tspan>
  </text>
  <text x="81" y="58" fill="#E2E8F0" font-family="'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9.5" font-weight="700" letter-spacing="1.5px">
    ELECTRONICS PVT LTD
  </text>
</svg>'''

with open('assets/embedgallery-white.svg', 'w', encoding='utf-8') as f:
    f.write(svg_white)

# 3. embedgallery-badge.svg (Full circular badge with 'EmbedGallery' beneath it)
svg_badge = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 230" width="100%" height="100%">
  <defs>
    <filter id="badgeSoftShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="rgba(11, 59, 149, 0.28)" />
    </filter>
  </defs>
  <g filter="url(#badgeSoftShadow)">
    <image href="data:image/png;base64,{b64_badge_trans}" x="10" y="10" width="220" height="210" />
  </g>
</svg>'''

with open('assets/embedgallery-badge.svg', 'w', encoding='utf-8') as f:
    f.write(svg_badge)

# 4. national-logo.svg and national-logo-white.svg updated to embedgallery
with open('assets/national-logo.svg', 'w', encoding='utf-8') as f:
    f.write(svg_horizontal)

with open('assets/national-logo-white.svg', 'w', encoding='utf-8') as f:
    f.write(svg_white)

print('Generated all logo SVGs successfully!')
