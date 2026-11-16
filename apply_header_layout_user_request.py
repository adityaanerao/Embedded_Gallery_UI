import re

# ==============================================================================
# RULE 1: SCREENS WITH BOTTOM NAVBAR:
# Remove the back button arrow!
# Place the EmbedGallery logo at the far LEFT CORNER (same as Home Screen).
# ==============================================================================

def update_all_motors():
    fpath = 'all_motors_device_list/code.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    header_html = '''<header class="bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B] text-white px-4 py-3 flex items-center justify-between shadow-md sticky top-0 z-40">
    <!-- EmbedGallery Logo in Left Corner (No Back Arrow on Tab Screen) -->
    <div class="flex items-center space-x-2.5 cursor-pointer btn-tactile" data-route="home">
      <div class="bg-white rounded-lg p-1 shadow-xs flex items-center justify-center" style="width: 38px; height: 38px;">
        <img src="../assets/embedgallery-emblem-transparent.png" alt="EmbedGallery Logo" class="h-7 w-auto object-contain">
      </div>
      <div class="text-left">
        <span class="text-base font-black tracking-tight text-white block leading-tight">EmbedGallery</span>
        <span class="text-[10px] font-medium text-white/90 block leading-tight">Electronics &bull; Smart Control</span>
      </div>
    </div>

    <!-- Quick Refresh Button with Animation -->
    <button id="btnRefreshMotors" aria-label="Refresh Motors" class="btn-tactile p-1.5 -mr-1 text-white hover:bg-white/15 rounded-full transition-all cursor-pointer" type="button">
      <svg id="iconRefreshMotors" class="w-5 h-5 transition-transform duration-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
      </svg>
    </button>
  </header>'''
    c = re.sub(r'<header class="bg-gradient-to-r from-\[#0B3B95\].*?<\/header>', header_html, c, flags=re.DOTALL)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated all_motors_device_list header')

def update_create_schedule():
    fpath = 'create_schedule_motor_timing_slots/code.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    header_html = '''<header class="bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B] text-white px-4 py-3 flex items-center justify-between shadow-md sticky top-0 z-40">
    <!-- EmbedGallery Logo in Left Corner (No Back Arrow on Tab Screen) -->
    <div class="flex items-center space-x-2.5 cursor-pointer btn-tactile" data-route="home">
      <div class="bg-white rounded-lg p-1 shadow-xs flex items-center justify-center" style="width: 38px; height: 38px;">
        <img src="../assets/embedgallery-emblem-transparent.png" alt="EmbedGallery Logo" class="h-7 w-auto object-contain">
      </div>
      <div class="text-left">
        <span class="text-base font-black tracking-tight text-white block leading-tight">EmbedGallery</span>
        <span class="text-[10px] font-medium text-white/90 block leading-tight">Electronics &bull; Smart Control</span>
      </div>
    </div>

    <!-- Quick Reset Schedule Icon -->
    <button id="btnResetSchedule" aria-label="Reset Times" class="btn-tactile p-1.5 -mr-1 text-white hover:bg-white/15 rounded-full transition-all cursor-pointer" type="button">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
      </svg>
    </button>
  </header>'''
    c = re.sub(r'<header class="bg-gradient-to-r from-\[#0B3B95\].*?<\/header>', header_html, c, flags=re.DOTALL)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated create_schedule header')

def update_analytics():
    fpath = 'national_motor_analytics_screen/code.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    header_html = '''<header class="bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B] px-4 py-3 flex items-center justify-between sticky top-0 z-40 shadow-sm text-white">
    <!-- EmbedGallery Logo in Left Corner (No Back Arrow on Tab Screen) -->
    <div class="flex items-center space-x-2.5 cursor-pointer btn-tactile" data-route="home">
      <div class="bg-white rounded-lg p-1 shadow-xs flex items-center justify-center" style="width: 38px; height: 38px;">
        <img src="../assets/embedgallery-emblem-transparent.png" alt="EmbedGallery Logo" class="h-7 w-auto object-contain">
      </div>
      <div class="text-left">
        <span class="text-base font-black tracking-tight text-white block leading-tight">EmbedGallery</span>
        <span class="text-[10px] font-medium text-white/90 block leading-tight">Electronics &bull; Smart Control</span>
      </div>
    </div>

    <!-- Live Status Pill -->
    <div class="flex items-center space-x-1.5 bg-white/15 border border-white/25 rounded-full px-2.5 py-1 text-[11px] font-bold text-white">
      <span class="w-2 h-2 rounded-full bg-emerald-400 animate-live-dot"></span>
      <span>Live</span>
    </div>
  </header>'''
    c = re.sub(r'<header class="bg-gradient-to-r from-\[#0B3B95\].*?<\/header>', header_html, c, flags=re.DOTALL)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated national_motor_analytics_screen header')

def update_profile():
    fpath = 'national_operator_profile_screen/code.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    header_html = '''<header class="bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B] text-white px-4 py-3 flex items-center justify-between sticky top-0 z-40 shadow-md">
    <!-- EmbedGallery Logo in Left Corner (No Back Arrow on Tab Screen) -->
    <div class="flex items-center space-x-2.5 cursor-pointer btn-tactile" data-route="home">
      <div class="bg-white rounded-lg p-1 shadow-xs flex items-center justify-center" style="width: 38px; height: 38px;">
        <img src="../assets/embedgallery-emblem-transparent.png" alt="EmbedGallery Logo" class="h-7 w-auto object-contain">
      </div>
      <div class="text-left">
        <span class="text-base font-black tracking-tight text-white block leading-tight">EmbedGallery</span>
        <span class="text-[10px] font-medium text-white/90 block leading-tight">Electronics &bull; Smart Control</span>
      </div>
    </div>

    <!-- Help / Support Icon -->
    <button id="helpBtn" aria-label="Support" class="p-1.5 -mr-1 text-white hover:bg-white/10 active:scale-90 rounded-full transition-transform flex items-center justify-center cursor-pointer" type="button">
      <svg class="w-5 h-5 stroke-[2.2]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <circle cx="12" cy="12" r="10"></circle>
        <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
        <line x1="12" y1="17" x2="12.01" y2="17"></line>
      </svg>
    </button>
  </header>'''
    c = re.sub(r'<header class="bg-gradient-to-r from-\[#0B3B95\].*?<\/header>', header_html, c, flags=re.DOTALL)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated national_operator_profile_screen header')

def update_motor_details():
    fpath = 'motor_details_screen/code.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    header_html = '''<header class="bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B] text-white px-4 py-3 flex items-center justify-between sticky top-0 z-30 shadow-md">
      <!-- EmbedGallery Logo in Left Corner (No Back Arrow on Tab Screen) -->
      <div class="flex items-center space-x-2.5 cursor-pointer btn-tactile" data-route="home">
        <div class="bg-white rounded-lg p-1 shadow-xs flex items-center justify-center" style="width: 38px; height: 38px;">
          <img src="../assets/embedgallery-emblem-transparent.png" alt="EmbedGallery Logo" class="h-7 w-auto object-contain">
        </div>
        <div class="text-left">
          <span class="text-base font-black tracking-tight text-white block leading-tight">EmbedGallery</span>
          <span class="text-[10px] font-medium text-white/90 block leading-tight">Electronics &bull; Smart Control</span>
        </div>
      </div>

      <!-- Context Overflow Menu Button -->
      <button id="menuBtn" aria-label="More options" class="p-1.5 -mr-1 text-white hover:bg-white/10 active:scale-90 rounded-full transition-transform flex items-center justify-center cursor-pointer" type="button">
        <svg class="w-6 h-6" fill="currentColor" viewbox="0 0 24 24">
          <circle cx="12" cy="5" r="2"></circle>
          <circle cx="12" cy="12" r="2"></circle>
          <circle cx="12" cy="19" r="2"></circle>
        </svg>
      </button>
    </header>'''
    c = re.sub(r'<header class="bg-gradient-to-r from-\[#0B3B95\].*?<\/header>', header_html, c, flags=re.DOTALL)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated motor_details_screen header')

def update_motor_control():
    fpath = 'motor_control_screen/code.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    header_html = '''<header class="bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B] text-white px-4 py-3 flex items-center justify-between sticky top-0 z-30 shadow-sm" data-purpose="top-app-bar">
  <!-- EmbedGallery Logo in Left Corner (No Back Arrow on Tab Screen) -->
  <div class="flex items-center space-x-2.5 cursor-pointer btn-tactile" data-route="home">
    <div class="bg-white rounded-lg p-1 shadow-xs flex items-center justify-center" style="width: 38px; height: 38px;">
      <img src="../assets/embedgallery-emblem-transparent.png" alt="EmbedGallery Logo" class="h-7 w-auto object-contain">
    </div>
    <div class="text-left">
      <span class="text-base font-black tracking-tight text-white block leading-tight">EmbedGallery</span>
      <span class="text-[10px] font-medium text-white/90 block leading-tight">Electronics &bull; Smart Control</span>
    </div>
  </div>
  <button aria-label="More options" class="p-1 text-white active:opacity-70 transition-opacity" type="button">
    <span class="material-symbols-outlined text-2xl font-bold">more_vert</span>
  </button>
</header>'''
    c = re.sub(r'<header class="bg-gradient-to-r from-\[#0B3B95\].*?<\/header>', header_html, c, flags=re.DOTALL)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated motor_control_screen header')

def update_protection_hub():
    fpath = 'motor_protection_main_hub/code.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    header_html = '''<header class="bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B] px-4 pt-4 pb-8 text-white relative shadow-md">
      <div class="flex items-center justify-between mb-3">
        <!-- EmbedGallery Logo in Left Corner (No Back Arrow on Tab Screen) -->
        <div class="flex items-center space-x-2.5 cursor-pointer btn-tactile" data-route="home">
          <div class="bg-white rounded-lg p-1 shadow-xs flex items-center justify-center" style="width: 38px; height: 38px;">
            <img src="../assets/embedgallery-emblem-transparent.png" alt="EmbedGallery Logo" class="h-7 w-auto object-contain">
          </div>
          <div class="text-left">
            <span class="text-base font-black tracking-tight text-white block leading-tight">EmbedGallery</span>
            <span class="text-[10px] font-medium text-white/90 block leading-tight">Electronics &bull; Smart Control</span>
          </div>
        </div>
        <span class="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-bold bg-white/15 text-white backdrop-blur-sm border border-white/20">
          Auto Starter Guard
        </span>
      </div>
      <div class="text-center px-4">
        <h1 class="text-2xl font-black tracking-tight text-white leading-tight">Motor Protection Hub</h1>
        <p class="text-blue-100 text-xs mt-0.5 font-medium">Automatic Starter Guard &amp; Electrical Safety Parameters</p>
      </div>
    </header>'''
    c = re.sub(r'<header class="bg-gradient-to-r from-\[#0B3B95\].*?<\/header>', header_html, c, flags=re.DOTALL)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated motor_protection_main_hub header')

# ==============================================================================
# RULE 2: SUB-SCREENS WITHOUT NAVBAR:
# Keep Back Arrow button, and shift EmbedGallery Logo in LEFT CORNER immediately AFTER back button!
# ==============================================================================

SUB_HEADER_TEMPLATE = '''    <!-- Top Header Bar (EmbedGallery Royal Blue) -->
    <header class="bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B] text-white pt-4 pb-5 px-4 rounded-b-[24px] shadow-md relative z-10">
      <div class="flex items-center justify-between mb-3">
        <!-- Left Corner: Back Arrow Button + EmbedGallery Logo Shifted Right After -->
        <div class="flex items-center space-x-2">
          <button data-route="protection" aria-label="Go back" class="p-1.5 -ml-1.5 rounded-full hover:bg-white/10 active:scale-90 transition-all focus:outline-none flex items-center justify-center cursor-pointer text-white" type="button">
            <svg class="w-6 h-6 stroke-[2.5]" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
              <path d="M15 19l-7-7 7-7"></path>
            </svg>
          </button>
          <div class="flex items-center space-x-2 cursor-pointer btn-tactile" data-route="home">
            <div class="bg-white rounded-lg p-1 shadow-xs flex items-center justify-center" style="width: 34px; height: 34px;">
              <img src="../assets/embedgallery-emblem-transparent.png" alt="EmbedGallery Logo" class="h-6 w-auto object-contain">
            </div>
            <div class="text-left">
              <span class="text-sm font-black tracking-tight text-white block leading-tight">EmbedGallery</span>
              <span class="text-[9.5px] font-medium text-white/90 block leading-tight">Electronics &bull; Smart Control</span>
            </div>
          </div>
        </div>

        <!-- Right Side Parameter Badge -->
        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-white/20 text-white backdrop-blur-sm border border-white/25">
          Active Guard
        </span>
      </div>

      <!-- Screen Title & Subtitle -->
      <div class="text-center px-2">
        <h1 class="text-xl font-extrabold tracking-tight text-white leading-tight">{TITLE}</h1>
        <p class="text-xs text-blue-100 mt-0.5 font-normal">{SUBTITLE}</p>
      </div>
    </header>'''

sub_screens = [
    ('voltage_protection_settings/code.html', 'Voltage Protection', 'Over/under voltage &amp; grid auto-restart safety'),
    ('overload_protection_settings/code.html', 'Overload Protection', 'Full load current (FLC), trip curve &amp; thermal memory'),
    ('dry_run_protection_settings/code.html', 'Dry Run Protection', 'Under-current sensing, water failure &amp; auto-restart delay'),
    ('phase_protection_settings/code.html', 'Phase Protection', 'Phase loss, reversal &amp; voltage imbalance guard'),
    ('advanced_electrical_settings/code.html', 'Auto Starter Engine', 'Auto start on power recovery, surge delay &amp; cyclic timing'),
    ('review_apply_settings/code.html', 'Review Settings', 'Verify safety parameters before dispatching to starter')
]

for fpath, title, subtitle in sub_screens:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    hdr = SUB_HEADER_TEMPLATE.replace('{TITLE}', title).replace('{SUBTITLE}', subtitle)
    c = re.sub(r'<!-- Top Header Bar.*?<\/header>|<!-- Header Section.*?<\/header>', hdr, c, flags=re.DOTALL)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'Updated sub-screen {fpath} with back button + left-corner logo')

# Also apply to apply_settings_confirmation_modal
with open('apply_settings_confirmation_modal/code.html', 'r', encoding='utf-8') as f:
    c = f.read()
modal_hdr = '''      <!-- Screen Header with Back Arrow and Logo in Left Corner -->
      <header class="bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B] pt-4 pb-4 px-4 text-center relative flex flex-col shadow-md">
        <div class="flex items-center justify-between mb-2">
          <!-- Left Corner: Back Arrow + Logo -->
          <div class="flex items-center space-x-2">
            <button aria-label="Back" data-route="review" class="cursor-pointer text-white/90 hover:text-white transition-all active:scale-90 p-1 rounded-lg" id="back-button" type="button">
              <svg class="w-5 h-5 stroke-[2.5]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path d="M15.75 19.5L8.25 12l7.5-7.5" stroke-linecap="round" stroke-linejoin="round"></path>
              </svg>
            </button>
            <div class="flex items-center space-x-2 cursor-pointer btn-tactile" data-route="home">
              <div class="bg-white rounded-lg p-1 shadow-xs flex items-center justify-center" style="width: 32px; height: 32px;">
                <img src="../assets/embedgallery-emblem-transparent.png" alt="EmbedGallery Logo" class="h-6 w-auto object-contain">
              </div>
              <div class="text-left">
                <span class="text-xs font-black tracking-tight text-white block leading-tight">EmbedGallery</span>
                <span class="text-[9px] font-medium text-white/80 block leading-tight">Electronics &bull; Smart Control</span>
              </div>
            </div>
          </div>
          <span class="text-[10px] font-bold text-white/90 bg-white/20 px-2 py-0.5 rounded-full">Confirmation</span>
        </div>
        <h1 class="text-sm font-bold text-white">Review &amp; Apply Settings</h1>
        <p class="text-[10.5px] text-blue-100 mt-0.5">EmbedGallery Auto Starter Configuration</p>
      </header>'''
c = re.sub(r'<!-- Screen Header.*?<\/header>', modal_hdr, c, flags=re.DOTALL)
with open('apply_settings_confirmation_modal/code.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated apply_settings_confirmation_modal header')

print('All header adjustments applied successfully!')
