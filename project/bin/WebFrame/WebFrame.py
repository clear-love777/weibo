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
from urllib import request
import requests


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
        if request["method"]=="GET":
            print(request)
            # print(request["info"])
            if request["info"]=="/" or request["info"][-5:]==".html":
                response=self.get_html(request["info"])
            else:
                info = re.search(r"/.+\?", request["info"]).group().rstrip("?")
                self.post = re.search(r"\?.+", request["info"]).group().lstrip("?").split("&")
                response = self.get_data(info)
                # response=self.get_data(request["info"])

        elif request["method"]=="POST":
            print(request)
            if request["info"]=="/" or request["info"][-5:]==".html":
                response=self.get_html(request["info"])
            else:
                # info=re.search(r"/.+\?", request["info"]).group().rstrip("?")
                # post=re.search(r"\?.+",request["info"]).group().lstrip("?").split("&")
                # print(post)
                # response=self.get_data(info)
                response=self.get_data(request["info"])
        response = json.dumps(response)
        conn.send(response.encode())
        conn.close()
    def get_html(self, info):
        if info=="/":
            filename=STATIC_DIR+"/login.html"
        else:
            filename=STATIC_DIR+info
        try:
            fd=open(filename)
        except:
            return {"status":"404","data":open("/home/tarena/save/project/bin/WebFrame/static/404.html").read()}
        else:
            return {"status":"200","data":fd.read()}
    def get_data(self,info):
        for url,func in urls:
            if info==url:
                try:
                    return {"status":"200","data":func()}
                except:
                    return {"status":"500","data":open(STATIC_DIR+"/500.html").read()}

        return {"status":"404","data":open(STATIC_DIR+"/404.html").read()}
if __name__ == '__main__':
    app=Application()
    app.start()#启动服务