import os

def merge_novel(directory_path, output_file):
    novel_files = [f for f in os.listdir(directory_path) if f.endswith(".txt")]

    if not novel_files:
        print("在指定目录下找不到小说文件。")
        return

    with open(f"{output_file}\merge.txt", 'w', encoding='utf-8') as output:
        for novel_file in novel_files:
            file_path = os.path.join(directory_path, novel_file)
            # print(f"正在读取：{file_path}")
            output.write(f"{novel_file}\n\n")

            with open(file_path, 'r', encoding='utf-8') as chapter:
                output.write(chapter.read())
                output.write('\n\n')

    print("小说合并完成。")

if __name__ == "__main__":
    # 请替换为你的目录路径和输出文件路径
    directory_path = r"F:\AndriodBackup\resiliosync\tts-vue\novel\心控东瀛篇"
    output_file = r"F:\AndriodBackup"

    merge_novel(directory_path, output_file)
