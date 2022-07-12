import threading  # 导入线程模块
import socket  # 导入套接字模块

# 设置主机及端口号,这是有关我们自己的电脑的
host = ''
port = 8889
locaddr = (host, port)

# 创建UDP的socket通信
# 获取Udp/Ip套接字（socket就是套接字）
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 第一个参数为socket家族：有AF_UNIX基于文件类型，及AF_INET基于网络类型
# 第二个参数为socket_type：流套接字类型为SOCK_STREAM、数据报套接字类型为SOCK_DGRAM（datagram）、原始套接字SOCK_RAW

tello_address = ('192.168.3.11', 8889)  # 设置tello主机及端口号
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
    try:  # 使用异常
        msg = input("")  # 输入指令

        if not msg:
            break  # 如果没有指令则退出

        if 'end' in msg:
            print('...')
            sock.close()  # 关闭套接字
            break

        # Send data
        msg = msg.encode(encoding="utf-8")  # 对要发送的信息进行编码
        sock.sendto(msg, tello_address)  # 发送UDP数据

    except KeyboardInterrupt:
        print('\n . . .\n')
        sock.close()  # 关闭套接字
        break
