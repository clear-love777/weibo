import json
import urllib.parse
import urllib.request as urllib2
import requests
import pickle

def post(server_url, params):
    data = urllib.parse.urlencode(params)
    request = urllib2.Request(server_url, data)
    return json.loads(urllib2.urlopen(request, timeout=10).read())


if __name__ == "__main__":
    # 图片的URL
    image_url = "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2637851855,2992656155&fm=200&gp=0.jpg"
    # http服务的URL
    url = "http://10.10.20.20:6060/image?"
    print(post(url, {"image_url": image_url}))