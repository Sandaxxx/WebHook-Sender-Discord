# problem ? add Sandax#3984

import requests
import os
import time
from os import system
import platform
from colorama import init
init()
from colorama import Fore, Back, Style

if platform.system == ("linux"):
   os.system("clear")
else:
  time.sleep(5)
  os.system("cls")


print(Fore.LIGHTBLUE_EX+'[#] Welcome to Webhook Sender developped by Sandax\n')
print("")
print("")
input(Fore.YELLOW+'[>] Press to continue...')

os.system('cls')

print("")
a = input(Fore.MAGENTA+'[+] Enter '+Fore.YELLOW+'Webhook : ')
# b = input('Enter Avatar [url] : ')
c = input(Fore.MAGENTA+'[+] Enter '+Fore.YELLOW+'Username : ')

def webhook():
    while True:
        try:
            webhook = (a)
            os.system('cls')
            avatar = 'LINK IMAGE' 
            username = (c)
            message = input(Fore.YELLOW+"[>] Message : ")
            data = requests.post(webhook, json={'content': message, 'avatar_url': avatar, "username": username})


            if data.status_code == 204:
                print(Fore.BLUE+'[Info] :'+Fore.GREEN+' Message has been sent successfully.')
                time.sleep(0.05)
                os.system('cls')
                continue
            else:
                data = requests.post(webhook, json={'content': message, "username": username})
                if data.status_code == 204:
                 print('\n' 'Sent : ' + message)
                 print('To : ' + a, '\n')
                 continue
                else:
                    print("\n[X]Error Syntaxe/WebHook deleted\n-> " + webhook)
                    break
            print("\nError Syntaxe/WebHook deleted\n-> " + webhook)
        except:
            print('\n Cannot connect to the webhook.')
            break


webhook()
