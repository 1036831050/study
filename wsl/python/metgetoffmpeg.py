import os

def combine(path):
    list_dir = os.listdir(path)
    new_list = []
    for i in list_dir:
        if i.split(".")[1] == "mp4":
            new_list.append(i)
            # print(list_dir[i])
    return new_list


def output(path, name):
    with open(f"{path}/output.txt", "w", encoding="utf-8")as f:
        for i in name:
            f.write("file "+ f"'{i}'" + "\n")


def ffm(path):
    if os.path.exists(f"{path}/output.txt") == False:
        print(f"{path}/output.txt文件不存在")
    os.system(f"ffmpeg -f concat -safe 0 -i {path}/output.txt -c copy D:\test\output.mp4")


path = "/mnt/e/desktop/merge"
name =combine(path)
output(path, name)
print(f"提示：ffmpeg合并视屏格式为：\n'ffmpeg -f concat -safe 0 -i 名称文档 -c copy 输出路径'")