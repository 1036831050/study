import sys

import pyautogui
sys.path.append(r'F:\git\study\vscode\python')
from game.ware import click

# 主要功能实现
def main():
    # 字典用于存储图片名称及其对应的坐标
    coordinates_dict = {}

    # 示例图片名称
    image_name = r"F:\git\study\vscode\python\game\phone\picture\fight.png"

    # 检查字典中是否已有坐标
    if image_name in coordinates_dict:
        x, y = coordinates_dict[image_name]
    else:
        # 获取坐标
        x, y = click.pic_look(image_name)
        # 调用simulate_click函数点击坐标
        # click.simulate_click(x, y)
        pyautogui.click(x, y)
        # 将图片名称和坐标写入字典
        coordinates_dict[image_name] = (x, y)
        print(f"Coordinates for {image_name} added to the dictionary: {x}, {y}")

    # 最后可以输出字典内容查看
    print(coordinates_dict)

if __name__ == "__main__":
    main()
