import requests
from colorama import Fore, Style
from os import system
import time

def sqlInjectionUrl(url):
    payloads = input(Fore.LIGHTYELLOW_EX + "SQL payload file path: ")
    system("cls||clear")

    try:
        with open(payloads.strip(), encoding="UTF-8") as f:
            for payload in f:
                fullUrl = f"{url}{payload.strip()}"

                try:
                    response = requests.get(fullUrl)
                    if response.status_code == 200:
                        if "error" not in response.text.lower():
                            print(f"{Fore.LIGHTGREEN_EX}[+] SQL Injection found with payload: {Style.RESET_ALL}{payload.strip()}")

                        else:
                            print(f"{Fore.LIGHTRED_EX}[-] SQL injection with payload not found: {Style.RESET_ALL}{payload.strip()}")

                    else:
                        print(f"Request to {fullUrl} returned status code: {response.status_code}")

                except requests.exceptions.RequestException as e:
                    print(f"{Fore.LIGHTRED_EX}Request failed: {e}")

    except FileNotFoundError:
        print(f"{Fore.LIGHTRED_EX}Payload file not found.")

    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}An error occurred: {e}")

def sqlInjPost(url, params):
    payloads = input(Fore.LIGHTYELLOW_EX + "SQL payload file path: ")
    system("cls||clear")

    try:
        with open(payloads.strip(), encoding="UTF-8") as f:
            for payload in f:
                data = {params: payload.strip()}

                try:
                    response = requests.post(url, data=data)

                    if response.status_code == 200:
                        if "error" not in response.text.lower():
                            print(f"{Fore.LIGHTGREEN_EX}[+] SQL Injection found with payload: {Style.RESET_ALL}{payload.strip()}")

                        else:
                            print(f"{Fore.LIGHTRED_EX}[-] SQL injection with payload not found: {Style.RESET_ALL}{payload.strip()}")

                    else:
                        print(f"Request to {url} returned status code: {response.status_code}")

                except requests.exceptions.RequestException as e:
                    print(f"{Fore.LIGHTRED_EX}Request failed: {e}")

    except FileNotFoundError:
        print(f"{Fore.LIGHTRED_EX}Payload file not found.")

    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}An error occurred: {e}")

system("cls||clear")

print(r"""
 _______  _______  _       _________ _       _________
(  ____ \(  ___  )( \      \__   __/( (    /|\__    _/
| (    \/| (   ) || (         ) (   |  \  ( |   )  (  
| (_____ | |   | || |         | |   |   \ | |   |  |  
(_____  )| |   | || |         | |   | (\ \) |   |  |  
      ) || | /\| || |         | |   | | \   |   |  |  
/\____) || (_\ \ || (____/\___) (___| )  \  ||\_)  )  
\_______)(____\/_)(_______/\_______/|/    )_)(____/   
                                          by:gupcoteles
""", end="\n")

print(f"{Fore.LIGHTCYAN_EX}1-) For url\n2-) For post\nq-) Quit\n")
process = input(">")
print("\n")

try:
    if process == "1":
        targetUrl = input(Fore.LIGHTYELLOW_EX + "Enter the target URL (e.g., http://example.com/page?id=): ")
        sqlInjectionUrl(targetUrl)

    elif process == "2":
        targetUrl = input(Fore.LIGHTYELLOW_EX + "Enter the target URL (e.g., http://example.com): ")
        targetParam = input(Fore.LIGHTYELLOW_EX + "Param name to be tested within the site (e.g., username): ")
        sqlInjPost(targetUrl, targetParam)

    elif process.lower() == "q":
        quit()

    else:
        system("cls||clear")
        print(f"{Fore.LIGHTRED_EX}Enter a valid transaction")
        time.sleep(3)

except Exception as e:
    print(f"error: {e}")