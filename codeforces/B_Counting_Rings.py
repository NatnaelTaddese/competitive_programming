smoke = input()

max_ring = 0
consecutive = 0

for i in range(0, len(smoke)):
    if smoke[i] == 'O':
        consecutive += 1
        max_ring = max(max_ring, consecutive)
    else:
        consecutive = 0

print(max_ring)