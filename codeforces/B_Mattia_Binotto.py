n = int(input())

pit_time = list(map(int, input().split()))
optimized_time = sorted(pit_time)

cumulative_time = 0

result = 0
for t in optimized_time:
    if t >= cumulative_time:
        result += 1
        cumulative_time += t


print(result)