#!E:/scoop/apps/anaconda3/current/envs/lmd/python.exe
import json
import sys
import cv2
import numpy as np
import pyautogui
import time
import os
import subprocess


# start_game = r"F:\git\study\python\game\picture\kaishiyouxi.png"
# yunding = r"F:\git\study\python\game\picture\yunding.png"
# kuangbao = r"F:\git\study\python\game\picture\kuangbao.png"
# queren = r"F:\git\study\python\game\picture\queren.png"
# fangjian = r"F:\git\study\python\game\picture\fangjian.png"
# duiju = r"F:\git\study\python\game\picture\duiju.png"
# jieshou = r"F:\git\study\python\game\picture\jieshou.png"
# zaiwanyici = r"F:\git\study\python\game\picture\zaiwanyici.png"
ahk_exe = r"E:/scoop/shims/autohotkey.exe"

# play_start_list:list = [start_game, yunding, kuangbao, queren, fangjian, duiju, jieshou, zaiwanyici]
play_start_list:dict = {"start_game" : r"F:\git\study\python\game\picture\kaishiyouxi.png","yunding" : r"F:\git\study\python\game\picture\yunding.png", "kuangbao" : r"F:\git\study\python\game\picture\kuangbao.png", "queren" : r"F:\git\study\python\game\picture\queren.png", "fangjian" : r"F:\git\study\python\game\picture\fangjian.png", "duiju" : r"F:\git\study\python\game\picture\duiju.png", "jieshou" : r"F:\git\study\python\game\picture\jieshou.png", "zaiwanyici" : r"F:\git\study\python\game\picture\zaiwanyici.png"}

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
    

# 循环获取坐标位置，返回复数坐标，字典
def record_coordinate(play_start_list, max_attempts = 3):
    coors:dict = {}
    no_found:list = []
    for key,i in play_start_list.items():
        found_position = pic_look(i)
        attempts = 0
        while not found_position and attempts < max_attempts:
            found_position = pic_look(i)
            attempts += 1
            if not found_position:
                print(f"第 {attempts} 次尝试未找到图片 {i}", end="\r")
                time.sleep(3)

        if found_position:
            print(f"找到图片 {i}，位置为 {found_position}",end="\n")
            # 使用
            coors[key] = found_position
        else:
            print(f"达到最大尝试次数，未找到图片 {i}")
            no_found.append(key)
            # sys.exit(f"达到最大尝试次数，未找到图片 {i}")
    print(f"未找到图片 {no_found}")
    return coors


# 保存坐标到文件内
def save_files(content, path=r'./coors.txt'):
    with open('coors.txt', 'w') as f:
        json.dump(content,f)


# 读取已保存的坐标值
def read_files(path):
    new_list = {}
    with open(path) as f:
        new_list = json.load(f)
    return new_list

def main(counts=5):
    all_coors = record_coordinate(play_start_list,counts)
    save_files(all_coors)

if __name__ == '__main__':
    main(6)