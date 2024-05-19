for _ in range(int(input())):
    prgmr, mths = map(int, input().split())
    '''
    a = 17 % 4 = 1
    b = 2 % 4 = 0

    a = 17 % 4 = 1
    b = 2 % 4 = 0

    max allowed = 2 which is the minimum 

    '''
    # ans = min(prgmr, mths) * (mths + prgmr) //2 
    # print(ans)

    team1 = min(mths, prgmr)
    team2 = (mths + prgmr) // 4

    print(min(team1,team2))