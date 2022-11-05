import pyfiglet
from colorama import init, Fore, Style
from time import sleep
import requests

init()

session = requests.session()

print(Fore.RED + Style.BRIGHT + " ")

info = print(">> Reports must be more than followers! ")

info1 = print(">> You need to have a good WiFi for the reporter to run faster! ")

print("")

sleep(0.05)

print(Fore.YELLOW + Style.BRIGHT + " ")

result = pyfiglet.figlet_format("Tiktok Mass Report Tool")

print(result)

print(Fore.BLUE + Style.BRIGHT + " ")

reports = 1

sleep(0.5)
url = input("Please enter your Inspect Element URL here >> ")
while True:   
    r = requests.get(url)
    print(Fore.GREEN + Style.BRIGHT + f">> Succesfully sended {reports} reports")
    reports += 1
else:
    print(Fore.RED + Style.BRIGHT + "Website down on your IP. Change your IP-Address.")