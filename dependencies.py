import time
import subprocess
import platform
import os
import sys

system = platform.system()

def system_func():
    global system

    if system == "Windows":
        subprocess.run(
            "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py",
            shell=True
        )
        subprocess.run(
            "python get-pip.py",
            shell=True
        )
        os.system('cls' if os.name == 'nt' else 'clear')

    elif system == "Linux":
        subprocess.run(
            "sudo apt install -y python3-pip",
            shell=True
        )
        os.system('cls' if os.name == 'nt' else 'clear')

    elif system == "Darwin":
        subprocess.run(
            "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py",
            shell=True
        )
        subprocess.run(
            "python3 get-pip.py",
            shell=True
        )
        os.system('cls' if os.name == 'nt' else 'clear')


def install_libraries():
    global system

    if system == "Windows":
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "requests"]
        )
        os.system('cls' if os.name == 'nt' else 'clear')

    elif system == "Linux":
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "requests"]
        )
        os.system('cls' if os.name == 'nt' else 'clear')

    elif system == "Darwin":
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "requests"]
        )
        os.system('cls' if os.name == 'nt' else 'clear')


print("[JoiningPy] Hello!")
time.sleep(2)

print("[JoiningPy] Before using the program, you need to install some dependencies.")
time.sleep(2)

print("[JoiningPy] Dependencies:")
time.sleep(1)

print("[JoiningPy] 1. Requests")
time.sleep(0.1)

system_func()
install_libraries()

os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)
print("[JoiningPy] Now run (python main.py) or (python3 main.py) to use JoiningPy")
time.sleep(2)