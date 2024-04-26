#!/usr/bin/python3
import glob
import os
import re
import sys
import subprocess
from moviepy.editor import VideoFileClip
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor

# 将时间转换为秒数
def time_to_sec(time_str):
    time_obj = datetime.strptime(time_str, '%H:%M:%S')
    total_sec = int((time_obj - datetime(1900, 1, 1)).total_seconds())
    return total_sec

# 裁剪视频
def process_video(mp4file, number, error_time, output_dir, solved_version=None):
    start = max(0, time_to_sec(error_time) - 10)
# 匹配视频文件
    matching_files = glob.glob(f"input/{mp4file}*.mp4")

    if not matching_files:
        print(f"No matching files found for {mp4file}")
        return False

    inputmp4 = matching_files[0]

    # inputmp4 = f"input/{mp4file}.mp4"
    # print(inputmp4)
    error_time_obj = datetime.strptime(error_time, '%H:%M:%S')

    # 将error_time转换为datetime对象，并将日期部分置为最小值，只保留时间部分
    error_time_obj = datetime.combine(datetime.min, error_time_obj.time())

    output = fr"{output_dir}/{number}.mp4"
    if solved_version is not None:
        output = fr"{output_dir}/{number}_{solved_version}-solved.mp4"

    # 裁剪视频
    clip = VideoFileClip(inputmp4)
    duration = clip.duration
    if start > duration:
        start = duration
    end = start + 25
    if end > duration:
        end = duration
    subclip = clip.subclip(start, end)
    try:
        if os.path.exists(output):
            print(f"已存在的视频为:{output},pass")
        else:
            subclip.write_videofile(output, codec='libx265')
        return True
    except Exception as e:
        print(f"视频裁剪失败: {output}")
        print(f"错误信息: {str(e)}")
        return False

# 批量处理视频
def process_videos(input_file, output_dir, solved_version=None):
    os.makedirs(output_dir, exist_ok=True)
    with open(input_file, 'r') as file:
        lines = file.readlines()
        # 过滤空白行
        lines = [line.strip() for line in lines if line.strip()]
        line_count = len(lines)



    success_count = 0
    for i, line in enumerate(lines, 1):
        try:
            counts = len(line.split(','))
            if counts == 2:
                number, error_time = line.split(',')
                mp4file = match_bag(number)
            elif counts == 3:
                mp4file, number, error_time = line.split(',')
            else:
                sys.exit("文本格式错误，请检查")
            if mp4file.endswith("bag") or mp4file.endswith("mp4"):
                pass
            else:
                mp4file = mp4file + ".bag"
            # print(f"\033[0;31m mp4file:{mp4file},\n,number:{number},\n,{error_time}\033[0m")
            if process_video(mp4file, number, error_time, output_dir, solved_version):
                success_count += 1
            print(f"视频处理完成: {i}/{line_count}")
        except Exception as e:
            print(f"处理视频时出现错误: {str(e)}")

    return success_count, len(lines)

# 检查要剪切的视频是否已存在
def check_video(mp4file, out_dir):
    result_mp4 = [os.path.splitext(mp4)[0] for mp4 in os.listdir(output_dir) if mp4.endswith(".mp4")]

# 检查视频是否都已裁剪完成
def check_videos(input_file, output_dir):
    print("\033[34m---------------检查视频是否都已裁剪完成---------------\033[0m")
    result_txt = []
    with open(input_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            try:
                number = line.strip().split(',')[1]
                result_txt.append(number)
            except IndexError:
                print(f"内容格式错误，无法获取number值：{line}")

    result_mp4 = [os.path.splitext(mp4)[0] for mp4 in os.listdir(output_dir) if mp4.endswith(".mp4")]

    all_success = True
    for number in result_txt:
        matching_mp4 = [mp4 for mp4 in result_mp4 if mp4.startswith(number)]
        # print(f"\033[0;31m result_txt:{result_txt},\nmatching_mp4:{matching_mp4}\033[0m")
        if matching_mp4:
            print("\033[0;32msuccess:", matching_mp4[0], "\033[0m")
        else:
            print("\033[0;31m fail:", number, "(需要手动裁剪视频)\033[0m")
            all_success = False

    total_lines = len(result_txt)
    if not lines[-1].strip('\n'):
        total_lines -= 1

    generated_videos = sum(1 for file in os.listdir(output_dir) if file.endswith('.mp4'))

    print(f"\033[34m需要裁剪的数量为：{total_lines}")
    print(f"最终裁剪数量为：{generated_videos}\033[0m")

# 切割图片
def convert_video_to_image(video_path, time, output_path):
    subprocess.run(['ffmpeg', '-i', video_path, '-ss', time, '-vframes', '1', output_path], check=True)

# 匹配bag包名
def match_bag(name):
    match = re.search(r'(?<=-)((tuan|sikeda)_\w+_\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}_\d{1,2})(\.bag)?', name)
    if match:
        name = match.group(0)
        return name
    else:
        print(f"{name}未匹配到包名,请检查")


# 批量切割图片
def convert_videos_to_images(input_file):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    picture_dir = os.path.join(script_dir, "output_picture")
    os.makedirs(picture_dir, exist_ok=True)  # 创建picture_output文件夹
    with open(input_file, 'r') as file:
        lines = file.readlines()
        with ProcessPoolExecutor() as executor:
            futures = []
            for line in lines:
                mp4file, number, time = line.strip().split(',')
                matching_files = glob.glob(f"input/{mp4file}*.mp4")

                if not matching_files:
                    print(f"No matching files found for {mp4file}")
                    return False

                inputmp4 = matching_files[0]
                # inputmp4 = f"{mp4file}.mp4"
                output = f"{number}.jpg"
                print(f"开始剪切{output}")
                output_path = os.path.join(picture_dir, output)  # 将输出路径设置为picture_output文件夹下的路径
                futures.append(executor.submit(convert_video_to_image, inputmp4, time, output_path))
            for future in futures:
                future.result()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python script.py input_file [s]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = './output_video'
    output_pictures_dir = './output_pictures'
    solved_version = None
    if len(sys.argv) > 2 and 's' in sys.argv[2]:
        solved_version = sys.argv[3]

    if len(sys.argv) > 2 and sys.argv[2] == 'n':
        convert_videos_to_images(input_file)
        # try:
        #     convert_videos_to_images(input_file)
        # except:
        #     print("图片剪切失败，请检查")

    success_count, total_count = process_videos(input_file, output_dir, solved_version=solved_version)
    check_videos(input_file, output_dir)

    print(f"\n\033[34m成功裁剪的数量为：{success_count}")
    print(f"未能成功裁剪的数量为：{total_count - success_count}\033[0m")
