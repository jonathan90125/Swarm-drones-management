import socket  # 导入套接字模块
import time  # 导入时间模块
import threading  # 导入线程模块
import easygui

# 设置主机及端口号
host = ''
port = 8889
locaddr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = ''
port = 9000
locaddr2 = (host, port)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = ''
port = 9001
locaddr3 = (host, port)
sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = ''
port = 9002
locaddr4 = (host, port)
sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.3.9', 8889)  # 设置tello主机及端口号
tello_address2 = ('192.168.3.10', 8889)
tello_address3 = ('192.168.3.11', 8889)
tello_address4 = ('192.168.3.12', 8889)

sock.bind(locaddr)  # 绑定（主机，端口号）到套接字
sock2.bind(locaddr2)  # 绑定（主机，端口号）到套接字
sock3.bind(locaddr3)  # 绑定（主机，端口号）到套接字
sock4.bind(locaddr4)  # 绑定（主机，端口号）到套接字

def button():
    global flag
    flag = 0
    while True:
        # Send data
        # 设置easyGUI界面，并将指令设置为button，将点击后的字符串赋值给变量“send”
        send = easygui.buttonbox(msg="Please click command first to control", title="Tello control Demo",
                                 choices=("command", "takeoff",  "land"))
        if send == "takeoff":
            flag = 1
        if send == "land":
            flag = 0
        print(send)  # 打印输出“send”
        print(flag)
        sock.sendto(send.encode(encoding="utf-8"), tello_address)  # 发送send指令给Tello EDU
        sock2.sendto(send.encode(encoding="utf-8"), tello_address2)  # 发送send指令给Tello EDU
        sock3.sendto(send.encode(encoding="utf-8"), tello_address3)  # 发送send指令给Tello EDU
        sock4.sendto(send.encode(encoding="utf-8"), tello_address4)  # 发送send指令给Tello EDU
        time.sleep(1)


print("start")

# 启动多线程
bThread = threading.Thread(target=button)  # 通过Thread类进行对象实例化为recvThread；
bThread.start()  # 启动多线程

while True:
    if flag == 0:
        continue
    else:
        # msg = "command"  # 输入指令
        # msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        # sock.sendto(msg, tello_address)  # 发送UDP数据
        # sock2.sendto(msg, tello_address2)  # 发送UDP数据
        # sock3.sendto(msg, tello_address3)  # 发送UDP数据
        # sock4.sendto(msg, tello_address4)  # 发送UDP数据
        # time.sleep(1)

        msg = "mon"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        sock2.sendto(msg, tello_address2)  # 发送UDP数据
        sock3.sendto(msg, tello_address3)  # 发送UDP数据
        sock4.sendto(msg, tello_address4)  # 发送UDP数据
        time.sleep(1)

        msg = "mdirection 0"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        sock2.sendto(msg, tello_address2)  # 发送UDP数据
        sock3.sendto(msg, tello_address3)  # 发送UDP数据
        sock4.sendto(msg, tello_address4)  # 发送UDP数据
        time.sleep(1)

        # msg = "takeoff"  # 输入指令
        # msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        # sock.sendto(msg, tello_address)  # 发送UDP数据
        # sock2.sendto(msg, tello_address2)  # 发送UDP数据
        # sock3.sendto(msg, tello_address3)  # 发送UDP数据
        # sock4.sendto(msg, tello_address4)  # 发送UDP数据
        # time.sleep(8)

        msg = "go 0 0 100 20 m1"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        msg = "go 0 0 100 20 m2"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock2.sendto(msg, tello_address2)  # 发送UDP数据
        msg = "go 0 0 100 20 m3"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock3.sendto(msg, tello_address3)  # 发送UDP数据
        msg = "go 0 0 100 20 m4"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock4.sendto(msg, tello_address4)  # 发送UDP数据
        time.sleep(5)

        msg = "go 0 -50 100 20 m1"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        msg = "go -50 0 100 20 m2"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock2.sendto(msg, tello_address2)  # 发送UDP数据
        msg = "go 50 0 100 20 m3"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock3.sendto(msg, tello_address3)  # 发送UDP数据
        msg = "go 0 50 100 20 m4"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock4.sendto(msg, tello_address4)  # 发送UDP数据
        time.sleep(5)

        msg = "go 0 0 100 20 m5"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        msg = "go 0 0 100 20 m6"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock2.sendto(msg, tello_address2)  # 发送UDP数据
        msg = "go 0 0 100 20 m8"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock3.sendto(msg, tello_address3)  # 发送UDP数据
        msg = "go 0 0 100 20 m7"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock4.sendto(msg, tello_address4)  # 发送UDP数据
        time.sleep(5)

        msg = "go 0 -50 100 20 m5"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        msg = "go -50 0 100 20 m6"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock2.sendto(msg, tello_address2)  # 发送UDP数据
        msg = "go 50 0 100 20 m8"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock3.sendto(msg, tello_address3)  # 发送UDP数据
        msg = "go 0 50 100 20 m7"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock4.sendto(msg, tello_address4)  # 发送UDP数据
        time.sleep(5)

        msg = "go 0 0 100 20 m2"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        msg = "go 0 0 100 20 m4"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock2.sendto(msg, tello_address2)  # 发送UDP数据
        msg = "go 0 0 100 20 m1"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock3.sendto(msg, tello_address3)  # 发送UDP数据
        msg = "go 0 0 100 20 m3"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock4.sendto(msg, tello_address4)  # 发送UDP数据
        time.sleep(5)

        msg = "go -50 0 100 20 m2"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        msg = "go 0 50 100 20 m4"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock2.sendto(msg, tello_address2)  # 发送UDP数据
        msg = "go 0 -50 100 20 m1"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock3.sendto(msg, tello_address3)  # 发送UDP数据
        msg = "go 50 0 100 20 m3"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock4.sendto(msg, tello_address4)  # 发送UDP数据
        time.sleep(5)

        msg = "go 0 0 100 20 m6"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        msg = "go 0 0 100 20 m7"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock2.sendto(msg, tello_address2)  # 发送UDP数据
        msg = "go 0 0 100 20 m5"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock3.sendto(msg, tello_address3)  # 发送UDP数据
        msg = "go 0 0 100 20 m8"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock4.sendto(msg, tello_address4)  # 发送UDP数据
        time.sleep(5)

        msg = "go -50 0 100 20 m6"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        msg = "go 0 50 100 20 m7"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock2.sendto(msg, tello_address2)  # 发送UDP数据
        msg = "go 0 -50 100 20 m5"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock3.sendto(msg, tello_address3)  # 发送UDP数据
        msg = "go 50 0 100 20 m8"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock4.sendto(msg, tello_address4)  # 发送UDP数据
        time.sleep(5)

        msg = "go 0 0 100 20 m4"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        msg = "go 0 0 100 20 m3"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock2.sendto(msg, tello_address2)  # 发送UDP数据
        msg = "go 0 0 100 20 m2"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock3.sendto(msg, tello_address3)  # 发送UDP数据
        msg = "go 0 0 100 20 m1"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock4.sendto(msg, tello_address4)  # 发送UDP数据
        time.sleep(5)

        msg = "cw 360"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        sock2.sendto(msg, tello_address2)  # 发送UDP数据
        sock3.sendto(msg, tello_address3)  # 发送UDP数据
        sock4.sendto(msg, tello_address4)  # 发送UDP数据
        time.sleep(5)

        msg = "go 0 0 100 20 m4"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        msg = "go 0 0 100 20 m3"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock2.sendto(msg, tello_address2)  # 发送UDP数据
        msg = "go 0 0 100 20 m2"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock3.sendto(msg, tello_address3)  # 发送UDP数据
        msg = "go 0 0 100 20 m1"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock4.sendto(msg, tello_address4)  # 发送UDP数据
        time.sleep(5)

        msg = "flip r"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        sock2.sendto(msg, tello_address2)  # 发送UDP数据
        sock3.sendto(msg, tello_address3)  # 发送UDP数据
        sock4.sendto(msg, tello_address4)  # 发送UDP数据
        time.sleep(5)

        msg = "flip l"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        sock2.sendto(msg, tello_address2)  # 发送UDP数据
        sock3.sendto(msg, tello_address3)  # 发送UDP数据
        sock4.sendto(msg, tello_address4)  # 发送UDP数据
        time.sleep(5)

        msg = "go 0 0 100 20 m4"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        msg = "go 0 0 100 20 m3"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock2.sendto(msg, tello_address2)  # 发送UDP数据
        msg = "go 0 0 100 20 m2"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock3.sendto(msg, tello_address3)  # 发送UDP数据
        msg = "go 0 0 100 20 m1"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock4.sendto(msg, tello_address4)  # 发送UDP数据
        time.sleep(5)



        msg = "land"  # 输入指令
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        sock2.sendto(msg, tello_address2)  # 发送UDP数据
        sock3.sendto(msg, tello_address3)  # 发送UDP数据
        sock4.sendto(msg, tello_address4)  # 发送UDP数据
        time.sleep(5)
        flag=0
