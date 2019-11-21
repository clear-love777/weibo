'''
WebFrame部分
从httpserver接收具体请求
根据请求进行逻辑处理和数据处理
将需要的数据反馈给httpserver
'''
from socket import *
import json
from settings import *
from threading import Thread
from urls import *
class Application:
    def __init__(self):
        self.sock=socket()
        self.sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.sock.bind((frame_ip,frame_port))
    def start(self):
        self.sock.listen(3)
        print("Running web server on %s"%frame_port)
        while True:
            conn,addr=self.sock.accept()
            print("Connect from",addr)
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
            if request["info"]=="/" or request["info"][-5:]==".html":
                response=self.get_html(request["info"])
            else:
                response=self.get_data(request["info"])
        elif request["method"]=="POST":
            pass
        response=json.dumps(response)
        conn.send(response.encode())
        conn.close()
    def get_html(self, info):
        if info=="/":
            filename=STATIC_DIR+"/index.html"
        else:
            filename=STATIC_DIR+info
        try:
            fd=open(filename)
        except:
            print("哈哈哈哈")
            return {"status":"404","data":open(STATIC_DIR+"/404.html").read()}
        else:
            return {"status":"200","data":fd.read()}
    def get_data(self,info):
        for url,func in urls:
            if info==url:
                return {"status":"200","data":func()}
        return {"status":"404","data":open(STATIC_DIR+"/404.html").read()}
if __name__ == '__main__':
    app=Application()
    app.start()#启动服务