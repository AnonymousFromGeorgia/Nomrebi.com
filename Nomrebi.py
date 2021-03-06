#!/usr/bin/env python3

import os
os.system('clear')

import pyfiglet 
  
result = pyfiglet.figlet_format("Nomrebi.com") 
print(result)

import signal

def keyboardInterruptHandler(signal, frame):
    print("\nპროგრამა გაითიშა.".format(signal))
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

print("Nomrebi.com პარსერი")
print("---------------------------------------------------")
print("https://github.com/AnonymousFromGeorgia/Nomrebi.com")
print("---------------------------------------------------")

import requests
import re
params = {'number' : input("შეიყვანეთ მობილურის ნომერი: ")}

var = requests.post('https://simpleapi.info/apps/numbers-info/info.php?results=json', data = params)
found = re.search('"items":\[(.+?)\]', var.text).group(1)
print("--------------------------------------------------")
print(found)
print("--------------------------------------------------")
print("პროგრამის ავტორი: გიო რგი")
print("--------------------------------------------------")
print("YouTube - https://youtube.com/AnonymousFromGeorgia")
print("--------------------------------------------------")
print("Github - https://github.com/AnonymousFromGeorgia")
print("--------------------------------------------------")
print("Facebook - https://facebook.com/anonimaluri")
print("--------------------------------------------------")
print("Twitter - https://twitter.com/anonimaluri")
print("--------------------------------------------------")
print("ანონიმუსი საქართველოდან - Anonymous From Georgia")
print("--------------------------------------------------")
