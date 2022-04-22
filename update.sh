#!/bin/bash

#
# Update script for DistroUpdater
#

echo "Updating DistroUpdater..."

sudo rm /usr/bin/distro-updater
sed -i "s;~;$HOME;g" distro-updater.py
sudo cp distro-updater.py /usr/bin/distro-updater
sudo chmod a+x /usr/bin/distro-updater

echo "DistroUpdater has been updated"
