import sqlite3

def read_database(db_file):
    # 连接到数据库
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # 执行查询操作
    cursor.execute('''SELECT * FROM files''')
    rows = cursor.fetchall()

    
    # 关闭连接
    conn.close()
    return rows

# 指定要读取的数据库文件
db_file = 'file_info.db'

# 读取数据库文件并打印查询结果
print(read_database(db_file)[0][3])
