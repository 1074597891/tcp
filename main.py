import socket

import fy_api

# 创建一个socket对象
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.3"
port = 8888
# 绑定地址
socket_server.bind((host, port))
# 设置监听
socket_server.listen(5)
# socket_server.accept()返回一个元组, 元素1为客户端的socket对象, 元素2为客户端的地址(ip地址，端口号)
client_socket, address = socket_server.accept()

# while循环是为了让对话持续
while True:
    # msg = input("发送: ")
    # 发送数据，需要进行编码
    msg = fy_api.fy()
    client_socket.send(msg.encode("UTF-8"))
# 关闭服务器端
socket_server.close()
