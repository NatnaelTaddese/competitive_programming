s = input()

stack = []
max_length = 0
last_index = -1

for i, char in enumerate(s):
    print(stack)
    if char == '(':
        stack.append(i)
    else:
        if stack:
            stack.pop()
            if stack:
                max_length = max(max_length, i - stack[-1])
            else:
                max_length = max(max_length, i - last_index)
        else:
            last_index = i
            # print(last_index)

print(max_length)

