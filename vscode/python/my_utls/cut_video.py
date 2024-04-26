import subprocess
import time
from moviepy.editor import VideoFileClip


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' 运行时间: {(end_time - start_time):.6f} seconds.")
        return result
    return wrapper


@timer
def cut_by_ffmpeg(input_file, output_file, start_time, end_time):
    # 构建 FFmpeg 命令
    command = [
        'ffmpeg',
        '-ss', str(start_time),  # 开始时间
        '-to', str(end_time),  # 结束时间
        '-i', input_file,  # 输入文件
        '-c', 'copy',  # 使用相同的编解码器
        output_file  # 输出文件
    ]

    # 执行 FFmpeg 命令
    subprocess.run(command, check=True)


def main():
    # 提示用户输入四位数，代表分钟和秒钟
    # time_str = input("请输入一个四位数（如：0123）：")
    time_str = "0500"    
    # 将输入的四位数转换为分钟和秒钟
    minutes = int(time_str[:2])
    seconds = int(time_str[2:])
    
    # 计算开始和结束时间
    start_time = max(0, minutes * 60 + seconds - 20)
    end_time = minutes * 60 + seconds + 20
    
    # 定义输入视频文件路径
    input_file = r"F:\BaiduNetdiskDownload\mp4\伏娲：JK学姐-熙娆.mp4"

    # 定义输出视频文件路径
    output_file = 'output1.mp4'

    # 调用剪切视频函数
    # cut_by_ffmpeg(input_file, output_file, start_time, end_time)
    cut_by_moviepy(input_file, output_file, start_time, end_time)

if __name__ == "__main__":
    main()
