import os
import sqlite3
import time

# 定义 ANSI 转义码
RED = '\033[91m'
END = '\033[0m'

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        # 使用 ANSI 转义码输出带颜色的文本
        print(f"{RED}Function '{func.__name__}' executed in {elapsed_time:.6f} seconds{END}")
        return result
    return wrapper



def create_database():
    # 连接到数据库（如果不存在则会创建一个）
    conn = sqlite3.connect('file_info.db')
    cursor = conn.cursor()

    # 创建文件信息表
    cursor.execute('''CREATE TABLE IF NOT EXISTS files
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      file_path TEXT UNIQUE,
                      file_name TEXT,
                      file_size INTEGER,
                      created_at TIMESTAMP)''')

    # 提交更改并关闭连接
    conn.commit()
    conn.close()

def insert_file_info(file_path):
    # 获取文件信息
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    created_at = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getctime(file_path)))

    # 连接到数据库
    conn = sqlite3.connect('file_info.db')
    cursor = conn.cursor()

    try:
        # 尝试插入文件信息到数据库表中
        cursor.execute('''INSERT INTO files (file_path, file_name, file_size, created_at)
                          VALUES (?, ?, ?, ?)''', (file_path, file_name, file_size, created_at))
        # 提交更改
        conn.commit()
    except sqlite3.IntegrityError:
        # 如果文件路径已存在，则跳过
        pass
    finally:
        # 关闭连接
        conn.close()


@timeit
def traverse_directory(directory):
    # 遍历目录，获取文件信息并插入到数据库
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            insert_file_info(file_path)

# 创建数据库
create_database()

# 指定要遍历的目录
directory = input("Enter directory to scan: ")

# 遍历目录并将文件信息插入到数据库
traverse_directory(directory)
