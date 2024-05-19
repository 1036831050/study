x:float
y:float
z:float
# 30 * x = 15 * y = 5 * (x + y + z) * 4 / 3
for x in range(30):
    for y in range(16):
        for z in range(100):
            if 30 * x == 15 * y == 5 * (x + y + z) * 4 / 3:
                print(f"如果排球单价为：{x},篮球单价为：{y},足球单价为：{z}")    # 输出排球数量 
                if z != 0:
                    print("足球数量为：", (30 * x - 5 * (x + y + z))/ z)