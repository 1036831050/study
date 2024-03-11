# /data/data/com.termux/files/usr/bin/python
import os
import sys
import subprocess
import time
import random

# 获取执行命令的输出
def getout(cmd):
    cmd = cmd.split(" ")
    output = subprocess.check_output(cmd).decode('utf-8')
    return output


# 获取手机分辨率
def getsize():
    # 构建adb shell wm size命令  
    output = getout("adb shell wm size")

    # 输出示例:Physical size: 1080x1920
    size = output.split(': ')[-1] 

    # 分割并打印宽高
    width, height = size.split('x')
    return str(width), str(height)

# 根据不同参数执行相应的滑动命令
def swipe(width, height, sec="300", forw="u"):
    width, height = int(width), int(height)
    list = []
    if forw == "u":
        list = [0.5, 0.8, 0.5, 0.3] 
    elif forw == "d":
        list = [0.5, 0.3, 0.5, 0.8]
    elif forw == "l":
        list = [0.9, 0.5, 0.3, 0.5]
    else:
        print("参数输入错误")
        return 1
    cmd = f"adb shell input swipe {width*list[0]} {height*list[1]} {width*list[2]} {height*list[3]} {sec}"
    # print(cmd)
    os.system(cmd)


if len(sys.argv) >= 2:
    wid, hei = getsize()
    for i in range(int(sys.argv[1])):
        swipe(wid, hei, forw=sys.argv[2])
        if i == int(sys.argv[1])-1:
            quit() 
        time.sleep(random.randint(5,10))



