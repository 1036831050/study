import os
import shutil
from tqdm import tqdm


'''复制源目录下的所有文件，转移到目标目录并显示进度条'''


def copy_files(source_dir, destination_dir):
    # 获取源目录下的所有文件列表
    files = []
    for root, dirs, filenames in os.walk(source_dir):
        for filename in filenames:
            files.append(os.path.relpath(os.path.join(root, filename), source_dir))

    # 显示进度条
    with tqdm(total=len(files), desc="Copying files", unit=" files") as pbar:
        # 遍历源目录及其子目录下的所有文件
        for file in files:
            source_path = os.path.join(source_dir, file)
            destination_path = os.path.join(destination_dir, file)
            # 创建目标路径的目录（如果不存在）
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            # 复制文件
            shutil.copy(source_path, destination_path)
            pbar.update(1)  # 更新进度条

    # 询问用户是否删除源文件
    answer = input("是否删除源文件？(y/n): ")
    if answer.lower() == 'y':
        for file in files:
            source_path = os.path.join(source_dir, file)
            os.remove(source_path)
        print("源文件已删除。")
    else:
        print("源文件未删除。")

if __name__ == "__main__":
    source_dir = input("请输入源目录路径：")
    destination_dir = input("请输入目标目录路径：")

    copy_files(source_dir, destination_dir)
