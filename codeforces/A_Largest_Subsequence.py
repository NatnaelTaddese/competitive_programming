# from collections import deque

for _ in range(int(input())):
    n = int(input())
    s = input()
    s = list(s)

    s_sorted = list(sorted(s))

    # stack = deque()
    operations = 0

    while True:
        max_idx = 0
        for i in range(n):
            if s[i] > s[max_idx]:
                max_idx = i
        
        if max_idx == n - 1:
            print(operations)
            break
        
        s = s[max_idx:] + s[:max_idx]
        operations += 1

        if s == s_sorted:
            print(-1)
            break
        
    print(operations)
    # for i in range(n):
    #     while stack and s[i] > stack[-1]:
    #         stack.pop()
    #     stack.append(s[i])

    #     if len(stack) == n - i:
    #         break
            
    #     while len(stack) > 1:
    #         operations += 1
    #         # stack.rotate(1)
    #         stack.pop()

    
    # print(operations)
###############################
    # s = list(s)

    # left = 0
    # right = 1

    # len_list = 1

    # while right < n:
    #     if s[right] > s[right - 1]:
    #         len_list = max(len_list, right - left + 1)
    #     else:
    #         left = right
        
    #     right += 1
    
    # if len_list == 1:
    #     print(-1)
    # else:
    #     print(n - len_list)