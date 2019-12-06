import pymysql
import hashlib
from project.bin.WebFrame.settings import *
class sql:
    # 　密码转换函数
    @classmethod
    def change_passwd(self, passwd):
        salt = '*#06#'
        hash = hashlib.md5(salt.encode())  # 生成加密对象
        hash.update(passwd.encode())  # 算法加密处理
        passwd = hash.hexdigest()  # 获取加密后的字串
        return passwd
    def __init__(self):
        self.db = pymysql.connect(host=sql_host,
                                  port=sql_port,
                                  user=sql_user,
                                  password=sql_password,
                                  database=sql_database,
                                  charset=sql_charset)
        self.cur = self.create_cur()

    def create_cur(self):
        return self.db.cursor()

    def close(self):
        if self.cur:
            self.cur.close()
        self.db.close()

    def login(self,list):
        # 和数据库信息进行比对
        sql = "select * from Users where user_name=%s and user_password=%s;"
        self.cur.execute(sql, [list[0], list[1]])
        r = self.cur.fetchone()
        if r:
            return True
        else:
            return False
    def regis(self,list):
        sql="select * from Users where user_name=%s"
        self.cur.execute(sql,list[0])
        r=self.cur.fetchone()
        # print(list)
        if r:
            return False
        else:
            sql_Users="insert into Users(user_name,user_password,user_register_time) values(%s,%s,now());"
            sql_Userinfo="insert into Userinfo(userinfo_uid,userinfo_sex,userinfo_email,userinfo_addr," \
                         "userinfo_birthday,userinfo_img,userinfo_intro) " \
                         "values(%s,%s,%s,%s,%s,%s,%s);"
            r_user=self.cur.execute(sql_Users,[list[0], list[1]])
            if r_user>0:
                self.db.commit()
                sql_getid = "select user_id from Users order by user_id desc limit 1"
                self.cur.execute(sql_getid)
                user_id = self.cur.fetchone()[0]
                r_userinfo = self.cur.execute(sql_Userinfo,
                                              [user_id, list[2], list[3], list[4], list[5], list[6], list[7]])
                if r_userinfo>0:

                    self.db.commit()
                    return True
                else:
                    self.db.rollback()
                    return False
            else:
                self.db.rollback()
                return False