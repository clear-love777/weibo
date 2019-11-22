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
print(STATIC_DIR)
