for _ in range(t):
    n, s = map(int, input().split())
    challenges = list(map(int, input().split()))

    prefix, skip_i = 0, 0
    mx_index = 0
    mx_time = 0