import project.bin.HTTPServer.http_server as hs
import project.bin.WebFrame.WebFrame as wf
from multiprocessing import *
import signal
if __name__ == '__main__':
    http=hs.HTTPServer()
    web=wf.Application()
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    ph=Process(target=http.serve_forever)
    pw=Process(target=web.start)
    ph.start()
    pw.start()