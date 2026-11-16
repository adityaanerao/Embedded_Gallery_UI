import os
import re

# Update app-runtime.js
with open('app-runtime.js', 'r', encoding='utf-8') as f:
    runtime = f.read()

# Replace Red navbar gradient with EmbedGallery Royal Blue
runtime = runtime.replace(
    'linear-gradient(135deg, #FF3D47 0%, #D81921 55%, #A60911 100%)',
    'linear-gradient(135deg, #2563EB 0%, #0B3B95 55%, #08296B 100%)'
)
runtime = runtime.replace(
    'rgba(216, 25, 33, 0.42)',
    'rgba(11, 59, 149, 0.42)'
)
runtime = runtime.replace(
    'color: #D81921 !important;',
    'color: #0B3B95 !important;'
)
runtime = runtime.replace(
    'background:#d81921;',
    'background:#0B3B95;'
)
runtime = runtime.replace(
    'rgba(216,25,33,0.3)',
    'rgba(11,59,149,0.3)'
)
runtime = runtime.replace(
    'National NMC-100',
    'EmbedGallery EG-400'
)
runtime = runtime.replace(
    'Log Out of National',
    'Log Out of EmbedGallery'
)
runtime = runtime.replace(
    'background:#d3232a;',
    'background:#0B3B95;'
)
runtime = runtime.replace(
    'border:2px solid #d91a23;',
    'border:2px solid #0B3B95;'
)
runtime = runtime.replace(
    'background:#d91a23;',
    'background:#0B3B95;'
)
runtime = runtime.replace(
    'National Smart Motor Control',
    'EmbedGallery Smart Motor Control'
)

with open('app-runtime.js', 'w', encoding='utf-8') as f:
    f.write(runtime)

print('Updated app-runtime.js')

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

idx = idx.replace('National Smart Motor Control', 'EmbedGallery Smart Motor Control')
idx = idx.replace('National Smart Motor Control & Monitoring Mobile Application', 'EmbedGallery Smart Motor Control & Monitoring Mobile Application')
idx = idx.replace('rgba(217, 29, 36, 0.12)', 'rgba(11, 59, 149, 0.22)')
idx = idx.replace('rgba(217, 29, 36, 0.15)', 'rgba(11, 59, 149, 0.25)')
idx = idx.replace('rgba(217, 29, 36, 0.4)', 'rgba(37, 99, 235, 0.4)')
idx = idx.replace('#ff4d53', '#38BDF8')
idx = idx.replace('assets/national-logo.svg', 'assets/embedgallery-badge.png')
idx = idx.replace('<span>NATIONAL</span>', '<span>EmbedGallery</span>')
idx = idx.replace('title="National Smart Motor Control Mobile Screen"', 'title="EmbedGallery Smart Motor Control Mobile Screen"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

print('Updated index.html')
