import os
import re
import chardet

def get_count(source_path, target_character="怀孕"):
    with open(f'"{source_path}"', "r", encoding="gbk") as file:
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
    print(f"字符序列 '{target_character}' 出现的次数: {count}")
    return count


def sanitize_filename(filename):
    # 使用正则表达式替换文件名中的非法字符
    return re.sub(r'[<>:"/\\|?*]', '-', filename)

# 获取用户输入的文件路径
file = input("请输入文件路径：").strip()

# 读取文件的原始二进制数据
rawdata = open(file, 'rb').read()

# 使用 chardet 检测文件编码
result = chardet.detect(rawdata)
encoding = result['encoding']

coding = ['GB2312','utf-8','UTF-8 BOM']
# 如果编码是 GB2312，则将其更改为 gb18030
if encoding in coding:
    encoding = 'gb18030'

# 打印检测到的文件编码
print(encoding)

# 以检测到的编码打开文件并输出其内容
f = open(file, 'r', encoding=encoding)
print(f.read())

# char = "[^避|是|又|，|来|人|了|尺|果|潮|的]孕|排卵|危险期|[怀]胎[儿]"
# count = get_count(file_path, char)