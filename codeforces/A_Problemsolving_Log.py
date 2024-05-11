for _ in range(int(input())):
    n = int(input())
    s = list(input())

    solved = 0

    minutes = dict()

    for i in range(len(s)):
        minutes[s[i]] = minutes.get(s[i], 0) + 1
    
    for key,value in minutes.items():
        if value > ord(key) - ord('A'):
            solved += 1
    

    print(solved)