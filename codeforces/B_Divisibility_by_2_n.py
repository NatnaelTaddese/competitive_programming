for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    dividend = 2 ** n

    # debug
    print(dividend, end=": ")

    total = 1
    for i in a:
        total *= i
    
    print(total,"...",(total % dividend) )