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
from project.bin.WebFrame.pro03 import *

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
                    # print(request["info"])
                    info = re.search(r"/.+\?", request["info"]).group().rstrip("?")
                except AttributeError:
                    # print(request["info"])
                    info=request["info"]
                    # info=re.search(r"/?",request["info"]).group()
                except Exception as e:
                    print(e)
                    info=False
                if info:
                    # try:
                    try:
                        jsonp = re.search(r"/\?callback=.+", request["info"]).group().lstrip("/?callback=")
                    except:
                        pass
                    try:
                        if not re.search(r"/\?callback",info):

                            post = re.search(r"\?.+", request["info"]).group().lstrip("?").split("&")
                        else:

                            post=re.search(r"/\?",info).group().rstrip("?")
                    except Exception as e:
                        # print("jjjjjj",e)
                        post={}
                    post_dict={}
                    for i,item  in enumerate(post):
                        if item:
                            try:
                                key=re.search(r".+=",item).group().rstrip("=")
                                value=re.search(r"=.+",item).group().lstrip("=")
                                post_dict[key]=value
                            except:
                                try:
                                    post_dict[key]=key+("=")+""
                                    continue
                                except:
                                    break
                        else:
                            break
                    # print(post_dict)
                    # print(info)
                    # print(jsonp)
                    # a=post_dict["file"].split("=")[1]
                    if not post_dict and info=="/login":
                        info="/"
                        # print(request["info"])
                    try:
                        re.search(r"/\?callback=.+",request["info"]).group()
                        request["info"]=jsonp
                        response=self.get_ajax(post,jsonp)
                    except AttributeError as e:
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
            # response = "callback" + "("+response+")"
            print("response>>", response)
            conn.send(response.encode())
        except Exception as e:
            # print("xxxxxx",e)
            response={"status":"404","data":open(STATIC_DIR+"/404.html").read()}
            response = json.dumps(response)
            conn.send(response.encode())
        conn.close()
    def get_html(self, info):
        print(info)
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
        print("get_data_info:",info)
        print("get_data_post:",post)
        if post:
            for k,v in post.items():
                    post[k]=urllib.request.unquote(v)
        # print(post)
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
                                print("ss")
                                # return {"status": "200", "data": func(post["name"],post["password"])}
                                return {"status": "200", "data": func(list_post_value)}
                            elif post["submit"]=="exit":
                                return {"status":"200","data":func()}
                    except Exception as e:
                        return {"status":"404","data":open(STATIC_DIR+"/404.html").read()}
                else:
                    if info!="/login":
                        return {"status": "200", "data": func()}
                    else:
                        return {"status": "200", "data": func((None,None))}
        return {"status":"404","data":open(STATIC_DIR+"/404.html").read()}

    def get_ajax(self, info, jsonp):
        print("get_ajax_info:",info)
        print("get_ajax_jsonp:",jsonp)
        for url,func in urls:
            # print(url,info)
            if info==url:
                return {"status":"200","data":"userHandler"+"("+self.getcontent()+")"}

    def getcontent(self):
        conn = pymysql.connect(host=sql_host,
                               port=sql_port,
                               user=sql_user,
                               password=sql_password,
                               database=sql_database,
                               charset=sql_charset)
        cur1 = conn.cursor()
        cur2 = conn.cursor()
        cur3 = conn.cursor()
        # sql = "select * from Users;"
        sql1 = "select u.user_id,u.user_name,i.userinfo_img from Users as u inner join Userinfo as i on " \
               "u.user_id=i.userinfo_uid;"
        cur1.execute(sql1)
        # sql2="select messages_info from Messages limit 1;"
        sql2="select messages_userid,messages_atid,messages_info from Messages;"
        sql3="select Users.user_id,Users.user_name,Userinfo.userinfo_img,Messages.messages_userid,\
                Messages.messages_atid,Messages.messages_info \
                from Users,Userinfo,Messages \
                where Users.user_id=Userinfo.userinfo_uid and Users.user_id=messages_userid;"
        cur3.execute(sql3)
        cur2.execute(sql2)
        data1 = cur1.fetchall()
        data2 = cur2.fetchall()
        data3=cur3.fetchall()
        # print(data2)
        para = []
        for i in data3:
            text={"id":i[0],"username": i[1], "img": i[2],"myid":i[3],"othersid":i[4],"message":i[5]}
            para.append(text)
        # for i in data1:
        #     # print(i)
        #     text = {"id": i[0], "username": i[1], "img": i[2],"message":data2}
        #     para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    app=Application()
    app.start()#启动服务