n, m = map(int,input().split())

A = []
B = [[0 for _ in range(m)] for _ in range(n)]

indexes = []

for _ in range(n):
    A.append(list(map(int, input().split())))



all_zero = True

for i in range(n - 1):
    for j in range(m - 1):

        # loop through
        if  A[i][j] == A[i + 1][j] == A[i][j + 1] == A[i+1][j+1] == 1:
            B[i][j] = B[i + 1][j] = B[i][j + 1] = B[i+1][j+1] = 1            
            indexes.append([i,j])

if A!=B:
    print(-1)

else:
    print(len(indexes))
    for index in indexes:
        print(index[0] + 1, index[1] + 1)