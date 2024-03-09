n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


count = 0
j = 0

for i in range(len(b)):
    while(j < len(a)):
        if  a[j] < b[i]:
            count += 1
            j += 1
        else:
            break
    print(count, end =" ")
