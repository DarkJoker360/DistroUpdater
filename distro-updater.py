#!/usr/bin/python3

import configparser, os
from datetime import datetime

if __name__ == "__main__":
    version = "1.0"
    config_path = "~/.config/distro-updater/config.ini"

    if not os.path.exists(config_path):
        print("ERROR: No config file found !")
        exit()

    def is_updated():
        if last_checked == current_date:
            return True
        if current_date > last_updated:
            match freq:
                case "yearly":
                    if int(last_updated[0:4]) < int(current_date[0:4]):
                        return False
                case "monthly":
                    if int(last_updated[5:7]) < int(current_date[5:7]):                    
                        return False
                case "weekly":
                    if int(last_updated[8:10]) < int(current_date[8:10]):
                        if int(current_date[8:10]) - int(last_updated[8:10]) > 7:
                            return False
                case "daily":
                    if int(last_updated[9:10]) < int(current_date[9:10]):
                        if int(current_date[8:10]) - int(last_updated[8:10]) > 0:
                            return False
        else:
            return True

    def update():
        print("Updating now...")
        match configs["configuration"]["pkg_manager"]:
            case "apt":
                if os.system("sudo apt-get update -y") == 0:
                    if os.system("sudo apt-get upgrade") == 0:
                        return True
                    else:
                        return False
                else:
                        return False
            case "dnf":
                if os.system("sudo dnf upgrade") == 0:
                    return True
                else:
                    return False
            case "pacman":
                if os.system("sudo pacman -Syu") == 0:
                    if os.system("yay -Syu") == 0:
                        return True
                else:
                    return False
            case "yum":
                if os.system("sudo yum upgrade") == 0:
                    return True
                else:
                    return False

    current_date = datetime.now().strftime("%Y-%m-%d")
    configs = configparser.ConfigParser()
    configs.read(config_path)
    freq = configs['configuration']['freq']
    last_updated = configs['history']['last_updated']
    last_checked = configs['history']['last_checked']
    configs.set('history', 'last_checked', current_date)

    if is_updated() == False:
        print("Update is required now !\nLast updated: " + last_updated)
        choice = input("Would you like to update your system now? (s/n) ")
        if choice == "s" or choice == "S":
            if update() == True:
                configs.set('history', 'last_updated', current_date)
                print("System has been updated !")
            else:
                print("FATAL: System has not been updated !")
        else:
            print("Aborting...")

    with open(config_path, "w") as configfile:
        configs.write(configfile)

    exit()
