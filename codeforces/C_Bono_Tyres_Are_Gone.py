n = int(input())
stack = []

answer = 0

for _ in range(2*n):
    order = list(input().split())

    if order[0] == 'remove':
        if stack:
            stack.pop()

    elif order[0] == 'add':
        if stack and stack[-1] < int(order[1]):
        # if stack and int(order[1]) < stack[-1]:
            answer += 1
            # stack.sort()
            stack = []
            # print(order[1])

        stack.append(int(order[1]))


# print(stack)
print(answer)

