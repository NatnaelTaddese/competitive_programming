for _ in range(int(input())):
    n = int(input())
    sizes = list(map(int, input().split()))
    min_size = min(sizes)
    max_size = max(sizes)
    if abs(min_size - max_size) < n:
        