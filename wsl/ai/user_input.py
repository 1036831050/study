import subprocess

def main():
    # 调用 C++ 程序
    process = subprocess.Popen("/home/lmd/script/python/input", stdout=subprocess.PIPE, text=True)

    # 读取 C++ 程序的输出
    multiline_text = process.communicate()[0]

    return multiline_text

if __name__ == '__main__':
    main()