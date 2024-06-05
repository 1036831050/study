import subprocess

def get_touch_coordinates():
    # 调用 adb shell input tap 命令，并捕获其输出
    output = subprocess.check_output(["adb", "shell", "getevent", "-lt", "/dev/input/event1"], universal_newlines=True)

    # 解析输出，获取点击事件的坐标
    coordinates = []
    for line in output.splitlines():
        if "ABS_MT_POSITION_X" in line or "ABS_MT_POSITION_Y" in line:
            parts = line.strip().split()
            if len(parts) == 4:
                if "ABS_MT_POSITION_X" in parts[3]:
                    x = int(parts[2], 16)
                elif "ABS_MT_POSITION_Y" in parts[3]:
                    y = int(parts[2], 16)
                    coordinates.append((x, y))
    return coordinates

# 获取点击坐标并打印出来
touch_coordinates = get_touch_coordinates()
print("点击坐标：", touch_coordinates)
