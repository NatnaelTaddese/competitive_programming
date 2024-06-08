n = input()

magic_numbers = ['1', '14', '144']

stack = []
answer = False

def backtrack(start):
    global answer
    if start == len(n):
        # print("".join(stack))
        if "".join(stack) == n:
            answer = True
        return
    
    for num in magic_numbers:
        #debug
        # print(stack)
        end = start + len(num)
        # print(end)
        if end <= len(n) and n[start:end] == num:
            stack.append(num)
            backtrack(end)
            stack.pop()

            if answer:
                return

backtrack(0)

if answer:
    print("YES")
else:
    print("NO")
