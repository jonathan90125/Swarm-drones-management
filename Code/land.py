import threading  # 导入线程模块
import socket  # 导入套接字模块
import sys  # 导入系统模块（其实没用到）
import time  # 导入时间模块

# 设置主机及端口号
host = ''
port = 8889
locaddr = (host, port)

# 创建UDP的socket通信
# 获取Udp/Ip套接字（socket就是套接字）
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 第一个参数为socket家族：有AF_UNIX基于文件类型，及AF_INET基于网络类型
# 第二个参数为socket_type：流套接字类型为SOCK_STREAM、数据报套接字类型为SOCK_DGRAM（datagram）、原始套接字SOCK_RAW

tello_address = ('192.168.10.1', 8889)  # 设置tello主机及端口号

sock.bind(locaddr)  # 绑定（主机，端口号）到套接字


# 定义数据接收函数（从Tello EDU返回的信息）
def recv():
    global flag  # 接收线程用来告诉发送线程是否检测到挑战卡的全局变量
    flag = 0  # 初始值设为0
    while True:
        try:
            data, server = sock.recvfrom(1518)  # 接收UDP数据；data为接收的数据，server为客户地址，1518为每次接收字节数
            print(data.decode(encoding="utf-8"))  # 输出从socket接收的数据，并以编码为"utf-8"；
            if data.decode(encoding="utf-8") == "error No valid marker":  # 没有检测到
                flag = 1  # 赋值为1，表示没有检测到
                print("not found")
            else:  # 检测到了
                flag = 0
        except Exception:
            print('\nExit . . .\n')
            break


print("START")

# 启动多线程
recvThread = threading.Thread(target=recv)  # 通过Thread类进行对象实例化为recvThread；
recvThread.start()  # 启动多线程

while True:

    msg = "command"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address)  # 发送UDP数据
    time.sleep(1)
    msg = "mon"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address)  # 发送UDP数据
    time.sleep(1)
    msg = "mdirection 0"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address)  # 发送UDP数据
    time.sleep(1)

    msg = "takeoff"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address)  # 发送UDP数据
    time.sleep(10)

    for num in range(0, 10):  # 设置最大平移次数
        msg = "go 0 0 50 20 m2"  # 检测
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据
        time.sleep(5)

        if flag == 0:
            msg = "land"  # 检测到挑战卡，降落
            msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
            sock.sendto(msg, tello_address)  # 发送UDP数据
            print("we found it!!!!!!!!!")
            time.sleep(1000)
        else:
            msg = "left 30"  # 平移
            msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
            sock.sendto(msg, tello_address)  # 发送UDP数据
            time.sleep(5)

    # 到达最大平移距离，仍然没有检测到，强制降落
    msg = "land"  # 输入指令
    msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
    sock.sendto(msg, tello_address)  # 发送UDP数据
    time.sleep(1000)
