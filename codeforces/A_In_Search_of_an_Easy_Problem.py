x = int(input())
y = list(map(int, input().split()))
hard = False
for question in y:
    if question == 0:
        continue
    else:
        print("HARD")
        hard = True
        break

if not hard:
    print("EASY")