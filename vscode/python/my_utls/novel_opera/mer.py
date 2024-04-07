# -*- coding = utf-8 -*-
# @Auther:lmd
# @Time    :2023/2/28--14:24
# @File    :merge.py
# @Software:PyCharm
import difflib
import os
import shutil


def merge(first_path, second_path): # 比较两文件的数量，把文件数量少的移动到大文件内
    if len(os.listdir(first_path)) > len(os.listdir(second_path)):
        count = second_path
        # print(count)
    for item in os.listdir(count):
        first_item = os.path.join(first_path, item)
        second_item = os.path.join(second_path, item)
        if os.path.isfile(second_item):
            shutil.move(second_item, first_item)
    if len(os.listdir(count)) == 0:
        os.rmdir(count)
        print("文件夹：{}已删除。".format(count))


def diff(first_file, second_file):
    rate = difflib.SequenceMatcher(None, first_file, second_file).ratio()
    return rate


path = r'F:\pycharm\lmd\pythonProject\novel\novel'
i = 0
while i <= len(os.listdir(path))-2:
    list_file = os.listdir(path)
    print(i, list_file[i])
    first = list_file[i]
    second = list_file[i+1]
    i += 1
    if diff(first, second) >= 0.8:
        merge(os.path.join(path, first), os.path.join(path, second))
    else:
        print("None")

# diff(first, second)
# print(os.listdir(path)[10])