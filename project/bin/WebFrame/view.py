from project.bin.WebFrame.settings import *
from project.bin.WebFrame.sql import *
sql=sql()
def show_time():
    import time
    return time.ctime()
def ai():
    return "what is ai"
def bye():
    return "Good bye"
def login(name="root",pwd="123456"):
    if sql.login(name,pwd):
        with open(STATIC_DIR+"/mobile-index.html") as f:
            return f.read()
    else:
        with open(STATIC_DIR+"/login.html") as f:
            return f.read()
def register():
    with open(STATIC_DIR + "/register.html") as f:
            return f.read()