import os
import concurrent.futures
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' 运行时间: {(end_time - start_time):.6f} seconds.")
        return result
    return wrapper


def list_files(directory):
    """
    列出指定目录下的所有文件
    """
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def process_file(file):
    """
    处理单个文件的函数，将文件路径写入 TXT 文档中
    """
    with open("file_list.txt", "a") as f:
        f.write(file + "\n")


def process_directory(directory):
    """
    处理单个目录的函数，列出目录下的所有文件并提交给线程池处理
    """
    files = list_files(directory)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for file in files:
            executor.submit(process_file, file)

@timer
def main():
    # 指定要遍历的根目录
    root_directory = input("请输入要遍历的根目录: ")

    # 遍历根目录下的所有子目录并处理
    for root, dirs, _ in os.walk(root_directory):
        for directory in dirs:
            full_path = os.path.join(root, directory)
            process_directory(full_path)



if __name__ == "__main__":
    # 在开始遍历之前先清空文件
    with open("file_list.txt", "w") as f:
        pass
    main()
