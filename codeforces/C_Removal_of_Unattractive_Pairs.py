for _ in range(int(input())):
    length = int(input())
    phrase = input()
    result = list()
    moves_availble = True
    while moves_availble:
        if(len(phrase) < 2):
            moves_availble = False
            break

        for i in range(0,len(phrase) - 1):
            if phrase[i] == phrase[i+1]:
                moves_availble = False
                continue
            else:
                phrase.remove(i)
                phrase.remove(i+1)
                moves_availble = True
                break
    
    print()
            