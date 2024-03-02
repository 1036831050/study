import os
import re


def main(source_path, target_character="怀孕"):
    # 打开文件以读取文本内容
    with open(source_path, "r", encoding="gbk") as file:
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


if __name__ == "__main__":
    # main(r"F:\AndriodBackup\share\novel\色 小说 全集10000篇\武侠\丹杏.txt","[^避|是|又|，|来|人|了|尺|果|潮|的]孕|排卵|危险期|怀上了|[怀]胎[儿]")
    main()