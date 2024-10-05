from math import ceil


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    dp = [0] * n
    
    operations = 0
    
    # for i in range(n - 1):
    #     if a[i] > a[i + 1]:
    #         while a[i] > a[i + 1]:        
    #             parts = ceil(a[i] / a[i + 1])
    #             operations += parts - 1
    #             a[i] = a[i] // parts
    # print(operations)

    minimum = a[-1]  

    for i in range(n - 2, -1, -1):
        if a[i] > minimum:
            parts = ceil(a[i] / minimum)
            operations += parts - 1
            minimum = a[i] // parts
        else:
            minimum = a[i]
    
    print(operations)
