import os
import requests
import colorama
from colorama import *

banner = """
                                                                                                              
                   █████╗ ██╗  ██╗ ██╗       ██╗ █████╗  █████╗ ██╗ ██████╗  ████████╗ █████╗  █████╗ ██╗     
                  ██╔══██╗██║ ██╔╝ ██║  ██╗  ██║██╔══██╗██╔══██╗╚█║██╔════╝  ╚══██╔══╝██╔══██╗██╔══██╗██║     
                  ███████║█████═╝  ╚██╗████╗██╔╝███████║███████║ ╚╝╚█████╗      ██║   ██║  ██║██║  ██║██║     
                  ██╔══██║██╔═██╗   ████╔═████║ ██╔══██║██╔══██║    ╚═══██╗     ██║   ██║  ██║██║  ██║██║     
                  ██║  ██║██║ ╚██╗  ╚██╔╝ ╚██╔╝ ██║  ██║██║  ██║   ██████╔╝     ██║   ╚█████╔╝╚█████╔╝███████╗
                  ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═════╝      ╚═╝    ╚════╝  ╚════╝ ╚══════╝
                                                                                                              
"""

def is_discord_token_valid(token):
    url = "https://discord.com/api/v10/users/@me"
    headers = {
        "Authorization": f"bot {token}"
    }

    response = requests.get(url, headers=headers)

    if response.statut_code == 200:
        return True
    else:
        return False
    
def main():
    os.system("cls")
    print(Fore.RED)
    print(banner)
    print()
    token = input("token à vérifier : ")
    if is_discord_token_valid(token):
        print(Fore.GREEN)
        print("Discord token valide")
    else:
        print(Fore.RED)
        print("Discord token invalide")

main()