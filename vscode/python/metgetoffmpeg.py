import os
'''获取指定目录下的所有视频文件，合并成一个视频'''
def combine(path, format):
    # 获取目录下所有文件名
    list_dir = os.listdir(path)
    new_list = []
    for i in list_dir:
        # 检查文件的扩展名是否为指定的格式
        if i.split(".")[1] == format:
            new_list.append(i)
    return new_list

def output(path, name):
    # 将文件名写入 output.txt 文件
    with open(f"{path}/output.txt", "w", encoding="utf-8") as f:
        for i in name:
            f.write("file "+ f"'{i}'" + "\n")

def ffm(path, format):
    # 检查 output.txt 文件是否存在
    if not os.path.exists(f"{path}/output.txt"):
        print(f"{path}/output.txt文件不存在")
    
    # 使用 ffmpeg 合并文件
    os.system(f"ffmpeg -f concat -safe 0 -i {path}/output.txt -c copy {path}/output.{format}")

# 指定目录
path = r"F:\AndriodBackup\resiliosync\tts-vue\merge"
# 获取目录下所有指定格式的文件名
name = combine(path, "mp3")
# 写入ffmpeg格式文件
output(path, name)
# 合并
ffm(path, "mp3")
# 提示
print(f"提示：ffmpeg合并视屏格式为：\n'ffmpeg -f concat -safe 0 -i 名称文档 -c copy 输出路径'")
