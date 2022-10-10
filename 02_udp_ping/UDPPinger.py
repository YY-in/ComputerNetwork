from http import server
from socket import *

import time

# 服务器地址 
serverName = 'localhost'
# 服务器端口
serverPort = 12000
# 创建UDP套接字，使用IPv4协议
clientSocket = socket(AF_INET, SOCK_DGRAM)
# 设置超时时间为1秒 
clientSocket.settimeout(1)


# 发送10个数据包
for i in range(10):
    # 发送时间 
    sendTime = time.time()
    # 发送数据包，编码为bytes以便发送 
    clientSocket.sendto(('Ping %d %s' % (i, sendTime)).encode(), (serverName, serverPort))
    try:
        # 接收数据包 
        message, serverAddress = clientSocket.recvfrom(1024)
        # 接收时间 
        receiveTime = time.time()
        # 打印从服务器接收的信息，以及往返时间RTT 
        print('Message: %s, RTT: %.3f' % (message.decode(), receiveTime - sendTime))
    except timeout:
        # 打印超时 
        print('Request timed out')