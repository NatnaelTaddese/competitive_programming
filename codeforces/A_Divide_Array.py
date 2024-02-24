n = int(input())
numbers = list(map(int, input().split()))

negative = []
positive = []
prod_zero = []

for num in numbers:
    if num == 0:
        prod_zero.append(num)
    elif num < 0:
        negative.append(num)
    elif num > 0:
        positive.append(num)

for num in negative:
    if len(negative) >= 3 and len(positive) == 0:
        positive.append(negative.pop())
        positive.append(negative.pop())
    if len(negative) % 2 == 0:
        prod_zero.append(negative.pop())


print(len(negative), end= " ")
for num in negative:
    print(num, end= " ")

print(end="\n")


print(len(positive), end= " ")
for num in positive:
    print(num, end= " ")

print(end="\n")

print(len(prod_zero), end= " ")
for num in prod_zero:
    print(num, end= " ")

