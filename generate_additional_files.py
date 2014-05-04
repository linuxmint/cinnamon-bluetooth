#!/usr/bin/python

DOMAIN = "cinnamon-bluetooth"
PATH = "/usr/share/cinnamon/locale"

import os, gettext, sys
sys.path.append('/usr/lib/linuxmint/common')
import additionalfiles

os.environ['LANG'] = "en_US.UTF-8"
gettext.install(DOMAIN, PATH)

prefix = """[Desktop Entry]
Icon=bluetooth
Exec=cinnamon-settings bluetooth
Terminal=false
Type=Application
Categories=GTK;Settings;X-Cinnamon-NetworkSettings;HardwareSettings;X-Cinnamon-Settings-Panel;
OnlyShowIn=X-Cinnamon;
StartupNotify=true
X-Cinnamon-Settings-Panel=bluetooth
"""

additionalfiles.generate(DOMAIN, PATH, "./panels/bluetooth/cinnamon-bluetooth-properties.desktop.in.in", prefix, _("Bluetooth"), _("Configure Bluetooth settings"), "")
