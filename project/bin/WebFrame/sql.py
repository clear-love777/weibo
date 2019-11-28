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
        sql = "select username,password from user where username=%s and password=%s;"
        self.cur.execute(sql, [list[0], list[1]])
        r = self.cur.fetchone()
        if r:
            return True
        else:
            return False
    # def regis(self,name,pwd,sex,portrait,idiograph,*args):
    def regis(self,list):
        sql="select * from user where username=%s"
        # self.cur.execute(sql,name)
        self.cur.execute(sql,list[0])
        r=self.cur.fetchone()
        print(list)
        if r:
            return False
        else:
            if not list[3] and list[4]:
                print("d")
                sql="insert into user(username,password,sex,idiograph) values(%s,%s,%s,%s)"
                r = self.cur.execute(sql, [list[0], list[1], list[2], list[4]])
            elif not list[4] and list[3]:
                print("a")
                sql="insert into user(username,password,sex,portrait) values(%s,%s,%s,%s)"
                r = self.cur.execute(sql, [list[0], list[1], list[2], list[3]])
            elif not list[3] and not list[4]:
                print("c")
                sql="insert into user(username,password,sex) values(%s,%s,%s)"
                r = self.cur.execute(sql, [list[0], list[1], list[2]])
            else:
                print("b")
                sql="insert into user(username,password,sex,portrait,idiograph) values(%s,%s,%s,%s,%s)"
                r=self.cur.execute(sql,[list[0],list[1],list[2],list[3],list[4]])
            if r>0:
                self.db.commit()
                return True
            else:
                self.db.rollback()
                return False