target = "hello"
i = 0
word = input()

for c in word:
    if c == target[i]:
        i += 1
        if i == len(target):
            print("YES")
            break

else:
    print("NO")