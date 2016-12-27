import pymysql
import time
from random import Random
from bili_spider.config import dbconfig

# 创建连接
conn = pymysql.connect(host=dbconfig['host'], port=dbconfig['port'], user=dbconfig['user'], passwd=dbconfig['passwd'],
                       db=dbconfig['db'], charset='utf8mb4')

# 创建游标
cursor = conn.cursor()


def random_str(randomlength=4):
    str1 = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str1 += chars[random.randint(0, length)]
    return str1


def insert_user(data=None):
    if data['name'] == '':
        data = {'name': random_str()}
    else:
        data['add_time'] = time.time()
    sql = 'insert into user_info set '
    for key in data.keys():
        sql += ' ' + str(key) + ' = \'' + str(data[key]) + '\' ,'
    sql = sql.rstrip(',')
    cursor.execute(sql)
    conn.commit()
    return cursor.lastrowid


def insert_extend_user(user_id=0, data=None):
    if not data:
        data = {'user_id': user_id}
    else:
        data['user_id'] = user_id
        data['add_time'] = time.time()
    sql = 'insert into extend_info set '
    for key in data.keys():
        sql += ' ' + str(key) + ' = \'' + str(data[key]) + '\' ,'
    sql = sql.rstrip(',')
    cursor.execute(sql)
    conn.commit()


def close():
    cursor.close()
    conn.close()
# # 获取第一行数据
# row_1 = cursor.fetchone()
# print(row_1)
# # 获取前n行数据
# row_2 = cursor.fetchmany(3)
# print(row_2)
# # 获取所有数据
# row_3 = cursor.fetchall()
# print(row_3)
# conn.commit()
# cursor.close()
# conn.close()