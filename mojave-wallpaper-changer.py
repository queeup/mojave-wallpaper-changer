#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Mojave Live Wallpaper

Mojave's live wallpaper, dynamically changing throughout the day.

author: queeup at zoho dot com
"""

import os
import subprocess
from time import localtime, sleep, strftime

SHOW_DEBUG = False


def get_gnome_wallpaper():
    current_wallpaper = subprocess.run(
        ["gsettings", "get", "org.gnome.desktop.background", "picture-uri"],
        check=True,
        capture_output=True,
        encoding="utf-8",
    )
    if SHOW_DEBUG:
        print(f"Current Wallpaper: {current_wallpaper.stdout}")
    return current_wallpaper.stdout


def set_gnome_wallpaper(file_path):
    try:
        subprocess.run(
            ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", file_path],
            check=True,
        )
        if SHOW_DEBUG:
            print(f"Setting Wallpaper: {file_path}")
    except subprocess.CalledProcessError as err:
        print(f"ERROR: {err}")


def calculate_background_wallpaper():
    now = strftime("%H:%M", localtime())
    if "05:59" < now < "07:00":
        set_background = "mojave-03.jpeg"
    elif "06:59" < now < "08:00":
        set_background = "mojave-04.jpeg"
    elif "07:59" < now < "09:00":
        set_background = "mojave-05.jpeg"
    elif "08:59" < now < "10:30":
        set_background = "mojave-06.jpeg"
    elif "10:29" < now < "12:00":
        set_background = "mojave-07.jpeg"
    elif "11:59" < now < "14:00":
        set_background = "mojave-08.jpeg"
    elif "13:59" < now < "15:50":
        set_background = "mojave-09.jpeg"
    elif "15:29" < now < "17:00":
        set_background = "mojave-10.jpeg"
    elif "16:59" < now < "18:00":
        set_background = "mojave-11.jpeg"
    elif "17:59" < now < "19:00":
        set_background = "mojave-12.jpeg"
    elif "18:59" < now < "20:00":
        set_background = "mojave-13.jpeg"
    elif "19:59" < now < "22:00":
        set_background = "mojave-14.jpeg"
    elif now > "21:59":
        set_background = "mojave-15.jpeg"
    elif now < "01:00":
        set_background = "mojave-15.jpeg"
    elif "00:59" < now < "04:00":
        set_background = "mojave-16.jpeg"
    elif "03:59" < now < "05:00":
        set_background = "mojave-01.jpeg"
    elif "04:59" < now < "06:00":
        set_background = "mojave-02.jpeg"
    else:
        set_background = ""
    if SHOW_DEBUG:
        print(f"Wallpaper: {set_background}")
    return f"'file://{os.environ['HOME']}/.local/share/backgrounds/Gnojave/{set_background}'"


def main():
    while True:
        if not get_gnome_wallpaper() == calculate_background_wallpaper():
            if SHOW_DEBUG:
                print("Wallpaper is not same. Changing wallpaper.")
            set_gnome_wallpaper(calculate_background_wallpaper())
        else:
            if SHOW_DEBUG:
                print("Wallpaper is same. Nothing changed.")
        sleep(2)


if __name__ == "__main__":
    main()
