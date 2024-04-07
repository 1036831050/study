import subprocess
import lol_coord as cord


# 通过ahk脚本模拟点击
def simulate_click(coor_tuple):
    x = coor_tuple[0]
    y = coor_tuple[1]
    ahk_script = "E:\desktop\coor_python.ahk"
    args = ["AutoHotkey.exe", ahk_script, str(x), str(y)]
    subprocess.run(args)


all_coors = cord.read_files("coors.txt")
simulate_click(all_coors["start_game"])