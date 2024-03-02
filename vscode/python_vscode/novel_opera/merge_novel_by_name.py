import os
import re

def extract_number_from_filename(filename):
    # 从文件名中提取数字部分
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')

def merge_novel(directory_path, output_file):
    novel_files = [f for f in os.listdir(directory_path) if f.endswith(".txt")]

    if not novel_files:
        print("在指定目录下找不到小说文件。")
        return

    novel_files.sort(key=extract_number_from_filename)

    with open(f"{output_file}\merge.txt", 'w', encoding='utf-8') as output:
        for novel_file in novel_files:
            file_path = os.path.join(directory_path, novel_file)
            with open(file_path, 'r', encoding='utf-8') as chapter:
                output.write(chapter.read())
                output.write('\n\n')

    print("小说合并完成。")

if __name__ == "__main__":
    # 请替换为你的目录路径和输出文件路径
    directory_path = r"F:\AndriodBackup\resiliosync\novel\ShaftNovels\心控反转"
    output_file = r"F:\AndriodBackup"

    merge_novel(directory_path, output_file)
