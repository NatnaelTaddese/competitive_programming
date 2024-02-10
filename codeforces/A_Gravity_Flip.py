colums = int(input())
values = list(map(int, input().split()))
values.sort()
print(" ".join(map(str, values)))