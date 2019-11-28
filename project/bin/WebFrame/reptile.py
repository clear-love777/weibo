import urllib.request
import urllib.parse
import re
def movieSpider():
    """
        模拟Ajax请求
    """


    url = "http://176.215.133.52:8080"
    # url = "http://www.baidu.com/img/bd_logo1.png"


    header = {"User-Agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.7.62 Version/11.01"}

    formData = {
        "type": "11",
        "interval_id": "100:90",
        "action": "",
        "start": "0",
        "limit": "20"
    }

    # 将str类型转换为bytes类型
    data = urllib.parse.urlencode(formData).encode("utf-8")

    request = urllib.request.Request(url, data=data, headers=header)

    return urllib.request.urlopen(request).read()


if __name__ == "__main__":
    s=movieSpider()
    print(s)