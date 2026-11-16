# Clean remaining titles, comments, and color tokens

def clean_file(path, replacements):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    for o, n in replacements:
        content = content.replace(o, n)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Cleaned {path}')

clean_file('all_motors_device_list/code.html', [
    ('<title>National - All Connected Motors</title>', '<title>EmbedGallery - All Connected Motors</title>'),
    ('National Official Vector', 'EmbedGallery Official Vector'),
    ('alt="National Logo"', 'alt="EmbedGallery Logo"')
])

clean_file('create_schedule_motor_timing_slots/code.html', [
    ('<title>National - Create Motor Schedule</title>', '<title>EmbedGallery - Create Motor Schedule</title>'),
    ('Official National Logo', 'Official EmbedGallery Logo'),
    ('National Official Vector', 'EmbedGallery Official Vector'),
    ('alt="National Logo"', 'alt="EmbedGallery Logo"')
])

clean_file('motor_details_screen/code.html', [
    ('<title>Motor Details - National Smart Agro</title>', '<title>Motor Details - EmbedGallery Smart Motor Control</title>'),
    ('alt="National Logo"', 'alt="EmbedGallery Logo"')
])

clean_file('motor_control_screen/code.html', [
    ("red: '#D32F2F'", "blue: '#0B3B95', red: '#0B3B95'"),
    ('alt="National Logo"', 'alt="EmbedGallery Logo"')
])

clean_file('national_farm_operator_home_dashboard/code.html', [
    ("red: '#D81921'", "blue: '#0B3B95', red: '#0B3B95'"),
    ('National Logo', 'EmbedGallery Logo'),
    ('alt="National Logo"', 'alt="EmbedGallery Logo"')
])

clean_file('national_login_screen/code.html', [
    ('border-color: #D91A23;', 'border-color: #0B3B95;'),
    ('alt="National Logo"', 'alt="EmbedGallery Logo"')
])

clean_file('index.html', [
    ('alt="National Logo"', 'alt="EmbedGallery Logo"')
])

clean_file('national_operator_profile_screen/code.html', [
    ('alt="National Logo"', 'alt="EmbedGallery Logo"')
])

clean_file('national_motor_analytics_screen/code.html', [
    ('alt="National Logo"', 'alt="EmbedGallery Logo"')
])

clean_file('motor_protection_main_hub/code.html', [
    ('alt="National Logo"', 'alt="EmbedGallery Logo"')
])

clean_file('national_splash_screen_custom_farm_background/code.html', [
    ('alt="National Logo"', 'alt="EmbedGallery Logo"')
])

print('Cleanup completed!')
