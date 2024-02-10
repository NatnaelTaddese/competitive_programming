x = int(input())
y = list(map(int, input().split()))
average = 0

for val in y:
    average += val

print(float(average)/x)