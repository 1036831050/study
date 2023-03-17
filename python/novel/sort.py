# -*- coding = utf-8 -*-
# @Auther:lmd
# @Time    :2023/2/26--18:34
# @File    :sort.py
# @Software:PyCharm

import os, re
import difflib
import shutil


def make_path(path):
    if not os.path.exists(path):
        os.makedirs(path)


def main(root_dir, file_list):
    for i in range(len(file_list)):
        if len(get_name(file_list[i])) == 0:
            continue
        dir_name = get_name(file_list[i])
        file_name = file_list[i]
        path = os.path.join(root_dir, dir_name)
        tar_path = os.path.join(path, os.path.basename(file_name))
        make_path(path)
        if os.path.exists(tar_path):
            # print("已存在:{}".format(tar_path))
            pass
        else:
            shutil.move(file_name, path)
        # print(file_name)
        # print("路径为：{}".format(path))
        # print(tar_path)


def get_name(filename):
    filename = os.path.basename(filename)
    fail_list = []
    # print(filename)
    try:
        pattern = re.compile(r'\[.*\]\s*(.*?)\s*\(.*?\)')
        filename = re.sub(r'\[(.*)\]|\-|\d|\(.*\)', '', filename)
        # print(filename)
        result = re.findall(r'(.*?)\s*.txt', filename)
        result = result[0]
        # print(result)
    except Exception as e:
        print("error:path fail",filename)
        # result = re.sub(r'\[(.*)\]|\-|\d', '', filename)
        # result = re.findall(r'[\[.*\]]{0,2}\s*(.*?)\s*[\(.*?\)]{0,2}.txt', result)
    return result


if __name__ == "__main__":
    path = r'F:\pycharm\lmd\pythonProject\novel\novel'
    cutoff = 0.8
    file_list = []
    root_dir = r"E:\desktop\novel"
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    file_list = sorted(file_list)
    print(file_list)
    main(root_dir, file_list)



