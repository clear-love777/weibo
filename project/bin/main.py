import project.bin.HTTPServer.http_server as hs
import project.bin.WebFrame.WebFrame as wf
from multiprocessing import *
if __name__ == '__main__':
    http=hs.HTTPServer()
    web=wf.Application()
    ph=Process(target=http.serve_forever)
    pw=Process(target=web.start)
    ph.start()
    pw.start()