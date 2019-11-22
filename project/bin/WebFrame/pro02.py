import base64
import json

def convert(image):
    f = open(image,'rb')
    img_raw_data = f.read()
    print(img_raw_data)
    # f.close()

    img_b64_string = base64.b64encode(img_raw_data)
    convert_img_raw_data = base64.b64decode(img_b64_string)
    return convert_img_raw_data
    # t = open("example.png", "w+")
    # t.write(convert_img_raw_data)
    # t.close()


if __name__ == "__main__":
    # convert("./static/img/author-main1.jpg")
    f=open("./static/img/author-main1.jpg","rb")
    # print(f.read())
    a=base64.b64decode(base64.b64encode(f.read()))
    print(type(a))
    # a=b"\""+convert("./static/img/author-main1.jpg")+b"\"}"
    # b="{\"status\":\"200\",\"data\":".encode()+b"\""+base64.b64decode(response["data"])+b"\"}"
    # c=b+a
    # print(c)
    # a={"status":"404","data":open("/home/tarena/save/project/bin/WebFrame/static/404.html").read()}
    # a=json.dumps(a)
    # print(a.encode())