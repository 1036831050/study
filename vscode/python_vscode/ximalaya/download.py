import requests
import json
import os
from tqdm import tqdm
import glob

#获取当前脚本所在目录并作为下载目录
# path = os.path.dirname(os.path.abspath(__file__))
path = r"F:\vscode\python_vscode\ximalaya\video"
file_extension = "*.mp3"
# print(path)

def main():
    with open("list.txt", "r")as f:
        content = json.load(f)

    # print(type(content))
    # 获取已存在视频长度
    files = glob.glob(os.path.join(path, file_extension))
    print("已下载视频:len(files)")
    # 总进度条长度
    total_progress = tqdm(total=len(content.keys())-len(files), desc="总进度")

    for title, url in content.items():
        # print(title, url)
        if os.path.exists(f"{path}/{title}.mp3"):
            print(f"{title}.mp3已存在，pass")
            continue
        response = requests.get(url)
        response.raise_for_status()
        # print(f"开始下载第{title}集")
        file_size = int(response.headers.get("Content-Length", 0))
        # 设置进度条
        progress_bar = tqdm(total=file_size, unit="B", unit_scale=True, desc=f"第{title}集")
        # with open(f"{title}.mp3", "wb")as f:
        #     f.write(response.content)
        with open(f"{path}/{title}.mp3", "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    progress_bar.update(len(chunk))
        # 关闭进度条
        progress_bar.close()
        total_progress.update(1)
    # 关闭总进度条
    total_progress.close()

if __name__ == '__main__':
    main()