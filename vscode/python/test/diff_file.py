import os
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


# ANSI 转义序列
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_RESET = "\033[0m"

def find_similar_files(directory, threshold=0.9):
    similar_files = []

    # 获取给定目录下的文件列表
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # 遍历文件列表
    for i, file1 in enumerate(files):
        # 只比较当前文件之后的文件名，避免重复比较
        for file2 in files[i+1:]:
            similarity = similar(os.path.basename(file1), os.path.basename(file2))
            if similarity >= threshold:
                # 根据相似度设置文件名颜色
                color1 = COLOR_RED if similarity >= 0.95 else COLOR_GREEN
                color2 = COLOR_RED if similarity >= 0.95 else COLOR_GREEN

                similar_files.append((os.path.join(directory, file1), os.path.join(directory, file2), similarity, color1, color2))

    return similar_files

# 指定要遍历的目录和相似度阈值
directory = input("Enter directory path: ")
threshold = 0.8

# 找出相似度较高的文件
similar_files = find_similar_files(directory, threshold)
for file1, file2, similarity, color1, color2 in similar_files:
    print(f"Similar files: {color1}{file1}{COLOR_RESET} and {color2}{file2}{COLOR_RESET}, similarity: {similarity}")
