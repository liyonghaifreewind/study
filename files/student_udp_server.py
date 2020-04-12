# coding=utf-8
"""
    练习：从客户端输入学生的id，姓名，年龄，分数
    将其发送到服务端，由服务器写入到一个文件中
    每个信息占一行，由udp完成
    服务器端
"""

import struct
from socket import *

st = struct.Struct("i32sif")
# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)
# 绑定地址
sockfd.bind(("0.0.0.0", 8000))

# 收发消息
while True:
    data, addr = sockfd.recvfrom(1024)
    if not data:
        break
    print(addr)
    sockfd.sendto(b'Yes!', addr)
    data = st.unpack(data)
    info = "%d %s %d %.2f\n" % (data[0], data[1].decode(), data[2], data[3])
    with open("student_msg.txt", mode='a+', encoding='utf-8') as fd:
        fd.write(info)
    print("写入成功...")

sockfd.close()
