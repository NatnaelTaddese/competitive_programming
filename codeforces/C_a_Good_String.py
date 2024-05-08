def if_good(s, c):
    n = len(s)

    if n == 1:
        return 0 if s[0] == c else 1

    # else:
    #     # for c in s:
    #     #     if c != s[0]:
    #     #         return 1
    #             # return(if_good(s[0:len(s)//2]) + if_good(s[len(s)//2:len(s)]))
    #     for i in range(len())
    
    # return 0

    first_half = if_good(s[:n//2], c)
    

for _ in range(int(input())):
    n = int(input())
    s = input()

    print(if_good(s, 'a'))