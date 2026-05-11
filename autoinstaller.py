import os
from pdb import run
import re
from tabnanny import check
import pyautogui
import questionary
from colorama import Fore, Style, init
import subprocess
import ctypes, sys
import socket
import platform
import requests

init(autoreset=True)

def get_root():
    os_name = platform.system()
    if os_name == "Windows":
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print(Fore.YELLOW + 'Запрос прав администратора')
            try:
                ctypes.windll.shell32.ShellExecuteW(
                    0,
                    "runas",
                    sys.executable,
                    " ".join(sys.argv),
                    None,
                    1
                )
                sys.exit(0)
            except Exception as e:
                print(e)
        elif os_name == "Darwin":
            if os.geteuid() != 0:
                print(Fore.YELLOW + "Запрос прав root (sudo)...")
                args = ['sudo', sys.executable] + sys.argv
                os.execvp('sud', args)

get_root()


# gettingremotecontrol
print(Fore.YELLOW + 'Loading gettingremotecontrol')
def gettingremotecontrol():
    try:
        result = subprocess.run(
            "sudo systemsetup -getremotelogin",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        status = result.stdout.strip()

        if "On" in status:
            print(Fore.GREEN + "Remote control: ON" + Style.RESET_ALL)
        else:
            print(Fore.RED + "ERROR: Remote control: OFF" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Ошибка gettingremotecontrol: {e}")
# gettingremotecontrol

def run_as_admin(command):
    logs.append(f"> {command}")
    try:
        print(f"> {command}")
        process = subprocess.Popen(
            ['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-Command', command],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=False
        )
        stdout, stderr = process.communicate(timeout=60)
        if stdout:
            print(stdout.strip())
        if stderr:
            print(Fore.RED + stderr.strip())

        return process.returncode == 0
    except Exception as e:
        print(Fore.RED + f"Ошибка при run_as_admin:{e}")
        return False

    process.wait()
# username
print(Fore.YELLOW + "Loading username")
username = os.environ.get('USER')
# username

# logs
print(Fore.YELLOW + "Creating programm logs")
logs = []
#logs

print(Fore.YELLOW + "Loading ip address")

print(Fore.GREEN + "Succes!" + Style.RESET_ALL)

ip = "0.0.0.0"

user_os = os.name

# Getting user OS
if user_os == 'nt':
    user_os = "windows"
    username = os.getlogin()
    print("Your os this" + Fore.BLUE + " Windows")
elif user_os == 'posix':
    # OS selecting
    user_os = questionary.select("Choose your OS", choices=[
        "macos",
        "linux",
        "debug"
    ]).ask()
    # OS selecting
    print("Your os this " + Fore.GREEN + str(user_os) + Style.RESET_ALL)
# Getting user OS


if user_os == "debug":
    if input('Password > ') == '1114':
        # OS selecting
        user_os = questionary.select("Choose your OS", choices=[
            "macos",
            "linux",
            "windows"
        ]).ask()
        # OS selecting
        print("Your os this " + Fore.GREEN + str(user_os))
    else:
        # OS selecting
        user_os = questionary.select("Choose your OS", choices=[
            "macos",
            "linux",
        ]).ask()
        # OS selecting
        print("Your os this" + Fore.GREEN + str(user_os))

# ip
elif user_os == 'macos':
    ip = subprocess.check_output(
        "ipconfig getifaddr en0",
        shell=True,
        text=True
    ).strip()
elif user_os == 'windows':
    ip = socket.gethostbyname(socket.gethostname())
# ip

while 1:
    # Chosing
    answer = questionary.select("Choose", choices=[
        "Installer",
        "Starter",
        "Exit"
    ]).ask()
    if answer == 'Installer':
        # Choosing
        answer = questionary.select("Choose", choices=[
            "Termius connecter phone",
            "Phone controller",
            "Cancel"
        ]).ask()
        
    # ==========================
    # ======= Installer ========
    # ==========================

        # Termius connector
        if answer == 'Termius connecter phone':
            # Getting user os
            if user_os == 'macos':
                # gettingremotecontrol()
                result = subprocess.run("sudo systemsetup -setremotelogin on", shell=True, capture_output=True, text=True)
                # gettingremotecontrol()

            # Termius connector

            elif user_os == "windows":
                try:
                    print(Fore.YELLOW + "Installing OpenSSH Server")
                    run_as_admin('Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0')
                    print(Fore.YELLOW + "Unblocking in Windows Firewall port 22" + Style.RESET_ALL)
                    run_as_admin('New-NetFirewallRule -Name sshd -DisplayName "OpenSSH Server (sshd)" -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22')
                except Exception as e:
                    print(e)
            
            elif answer == "Cancel":
                pyautogui.press('control' + 'c')
            # Termius connector

        elif answer == "Phone controller":      
            answer = questionary.select("Choose your OS", choices=[
                "Android",
                "IPhone",
                "Cancel"
            ]).ask()
            if user_os == "macos":
                if answer == "Android":
                    print(Fore.YELLOW + 'Homebrew installing' + Style.RESET_ALL)
                    result = subprocess.run('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"', shell=True, capture_output=True, text=True)
                    print(Fore.CYAN + str(result))
                    print(Fore.YELLOW + 'Scrcpy installing' + Style.RESET_ALL)
                    result = subprocess.run('brew install scrcpy', shell=True, capture_output=True, text=True)
                    print(Fore.CYAN + str(result))
                    print(Fore.YELLOW + 'ADB installing' + Style.RESET_ALL)
                    result = subprocess.run('brew install --cask android-platform-tools', shell=True, capture_output=True, text=True)
                    print(Fore.CYAN + str(result))
                    print(Fore.YELLOW + 'ADB checking' + Style.RESET_ALL)
                    result = subprocess.run('adb version', shell=True, capture_output=True, text=True)
                    print(Fore.CYAN + str(result) + Style.RESET_ALL)
                elif answer == "IPhone":
                    print('This function not created')
                elif answer == "Cancel":
                    pyautogui.press('control' + 'c')
            if user_os == "windows":
                if answer == "Android":
                    print(Fore.RED + 'This function not created')
            
                elif answer == "IPhone":
                    print('This function not created')
                elif answer == "Cancel":
                    pyautogui.press('control' + 'c')
    

    # ==========================
    # ======== Starter =========
    # ==========================



    elif answer == "Starter":
        answer = questionary.select("Choose", choices=[
            "Start SSH",
            "Start phone controller",
            "Cancel"
        ]).ask()

        if answer == 'Start SSH':
            # ===============
            # === Windows ===
            # ===============
            if user_os == 'windows':
                print(Fore.YELLOW + "Starting sshd")
                run_as_admin('Start-Service sshd')

                # SSH build
                ssh = f"ssh {username}@{ip}"
                print(ssh)
                # SSH build

                answer = questionary.select("Add auto start?", choices=[
                    "Yes",
                    "No"
                ]).ask()

                # Auto start ssh
                if answer == "Yes":
                    print(Fore.YELLOW + "Setting automaticly starting")
                    run_as_admin('Set-Service -Name sshd -StartupType Automatic')
                # Auto start ssh

                else:
                    pass

            # =============
            # === MACOS ===
            # =============
            elif user_os == 'macos':
                print(Fore.YELLOW + "SSH build")
                ssh_address = f"ssh {username}@{ip}"
                print(Style.RESET_ALL + ssh_address)
                print(Fore.GREEN + "Enter this SSH in mobile app")
                


        elif answer == 'Start phone controller':
            # Phone connected?
            answer = questionary.select("Connect your phone with cable", choices=[
                "Next",
                "Cancel"
                ]).ask()
            # Phone connected?

            # Cancel button
            if answer == "Cancel":
                pyautogui.press('control' + 'c')
            # Cancel button

            # Next button
            else:
                if user_os == 'macos':
                    try:
                        answer = questionary.select("Connect your phone with cable", choices=[
                            "Start",
                            "Cancel"
                        ]).ask()
                        if answer == 'Start':
                            result = subprocess.run('scrcpy', shell=True, capture_output=True, text=True)
                        
                        else:
                            pyautogui.press('control' + 'c')
                    except Exception as e:
                        print(e)
                elif user_os == 'windows':
                    print(Fore.RED + 'Function not created for WINDOWS')



    elif answer == "Exit":
        break
