l = int(input())
stack = [1]


max_val = (2**32) - 1

result = 0

for _ in range(l):
    command = input().split()

    if command[0] == 'end':
        stack.pop()
    elif command[0] == 'for':
        stack.append(min(max_val, int(command[1])) * stack[-1])
    else:
        result += stack[-1]


if result > max_val:
    print("OVERFLOW!!!")
else:
    print(result)
