from socket import *

# 创建socket对象
serverSocket = socket(AF_INET, SOCK_STREAM)
# 将TCP欢迎套接字绑定到指定端口
serverSocket.bind(('', 6789))
# 最大连接数为1
serverSocket.listen(1)

while True:
    # 被动接受TCP客户端连接，（阻塞式）等待连接的到来
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        # 获取客户发送的报文
        message = connectionSocket.recv(1024)

        print(message)

        # 获取请求的文件名
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        # 发送HTTP 200 响应头
        header = ' HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (
            len(outputdata))
        connectionSocket.send(header.encode())

        # 发送HTTP响应正文
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        # 发送HTTP响应404报文
        header = ' HTTP/1.1 404 Found'
        connectionSocket.send(header.encode())

        # 关闭socket客户端连接
        connectionSocket.close()
