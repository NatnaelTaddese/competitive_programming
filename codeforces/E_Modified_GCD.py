a, b = map(int, input().split())
n = int(input())

def cutom_gcd(x, y, lower, upper):
    original_x = x
    original_y = y

    while y!= 0:
        x, y = y, x % y
    
    if x > upper:
        return cutom_gcd(x, original_y, lower, upper)
    if lower <= x <= upper:
        return x
    else:
        return -1


for _ in range(n):
    low, high = map(int, input().split())
    print(cutom_gcd(a, b, low, high))
