money = int(input())
money = 30

notes = 0
bills = [100,20,6,1]

for bill in bills:
    if money == 0:
        break
    notes += money // bill 
    money %= bill

print(notes)