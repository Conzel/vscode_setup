#! /usr/bin/env python3

import os
import sys
import subprocess
import shutil

# ------------------------------------------------------------------------------------
# --- User variables
# see: https://code.visualstudio.com/docs/getstarted/settings
# enter the string for your OS here 
# if you built from Open Source (OSS) build the folder might differ
settings_path = os.path.expandvars("$HOME/.config/Code/User/settings.json")

# ------------------------------------------------------------------------------------

def print_help_and_exit():
    print("Usage: Enter the extension pack you want to install or enter \"settings\" to copy general settings.")
    print("Available packages:")
    for extension in extension_packs:
        print("\t" + extension)
    sys.exit()

def copy_settings_to_local_vscode():
    settings_base_directory = os.path.dirname(settings_path)
    if not os.path.exists(settings_base_directory):
        print("The settings path in the script file does not exist.")
        print("Check the variable given in vsconfigure.py")
    shutil.copy("keybindings.json", settings_base_directory)
    shutil.copy("settings.json", settings_base_directory)

def install_extension_pack(extension_pack):
    # that the pack exists has been verified in main
    with open("extensions/" + extension_pack, "r") as extension_pack_file:
        for extension in extension_pack_file:
            extension = extension.strip('\n')
            subprocess.call(["code", "--install-extension", extension])

def verify_arguments():
    for argument in sys.argv[1:]:
        if argument != "settings" and argument not in extension_packs:
            print("Unknown argument entered. ")
            print_help_and_exit()
    return True


def main():
    if len(sys.argv) == 1:
        print_help_and_exit()
        return
    
    for argument in sys.argv[1:]:
        if argument == "settings":
            copy_settings_to_local_vscode()
        
        else:
            install_extension_pack(argument)

if __name__ == "__main__":
    # makes script callable from symlinks
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    extension_packs = os.listdir("extensions")
    verify_arguments()
    main()
