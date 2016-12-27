import pymysql
from bili_spider.config import dbconfig
# 创建连接
conn = pymysql.connect(host=dbconfig['host'], port=dbconfig['port'], user=dbconfig['user'], passwd=dbconfig['passwd'], db=dbconfig['db'])

# 创建游标
cursor = conn.cursor()


cursor.execute("select * from tp_client")

# 获取第一行数据
row_1 = cursor.fetchone()
print(row_1)
# 获取前n行数据
row_2 = cursor.fetchmany(3)
print(row_2)
# 获取所有数据
row_3 = cursor.fetchall()
print(row_3)
conn.commit()
cursor.close()
conn.close()
