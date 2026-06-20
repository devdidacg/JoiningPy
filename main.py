from requeriments import *    
from variables import *
import platform
import requests
import PyLibSearch


system = platform.system()
firstTime = True
    
def list():
    print("Searching libraries...")
    time.sleep(1.5)
    subprocess.run("pip list", shell=True)
    goToMenu = input("[JoiningPy] Go to menu? (y/n): ")
    
    if goToMenu == "y" or goToMenu == "Y":
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()        
    if goToMenu != "y" or goToMenu != "Y":
        print("[JoiningPy] Exiting...")
        time.sleep(1)
        exit()

def menu():
    print("[JoiningPy] (MENU) " + NAME + " " + VERSION + " " + "by " + AUTHOR)
    time.sleep(1.5)
    toDo = input("[JoiningPy] What do you want to do? (install, remove, list, search, exit): ")
    if toDo == "search":
        PyLibSearch.search(menu)

    if toDo == "exit":
        askExit = input("[JoiningPy] Are you sure you want to exit? (y/n): ")
        if askExit == "y" or askExit == "Y":
            print("[JoiningPy] Exiting...")
            time.sleep(1)
            exit()
        if askExit != "y" or askExit != "Y":
            os.system('cls' if os.name == 'nt' else 'clear')
            menu()
    if toDo == "install":
        install()
    if toDo == "remove":
        print("[JoiningPy] Starting...")
        time.sleep(1.5)
        print("[JoiningPy] Select libraries to remove:")
        time.sleep(1.5)
        print("[JoiningPy] 1. " + oneName)
        time.sleep(0.1)
        print("[JoiningPy] 2. " + twoName)
        time.sleep(0.1)
        print("[JoiningPy] 3. " + threeName)
        time.sleep(0.1)
        print("[JoiningPy] 4. " + fourName)
        time.sleep(0.1)
        print("[JoiningPy] 5. " + fiveName)
        time.sleep(0.1)
        print("[JoiningPy] 6. " + sixName)
        time.sleep(0.1)
        print("[JoiningPy] 7. " + sevenName)
        time.sleep(0.1)
        print("[JoiningPy] 8. " + eightName)
        time.sleep(0.1)
        print("[JoiningPy] 9. " + nineName)
        time.sleep(0.1)
        print("[JoiningPy] 10. " + tenName)
        time.sleep(0.1)
        print("[JoiningPy] 11. " + elevenName)
        time.sleep(0.1)
        print("[JoiningPy] 12. " + twelveName)
        time.sleep(0.1)
        print("[JoiningPy] 13. " + thirteenName)
        time.sleep(0.1)
        print("[JoiningPy] 14. " + fourteenName)
        time.sleep(0.1)
        print("[JoiningPy] 15. " + fifteenName)
        time.sleep(0.1)
        print("[JoiningPy] 16. " + sixteenName)
        time.sleep(0.1)
        print("[JoiningPy] 17. " + seventeenName)
        time.sleep(0.1)
        print("[JoiningPy] 18. " + eighteenName)
        time.sleep(0.1)
        print("[JoiningPy] 19. " + nineteenName)
        time.sleep(0.1)
        print("[JoiningPy] 20. " + twentyName)
        time.sleep(0.1)
        print("[JoiningPy] 21. " + twentyOneName)
        time.sleep(0.1)
        print("[JoiningPy] 22. " + twentyTwoName)
        time.sleep(0.1)
        print("[JoiningPy] 23. " + twentyThreeName)
        time.sleep(0.1)
        print("[JoiningPy] 24. " + twentyFourName)
        time.sleep(0.1)
        print("[JoiningPy] 25. " + twentyFiveName)
        time.sleep(0.1)
        print("[JoiningPy] 26. " + twentySixName)
        time.sleep(0.1)
        print("[JoiningPy] 27. " + twentySevenName)
        time.sleep(0.1)
        print("[JoiningPy] 28. " + twentyEightName)
        time.sleep(0.1)
        print("[JoiningPy] 29. " + twentyNineName)
        time.sleep(0.1)
        print("[JoiningPy] 30. " + thirtyName)
        time.sleep(0.1)
        print("[JoiningPy] 31. " + thirtyOneName)
        time.sleep(0.1)
        print("[JoiningPy] 32. " + thirtyTwoName)
        time.sleep(0.1)
        print("[JoiningPy] 33. " + thirtyThreeName)
        time.sleep(0.1)
        print("[JoiningPy] 34. " + thirtyFourName)
        time.sleep(0.1)
        print("[JoiningPy] 35. " + thirtyFiveName)
        time.sleep(0.1)
        print("[JoiningPy] 36. " + thirtySixName)
        time.sleep(0.1)
        print("[JoiningPy] 37. " + thirtySevenName)
        time.sleep(0.1)
        print("[JoiningPy] 38. " + thirtyEightName)
        time.sleep(0.1)
        print("[JoiningPy] 39. " + thirtyNineName)
        time.sleep(0.1)
        print("[JoiningPy] 40. " + fortyName)
        time.sleep(0.1)
        askLibrariesRemove = input("[JoiningPy] Enter the numbers of the libraries you want to remove (separated by commas, don't use spaces): ")

        if askLibrariesRemove:
            libraries = askLibrariesRemove.split(",")
            print("[JoiningPy] You selected the following libraries:")
            for library in libraries:
                print("[JoiningPy] - " + library.strip())
    
        removeLibraries = input("[JoiningPy] Do you want to remove the libraries? (y/n): ")
        if removeLibraries != "y" and removeLibraries != "Y":
            os.system('cls' if os.name == 'nt' else 'clear')
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
            if "21" in libraries:
                print("[JoiningPy] Removing " + twentyOneName + "...")
                time.sleep(1)
                subprocess.run(twentyOneRemove, shell=True)
                print("[JoiningPy] " + twentyOneName + " removed successfully.")
            if "22" in libraries:
                print("[JoiningPy] Removing " + twentyTwoName + "...")
                time.sleep(1)
                subprocess.run(twentyTwoRemove, shell=True)
                print("[JoiningPy] " + twentyTwoName + " removed successfully.")
            if "23" in libraries:
                print("[JoiningPy] Removing " + twentyThreeName + "...")
                time.sleep(1)
                subprocess.run(twentyThreeRemove, shell=True)
                print("[JoiningPy] " + twentyThreeName + " removed successfully.")
            if "24" in libraries:
                print("[JoiningPy] Removing " + twentyFourName + "...")
                time.sleep(1)
                subprocess.run(twentyFourRemove, shell=True)
                print("[JoiningPy] " + twentyFourName + " removed successfully.")
            if "25" in libraries:
                print("[JoiningPy] Removing " + twentyFiveName + "...")
                time.sleep(1)
                subprocess.run(twentyFiveRemove, shell=True)
                print("[JoiningPy] " + twentyFiveName + " removed successfully.")
            if "26" in libraries:
                print("[JoiningPy] Removing " + twentySixName + "...")
                time.sleep(1)
                subprocess.run(twentySixRemove, shell=True)
                print("[JoiningPy] " + twentySixName + " removed successfully.")
            if "27" in libraries:
                print("[JoiningPy] Removing " + twentySevenName + "...")
                time.sleep(1)
                subprocess.run(twentySevenRemove, shell=True)
                print("[JoiningPy] " + twentySevenName + " removed successfully.")
            if "28" in libraries:
                print("[JoiningPy] Removing " + twentyEightName + "...")
                time.sleep(1)
                subprocess.run(twentyEightRemove, shell=True)
                print("[JoiningPy] " + twentyEightName + " removed successfully.")
            if "29" in libraries:
                print("[JoiningPy] Removing " + twentyNineName + "...")
                time.sleep(1)
                subprocess.run(twentyNineRemove, shell=True)
                print("[JoiningPy] " + twentyNineName + " removed successfully.")
            if "30" in libraries:
                print("[JoiningPy] Removing " + thirtyName + "...")
                time.sleep(1)
                subprocess.run(thirtyRemove, shell=True)
                print("[JoiningPy] " + thirtyName + " removed successfully.")
            if "31" in libraries:
                print("[JoiningPy] Removing " + thirtyOneName + "...")
                time.sleep(1)
                subprocess.run(thirtyOneRemove, shell=True)
                print("[JoiningPy] " + thirtyOneName + " removed successfully.")
            if "32" in libraries:
                print("[JoiningPy] Removing " + thirtyTwoName + "...")
                time.sleep(1)
                subprocess.run(thirtyTwoRemove, shell=True)
                print("[JoiningPy] " + thirtyTwoName + " removed successfully.")
            if "33" in libraries:
                print("[JoiningPy] Removing " + thirtyThreeName + "...")
                time.sleep(1)
                subprocess.run(thirtyThreeRemove, shell=True)
                print("[JoiningPy] " + thirtyThreeName + " removed successfully.")
            if "34" in libraries:
                print("[JoiningPy] Removing " + thirtyFourName + "...")
                time.sleep(1)
                subprocess.run(thirtyFourRemove, shell=True)
                print("[JoiningPy] " + thirtyFourName + " removed successfully.")
            if "35" in libraries:
                print("[JoiningPy] Removing " + thirtyFiveName + "...")
                time.sleep(1)
                subprocess.run(thirtyFiveRemove, shell=True)
                print("[JoiningPy] " + thirtyFiveName + " removed successfully.")
            if "36" in libraries:
                print("[JoiningPy] Removing " + thirtySixName + "...")
                time.sleep(1)
                subprocess.run(thirtySixRemove, shell=True)
                print("[JoiningPy] " + thirtySixName + " removed successfully.")
            if "37" in libraries:
                print("[JoiningPy] Removing " + thirtySevenName + "...")
                time.sleep(1)
                subprocess.run(thirtySevenRemove, shell=True)
                print("[JoiningPy] " + thirtySevenName + " removed successfully.")
            if "38" in libraries:
                print("[JoiningPy] Removing " + thirtyEightName + "...")
                time.sleep(1)
                subprocess.run(thirtyEightRemove, shell=True)
                print("[JoiningPy] " + thirtyEightName + " removed successfully.")
            if "39" in libraries:
                print("[JoiningPy] Removing " + thirtyNineName + "...")
                time.sleep(1)
                subprocess.run(thirtyNineRemove, shell=True)
                print("[JoiningPy] " + thirtyNineName + " removed successfully.")
            if "40" in libraries:
                print("[JoiningPy] Removing " + fortyName + "...")
                time.sleep(1)
                subprocess.run(fortyRemove, shell=True)
                print("[JoiningPy] " + fortyName + " removed successfully.")

            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            menu()
    
    if toDo == "list":
        list()

def install():
    print("[JoiningPy] Starting...")
    time.sleep(1.5)
    askForDirectory = input("In which folder do you want to install the libraries?: ")
    subprocess.run("pwd", shell=True)
    print("[JoiningPy] Select libraries to install:")
    time.sleep(1.5)
    print("[JoiningPy] 1. " + oneName)
    time.sleep(0.1)
    print("[JoiningPy] 2. " + twoName)
    time.sleep(0.1)
    print("[JoiningPy] 3. " + threeName)
    time.sleep(0.1)
    print("[JoiningPy] 4. " + fourName)
    time.sleep(0.1)
    print("[JoiningPy] 5. " + fiveName)
    time.sleep(0.1)
    print("[JoiningPy] 6. " + sixName)
    time.sleep(0.1)
    print("[JoiningPy] 7. " + sevenName)
    time.sleep(0.1)
    print("[JoiningPy] 8. " + eightName)
    time.sleep(0.1)
    print("[JoiningPy] 9. " + nineName)
    time.sleep(0.1)
    print("[JoiningPy] 10. " + tenName)
    time.sleep(0.1)
    print("[JoiningPy] 11. " + elevenName)
    time.sleep(0.1)
    print("[JoiningPy] 12. " + twelveName)
    time.sleep(0.1)
    print("[JoiningPy] 13. " + thirteenName)
    time.sleep(0.1)
    print("[JoiningPy] 14. " + fourteenName)
    time.sleep(0.1)
    print("[JoiningPy] 15. " + fifteenName)
    time.sleep(0.1)
    print("[JoiningPy] 16. " + sixteenName)
    time.sleep(0.1)
    print("[JoiningPy] 17. " + seventeenName)
    time.sleep(0.1)
    print("[JoiningPy] 18. " + eighteenName)
    time.sleep(0.1)
    print("[JoiningPy] 19. " + nineteenName)
    time.sleep(0.1)
    print("[JoiningPy] 20. " + twentyName)
    time.sleep(0.1)
    print("[JoiningPy] 21. " + twentyOneName)
    time.sleep(0.1)
    print("[JoiningPy] 22. " + twentyTwoName)
    time.sleep(0.1)
    print("[JoiningPy] 23. " + twentyThreeName)
    time.sleep(0.1)
    print("[JoiningPy] 24. " + twentyFourName)
    time.sleep(0.1)
    print("[JoiningPy] 25. " + twentyFiveName)
    time.sleep(0.1)
    print("[JoiningPy] 26. " + twentySixName)
    time.sleep(0.1)
    print("[JoiningPy] 27. " + twentySevenName)
    time.sleep(0.1)
    print("[JoiningPy] 28. " + twentyEightName)
    time.sleep(0.1)
    print("[JoiningPy] 29. " + twentyNineName)
    time.sleep(0.1)
    print("[JoiningPy] 30. " + thirtyName)
    time.sleep(0.1)
    print("[JoiningPy] 31. " + thirtyOneName)
    time.sleep(0.1)
    print("[JoiningPy] 32. " + thirtyTwoName)
    time.sleep(0.1)
    print("[JoiningPy] 33. " + thirtyThreeName)
    time.sleep(0.1)
    print("[JoiningPy] 34. " + thirtyFourName)
    time.sleep(0.1)
    print("[JoiningPy] 35. " + thirtyFiveName)
    time.sleep(0.1)
    print("[JoiningPy] 36. " + thirtySixName)
    time.sleep(0.1)
    print("[JoiningPy] 37. " + thirtySevenName)
    time.sleep(0.1)
    print("[JoiningPy] 38. " + thirtyEightName)
    time.sleep(0.1)
    print("[JoiningPy] 39. " + thirtyNineName)
    time.sleep(0.1)
    print("[JoiningPy] 40. " + fortyName)
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
        if "21" in libraries:
            print("[JoiningPy] Installing " + twentyOneName + "...")
            time.sleep(1)
            subprocess.run(twentyOneInstall, shell=True)
            print("[JoiningPy] " + twentyOneName + " installed successfully.")
        if "22" in libraries:
            print("[JoiningPy] Installing " + twentyTwoName + "...")
            time.sleep(1)
            subprocess.run(twentyTwoInstall, shell=True)
            print("[JoiningPy] " + twentyTwoName + " installed successfully.")
        if "23" in libraries:
            print("[JoiningPy] Installing " + twentyThreeName + "...")
            time.sleep(1)
            subprocess.run(twentyThreeInstall, shell=True)
            print("[JoiningPy] " + twentyThreeName + " installed successfully.")
        if "24" in libraries:
            print("[JoiningPy] Installing " + twentyFourName + "...")
            time.sleep(1)
            subprocess.run(twentyFourInstall, shell=True)
            print("[JoiningPy] " + twentyFourName + " installed successfully.")
        if "25" in libraries:
            print("[JoiningPy] Installing " + twentyFiveName + "...")
            time.sleep(1)
            subprocess.run(twentyFiveInstall, shell=True)
            print("[JoiningPy] " + twentyFiveName + " installed successfully.")
        if "26" in libraries:
            print("[JoiningPy] Installing " + twentySixName + "...")
            time.sleep(1)
            subprocess.run(twentySixInstall, shell=True)
            print("[JoiningPy] " + twentySixName + " installed successfully.")
        if "27" in libraries:
            print("[JoiningPy] Installing " + twentySevenName + "...")
            time.sleep(1)
            subprocess.run(twentySevenInstall, shell=True)
            print("[JoiningPy] " + twentySevenName + " installed successfully.")
        if "28" in libraries:
            print("[JoiningPy] Installing " + twentyEightName + "...")
            time.sleep(1)
            subprocess.run(twentyEightInstall, shell=True)
            print("[JoiningPy] " + twentyEightName + " installed successfully.")
        if "29" in libraries:
            print("[JoiningPy] Installing " + twentyNineName + "...")
            time.sleep(1)
            subprocess.run(twentyNineInstall, shell=True)
            print("[JoiningPy] " + twentyNineName + " installed successfully.")
        if "30" in libraries:
            print("[JoiningPy] Installing " + thirtyName + "...")
            time.sleep(1)
            subprocess.run(thirtyInstall, shell=True)
            print("[JoiningPy] " + thirtyName + " installed successfully.")
        if "31" in libraries:
            print("[JoiningPy] Installing " + thirtyOneName + "...")
            time.sleep(1)
            subprocess.run(thirtyOneInstall, shell=True)
            print("[JoiningPy] " + thirtyOneName + " installed successfully.")
        if "32" in libraries:
            print("[JoiningPy] Installing " + thirtyTwoName + "...")
            time.sleep(1)
            subprocess.run(thirtyTwoInstall, shell=True)
            print("[JoiningPy] " + thirtyTwoName + " installed successfully.")
        if "33" in libraries:
            print("[JoiningPy] Installing " + thirtyThreeName + "...")
            time.sleep(1)
            subprocess.run(thirtyThreeInstall, shell=True)
            print("[JoiningPy] " + thirtyThreeName + " installed successfully.")
        if "34" in libraries:
            print("[JoiningPy] Installing " + thirtyFourName + "...")
            time.sleep(1)
            subprocess.run(thirtyFourInstall, shell=True)
            print("[JoiningPy] " + thirtyFourName + " installed successfully.")
        if "35" in libraries:
            print("[JoiningPy] Installing " + thirtyFiveName + "...")
            time.sleep(1)
            subprocess.run(thirtyFiveInstall, shell=True)
            print("[JoiningPy] " + thirtyFiveName + " installed successfully.")
        if "36" in libraries:
            print("[JoiningPy] Installing " + thirtySixName + "...")
            time.sleep(1)
            subprocess.run(thirtySixInstall, shell=True)
            print("[JoiningPy] " + thirtySixName + " installed successfully.")
        if "37" in libraries:
            print("[JoiningPy] Installing " + thirtySevenName + "...")
            time.sleep(1)
            subprocess.run(thirtySevenInstall, shell=True)
            print("[JoiningPy] " + thirtySevenName + " installed successfully.")
        if "38" in libraries:
            print("[JoiningPy] Installing " + thirtyEightName + "...")
            time.sleep(1)
            subprocess.run(thirtyEightInstall, shell=True)
            print("[JoiningPy] " + thirtyEightName + " installed successfully.")
        if "39" in libraries:
            print("[JoiningPy] Installing " + thirtyNineName + "...")
            time.sleep(1)
            subprocess.run(thirtyNineInstall, shell=True)
            print("[JoiningPy] " + thirtyNineName + " installed successfully.")
        if "40" in libraries:
            print("[JoiningPy] Installing " + fortyName + "...")
            time.sleep(1)
            subprocess.run(fortyInstall, shell=True)
            print("[JoiningPy] " + fortyName + " installed successfully.")
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()



def system_func():
    global firstTime, system
    if firstTime == True:
        if system == "Windows":
            firstTime = False
            subprocess.run("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py", shell=True)
            subprocess.run("python get-pip.py", shell=True)
            os.system('cls' if os.name == 'nt' else 'clear')
            menu()
        
        elif system == "Linux":
            firstTime = False
            subprocess.run("sudo apt install python3-pip", shell=True)
            os.system('cls' if os.name == 'nt' else 'clear')
            menu()
        
        elif system == "Darwin":
            firstTime = False
            subprocess.run("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py",shell=True)
            subprocess.run("python3 get-pip.py", shell=True)
            os.system('cls' if os.name == 'nt' else 'clear')
            menu()
        

print("[JoiningPy] (Ready) " + NAME + " " + VERSION + " " + "by " + AUTHOR)

time.sleep(1.5)

askReady = input("[JoiningPy] Hello, Ready to start? (y/n): ")

if askReady == "y" or askReady == "Y":
    print("[JoiningPy] Starting...")
    time.sleep(1)
    if firstTime == True:
        askPip = input("[JoiningPy] Do you want install pip? (y/n): ")
        if askPip == "y" or askPip == "Y":
            system_func()
        if askPip != "y" or askPip != "Y":
            print("[JoiningPy] Going to menu...")
            time.sleep(1)
            menu()
    if firstTime != True:
        menu()
else:
    print("[JoiningPy] Exiting...")
    time.sleep(1)
    exit()

