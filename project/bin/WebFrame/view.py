from project.bin.WebFrame.settings import *
def show_time():
    import time
    return time.ctime()
def ai():
    return "what is ai"
def bye():
    return "Good bye"
def img_author_main1():
    # with open("./static/img/author-main1.jpg","rb") as f:
    # file_path=STATIC_DIR+"/img/"+"author-main1.jpg"
    # return "<img src=\"%s\">"%file_path
    return "<img src=\"img/author-main1.jpg\">"