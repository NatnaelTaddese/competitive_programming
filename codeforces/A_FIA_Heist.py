word = list(input())

stack = []

i = 0

while i < len(word):
    if word[i] == '<':
        if  i + 1 < len(word) and word[i + 1] == '-':
            if stack:
                stack.pop()
            i += 2
        else:
            stack.append(word[i])
            i += 1
    else:
        stack.append(word[i])
        i += 1

stack = ''.join(stack)

print(stack)