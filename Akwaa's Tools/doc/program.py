import os
import fade 
import time
from fade import *

banner = """
                                                                                                               
                   █████╗ ██╗  ██╗ ██╗       ██╗ █████╗  █████╗ ██╗ ██████╗  ████████╗ █████╗  █████╗ ██╗      
                  ██╔══██╗██║ ██╔╝ ██║  ██╗  ██║██╔══██╗██╔══██╗╚█║██╔════╝  ╚══██╔══╝██╔══██╗██╔══██╗██║      
                  ███████║█████═╝  ╚██╗████╗██╔╝███████║███████║ ╚╝╚█████╗      ██║   ██║  ██║██║  ██║██║      
                  ██╔══██║██╔═██╗   ████╔═████║ ██╔══██║██╔══██║    ╚═══██╗     ██║   ██║  ██║██║  ██║██║      
                  ██║  ██║██║ ╚██╗  ╚██╔╝ ╚██╔╝ ██║  ██║██║  ██║   ██████╔╝     ██║   ╚█████╔╝╚█████╔╝███████╗ 
                  ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═════╝      ╚═╝    ╚════╝  ╚════╝ ╚══════╝ 
                                                                                                               
"""
banner = fade.greenblue(banner)

menu = """
                                ╔══════════════════════╗
                                ║ [0] MENU             ║
                                ║ [1] EMAIL TRACKER    ║
                                ║ [2] URL SHORTENER    ║
                                ║ [3] WIFI HACKER      ║
                                ║ [4] ...              ║
                                ╚══════════════════════╝
"""

menu = fade.greenblue(menu)

def main():
    os.system("cls")  # Pour Windows, sinon utilisez 'clear' pour Linux/macOS
    print("Connexion...")
    time.sleep(4)
    print("Veuillez patienter...")
    time.sleep(5)
    print("Chargement terminé !")
    print(banner)
    print()
    print(menu)

    choice = input("Choisissez un nombre : ")
    if choice == "0":
        os.system("program.py")  # Remplacez 'program.py' par le programme réel
    elif choice == "1":
        os.system("python EMAILTRACKER.py")  # Exécuter le script Email Tracker
    elif choice == "2":
        os.system("python URLSHORTENER.py")  # Exécuter le script URL Shortener
    elif choice == "3":
        os.system("python WIFIHACKER.py")  # Exécuter le script Wifi Hacker
    else:
        print("Merci de rentrer un nombre valide")
        main()

    # Attendre que l'utilisateur appuie sur "R" pour relancer le programme principal
    retry = input("Appuyez sur 'R' pour relancer le menu principal : ").upper()
    if retry == 'R':
        main()  # Relancer le menu principal
    else:
        print("Sortie...")

main()
