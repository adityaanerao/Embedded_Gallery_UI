import os
import re

# Standard EmbedGallery Brand Header Logo Component (Exact same as Home Screen)
# Relative path from screen directories: ../assets/embedgallery-emblem-transparent.png
LOGO_HTML_SUBDIR = '''<div class="flex items-center space-x-2.5 cursor-pointer btn-tactile" data-route="home">
      <div class="bg-white rounded-lg p-1 shadow-xs flex items-center justify-center" style="width: 38px; height: 38px;">
        <img src="../assets/embedgallery-emblem-transparent.png" alt="EmbedGallery Logo" class="h-7 w-auto object-contain">
      </div>
      <div class="text-left">
        <span class="text-base font-black tracking-tight text-white block leading-tight">EmbedGallery</span>
        <span class="text-[10px] font-medium text-white/90 block leading-tight">Electronics &bull; Smart Control</span>
      </div>
    </div>'''

LOGO_HTML_INDEX = '''<div class="showcase-brand">
        <div class="bg-white rounded-lg p-1 shadow-xs flex items-center justify-center" style="width: 36px; height: 36px;">
          <img src="assets/embedgallery-emblem-transparent.png" alt="EmbedGallery Logo" style="height: 26px; width: auto; object-fit: contain;">
        </div>
        <div style="text-align: left;">
          <span style="font-size: 15px; font-weight: 900; color: #ffffff; display: block; line-height: 1.1; letter-spacing: 0.2px;">EmbedGallery</span>
          <span style="font-size: 10.5px; font-weight: 500; color: #94a3b8; display: block; line-height: 1.1;">Electronics &bull; Smart Control</span>
        </div>
        <div class="showcase-badge">
          <span class="dot"></span>
          Live App
        </div>
      </div>'''

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
# Replace showcase-brand section
c = re.sub(
    r'<div class="showcase-brand">.*?</div>\s*</div>\s*</div>',
    LOGO_HTML_INDEX,
    c,
    flags=re.DOTALL
) or c
# In case the regex pattern was slightly different, do targeted replacement:
if '<div class="showcase-brand">' in c:
    c = re.sub(
        r'<div class="showcase-brand">.*?<div class="showcase-actions">',
        LOGO_HTML_INDEX + '\n\n      <div class="showcase-actions">',
        c,
        flags=re.DOTALL
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated index.html showcase logo')

# 2. Update all_motors_device_list/code.html
with open('all_motors_device_list/code.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = re.sub(
    r'<!-- Center Logo.*?</div>',
    f'<!-- Center Logo (Same as Home Screen) -->\n    {LOGO_HTML_SUBDIR}',
    c,
    flags=re.DOTALL
)
with open('all_motors_device_list/code.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated all_motors_device_list logo')

# 3. Update motor_details_screen/code.html
with open('motor_details_screen/code.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = re.sub(
    r'<!-- Centered EmbedGallery Brand Logo & Title -->\s*<div class="flex items-center space-x-2 cursor-pointer".*?</div>\s*</div>',
    f'<!-- Centered EmbedGallery Brand Logo (Same as Home Screen) -->\n      {LOGO_HTML_SUBDIR}',
    c,
    flags=re.DOTALL
)
with open('motor_details_screen/code.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated motor_details_screen logo')

# 4. Update motor_control_screen/code.html
with open('motor_control_screen/code.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = re.sub(
    r'<div data-route="home" class="flex items-center justify-center cursor-pointer">.*?</div>',
    LOGO_HTML_SUBDIR,
    c,
    flags=re.DOTALL
)
with open('motor_control_screen/code.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated motor_control_screen logo')

# 5. Update create_schedule_motor_timing_slots/code.html
with open('create_schedule_motor_timing_slots/code.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = re.sub(
    r'<!-- Center Logo.*?</div>',
    f'<!-- Center Logo (Same as Home Screen) -->\n    {LOGO_HTML_SUBDIR}',
    c,
    flags=re.DOTALL
)
with open('create_schedule_motor_timing_slots/code.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated create_schedule_motor_timing_slots logo')

# 6. Update motor_protection_main_hub/code.html
with open('motor_protection_main_hub/code.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = re.sub(
    r'<!-- EmbedGallery Brand Pill -->\s*<div class="flex items-center gap-2 cursor-pointer".*?</div>\s*</div>',
    f'<!-- EmbedGallery Brand Logo (Same as Home Screen) -->\n        {LOGO_HTML_SUBDIR}',
    c,
    flags=re.DOTALL
)
with open('motor_protection_main_hub/code.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated motor_protection_main_hub logo')

# 7. Update national_motor_analytics_screen/code.html
with open('national_motor_analytics_screen/code.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = re.sub(
    r'<!-- Center Title with EmbedGallery Logo -->\s*<div class="flex items-center space-x-2 cursor-pointer btn-tactile".*?</div>\s*</div>',
    f'<!-- Center Logo (Same as Home Screen) -->\n    {LOGO_HTML_SUBDIR}',
    c,
    flags=re.DOTALL
)
with open('national_motor_analytics_screen/code.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated national_motor_analytics_screen logo')

# 8. Update national_operator_profile_screen/code.html
with open('national_operator_profile_screen/code.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = re.sub(
    r'<!-- Centered EmbedGallery Logo & Title -->\s*<div class="flex items-center space-x-2 cursor-pointer".*?</div>\s*</div>',
    f'<!-- Centered EmbedGallery Logo (Same as Home Screen) -->\n    {LOGO_HTML_SUBDIR}',
    c,
    flags=re.DOTALL
)
with open('national_operator_profile_screen/code.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated national_operator_profile_screen logo')

# 9. Update national_login_screen/code.html
with open('national_login_screen/code.html', 'r', encoding='utf-8') as f:
    c = f.read()
login_logo = '''<!-- EmbedGallery Brand Logo (Same as Home Screen) -->
  <div class="transform transition duration-300 hover:scale-105" data-purpose="embedgallery-brand-logo">
    <div class="flex items-center space-x-3 bg-white/95 backdrop-blur-md px-5 py-3 rounded-2xl shadow-xl border border-white/80">
      <div class="bg-white rounded-xl p-1.5 shadow-xs flex items-center justify-center" style="width: 48px; height: 48px;">
        <img src="../assets/embedgallery-emblem-transparent.png" alt="EmbedGallery Logo" class="h-9 w-auto object-contain">
      </div>
      <div class="text-left">
        <span class="text-xl font-black tracking-tight text-[#0B3B95] block leading-tight">EmbedGallery</span>
        <span class="text-[11px] font-bold text-slate-500 tracking-wider block uppercase">Electronics &bull; Smart Control</span>
      </div>
    </div>
  </div>'''
c = re.sub(
    r'<!-- EmbedGallery Brand Logo Badge -->\s*<div class="transform transition duration-300.*?</div>\s*</div>',
    login_logo,
    c,
    flags=re.DOTALL
)
with open('national_login_screen/code.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated national_login_screen logo')

# 10. Update national_splash_screen_custom_farm_background/code.html
with open('national_splash_screen_custom_farm_background/code.html', 'r', encoding='utf-8') as f:
    c = f.read()
splash_logo = '''<!-- EmbedGallery Brand Logo (Same as Home Screen) -->
<div class="animate-in-1 opacity-0 mb-7 transition-transform hover:scale-[1.02] duration-300" data-purpose="logo-card">
  <div class="flex items-center space-x-3.5 bg-white/95 backdrop-blur-md px-6 py-3.5 rounded-2xl shadow-2xl border border-white/80">
    <div class="bg-white rounded-xl p-1.5 shadow-xs flex items-center justify-center" style="width: 52px; height: 52px;">
      <img src="../assets/embedgallery-emblem-transparent.png" alt="EmbedGallery Logo" class="h-10 w-auto object-contain">
    </div>
    <div class="text-left">
      <span class="text-2xl font-black tracking-tight text-[#0B3B95] block leading-tight">EmbedGallery</span>
      <span class="text-xs font-bold text-slate-500 tracking-wider block uppercase">Electronics &bull; Smart Control</span>
    </div>
  </div>
</div>'''
c = re.sub(
    r'<!-- EmbedGallery Brand Badge -->\s*<div class="animate-in-1 opacity-0 mb-7.*?</div>\s*</div>',
    splash_logo,
    c,
    flags=re.DOTALL
)
with open('national_splash_screen_custom_farm_background/code.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated splash screen logo')

# 11. Update Protection Settings Screens to include the top header logo (same as home screen)
settings_screens = [
    'voltage_protection_settings/code.html',
    'overload_protection_settings/code.html',
    'dry_run_protection_settings/code.html',
    'phase_protection_settings/code.html',
    'advanced_electrical_settings/code.html',
    'review_apply_settings/code.html',
    'apply_settings_confirmation_modal/code.html'
]

header_logo_subscreen = '''<div class="flex items-center space-x-2 cursor-pointer btn-tactile" data-route="home">
            <div class="bg-white rounded-lg p-0.5 shadow-xs flex items-center justify-center" style="width: 30px; height: 30px;">
              <img src="../assets/embedgallery-emblem-transparent.png" alt="EmbedGallery Logo" class="h-5.5 w-auto object-contain">
            </div>
            <span class="text-xs font-bold tracking-tight text-white/95">EmbedGallery</span>
          </div>'''

for sf in settings_screens:
    with open(sf, 'r', encoding='utf-8') as f:
        c = f.read()
    # If the sub-screen has a top-bar with back button and title, replace the right placeholder or badge with the logo
    c = c.replace('<span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold bg-white/20 text-white backdrop-blur-sm">\n              Auto Starter\n            </span>',
                  header_logo_subscreen)
    c = c.replace('<span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold bg-white/20 text-white backdrop-blur-sm">\n              Smart Logic\n            </span>',
                  header_logo_subscreen)
    c = c.replace('<span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold bg-white/20 text-white backdrop-blur-sm">\n              Active Guard\n            </span>',
                  header_logo_subscreen)
    c = c.replace('<span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold bg-white/20 text-white backdrop-blur-sm">\n              Phase Guard\n            </span>',
                  header_logo_subscreen)
    c = c.replace('<span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold bg-white/20 text-white backdrop-blur-sm">\n              Safety Guard\n            </span>',
                  header_logo_subscreen)
    with open(sf, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'Updated {sf} header logo')

print('All screens successfully updated with identical home screen logo!')
