n = int(input())
stack = []
removed = 1

answer = 0

for _ in range(2*n):
    order = list(input().split())

    if order[0] == 'remove':
        if (stack) and (stack[-1] == removed):
            stack.pop()
        else:
            if stack:
                answer += 1
            # stack.sort(reverse=True)
            stack = []
            
        removed += 1


    elif order[0] == 'add':
        # if stack and stack[-1] < int(order[1]):
        # if stack and stack[-1] < int(order[1]):
        #     answer += 1
        #     # stack.sort()
        #     stack = []
        #     # print(order[1])

        stack.append(int(order[1]))


# print(stack)
print(answer)