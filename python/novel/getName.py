# -*- coding = utf-8 -*-
# @Auther:lmd
# @Time    :2023/2/3--19:42
# @File    :getName.py
# @Software:PyCharm

import random
"""
from faker import Faker


def get_name():
    build = Faker(locale='zh_CN')
    name = build.name_female()
    # print(name)
    first_name = ['王', '田', '石', '车', '阚', '包',]
    re = build.first_name_female()
    if re in first_name:
        pass
    else:
        return name


count = 10
for i in range(0, count):
    print(get_name())
"""
# count = input("请输入所需次数(默认5次)：")
# if len(count) == 0:
#     count = 5
# else:
#     count = int(count)


def is_chinese(word):  # 判断是否为中文
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def get_text(path):
    with open(path, 'r', encoding='utf-8') as f:  # 打开并拆分各字
        content = f.read()
        contents = []
        for _ in range(len(content)):
            if is_chinese(content[_]):
                contents.append(content[_])
    #    print(content)
        f.close()
        return contents, len(contents)


def first_name_get(path):
    first_name, count = get_text(path)
    index_first = random.randint(0, count)
    return first_name[index_first]


def after_name_get(path):
    after_name, count = get_text(path)
    index_after = random.randint(0, count)
    names = random.randint(0, 2)
    if names == 0:
        return after_name[index_after]
    else:
        return after_name[index_after] + after_name[index_after+1]


def main():
    print(first_name_get('first_name.txt') + after_name_get('after_name.txt'))

if __name__ == '__main__':
    main()
