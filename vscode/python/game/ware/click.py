import os
import subprocess
import cv2
import numpy as np
import pyautogui


# 通过ahk脚本模拟点击
def simulate_click(x, y):
    ahk_script = r"E:\desktop\coor_python.ahk"
    ahk_path = r"E:/scoop/shims/autohotkey.exe"
    # args = [ahk_path, ahk_script, str(x), str(y)]
    args = [ahk_path, ahk_script, f"{x},{y}"]
    subprocess.run(args, capture_output=True, text=True)

# 寻找图片，返回坐标，元组
def pic_look(pic_path):
    # 打印目前搜索图片
    pic_name = os.path.basename(pic_path)
    print("目前搜索图片:", pic_name, end="\r")
    # 加载需要查找的图片和屏幕截图
    template = cv2.imread(pic_path, cv2.IMREAD_GRAYSCALE)
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # 使用模板匹配算法
    res = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    # 获取图片在屏幕中的位置
    for pt in zip(*loc[::-1]):
        # 点击图片所在位置
        pyautogui.click(pt[0] + template.shape[1] / 2, pt[1] + template.shape[0] / 2)
        return pt[0] + template.shape[1] / 2, pt[1] + template.shape[0] / 2
    

if __name__ == '__main__':
    simulate_click(100, 100)