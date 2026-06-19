from requeriments import *    
from variables import *

def menu():
    print("[JoiningPy] (MENU) " + NAME + " " + VERSION + " " + "by " + AUTHOR)
    time.sleep(1.5)
    toDo = input("What do you want to do? (install, remove, exit): ")
    if toDo == "exit":
        askExit = input("[JoiningPy] Are you sure you want to exit? (y/n): ")
        if askExit == "y" or askExit == "Y":
            print("[JoiningPy] Exiting...")
            time.sleep(1)
            exit()
        if askExit != "y" or askExit != "Y":
            subprocess.run("cls", shell=True)
            menu()
    if toDo == "install":
        install()
    if toDo == "remove":
        remove()

        time.sleep(1.5)
        subprocess.run("cls", shell=True)
        menu()
        
def install():
    print("[JoiningPy] Starting...")
    time.sleep(1.5)
    print("[JoiningPy] Select libraries to install:")
    time.sleep(1.5)
    print("[JoiningPy] 1. Pandas")
    time.sleep(0.1)
    print("[JoiningPy] 2. Numpy")
    time.sleep(0.1)
    print("[JoiningPy] 3. Requests")
    time.sleep(0.1)
    print("[JoiningPy] 4. Matplotlib")
    time.sleep(0.1)
    print("[JoiningPy] 5. Scikit-learn")
    time.sleep(0.1)
    print("[JoiningPy] 6. TensorFlow")
    time.sleep(0.1)
    print("[JoiningPy] 7. PyTorch")
    time.sleep(0.1)
    print("[JoiningPy] 8. Flask")
    time.sleep(0.1)
    print("[JoiningPy] 9. Django")
    time.sleep(0.1)
    print("[JoiningPy] 10. BeautifulSoup")
    time.sleep(0.1)
    print("[JoiningPy] 11. Selenium")
    time.sleep(0.1)
    print("[JoiningPy] 12. OpenCV")
    time.sleep(0.1)
    print("[JoiningPy] 13. Pillow")
    time.sleep(0.1)
    print("[JoiningPy] 14. SQLAlchemy")
    time.sleep(0.1)
    print("[JoiningPy] 15. PyGame")
    time.sleep(0.1)
    print("[JoiningPy] 16. Keras")
    time.sleep(0.1)
    print("[JoiningPy] 17. Pytest")
    time.sleep(0.1)
    print("[JoiningPy] 18. Jupyter")
    time.sleep(0.1)
    print("[JoiningPy] 19. Plotly")
    time.sleep(0.1)
    print("[JoiningPy] 20. Seaborn")
    time.sleep(0.1)
    
    askLibrariesInstall = input("[JoiningPy] Enter the numbers of the libraries you want to install (separated by commas, don't use spaces): ")

    if askLibrariesInstall:
        libraries = askLibrariesInstall.split(",")
        print("[JoiningPy] You selected the following libraries:")
        for library in libraries:
            print("[JoiningPy] - " + library.strip())
    
    installLibraries = input("[JoiningPy] Do you want to install the libraries? (y/n): ")
    if installLibraries == "y" or installLibraries == "Y":
        if "1" in libraries:
            print("[JoiningPy] Installing " + oneName + "...")
            time.sleep(1)
            subprocess.run(oneInstall, shell=True)
            print("[JoiningPy] " + oneName + " installed successfully.")    
        if "2" in libraries:
            print("[JoiningPy] Installing " + twoName + "...")
            time.sleep(1)
            subprocess.run(twoInstall, shell=True)
            print("[JoiningPy] " + twoName + " installed successfully.")
        if "3" in libraries:
            print("[JoiningPy] Installing " + threeName + "...")
            time.sleep(1)
            subprocess.run(threeInstall, shell=True)
            print("[JoiningPy] " + threeName + " installed successfully.")
        if "4" in libraries:
            print("[JoiningPy] Installing " + fourName + "...")
            time.sleep(1)
            subprocess.run(fourInstall, shell=True)
            print("[JoiningPy] " + fourName + " installed successfully.")
        if "5" in libraries:
            print("[JoiningPy] Installing " + fiveName + "...")
            time.sleep(1)
            subprocess.run(fiveInstall, shell=True)
            print("[JoiningPy] " + fiveName + " installed successfully.")
        if "6" in libraries:
            print("[JoiningPy] Installing " + sixName + "...")
            time.sleep(1)
            subprocess.run(sixInstall, shell=True)
            print("[JoiningPy] " + sixName + " installed successfully.")
        if "7" in libraries:
            print("[JoiningPy] Installing " + sevenName + "...")
            time.sleep(1)
            subprocess.run(sevenInstall, shell=True)
            print("[JoiningPy] " + sevenName + " installed successfully.")
        if "8" in libraries:
            print("[JoiningPy] Installing " + eightName + "...")
            time.sleep(1)
            subprocess.run(eightInstall, shell=True)
            print("[JoiningPy] " + eightName + " installed successfully.")    
        if "9" in libraries:
            print("[JoiningPy] Installing " + nineName + "...")
            time.sleep(1)
            subprocess.run(nineInstall, shell=True)
            print("[JoiningPy] " + nineName + " installed successfully.")
        if "10" in libraries:
            print("[JoiningPy] Installing " + tenName + "...")
            time.sleep(1)
            subprocess.run(tenInstall, shell=True)
            print("[JoiningPy] " + tenName + " installed successfully.") 
        if "11" in libraries:
            print("[JoiningPy] Installing " + elevenName + "...")
            time.sleep(1)
            subprocess.run(elevenInstall, shell=True)
            print("[JoiningPy] " + elevenName + " installed successfully.")
        if "12" in libraries:
            print("[JoiningPy] Installing " + twelveName + "...")
            time.sleep(1)
            subprocess.run(twelveInstall, shell=True)
            print("[JoiningPy] " + twelveName + " installed successfully.")
        if "13" in libraries:
            print("[JoiningPy] Installing " + thirteenName + "...")
            time.sleep(1)
            subprocess.run(thirteenInstall, shell=True)
            print("[JoiningPy] " + thirteenName + " installed successfully.")
        if "14" in libraries:
            print("[JoiningPy] Installing " + fourteenName + "...")
            time.sleep(1)
            subprocess.run(fourteenInstall, shell=True)
            print("[JoiningPy] " + fourteenName + " installed successfully.")
        if "15" in libraries:
            print("[JoiningPy] Installing " + fifteenName + "...")
            time.sleep(1)
            subprocess.run(fifteenInstall, shell=True)
            print("[JoiningPy] " + fifteenName + " installed successfully.")
        if "16" in libraries:
            print("[JoiningPy] Installing " + sixteenName + "...")
            time.sleep(1)
            subprocess.run(sixteenInstall, shell=True)
            print("[JoiningPy] " + sixteenName + " installed successfully.")
        if "17" in libraries:
            print("[JoiningPy] Installing " + seventeenName + "...")
            time.sleep(1)
            subprocess.run(seventeenInstall, shell=True)
            print("[JoiningPy] " + seventeenName + " installed successfully.")
        if "18" in libraries:
            print("[JoiningPy] Installing " + eighteenName + "...")
            time.sleep(1)
            subprocess.run(eighteenInstall, shell=True)
            print("[JoiningPy] " + eighteenName + " installed successfully.")
        if "19" in libraries:
            print("[JoiningPy] Installing " + nineteenName + "...")
            time.sleep(1)
            subprocess.run(nineteenInstall, shell=True)
            print("[JoiningPy] " + nineteenName + " installed successfully.")
        if "20" in libraries:
            print("[JoiningPy] Installing " + twentyName + "...")
            time.sleep(1)
            subprocess.run(twentyInstall, shell=True)
            print("[JoiningPy] " + twentyName + " installed successfully.")
        time.sleep(1.5)
        subprocess.run("cls", shell=True)
        menu()

def remove():
    print("[JoiningPy] Starting...")
    time.sleep(1.5)
    print("[JoiningPy] Select libraries to remove:")
    time.sleep(1.5)
    print("[JoiningPy] 1. Pandas")
    time.sleep(0.1)
    print("[JoiningPy] 2. Numpy")
    time.sleep(0.1)
    print("[JoiningPy] 3. Requests")
    time.sleep(0.1)
    print("[JoiningPy] 4. Matplotlib")
    time.sleep(0.1)
    print("[JoiningPy] 5. Scikit-learn")
    time.sleep(0.1)
    print("[JoiningPy] 6. TensorFlow")
    time.sleep(0.1)
    print("[JoiningPy] 7. PyTorch")
    time.sleep(0.1)
    print("[JoiningPy] 8. Flask")
    time.sleep(0.1)
    print("[JoiningPy] 9. Django")
    time.sleep(0.1)
    print("[JoiningPy] 10. BeautifulSoup")
    time.sleep(0.1)
    print("[JoiningPy] 11. Selenium")
    time.sleep(0.1)
    print("[JoiningPy] 12. OpenCV")
    time.sleep(0.1)
    print("[JoiningPy] 13. Pillow")
    time.sleep(0.1)
    print("[JoiningPy] 14. SQLAlchemy")
    time.sleep(0.1)
    print("[JoiningPy] 15. PyGame")
    time.sleep(0.1)
    print("[JoiningPy] 16. Keras")
    time.sleep(0.1)
    print("[JoiningPy] 17. Pytest")
    time.sleep(0.1)
    print("[JoiningPy] 18. Jupyter")
    time.sleep(0.1)
    print("[JoiningPy] 19. Plotly")
    time.sleep(0.1)
    print("[JoiningPy] 20. Seaborn")
    time.sleep(0.1)
    askLibrariesRemove = input("[JoiningPy] Enter the numbers of the libraries you want to remove (separated by commas, don't use spaces): ")
        
    if askLibrariesRemove:
        libraries = askLibrariesRemove.split(",")
        print("[JoiningPy] You selected the following libraries:")
        for library in libraries:
            print("[JoiningPy] - " + library.strip())
    
    removeLibraries = input("[JoiningPy] Do you want to remove the libraries? (y/n): ")
    if removeLibraries != "y" and removeLibraries != "Y":
        subprocess.run("cls", shell=True)
        menu()
    if removeLibraries == "y" or removeLibraries == "Y":
        if "1" in libraries:
            print("[JoiningPy] Removing " + oneName + "...")
            time.sleep(1)
            subprocess.run(oneRemove, shell=True)
            print("[JoiningPy] " + oneName + " removed successfully.")
        if "2" in libraries:
            print("[JoiningPy] Removing " + twoName + "...")
            time.sleep(1)
            subprocess.run(twoRemove, shell=True)
            print("[JoiningPy] " + twoName + " removed successfully.")
        if "3" in libraries:
            print("[JoiningPy] Removing " + threeName + "...")
            time.sleep(1)
            subprocess.run(threeRemove, shell=True)
            print("[JoiningPy] " + threeName + " removed successfully.")
        if "4" in libraries:
            print("[JoiningPy] Removing " + fourName + "...")
            time.sleep(1)
            subprocess.run(fourRemove, shell=True)
            print("[JoiningPy] " + fourName + " removed successfully.")
        if "5" in libraries:
            print("[JoiningPy] Removing " + fiveName + "...")
            time.sleep(1)
            subprocess.run(fiveRemove, shell=True)
            print("[JoiningPy] " + fiveName + " removed successfully.")
        if "6" in libraries:
            print("[JoiningPy] Removing " + sixName + "...")
            time.sleep(1)
            subprocess.run(sixRemove, shell=True)
            print("[JoiningPy] " + sixName + " removed successfully.")
        if "7" in libraries:
            print("[JoiningPy] Removing " + sevenName + "...")
            time.sleep(1)
            subprocess.run(sevenRemove, shell=True)
            print("[JoiningPy] " + sevenName + " removed successfully.")
        if "8" in libraries:
            print("[JoiningPy] Removing " + eightName + "...")
            time.sleep(1)
            subprocess.run(eightRemove, shell=True)
            print("[JoiningPy] " + eightName + " removed successfully.")
        if "9" in libraries:
            print("[JoiningPy] Removing " + nineName + "...")
            time.sleep(1)
            subprocess.run(nineRemove, shell=True)
            print("[JoiningPy] " + nineName + " removed successfully.")
        if "10" in libraries:
            print("[JoiningPy] Removing " + tenName + "...")
            time.sleep(1)
            subprocess.run(tenRemove, shell=True)
            print("[JoiningPy] " + tenName + " removed successfully.")
        if "11" in libraries:
            print("[JoiningPy] Removing " + elevenName + "...")
            time.sleep(1)
            subprocess.run(elevenRemove, shell=True)
            print("[JoiningPy] " + elevenName + " removed successfully.")
        if "12" in libraries:
            print("[JoiningPy] Removing " + twelveName + "...")
            time.sleep(1)
            subprocess.run(twelveRemove, shell=True)
            print("[JoiningPy] " + twelveName + " removed successfully.")
        if "13" in libraries:
            print("[JoiningPy] Removing " + thirteenName + "...")
            time.sleep(1)
            subprocess.run(thirteenRemove, shell=True)
            print("[JoiningPy] " + thirteenName + " removed successfully.") 
        if "14" in libraries:
            print("[JoiningPy] Removing " + fourteenName + "...")
            time.sleep(1)
            subprocess.run(fourteenRemove, shell=True)
            print("[JoiningPy] " + fourteenName + " removed successfully.")
        if "15" in libraries:
            print("[JoiningPy] Removing " + fifteenName + "...")
            time.sleep(1)
            subprocess.run(fifteenRemove, shell=True)
            print("[JoiningPy] " + fifteenName + " removed successfully.")
        if "16" in libraries:
            print("[JoiningPy] Removing " + sixteenName + "...")
            time.sleep(1)
            subprocess.run(sixteenRemove, shell=True)
            print("[JoiningPy] " + sixteenName + " removed successfully.")
        if "17" in libraries:
            print("[JoiningPy] Removing " + seventeenName + "...")
            time.sleep(1)
            subprocess.run(seventeenRemove, shell=True)
            print("[JoiningPy] " + seventeenName + " removed successfully.")
        if "18" in libraries:
            print("[JoiningPy] Removing " + eighteenName + "...")
            time.sleep(1)
            subprocess.run(eighteenRemove, shell=True)
            print("[JoiningPy] " + eighteenName + " removed successfully.")
        if "19" in libraries:
            print("[JoiningPy] Removing " + nineteenName + "...")
            time.sleep(1)
            subprocess.run(nineteenRemove, shell=True)
            print("[JoiningPy] " + nineteenName + " removed successfully.")
        if "20" in libraries:
            print("[JoiningPy] Removing " + twentyName + "...")
            time.sleep(1)
            subprocess.run(twentyRemove, shell=True)
            print("[JoiningPy] " + twentyName + " removed successfully.")

print("[JoiningPy] (Ready) " + NAME + " " + VERSION + " " + "by " + AUTHOR)

time.sleep(1.5)

askReady = input("[JoiningPy] Hello, Ready to start? (y/n): ")

if askReady == "y" or askReady == "Y":
    print("[JoiningPy] Starting...")
    time.sleep(1)
    menu()
else:
    print("[JoiningPy] Exiting...")
    time.sleep(1)
    exit()


