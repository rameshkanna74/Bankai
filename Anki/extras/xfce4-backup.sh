#!/bin/bash

# Backup XFCE configuration files
tar -czvf ~/xfce-config-backup.tar.gz ~/.config ~/.local/share

# Backup XFCE panel configuration
tar -czvf ~/xfce-panel-backup.tar.gz ~/.config/xfce4/panel

# Backup XFCE themes and icons
tar -czvf ~/xfce-themes-backup.tar.gz ~/.themes ~/.icons

# Backup wallpaper settings
tar -czvf ~/xfce-wallpaper-backup.tar.gz ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml

# Backup keyboard shortcuts
tar -czvf ~/xfce-keyboard-shortcuts-backup.tar.gz ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml

# Notify user
echo "XFCE settings backup completed!"
