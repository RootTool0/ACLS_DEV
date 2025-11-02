
define config.name = _("A Cold Love Story Remaster")

define gui.show_name = True

define config.version = "1.0"

define gui.about = _p("""
Fan remaster of the original visual novel 'A Cold Love Story' (2015) by Liam Vickers\n
Key improvements:\n
• Engine updated to Ren'Py 8.3.7\n
• Completely redesigned interface\n
• Added mobile device support (Android)\n
• Performance optimization\n
Authors:\n
• RootTool - (Programmer) - ported the original game to the new engine version, adapted builds for Windows and Android devices\n
• At0m - (UI Designer) - designed the main menu\n
• Ponder_Static - (Translator) - translated the original novel into Russian\n
• Nucita - (Translator) - translated the original novel into Brazilian Portuguese\n
DISCLAIMER: This is an unofficial project. All rights belong to Liam Vickers\n
Special thanks: You\n
""")

define build.name = "AColdLoveStoryRemaster"
define build.version = "1.3"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.main_menu_music = "audio/Eternity Complete Master-2.mp3"


define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.after_load_transition = dissolve

define config.intra_transition = dissolve


define config.after_load_transition = None


define config.end_game_transition = None


define config.window = "auto"

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 0

default preferences.afm_time = 15

define config.save_directory = "AColdLoveStoryRemaster-1742831320"

define config.window_icon = "gui/window_icon.png"
define config.default_language = "None"

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    def set_language(lang):
        renpy.change_language(lang)
        print(lang)

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('stories/**', "stories")

    build.documentation('*.html')
    build.documentation('*.txt')

