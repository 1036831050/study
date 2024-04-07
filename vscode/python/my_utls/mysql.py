# -*- coding = utf-8 -*-
# @Auther:lmd
# @Time    :2023/3/2--17:03
# @File    :mysql.py
# @Software:PyCharm
import pymysql
import json


class Mysql:
    def __init__(self, user, passwd, database="lmd", ip="192.168.1.107", port=3306):
        self.ip = ip
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database

    def connect(self, sql):
        db = pymysql.connect(host=self.ip, user=self.user, passwd=self.passwd,
                             database=self.database, port=self.port, charset='utf8')
        cur = db.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        db.close()
        return result


sql = "select * from mycount;"
db = Mysql("root", "lucian")
json_data: tuple = db.connect(sql)
json_list = []
# json_list = list(json_data[1])

for i in range(len(json_data)):
    json_list.append(list(json_data[i]))
# print(json_list)
result = {}
for j in json_list:
    result.setdefault("id", []).append(j[0])
    result.setdefault("name", []).append(j[1])
    result.setdefault("user", []).append(j[2])
    result.setdefault("passwd", []).append(j[3])
    result.setdefault("desc", []).append(j[4])
    result.setdefault("token", []).append(j[5])

json_final = json.dumps(result, ensure_ascii=False)
print(json_list)
print(type(json_final))
