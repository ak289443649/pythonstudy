import pymysql
from pypinyin import pinyin, Style

# 连接数据库
conn = pymysql.connect(host='192.168.10.14', port=33060, user='root', passwd='xxx', db='xxx')
cursor = conn.cursor()

# 选择操作的表
table = 'xxx' 

# 主键字段
id_column = 'pk_id'

# 源字段
src_column = 'resource_name'

# 目标字段  
dst_column = 'pinyin'

# 查询数据
select_sql = f"SELECT {id_column},{src_column} FROM {table}"
cursor.execute(select_sql)
results = cursor.fetchall()

# 转换拼音函数
def get_pinyin_list(name, style=Style.NORMAL):
  py_list = pinyin(name, style=style)
  return py_list

# 转换拼音并更新
for row in results:
    id = row[0]
    name = row[1]
    py_list = get_pinyin_list(name)
    if py_list:
        pinyin_names = []
        for item in py_list :
            pinyin_names.append(item[0])
        # 需要一个字符串集合
        pinyin_name = "".join(pinyin_names)
    else:
        pinyin_name = ''

    update_sql = f"UPDATE {table} SET {dst_column}='{pinyin_name}' WHERE {id_column}='{id}'"
    cursor.execute(update_sql)

# 提交事务    
conn.commit() 

print('拼音转换完成!')

cursor.close()
conn.close()