for _ in range(int(input())):
    n = int(input())
    s = input()
    s = list(s)

    moves_availble = True
    # simulation for now.., couldn't come up with a better solution 
    # count_a = 0
    # for i in range(n - 1):
    count = 0

    used_indexes = set()

    while moves_availble:
        moves_availble = False
        for i in range(n - 1):
            if i in used_indexes:
                continue

            if s[i] == 'A' and s[i + 1] == 'B':
                moves_availble = True
                s[i], s[i + 1] = s[i + 1], s[i]
                used_indexes.add(i)
                count += 1
    
    print(count)

        
