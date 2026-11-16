import re

SUB_HEADER_TEMPLATE = '''    <!-- Top Header Bar (EmbedGallery Royal Blue) -->
    <header class="bg-gradient-to-r from-[#0B3B95] via-[#0E4CBF] to-[#08296B] text-white pt-4 pb-6 px-4 rounded-b-[24px] shadow-md relative z-10">
      <div class="flex items-center justify-between mb-3">
        <!-- Back Navigation Button -->
        <button data-route="protection" aria-label="Go back" class="p-2 -ml-2 rounded-full hover:bg-white/10 active:scale-90 transition-all focus:outline-none flex items-center justify-center cursor-pointer" type="button">
          <svg class="w-6 h-6 text-white stroke-[2.5]" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
            <path d="M15 19l-7-7 7-7"></path>
          </svg>
        </button>

        <!-- Center Logo (Same as Home Screen) -->
        <div class="flex items-center space-x-2.5 cursor-pointer btn-tactile" data-route="home">
          <div class="bg-white rounded-lg p-1 shadow-xs flex items-center justify-center" style="width: 38px; height: 38px;">
            <img src="../assets/embedgallery-emblem-transparent.png" alt="EmbedGallery Logo" class="h-7 w-auto object-contain">
          </div>
          <div class="text-left">
            <span class="text-base font-black tracking-tight text-white block leading-tight">EmbedGallery</span>
            <span class="text-[10px] font-medium text-white/90 block leading-tight">Electronics &bull; Smart Control</span>
          </div>
        </div>

        <!-- Right Spacer -->
        <div class="w-8"></div>
      </div>

      <!-- Screen Title & Subtitle -->
      <div class="text-center px-2">
        <h1 class="text-xl font-extrabold tracking-tight text-white leading-tight">{TITLE}</h1>
        <p class="text-xs text-blue-100 mt-0.5 font-normal">{SUBTITLE}</p>
      </div>
    </header>'''

screens_meta = [
    (
        'voltage_protection_settings/code.html',
        'Voltage Protection',
        'Over/under voltage &amp; grid auto-restart safety'
    ),
    (
        'overload_protection_settings/code.html',
        'Overload Protection',
        'Full load current (FLC), trip curve &amp; thermal memory'
    ),
    (
        'dry_run_protection_settings/code.html',
        'Dry Run Protection',
        'Under-current sensing, water failure &amp; auto-restart delay'
    ),
    (
        'phase_protection_settings/code.html',
        'Phase Protection',
        'Phase loss, reversal &amp; voltage imbalance guard'
    ),
    (
        'advanced_electrical_settings/code.html',
        'Auto Starter Engine',
        'Auto start on power recovery, surge delay &amp; cyclic timing'
    ),
    (
        'review_apply_settings/code.html',
        'Review Settings',
        'Verify safety parameters before dispatching to starter'
    )
]

for fpath, title, subtitle in screens_meta:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_header = SUB_HEADER_TEMPLATE.replace('{TITLE}', title).replace('{SUBTITLE}', subtitle)
    # Replace the existing header tag
    content = re.sub(
        r'<!-- Top Header Bar.*?<\/header>|<!-- Header Section.*?<\/header>',
        new_header,
        content,
        flags=re.DOTALL
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Applied unified header to {fpath}')

print('All settings headers unified!')
