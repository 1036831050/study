from concurrent.futures import ProcessPoolExecutor
import subprocess
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' 运行时间: {(end_time - start_time):.6f} seconds.")
        return result
    return wrapper


def convert_video_to_image(video_path, time, output_path):
    # subprocess.run(['ffmpeg', '-i', video_path, '-ss', time, '-vframes', '1', output_path], check=True)
    subprocess.run(['ffmpeg', '-i', video_path, '-ss', time, '-copyinkf', '-vframes', '1', output_path], check=True)



# video_path = r"F:\AndriodBackup\resiliosync\mp4\【3D动画】【骨科多P】催眠Family【RJ409399】\scene.mp4"
video_path = "/mnt/f/AndriodBackup/resiliosync/mp4/【3D动画】【骨科多P】催眠Family【RJ409399】/scene.mp4"
pic_path = r"cut_pic.jpg"
# convert_video_to_image(video_path, '00:01:00', pic_path)
@timer
def main():
    with ProcessPoolExecutor() as executor:
        future = executor.submit(convert_video_to_image, video_path, '00:01:00', pic_path)
        result = future.result()
        print(result)

main()