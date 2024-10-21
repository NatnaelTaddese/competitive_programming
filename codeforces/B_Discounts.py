n = int(input())
a = list(map(int, input().split()))
m = int(input())

q = list(map(int, input().split()))

a.sort()

total_cost = sum(a)

for cupon in q:
    # cost = 0
    # for i in range(n - 1, n - cupon - 3, -1):
    #     print(a[i])
    #     cost += a[i]
    
    # for i in range(cupon - 1):
    #     cost += a[i]
    
    # print(cost)
    cost = total_cost - a[n - cupon]
    print(cost)



    """
    7 1 3 1 4 10 8
    1 1 3 4 7 8 10

    3 


    """