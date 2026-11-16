import os
import re

def update_splash():
    fpath = 'national_splash_screen_custom_farm_background/code.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('National - Smart Motor Control', 'EmbedGallery - Smart Motor Control')
    c = c.replace('National Red Box', 'EmbedGallery Brand Badge')
    c = c.replace('<img src="../assets/national-logo.svg" alt="National Logo" class="w-[190px] h-auto drop-shadow-2xl">',
                  '<img src="../assets/embedgallery-badge.png" alt="EmbedGallery Logo" class="w-[175px] h-auto drop-shadow-2xl">')
    c = c.replace('from-[#d91d24] via-[#f02d35] to-[#d91d24]', 'from-[#0B3B95] via-[#2563EB] to-[#0B3B95]')
    c = c.replace('stop-color="#D91D24"', 'stop-color="#0B3B95"')
    c = c.replace('stop-color="#E5232B"', 'stop-color="#1E40AF"')
    c = c.replace('stop-color="#FF1A23"', 'stop-color="#38BDF8"')
    c = c.replace("rgba(217,29,36,0.2)", "rgba(11,59,149,0.25)")
    c = c.replace("red: '#D91D24'", "blue: '#0B3B95', red: '#0B3B95'")
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated splash screen')

def update_login():
    fpath = 'national_login_screen/code.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('National - Smart Motor Control', 'EmbedGallery - Smart Motor Control')
    c = c.replace('National Brand Logo Badge', 'EmbedGallery Brand Logo Badge')
    c = c.replace('data-purpose="national-brand-logo"', 'data-purpose="embedgallery-brand-logo"')
    c = c.replace('<img src="../assets/national-logo.svg" alt="National Logo" class="w-[160px] h-auto drop-shadow-xl rounded-2xl">',
                  '<img src="../assets/embedgallery-badge.png" alt="EmbedGallery Logo" class="w-[155px] h-auto drop-shadow-xl rounded-2xl">')
    c = c.replace("red: '#D91A23'", "red: '#0B3B95'")
    c = c.replace("'red-hover': '#C0131B'", "'red-hover': '#082A85'")
    c = c.replace("'red-light': '#FEE2E2'", "'red-light': '#DBEAFE'")
    c = c.replace('background-color: #E31B23;', 'background-color: #0B3B95;')
    c = c.replace('fill="#F87171"', 'fill="#93C5FD"')
    c = c.replace('fill="#FEE2E2"', 'fill="#DBEAFE"')
    c = c.replace('fill="#FED7AA"', 'fill="#BFDBFE"')
    c = c.replace('shadow-red-500/20', 'shadow-blue-900/25')
    c = c.replace('hover:bg-red-50', 'hover:bg-blue-50')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated login screen')

def update_home():
    fpath = 'national_farm_operator_home_dashboard/code.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('National Farm Operator Dashboard - Smart Motor Control', 'EmbedGallery Farm Operator Dashboard - Smart Motor Control')
    c = c.replace('bg-[#D81921] px-4 py-2.5', 'bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B] px-4 py-2.5')
    c = c.replace('<!-- White Box with Red National Logo Badge -->', '<!-- White Box with EmbedGallery Logo Badge -->')
    c = c.replace('<img src="../assets/national-logo.svg" alt="National Logo" class="h-6 w-auto object-contain">',
                  '<img src="../assets/embedgallery-emblem-transparent.png" alt="EmbedGallery Logo" class="h-7 w-auto object-contain">')
    c = c.replace('<span class="text-lg font-black tracking-tight text-white block leading-tight">National</span>',
                  '<span class="text-lg font-black tracking-tight text-white block leading-tight">EmbedGallery</span>')
    c = c.replace('<span class="text-[11px] font-medium text-white/90 block leading-tight">Smart Motor Control</span>',
                  '<span class="text-[11px] font-medium text-white/90 block leading-tight">Electronics &bull; Smart Control</span>')
    c = c.replace('text-[#D81921]', 'text-[#0B3B95]')
    c = c.replace('ring-[#D81921]', 'ring-[#0B3B95]')
    c = c.replace('bg-[#D81921]', 'bg-[#0B3B95]')
    c = c.replace('#B91219', '#082A85')
    c = c.replace('National NMC-100', 'EmbedGallery EG-400')
    c = c.replace('National Smart Motor Pump', 'EmbedGallery Smart Motor Pump')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated home dashboard')

def update_all_motors():
    fpath = 'all_motors_device_list/code.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('All Motors & Device List - National Smart Motor Control', 'All Motors & Device List - EmbedGallery Smart Motor Control')
    c = c.replace('Official National Brand Logo', 'EmbedGallery Brand Logo')
    c = c.replace('bg-[#D81921] text-white px-4 py-3', 'bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B] text-white px-4 py-3')
    c = c.replace('<img src="../assets/national-logo.svg" alt="National Logo" class="h-8 w-auto rounded-md shadow-xs">',
                  '<img src="../assets/embedgallery-white.svg" alt="EmbedGallery Logo" class="h-8 w-auto">')
    c = c.replace('bg-red-100 text-[#D81921]', 'bg-blue-100 text-[#0B3B95]')
    c = c.replace('bg-[#D81921] hover:bg-red-700 active:bg-red-800 text-white flex items-center justify-center shadow-tactileRed',
                  'bg-[#0B3B95] hover:bg-[#082A85] active:bg-[#051954] text-white flex items-center justify-center shadow-lg shadow-blue-900/30')
    c = c.replace('#D81921', '#0B3B95')
    c = c.replace('#B91219', '#082A85')
    c = c.replace('National NMC-100', 'EmbedGallery EG-400')
    c = c.replace('National NMC-200', 'EmbedGallery EG-500')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated all motors device list')

def update_motor_details():
    fpath = 'motor_details_screen/code.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('Motor Details & Remote Telemetry - National Smart Motor Control', 'Motor Details & Remote Telemetry - EmbedGallery Smart Motor Control')
    c = c.replace('bg-gradient-to-r from-[#D81921] via-[#D81921] to-[#B91219]', 'bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B]')
    c = c.replace('Centered National Brand Logo', 'Centered EmbedGallery Brand Logo')
    c = c.replace('<img src="../assets/national-logo.svg" alt="National Logo" class="h-6 w-auto object-contain">',
                  '<img src="../assets/embedgallery-badge.png" alt="EmbedGallery Logo" class="h-6 w-auto object-contain">')
    c = c.replace('<span class="text-sm font-bold tracking-tight text-white/95">Pump Details</span>',
                  '<span class="text-sm font-bold tracking-tight text-white/95">EmbedGallery Pump</span>')
    c = c.replace('#D81921', '#0B3B95')
    c = c.replace('#B91219', '#082A85')
    c = c.replace('bg-red-50', 'bg-blue-50')
    c = c.replace('text-red-700', 'text-blue-700')
    c = c.replace('National NMC-100', 'EmbedGallery EG-400')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated motor details screen')

def update_motor_control():
    fpath = 'motor_control_screen/code.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('Motor Control Screen - National Smart Motor Control', 'Motor Control Screen - EmbedGallery Smart Motor Control')
    c = c.replace('Solid National Red Top Navigation Bar', 'EmbedGallery Royal Blue Top Navigation Bar')
    c = c.replace('bg-[#D32F2F]', 'bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B]')
    c = c.replace('<img src="../assets/national-logo.svg" alt="National Logo" class="h-8 w-auto rounded-md shadow-xs">',
                  '<img src="../assets/embedgallery-white.svg" alt="EmbedGallery Logo" class="h-8 w-auto">')
    c = c.replace('National NMC-100', 'EmbedGallery EG-400')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated motor control screen')

def update_schedule():
    fpath = 'create_schedule_motor_timing_slots/code.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('Create Schedule & Motor Timing Slots - National Smart Motor Control', 'Create Schedule & Motor Timing Slots - EmbedGallery Smart Motor Control')
    c = c.replace('bg-[#D81921]', 'bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B]')
    c = c.replace('<img src="../assets/national-logo.svg" alt="National Logo" class="h-8 w-auto rounded-md shadow-xs">',
                  '<img src="../assets/embedgallery-white.svg" alt="EmbedGallery Logo" class="h-8 w-auto">')
    c = c.replace('#D81921', '#0B3B95')
    c = c.replace('#B91219', '#082A85')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated create schedule screen')

def update_protection_hub():
    fpath = 'motor_protection_main_hub/code.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('Motor Protection Hub - National Smart Motor Control', 'Motor Protection Hub - EmbedGallery Smart Motor Control')
    c = c.replace('Top Header Bar (National Crimson)', 'Top Header Bar (EmbedGallery Royal Blue)')
    c = c.replace('bg-gradient-to-r from-[#D81921] via-[#D81921] to-[#B91219]', 'bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B]')
    c = c.replace('National Brand Pill', 'EmbedGallery Brand Pill')
    c = c.replace('<img src="../assets/national-logo.svg" alt="National Logo" class="h-6 w-auto object-contain">',
                  '<img src="../assets/embedgallery-badge.png" alt="EmbedGallery Logo" class="h-6 w-auto object-contain">')
    c = c.replace('text-red-100', 'text-blue-100')
    c = c.replace('bg-red-50 overflow-hidden flex-shrink-0 border border-red-100', 'bg-blue-50 overflow-hidden flex-shrink-0 border border-blue-100')
    c = c.replace('#D81921', '#0B3B95')
    c = c.replace('#B91219', '#082A85')
    c = c.replace('National Auto Starter', 'EmbedGallery Auto Starter')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated motor protection hub')

def update_profile():
    fpath = 'national_operator_profile_screen/code.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('Operator Profile & Settings - National Smart Agro', 'Operator Profile & Settings - EmbedGallery Smart Motor Control')
    c = c.replace('Operator Profile &amp; Settings - National Smart Agro', 'Operator Profile &amp; Settings - EmbedGallery Smart Motor Control')
    c = c.replace('bg-gradient-to-r from-[#D81921] via-[#D81921] to-[#B91219]', 'bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B]')
    c = c.replace('Centered National Logo & Title', 'Centered EmbedGallery Logo & Title')
    c = c.replace('<img src="../assets/national-logo.svg" alt="National Logo" class="h-6 w-auto object-contain">',
                  '<img src="../assets/embedgallery-badge.png" alt="EmbedGallery Logo" class="h-6 w-auto object-contain">')
    c = c.replace('bg-gradient-to-tr from-[#D81921] to-red-500 text-white flex items-center justify-center text-2xl font-black shadow-tactileRed',
                  'bg-gradient-to-tr from-[#0B3B95] to-blue-500 text-white flex items-center justify-center text-2xl font-black shadow-lg shadow-blue-900/30')
    c = c.replace('National Smart ID', 'EmbedGallery Smart ID')
    c = c.replace('National Customer Support', 'EmbedGallery Customer Support')
    c = c.replace('Log Out of National', 'Log Out of EmbedGallery')
    c = c.replace('National Support Line', 'EmbedGallery Support Line')
    c = c.replace('#D81921', '#0B3B95')
    c = c.replace('#B91219', '#082A85')
    c = c.replace("red: '#D81921'", "blue: '#0B3B95', red: '#0B3B95'")
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated operator profile screen')

def update_analytics():
    fpath = 'national_motor_analytics_screen/code.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('Auto Motor Starter Analytics - National Smart Agro', 'Auto Motor Starter Analytics - EmbedGallery Smart Motor Control')
    c = c.replace("red: '#D81921'", "blue: '#0B3B95', red: '#0B3B95'")
    c = c.replace('background: #D81921 !important;', 'background: #0B3B95 !important;')
    c = c.replace('linear-gradient(135deg, #FF3D47 0%, #D81921 55%, #A60911 100%)', 'linear-gradient(135deg, #2563EB 0%, #0B3B95 55%, #08296B 100%)')
    c = c.replace('rgba(216, 25, 33, 0.42)', 'rgba(11, 59, 149, 0.42)')
    c = c.replace('color: #D81921 !important;', 'color: #0B3B95 !important;')
    c = c.replace('bg-[#D81921]', 'bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B]')
    c = c.replace('Center Title with National Logo', 'Center Title with EmbedGallery Logo')
    c = c.replace('<img src="../assets/national-logo.svg" alt="National Logo" class="h-5 w-auto object-contain">',
                  '<img src="../assets/embedgallery-emblem-transparent.png" alt="EmbedGallery Logo" class="h-6 w-auto object-contain">')
    c = c.replace('Starter Analytics</h1>', 'EmbedGallery Analytics</h1>')
    c = c.replace('#D81921', '#0B3B95')
    c = c.replace('#B91219', '#082A85')
    c = c.replace('National_Auto_Starter_Summary.csv', 'EmbedGallery_Auto_Starter_Summary.csv')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated motor analytics screen')

def update_settings_screens():
    settings_files = [
        'overload_protection_settings/code.html',
        'voltage_protection_settings/code.html',
        'dry_run_protection_settings/code.html',
        'phase_protection_settings/code.html',
        'advanced_electrical_settings/code.html',
        'review_apply_settings/code.html',
        'apply_settings_confirmation_modal/code.html'
    ]
    for sf in settings_files:
        with open(sf, 'r', encoding='utf-8') as f:
            c = f.read()
        c = c.replace('National Auto Starter', 'EmbedGallery Auto Starter')
        c = c.replace('National Smart Motor Control', 'EmbedGallery Smart Motor Control')
        c = c.replace('National Smart Agro', 'EmbedGallery Smart Motor Control')
        c = c.replace('bg-gradient-to-r from-[#D81921] via-[#D81921] to-[#B91219]', 'bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B]')
        c = c.replace('bg-gradient-to-r from-[#D81921] to-[#B91219]', 'bg-gradient-to-r from-[#0B3B95] to-[#08296B]')
        c = c.replace('text-red-100', 'text-blue-100')
        c = c.replace('#D81921', '#0B3B95')
        c = c.replace('#B91219', '#082A85')
        c = c.replace('shadow-red-600/30', 'shadow-blue-900/30')
        c = c.replace('bg-red-50/60', 'bg-blue-50/70')
        c = c.replace('bg-red-50', 'bg-blue-50')
        c = c.replace('border-red-100', 'border-blue-100')
        c = c.replace('border-red-200', 'border-blue-200')
        c = c.replace('National', 'EmbedGallery')
        with open(sf, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'Updated {sf}')

update_splash()
update_login()
update_home()
update_all_motors()
update_motor_details()
update_motor_control()
update_schedule()
update_protection_hub()
update_profile()
update_analytics()
update_settings_screens()
print('All screens updated successfully!')
