n, m = map(int, input().split())

flag = []

for _ in range(n):
    row = list(input().strip())
    flag.append(row)

# Function to check if all elements in a list are the same
def all_elements_same(row):
    return all(x == row[0] for x in row)

# Check if the flag meets the ISO standard
valid = True

for i in range(n):
    if not all_elements_same(flag[i]):
        valid = False
        break

for i in range(n - 1):
    if flag[i][0] == flag[i + 1][0]:
        valid = False
        break

if valid:
    print("YES")
else:
    print("NO")
