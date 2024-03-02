import os
import re
import chardet

def get_default(var, default):
    return var or default


def get_count(source_path, encoding="", target_character="怀孕"):
    if len(encoding) == 0:
        with open(source_path, "r") as file:
            text = file.read()
    else:
        with open(source_path, "r", encoding=encoding) as file:
            text = file.read()

    # 要统计的中文字符
    # target_character = "怀孕"

    # 使用正则表达式查找匹配
    # pattern = re.compile(re.escape(target_character))
    # matches = pattern.findall(text)

    # pattern = r"[^避是又，来人了尺果潮的]孕|排卵|危险期|怀上了|[怀]胎[儿]"
    pattern = target_character

    # 执行正则表达式匹配
    matches = re.findall(pattern, text)


    # 统计匹配次数
    count = len(matches)

    # 打印出现次数
    # print(f"字符序列 '{target_character}' 出现的次数: {count}")
    return count


def get_absolute_file_paths(directory):
    file_paths = []  # 用于存储文件的绝对路径

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file_path)[1]
            # print(f"{file_path}扩展名为：{file_extension}")
            if file_extension == ".txt":
                # print(file_path)
                file_paths.append(file_path)
    
    return file_paths


def get_encoding(file_path):
    rawdata = open(file, 'rb').read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']
    if encoding == 'GB2312':
        encoding = 'gb18030'
    return encoding


def save_data(file,count):
    # print("文件:", file,f"关键字: {count} 次出现")
    file_name = os.path.basename(file)
    if count >= 5:
        with open(f"{file_path}/count.txt", "a+", encoding="utf-8")as f:
            f.write(f"{file}------出现{count}次\n")


if __name__ == "__main__":
    
    file_path = get_default(input("请输入文件路径（生成的文件也在此路径下）: "), os.getcwd())
    # file_path = user_input or os.getcwd()
    # 调用函数获取所有文件的绝对路径
    absolute_paths = get_absolute_file_paths(file_path)
    # char = "[^避|是|又|，|来|人|了|尺|果|潮|的]孕|排卵|危险期|[怀]胎[儿]"
    char = '''
    [怀|有|受|成|身]孕|[怀]胎儿|排卵|[肚|腹][\u4e00-\u9fa5]{1,6}[隆|凸]|[怀]{0,1}胎[儿]{0,1}
            '''

    # 打印所有文件的绝对路径
    suc = 0
    fail = 0
    for file in absolute_paths:
        try:
            count = get_count(file, target_character=char)
            print(file,f"关键字: {count} 次出现")
            save_data(file,count)
            suc += 1
        except:
            try:
                count = get_count(file, "gb18030", char)
                print(file,f"关键字: {count} 次出现")
                save_data(file,count)
                suc += 1
            except:
                try:
                    count = get_count(file, get_encoding(file), char)
                    print(file,f"关键字: {count} 次出现")
                    save_data(file,count)
                    suc += 1
                except:
                    print("文件:",              file,               "打开失败")
                    fail += 1
    print("成功:", suc, "失败:", fail,"总共:",len(absolute_paths))  