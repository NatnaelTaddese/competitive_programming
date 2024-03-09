damge = list(map(int, input().split()))
soldiers = list(map(int, input().split()))

home = 0
other = 0

for i in range(0,3):
    home += damge[i] * soldiers[i]

for i in range(3,5):
    other += damge[i] * soldiers[i]

    

if home > other:
    print("WIN")
elif other  > home:
    print("LOSE")
else:
    print("DRAW")