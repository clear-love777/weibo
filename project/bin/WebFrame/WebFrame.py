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
import urllib
from urllib import request
import requests
from time import sleep
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
        request=conn.recv(1024).decode("utf-8")
        # request=urllib.request.unquote(conn.recv(1024).decode("utf-8"))
        if not request:
            return
        request=json.loads(request)
        if request["method"]=="GET":
            print(request)
            # request_change="http://176.215.133.52:8080" + request["info"]
            if request["info"]=="/" or request["info"][-5:]==".html":
                response=self.get_html(request["info"])
            else:
                try:
                    info = re.search(r"/.+\?", request["info"]).group().rstrip("?")
                except:
                    info=False
                if info:
                    post = re.search(r"\?.+", request["info"]).group().lstrip("?").split("&")
                    post_dict={}
                    for i,item  in enumerate(post):
                        try:
                            key=re.search(r".+=",item).group().rstrip("=")
                            value=re.search(r"=.+",item).group().lstrip("=")
                            post_dict[key]=value
                        except:
                            post_dict[key]=key+("=")+""
                            continue
                    # a=post_dict["file"].split("=")[1]
                    if not post_dict and info=="/login":
                        info="/"
                    response = self.get_data(info, post_dict)
                else:
                    response = self.get_data(request["info"],None)

        elif request["method"]=="POST":
            print(request)
            if request["info"]=="/" or request["info"][-5:]==".html":
                response=self.get_html(request["info"])
            else:
                response=self.get_data(request["info"],None)
        try:
            response = json.dumps(response)
            conn.send(response.encode())
        except Exception as e:
            print(e)
            response={"status":"404","data":open(STATIC_DIR+"/404.html").read()}
            response = json.dumps(response)
            conn.send(response.encode())
        conn.close()
    def get_html(self, info):
        # print(info)
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
    def get_data(self,info,post):
        print(info)
        print(post)
        if post:
            for k,v in post.items():
                    post[k]=urllib.request.unquote(v)
        for url,func in urls:
            if info==url:
                if post:
                    try:
                        list_post_key=[]
                        list_post_value=[]
                        for k,v in post.items():
                            if not v:
                                list_post_key.append("#")
                                continue
                            list_post_key.append(k)
                            if k!="submit":
                                try:
                                    list_post_value.append(v.split("=")[1])
                                except:
                                    list_post_value.append(v.split("=")[0])
                        # print(list_post_key)
                        # print(list_post_value)
                        if "submit" in list_post_key:
                            if post["submit"]=="login":
                                if len(list_post_key)==3:
                                    # return {"status":"200","data":func(post["username"],post["password"])}
                                    return {"status":"200","data":func(list_post_value)}
                                else:
                                    return {"status": "200", "data": func(None, None)}
                            elif post["submit"]=="regis":
                                return {"status":"200","data":func()}
                            elif post["submit"]=="regis_submit":
                                # return {"status": "200", "data": func(post["name"],post["password"])}
                                return {"status": "200", "data": func(list_post_value)}
                            elif post["submit"]=="exit":
                                return {"status":"200","data":func()}
                    except Exception as e:
                        print(e)
                        return {"status":"404","data":open(STATIC_DIR+"/404.html").read()}
                if info!="/login":
                    return {"status": "200", "data": func()}
        return {"status":"404","data":open(STATIC_DIR+"/404.html").read()}
if __name__ == '__main__':
    app=Application()
    app.start()#启动服务