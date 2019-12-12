# import pymysql
# import os
# import json
# from project.bin.WebFrame.settings import *
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
# from flask import Flask, request
#
# app = Flask(__name__)
#
#
# @app.route('/index1', methods=['POST'])
# def getcontent():
#     conn = pymysql.connect(host=sql_host,
#                            port=sql_port,
#                            user=sql_user,
#                            password=sql_password,
#                            database=sql_database,
#                            charset=sql_charset)
#     cur = conn.cursor()
#     sql = "select * from Users;"
#     cur.execute(sql)
#     data = cur.fetchall()
#     # print(data)
#     para = []
#     for i in data:
#         # print(i)
#         text={"id":i[0],"username":i[1],"password":i[2]}
#         para.append(text)
#     return json.dumps(para, ensure_ascii=False, indent=4)
#
#
# if __name__ == '__main__':
#     app.run(host='176.215.133.52', port=4444)
#     print(getcontent())