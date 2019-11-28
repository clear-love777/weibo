from project.bin.WebFrame.sql import *
sql=sql()
def show_time(*args):
    import time
    return time.ctime()
def ai(*args):
    return "what is ai"
def bye(*args):
    return "Good bye"
def index(*args):
    with open(STATIC_DIR + "/login.html") as f:
        return f.read()
def login(list):
    if sql.login(list):
        with open(STATIC_DIR+"/mobile-index.html") as f:
            return f.read()
    else:
        with open(STATIC_DIR+"/login.html") as f:
            return f.read()
def register(*args):
    with open(STATIC_DIR + "/register.html") as f:
            return f.read()
# def register_submit(name,pwd,sex,portrait,idiograph,*args):
def register_submit(list):
    fs=open(STATIC_DIR + "/regis-success.html").read()
    ff=open(STATIC_DIR + "/regis-fail.html").read()
    if sql.regis(list):
        return fs
    else:
        return ff
def exit(*args):
    with open(STATIC_DIR + "/login.html") as f:
        return f.read()