def solution(n, k):
    for i in range(0,k):
        if n % 10 == 0:
            n = n // 10
        else:
            n = n - 1
    
    return n
 
i = input().split()
n = int(i[0])
k = int(i[1])
print(solution(n,k))
