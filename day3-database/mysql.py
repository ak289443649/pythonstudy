# mysql
import pymysql

conn = pymysql.connect(host='192.168.10.16',
                       port=33060,
                       user='root',
                       password='A45di22WeR',
                       database='600ly_manage',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)

# 如果是插入语句，可以使用executemany进行批量插入，但是要注意，executemany只能在insert语句中执行一次

try:
    with conn.cursor() as cursor:
        sql = "select * from t_mission"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        print(len(result))
        print(type(result))
except Exception as e:
    print(e)
finally:
    conn.close()
