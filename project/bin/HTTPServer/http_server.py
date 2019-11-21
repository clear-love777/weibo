'''
http server部分的主体程序
功能:
获取http请求
解析http请求
将请求发送给WebFrame
从WebFrame接收反馈数据
将数据组织为Response格式发送给客户端
'''
from socket import *
from config import *
from select import *
import sys
import re
import json
from threading import Thread

def serve(env):
    sock=socket()
    try:
        sock.connect((frame_ip,frame_port))
    except:
        print("连接不到webfrom")
        return
    #发送字典("method":xxx,"info":...)
    data=json.dumps(env)
    sock.send(data.encode())
    #接受返回的数据
    data=sock.recv(1024*1024*10).decode()
    if data:
        # print(data)
        return json.loads(data) #返回一个字典

#封装htto类
class HTTPServer:
    def __init__(self,HOST="0.0.0.0",PORT=4396):
        self.host=HOST
        self.port=PORT
        self.address=(HOST,PORT)
        self.sock=self.create_socket()
        self.ep=epoll()
        self.fdmap={}
    def serve_forever(self):
        self.sock.listen(3)
        print("你启动了http服务,监听%s端口" % self.port)
        self.ep.register(self.sock,EPOLLIN)
        self.fdmap[self.sock.fileno()]=self.sock
        while True:
            try:
                events=self.ep.poll()
            except:
                self.sock.close()
                sys.exit("服务器关闭")
            for fd,event in events:
                if fd==self.sock.fileno():
                    conn,addr=self.fdmap[fd].accept()
                    print("Connect from", addr)
                    self.ep.register(conn,EPOLLIN)
                    self.fdmap[conn.fileno()]=conn
                elif event & EPOLLIN:
                    #浏览器发送了http请求
                    self.handle(self.fdmap[fd])
                    self.handle(self.fdmap[fd])
                    self.ep.unregister(fd)
                    del self.fdmap[fd]
                    # request = self.handle(self.fdmap[fd])
                    # if not request:
                    #     self.ep.unregister(fd)
                    #     del self.fdmap[fd]
                    #     continue
                    # self.request(self.fdmap[fd],data)
                    # break

    def handle(self, conn):
        try:
            request = conn.recv(4096).decode()
        except OSError:
            return
        # print(request)
        pattern=r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"
        try:
            env=re.match(pattern,request).groupdict()
        except:
            conn.close()
            return
        else:
            # print(env)
            data=serve(env)
            if data:
                self.response(conn,data)
        return request

    #创建套接字
    def create_socket(self):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        sock.bind(self.address)
        return sock

    def request(self, param, data):
        pass

    #组织http响应给浏览器发送
    def response(self, conn, data):
        if data["status"]=="200":
            responseHeaders="HTTP/1.1 200 OK\r\n"
            responseHeaders+="Content-Type:text/html\r\n"
            responseHeaders+="\r\n"
            responseBody=data["data"]
        elif data["status"]=="404":
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += "\r\n"
            responseBody = data["data"]
        response_data=responseHeaders+responseBody
        conn.send(response_data.encode())
if __name__ == '__main__':
    httpd=HTTPServer(HOST,PORT)
    httpd.serve_forever()#启动服务