import os
import threading

def traverse_directory(directory, result_list):
    files_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            files_list.append(os.path.join(root, file))
    result_list.extend(files_list)

# 目录列表
directories = os.listdir(input(f"需要遍历的目录:")) # 在这里填入你要遍历的目录列表

# 用于存储所有文件路径的列表
all_files = []

# 创建线程列表
threads = []

# 遍历每个目录，创建线程进行遍历
for directory in directories:
    thread = threading.Thread(target=traverse_directory, args=(directory, all_files))
    thread.start()
    threads.append(thread)

# 等待所有线程结束
for thread in threads:
    thread.join()

# 将结果写入到文本文件中
with open('files_list.txt', 'w') as f:
    for file_path in all_files:
        f.write(file_path + '\n')
