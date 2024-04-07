#!/usr/bin/env python3
import os
import subprocess

temp_path = os.path.join(os.getcwd(), 'temp')
video_path = os.path.expanduser('~/shipin')
file_path = os.path.join(video_path, '1.txt')

def touch_list(main_path):
    print("开始获取视频目录")
    os.makedirs(temp_path, exist_ok=True)
    with open(file_path, 'w') as file_list:
        for root, _, files in os.walk(main_path):
            for file in files:
                if file.endswith('.mp4'):
                    file_list.write(os.path.join(root, file) + '\n')

def judge_file(file_list):
    if os.path.isfile(file_list):
        opts = input("目录list已存在,是否重新获取(y/n): ")
        if opts == "y":
            touch_list(main_path)
    else:
        touch_list(main_path)

def copy(files, file_list):
    with open(file_list) as f:
        file_paths = sorted(set(map(str.strip, f.readlines())))
    for i in file_paths:
        file_name = os.path.basename(i.split(',')[0])
        print(file_name)
        os.makedirs(os.path.join(video_path, 'input'), exist_ok=True)
        subprocess.run(['grep', file_name, file_list, '|', 'xargs', '-i', 'cp', '{}', os.path.join(video_path, 'input')])

def by_vlc(file_path):
    while True:
        name = input("视频名称(退出脚本q,复制文件c)：")
        if name == "q":
            exit(0)
        elif name == "c":
            break
        elif not name:
            print("输入错误，请重试。")
        else:
            name = name.split('bag')[0]
            subprocess.run(['grep', name, file_path, '|', 'xargs', '-i', 'vlc', '-q', '{}'])

def get_path():
    base_path = os.path.expanduser('~/nas/CornerRadarDataAnalysis/02_sil')
    output_path = sorted(filter(lambda x: 'track_6.3g' in x, os.listdir(base_path)), reverse=True)[0]
    main_path = os.path.join(base_path, output_path)
    opt = input(f"版本路径为:\n{main_path}\n是否继续(y/n,输入n开始手动输入版本路径): ")
    if opt == "n":
        main_path = input("请输入版本路径: ")
    else:
        print("自动获取最新目录...")
    file_name = os.path.basename(main_path) + '.txt'
    file_path = os.path.join(temp_path, file_name)
    return main_path, file_path

def copy1(files, file_list):
    with open(file_list) as f:
        file_paths = sorted(set(map(lambda x: x.split(',')[0].split('_E')[1].split('bag')[0], map(str.strip, f.readlines()))))
    for i in file_paths:
        print(i)
        os.makedirs(os.path.join(video_path, 'input'), exist_ok=True)
        subprocess.run(['grep', i, file_list, '|', 'xargs', '-i', 'cp', '{}', os.path.join(video_path, 'input')])

def check_list(file):
    with open(file) as f:
        line = len(f.readline().strip().split(','))
    print(line)
    return line

line = check_list(file_path)
main_path, file_path = get_path()
print("file_path:", file_path, "file:", file)
judge_file(file_path)
by_vlc(file_path)
if line == 3:
    copy(file_path, file)
elif line == 2:
    copy1(file_path, file)
