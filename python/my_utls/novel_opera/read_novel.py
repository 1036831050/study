import os
import re
from chardet.universaldetector import UniversalDetector


def get_encoding(file_path):
    detector = UniversalDetector()
    with open(file_path, 'rb') as file:
        for line in file:
            detector.feed(line)
            if detector.done: break
    detector.close()
    return detector.result['encoding']


def main(source_path, target_character="怀孕"):
    # 打开文件以读取文本内容
    with open(source_path, "r", encoding=get_encoding(source_path)) as file:
        text = file.read()

    # 要统计的中文字符
    # target_character = "怀孕"
    pattern = target_character

    # 执行正则表达式匹配
    matches = re.findall(pattern, text)


    # 统计匹配次数
    count = len(matches)

    # 打印出现次数
    print(f"字符序列 '{target_character}' 出现的次数: {count}")
    return count


if __name__ == "__main__":
    pattern = r"[^避是又，来人了尺果潮的]孕|排卵|危险期|怀上了|[怀]胎[儿]"
    main(input("请输入文件路径："), pattern)