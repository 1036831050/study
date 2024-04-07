import chardet


def get_encoding(file_path=""):
    rawdata = open(file_path, 'rb').read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']
    return encoding


def main(path=r"F:\git\study\vscode\python\my_utls\novel_opera\sort.py"):
    with open(path, "r", encoding=get_encoding(path)) as f:
        return f.read()
        # print(content)


def split_content(content=""):
    return content.split("\n")

if __name__ == '__main__':
    main()