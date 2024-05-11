for _ in range(int(input())):
    k, q = map(int,input().split())
    a = list(map(int, input().split()))
    n = list(map(int, input().split()))

    # answer = []
    # for players in n:
        # playable range = index_of_min , index_of_max  compared to players
        # playable_range =
        # elimination per round
        # elimination = 1
    # prefix_sum = [0] * (k + 1)
    # for i in range(1, k+ 1):
    #     prefix_sum[i] = prefix_sum[i-1] + a[i - 1]

    # answer = []

    # for players in n:
    #     remaining = players

    #     round = 0

    #     while remaining > 0:
    #         round += 1
    #         remaining -= (prefix_sum[min(round, k)]  - prefix_sum[max(0, round - k)])
        
    #     answer.append(players - round)
    
    # print(*answer)

    answer = []

    for players in n:
        for index in reversed(a):
            if index > players:
                continue
            players = players - (players - index) - 1
        
        answer.append(players)
    
    print(*answer)