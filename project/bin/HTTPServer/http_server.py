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
from project.bin.HTTPServer.config import *
from select import *
import sys
import re
import json
from time import sleep
from threading import Thread
from project.bin.HTTPServer.re_get import *
import os
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
    datas=[]
    data_result=""
    while True:
        data=sock.recv(1024*1024).decode()
        if not data:
            break
        datas.append(data)
    if datas:
        for i in datas:
            data_result+=i
    else:
        return
    if data_result:
        try:
            return json.loads(data_result) #返回一个字典
        except json.decoder.JSONDecodeError:
            return

#封装htto类
class HTTPServer:
    def __init__(self):
        self.address=(HOST,PORT)
        self.sock=self.create_socket()
    def serve_forever(self):
        self.sock.listen(3)
        print("你启动了http服务,监听%s端口" % PORT)
        while True:
            try:
                conn,addr=self.sock.accept()
                # print("Connect from", addr)
            except KeyboardInterrupt:
                self.sock.close()
                sys.exit("httpServer关闭")
            except Exception as e:
                print(e)
                continue
            else:
                t = Thread(target=self.handle, args=(conn,))
                t.setDaemon(True)
                t.start()

    def handle(self, conn):
        try:
            pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"
            request = conn.recv(4096).decode()
            try:
                env = re.match(pattern, request).groupdict()
                data = serve(env)
                print(data)
                if data:
                    self.response(conn, data)
                return request
            except:
                conn.close()
                return
            # if env["info"]=="/":
            #     data = serve(env)
            #     if data:
            #         self.response(conn, data)
            #     return request
            # else:
            #     re_request=re.match(r"GET /.+ HTTP/1.1",request).group().replace("GET /","").replace(" HTTP/1.1","")
            #     # print(re_request)
            #     re_request=res(re_request)
            #     # print(re_request)
        except OSError:
            return
        # if re_request == "html":
        #     data=serve(env)
        #     print(data)
        #     if data:
        #         self.response(conn,data)
        #     return request

    #创建套接字
    def create_socket(self):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        sock.bind(self.address)
        return sock

    #组织http响应给浏览器发送
    def response(self, conn, data):
        # print(data)
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
    httpd=HTTPServer()
    httpd.serve_forever()#启动服务