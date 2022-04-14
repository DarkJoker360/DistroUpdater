#!/bin/bash

#
# Install script for DistroUpdater
#

current_date=$(date +%Y-%m-%d) # Dummy initial date

echo "Installing DistroUpdater..."

sed -i "s;~;$HOME;g" distro-updater.py
sudo cp distro-updater.py /usr/bin/distro-updater
sudo chmod a+x /usr/bin/distro-updater
echo " " >> ~/.bashrc
echo "distro-updater" >> ~/.bashrc
mkdir ~/.config/distro-updater 

read -p "How often do you want to update your distro? (yearly, monthly, weekly, daily) " freq

if [ $freq != "yearly" ] && [ $freq != "monthly" ] && [ $freq != "weekly" ] && [ $freq != "daily" ]; then
    echo "Invalid frequency, aborting..."
    exit 1
fi

if [ -f /usr/bin/apt ]; then
    pkgm="apt"
elif [ -f /usr/bin/dnf ]; then
    pkgm="dnf"
elif [ -f /usr/bin/pacman ]; then
    pkgm="pacman"
elif [ -f /usr/bin/yum ]; then
    pkgm="yum"
else
    echo "No compatible package manager found, aborting..."
    exit 1
fi

echo "[configuration]" > ~/.config/distro-updater/config.ini
echo "freq = $freq" >> ~/.config/distro-updater/config.ini
echo "pkg_manager = $pkgm" >> ~/.config/distro-updater/config.ini
echo " " >> ~/.config/distro-updater/config.ini
echo "[history]" >> ~/.config/distro-updater/config.ini
echo "last_updated = $current_date" >> ~/.config/distro-updater/config.ini
echo "last_checked = $current_date" >> ~/.config/distro-updater/config.ini

echo "DistroUpdater has been installed"
