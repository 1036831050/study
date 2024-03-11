import os
import re

def extract_number_from_filename(filename):
    """
    从文件名中提取数字部分。
    """
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')

def merge_novel(directory_path, output_file=None):
    """
    将按章节切分后的小说合并为一本完整的小说。

    Args:
        directory_path (str): 小说文件所在目录的路径。
        output_file (str, optional): 合并后的小说输出文件路径。如果未提供，默认保存在原始小说文件所在目录中。

    """
    # 获取目录下所有的小说文件
    novel_files = [f for f in os.listdir(directory_path) if f.endswith(".txt")]

    if not novel_files:
        print("在指定目录下找不到小说文件。")
        return

    # 根据文件名中的数字部分进行排序
    novel_files.sort(key=extract_number_from_filename)

    # 如果未提供输出文件路径，则保存在原始小说文件所在目录中
    if output_file is None:
        output_file = os.path.join(directory_path, "merge.txt")

    # 合并小说文件
    with open(output_file, 'w', encoding='utf-8') as output:
        for novel_file in novel_files:
            file_path = os.path.join(directory_path, novel_file)
            with open(file_path, 'r', encoding='utf-8') as chapter:
                output.write(chapter.read())
                output.write('\n\n')

    print("小说合并完成。")

if __name__ == "__main__":
    # 获取用户输入的小说文件目录路径
    directory_path = input("请输入小说文件所在目录：")
    merge_novel(directory_path)
