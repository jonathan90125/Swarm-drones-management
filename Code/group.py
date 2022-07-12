import socket  # 导入套接字模块
import time  # 导入时间模块
import threading  # 导入线程模块

# 设置主机及端口号
host = ''
port = 8889
locaddr = (host, port)

# 创建UDP的socket通信
# 获取Udp/Ip套接字（socket就是套接字）
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 第一个参数为socket家族：有AF_UNIX基于文件类型，及AF_INET基于网络类型
# 第二个参数为socket_type：流套接字类型为SOCK_STREAM、数据报套接字类型为SOCK_DGRAM（datagram）、原始套接字SOCK_RAW

tello_address = ('192.168.3.9', 8889)  # 设置tello主机及端口号
tello_address2 = ('192.168.3.10', 8889)
tello_address3 = ('192.168.3.11', 8889)
tello_address4 = ('192.168.3.12', 8889)

sock.bind(locaddr)  # 绑定（主机，端口号）到套接字


# 定义数据接收函数（从Tello EDU返回的信息）
def recv():
    while True:
        try:
            data, server = sock.recvfrom(1518)  # 接收UDP数据；data为接收的数据，server为客户地址，1518为每次接收字节数
            print(data.decode(encoding="utf-8"))  # 输出从socket接收的数据，并以编码为"utf-8"；
        except Exception:
            print('\nExit . . .\n')
            break


print("start")

# 启动多线程
recvThread = threading.Thread(target=recv)  # 通过Thread类进行对象实例化为recvThread；
recvThread.start()  # 启动多线程

while True:

    msg = "command"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address)  # 发送UDP数据
    sock.sendto(msg, tello_address2)  # 发送UDP数据
    sock.sendto(msg, tello_address3)  # 发送UDP数据
    sock.sendto(msg, tello_address4)  # 发送UDP数据
    time.sleep(1)

    msg = "mon"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address)  # 发送UDP数据
    sock.sendto(msg, tello_address2)  # 发送UDP数据
    sock.sendto(msg, tello_address3)  # 发送UDP数据
    sock.sendto(msg, tello_address4)  # 发送UDP数据
    time.sleep(1)

    msg = "mdirection 0"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address)  # 发送UDP数据
    sock.sendto(msg, tello_address2)  # 发送UDP数据
    sock.sendto(msg, tello_address3)  # 发送UDP数据
    sock.sendto(msg, tello_address4)  # 发送UDP数据
    time.sleep(1)

    msg = "takeoff"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address)  # 发送UDP数据
    sock.sendto(msg, tello_address2)  # 发送UDP数据
    sock.sendto(msg, tello_address3)  # 发送UDP数据
    sock.sendto(msg, tello_address4)  # 发送UDP数据
    time.sleep(8)

    msg = "go 0 0 50 20 m1"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address)  # 发送UDP数据
    msg = "go 0 0 50 20 m2"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address2)  # 发送UDP数据
    msg = "go 0 0 50 20 m3"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address3)  # 发送UDP数据
    msg = "go 0 0 50 20 m4"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address4)  # 发送UDP数据
    time.sleep(8)

    msg = "go 0 -50 50 20 m1"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address)  # 发送UDP数据
    msg = "go -50 0 50 20 m2"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address2)  # 发送UDP数据
    msg = "go 50 0 50 20 m3"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address3)  # 发送UDP数据
    msg = "go 0 50 50 20 m4"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address4)  # 发送UDP数据
    time.sleep(8)

    msg = "go 0 0 50 20 m2"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address)  # 发送UDP数据
    msg = "go 0 0 50 20 m4"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address2)  # 发送UDP数据
    msg = "go 0 0 50 20 m1"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address3)  # 发送UDP数据
    msg = "go 0 0 50 20 m3"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address4)  # 发送UDP数据
    time.sleep(5)

    msg = "land"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address)  # 发送UDP数据
    sock.sendto(msg, tello_address2)  # 发送UDP数据
    sock.sendto(msg, tello_address3)  # 发送UDP数据
    sock.sendto(msg, tello_address4)  # 发送UDP数据
    time.sleep(1000)
