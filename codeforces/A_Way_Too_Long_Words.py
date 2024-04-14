for _ in range(int(input())):
    phrase = input()
    if len(phrase) > 10:
        print(phrase[0] + str(len(phrase) - 2) + phrase[-1])
    else:
        print(phrase)