rows, cols = map(int, input().split())

matrix = []

for  _ in range(rows):
    line = list(map(int, input().split()))
    matrix.append(line)

prefix_sum_matrix = [[0] * (cols + 1) for _ in range(rows + 1)]

for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix_sum_matrix[i][j] = prefix_sum_matrix[i - 1][j] + prefix_sum_matrix[i][j - 1] - prefix_sum_matrix[i - 1][j - 1] + matrix[i - 1][j - 1]


count = 0

for row1 in range(1, rows + 1):
            for row2 in range(row1, rows + 1):
                prefix_sum = {}

                for col in range(1, cols + 1):
                    current_sum = prefix_sum_matrix[row2][col] - prefix_sum_matrix[row1 - 1][col]

                    area = (row2 - row1 + 1) * col
                    if 2 * (current_sum) == area:
                        count += 1

                    # count += prefix_sum.get(current_sum - area, 0)
                    count += prefix_sum.get((current_sum - (area)), 0)


                    prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1


print(count)
