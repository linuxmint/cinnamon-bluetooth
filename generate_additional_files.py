#!/usr/bin/python

import os, gettext

DOMAIN = "cinnamon-bluetooth"
PATH = "/usr/share/cinnamon/locale"

def generate(filename, prefix, name, comment, suffix):
    gettext.install(DOMAIN, PATH)
    desktopFile = open(filename, "w")

    desktopFile.writelines(prefix)

    desktopFile.writelines("Name=%s\n" % name)
    for directory in sorted(os.listdir(PATH)):
        if os.path.isdir(os.path.join(PATH, directory)):
            try:
                language = gettext.translation(DOMAIN, PATH, languages=[directory])
                language.install()          
                desktopFile.writelines("Name[%s]=%s\n" % (directory, _(name)))
            except:
                pass

    desktopFile.writelines("Comment=%s\n" % comment)
    for directory in sorted(os.listdir(PATH)):
        if os.path.isdir(os.path.join(PATH, directory)):
            try:
                language = gettext.translation(DOMAIN, PATH, languages=[directory])
                language.install()                      
                desktopFile.writelines("Comment[%s]=%s\n" % (directory, _(comment)))
            except:
                pass

    desktopFile.writelines(suffix)

os.environ['LANG'] = "en"
gettext.install(DOMAIN, PATH)

prefix = """[Desktop Entry]
Icon=cinnamon-bluetooth
Exec=cinnamon-settings bluetooth
Terminal=false
Type=Application
Categories=GTK;Settings;X-Cinnamon-NetworkSettings;HardwareSettings;X-Cinnamon-Settings-Panel;
OnlyShowIn=GNOME;
StartupNotify=true
X-Cinnamon-Settings-Panel=bluetooth
"""

generate("./panels/bluetooth/cinnamon-bluetooth-properties.desktop.in.in", prefix, _("Bluetooth"), _("Configure Bluetooth settings"), "")


