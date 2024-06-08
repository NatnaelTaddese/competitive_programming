def find_max_strictly_increasing_subarray_indices(s):
    n = len(s)
    if n == 0:
        return []

    max_len = 1
    max_start = 0
    max_end = 0
    current_start = 0
    current_len = 1

    for i in range(1, n):
        if s[i] > s[i - 1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_start = current_start
                max_end = i - 1
            current_start = i
            current_len = 1

    # Final comparison to catch the last increasing subarray
    if current_len > max_len:
        max_len = current_len
        max_start = current_start
        max_end = n - 1

    return [max_start, max_end]

for _ in range(int(input())):
    s = input()
    print(find_max_strictly_increasing_subarray_indices(s))
    
#     print(s)
#     res = 1
#     # we only need only one 0->1 transition
#     # we need to find the maximum window where 0->1 changes and is increasing

#     for i in range(len(s) - 1):
#         if s[i] == '1' and s[i+1] == '0':
#             res += 1
    
#     # transitions = 0
#     # for i in range(len(s) - 1):
#     #     if s[i] != s[i - 1]:
#     #         transitions += 1
#     # # print(res)
#     # print(transitions)