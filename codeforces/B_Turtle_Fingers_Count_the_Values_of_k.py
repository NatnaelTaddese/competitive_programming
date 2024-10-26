for _ in range(int(input())):
    a, b, l = map(int, input().split())
    """
    k = l / (a*b)

    0, 0
    a=4,b=6,l=48


    Choose k=48,x=0,y=0 Then k⋅ax⋅by=48⋅40⋅60=48=l

    Choose k=8, x=0,y=1  Then k⋅ax⋅by=8⋅40⋅61=48=l

    Choose k=12,x=1,y=0 Then k⋅ax⋅by=12⋅41⋅60=48=l

    Choose k=2, x=1,y=1  Then k⋅ax⋅by=2⋅41⋅61=48=l
    
    Choose k=3, x=2, y=0  Then k⋅ax⋅by=3⋅42⋅60=48=l

    """
    ks = set()

    x = 0
    while(a**x <= l):
        y = 0
        while(a**x * b**y <= l):
            # k = l / (a*b)
            if l % (a**x * b**y) == 0:
                ks.add(l // (a**x * b**y))
            y += 1
        x += 1
    
    print(len(ks))
