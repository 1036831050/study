import chardet

# 定义一个函数，用于获取文件的编码方式
def get_encoding(file_path=""):
    rawdata = open(file_path, 'rb').read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']
    return encoding


# 定义一个主函数，接受一个文件路径参数，默认路径为"F:\git\study\vscode\python\my_utls\novel_opera\sort.py"
def main(path=r"F:\git\study\vscode\python\my_utls\novel_opera\sort.py"):
    # 使用指定的编码方式打开文件，并读取文件内容
    with open(path, "r", encoding=get_encoding(path)) as f:
        return f.readlines()
        # print(content)

# 定义一个函数，用于将文件内容按行分割
def split_content(content=""):  
    return content.split("\n")

if __name__ == '__main__':
    main()