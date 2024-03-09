# 首先，我们需要定义一个二维列表，表示矩阵
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 然后，我们遍历每一行和每一列，找到行列交点上的单元格
# 并将它们的值设为None
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            matrix[i][j] = None

# 最后，我们输出结果矩阵
print(matrix)
