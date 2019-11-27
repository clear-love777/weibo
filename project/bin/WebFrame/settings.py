"""
模拟后端应用处理程序
"""
#设置应用服务地址
import os
frame_ip ="0.0.0.0"
frame_port =8000

#debug
DEBUG= True

#静态网页位置
STATIC_DIR=os.path.join(os.path.abspath(os.path.dirname(__file__)), "./static")

#请求地址
HTTP_HOST="http://127.0.0.1:8080"

#项目地址
Project_Path=os.getcwd().replace(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))),"")
Request_path=HTTP_HOST+Project_Path

#数据库配置
sql_host="176.215.133.52"
sql_port=3306
sql_user="root"
sql_password="123456"
sql_database="stu"
sql_charset="utf8"
