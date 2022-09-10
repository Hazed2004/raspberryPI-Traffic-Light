from os import system
from time import sleep
print("[+] Running library __init__()")
try:
    from gpiozero import LED
except:
    gpio_missing = True
try:
    from flask import Flask
except:
    flash_missing = True
def DependenciesFix():
    print("[+] Checking for missing dependencies")
    print("[+] Installed modules log can be found in mod.log file inside library folder")
    system('echo "Make sure that pip is installed if there is any error while installing dependencies" > ./library/mod.log')
    try:
        if gpio_missing:
            print("[!] GPIO module not installed")
            print("[+] Installing gpiozero...")
            system("pip install gpiozero >> ./library/mod.log")
            print("[+] Installed gpiozero")
    except NameError:
        pass
    try:
        if flash_missing:
            print("[!] Flask webserver framework not installed")
            print("[+] Installing Flask...")
            system("pip install flask >> ./library/mod.log")
            print("[+] Installed Flask")
    except NameError:
        pass

