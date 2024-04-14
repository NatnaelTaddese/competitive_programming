def apply_operations(array, operations):
    n = len(array)
    for operation in operations:
        l, r, d = operation
        for i in range(l - 1, r):
            array[i] += d

def process_queries(array, queries, operations):
    for query in queries:
        x, y = query
        l, r, d = operations[x - 1]  # Operation index is 0-based
        for i in range(x, y):
            _, _, d = operations[i]  # Get operation values
            for j in range(l - 1, r):
                array[j] += d

n, m, k = map(int, input().split())
initial_array = list(map(int, input().split()))

operations = [list(map(int, input().split())) for _ in range(m)]
queries = [list(map(int, input().split())) for _ in range(k)]

apply_operations(initial_array, operations)
process_queries(initial_array, queries, operations)

print(*initial_array)

