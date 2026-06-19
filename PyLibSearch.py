import requests
import os
import subprocess
import time
from requeriments import *

def search(menu):
    library = input("[JoiningPy] Enter the library name to search: ").strip()

    url = f"https://pypi.org/pypi/{library}/json"
    data = None

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            print("\n[JoiningPy] Library found!")
            print("[JoiningPy] Name:", data["info"]["name"])
            print("[JoiningPy] Version:", data["info"]["version"])
            print("[JoiningPy] Summary:", data["info"]["summary"])

        elif response.status_code == 404:
            print("\n[JoiningPy] Library not found.")

        else:
            print(f"\n[JoiningPy] Error: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print("\n[JoiningPy] Connection error:", e)

    if data:
        askForInstall = input(
            "[JoiningPy] You want to install this library? (y/n): "
        )

        if askForInstall.lower() == "y":
            print("[JoiningPy] Installing " + data["info"]["name"] + "...")
            time.sleep(1)

            subprocess.run(
                ["pip", "install", data["info"]["name"]],
                check=False
            )

            print(
                "[JoiningPy] "
                + data["info"]["name"]
                + " installed successfully."
            )

            time.sleep(1)

    goToMenu = input("[JoiningPy] Go to menu? (y/n): ")

    if goToMenu.lower() == "y":
        os.system("cls" if os.name == "nt" else "clear")
        menu()
    else:
        print("[JoiningPy] Exiting...")
        time.sleep(1)
        exit()