import math

for _ in range(int(input())):
    n = int(input())

    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    

    for i in range(n / 2):
        for j in range(4):
            # compare
            matrix[i][j]