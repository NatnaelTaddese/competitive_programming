for _ in range(int(input())):
    nails = dict()
    n = int(input())
    for _ in range(n):
        nail, height = map(int,input().split())
        nails[nail] = height
    
    nails = sorted(nails.items(), key=lambda x: x[1], reverse=True)
    
    # print(nails)
    max_rope = 0
    cut = 0

    for n in nails:
        # if n[1] <= max_rope:
        #     cut += 1
        # else:
        #     max_rope = n[1]
        if n[0] - n[1] > 0:
            cut += 1
    
    print(cut)
