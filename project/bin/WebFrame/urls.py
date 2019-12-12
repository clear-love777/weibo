from project.bin.WebFrame.view import *
#路由列表
urls=[
    ("/time",show_time),
    ("/ai",ai),
    ("/bye",bye),
    ("/",index),
    ("/login",login),
    ("/regis",register),
    ("/regis_submit",register_submit),
    ("/exit",exit),
    ("/dict",dicts)
]