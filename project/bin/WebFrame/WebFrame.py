'''
WebFrame部分
从httpserver接收具体请求
根据请求进行逻辑处理和数据处理
将需要的数据反馈给httpserver
'''
from socket import *
import json
from project.bin.WebFrame.settings import *
from threading import Thread
from project.bin.WebFrame.urls import *
import sys
import os
import base64
import re
class Application:
    def __init__(self):
        self.sock=socket()
        self.sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.sock.bind((frame_ip,frame_port))
    def start(self):
        self.sock.listen(3)
        print("Running web server on %s"%frame_port)
        while True:
            try:
                conn,addr=self.sock.accept()
                print("Connect from", addr)
            except KeyboardInterrupt:
                self.sock.close()
                sys.exit("WebFrame关闭")
            t=Thread(target=self.handle,args=(conn,))
            t.setDaemon(True)
            t.start()

    def handle(self,conn):
        #接受请求
        request=conn.recv(1024).decode()
        if not request:
            return
        request=json.loads(request)
        print(request)
        if request["method"]=="GET":
            print(request["info"])
            if request["info"]=="/" or request["info"][-5:]==".html":
                response=self.get_html(request["info"])
            else:
                response=self.get_data(request["info"])
        elif request["method"]=="POST":
            pass
        # print(base64.b64decode(response["data"]))
        # print(response["data"])
        # response["data"] = base64.b64decode(response["data"])
        # a=base64.b64decode(response["data"])
        response=json.dumps(response)
        # str_byte=response.replace("\"status\": \"200\"","").replace("{\"data\": \"","").replace("\", }","").replace("{, \"data\": \"","").replace("\"}","")
        # head=str_byte[:10]
        # foot=str_byte[-10:]
        # head_index=response.find(head)
        # foot_index=response.find(foot)+10
        # response="{\"status\":\"200\",\"data\":".encode() + b"\"" + base64.b64decode(base64.b64encode(response["data"])) + b"\"}"
        # response="{\"status\":\"200\",\"data\":".encode() + b"\"" + base64.b64encode(response["data"]) + b"\"}"
        # response="{\"status\":\"200\",\"data\":".encode() + b"\"" + "哈哈哈".encode() + b"\"}"
        print(response)
        # response1=response.replace(response[head_index:foot_index],base64.b64decode(str_byte))
        # print(response1)
        # print(head,foot)
        # print(re.search(r"data\": \".+\"",response).group().replace("data\": ","").replace("\"",""))
        # print(base64.b64decode(response["data"]))
        # print(response["data"])
        # conn.send(response.encode())
        conn.send(response.encode())
        conn.close()
    def get_html(self, info):
        # print(info)
        if info=="/":
            filename=STATIC_DIR+"/login.html"
        else:
            filename=STATIC_DIR+info
        try:
            # print(filename)
            fd=open(filename)
            # print(fd)
        except:

            # return {"status":"404","data":open(STATIC_DIR+"/404.html").read()}
            return {"status":"404","data":open("/home/tarena/save/project/bin/WebFrame/static/404.html").read()}
        else:
            return {"status":"200","data":fd.read()}
    def get_data(self,info):
        for url,func in urls:
            if info==url:
                # print(type(base64.b64encode(func()).decode()))
                if TypeError:
                    return {"status":"200","data":func()}
                else:
                    return {"status":"200","data":func()}

        return {"status":"404","data":open(STATIC_DIR+"/404.html").read()}
if __name__ == '__main__':
    app=Application()
    app.start()#启动服务