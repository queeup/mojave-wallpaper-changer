#!/usr/bin/env sh

mkdir -p ~/.local/bin \
         ~/.config/autostart \
         ~/.local/share/backgrounds/Gnojave

echo "Downloading wallpapers..."
for i in $(seq -w 1 16)
do
    if [ ! -f ~/.local/share/backgrounds/Gnojave/mojave-$i.jpeg ]; then
        curl -sSL "https://github.com/danielyor/macOS-Mojave-Dynamic-Wallpaper-for-Gnome/raw/master/Gnojave/mojave-$i.jpeg" --output ~/.local/share/backgrounds/Gnojave/mojave-$i.jpeg
    fi
done

echo "Installing files..."
curl -sSL "https://github.com/queeup/mojave-wallpaper-changer/raw/main/mojave-wallpaper-changer.py" --output ~/.local/bin/mojave-wallpaper-changer.py
curl -sSL "https://github.com/queeup/mojave-wallpaper-changer/raw/main/mojave-wallpaper-changer.desktop" --output ~/.config/autostart/mojave-wallpaper-changer.desktop

echo "Starting mojave-wallpaper-changer..."
chmod +x ~/.local/bin/mojave-wallpaper-changer.py
~/.local/bin/mojave-wallpaper-changer.py &

echo "Done."
