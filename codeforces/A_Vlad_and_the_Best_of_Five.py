from collections import Counter


for _ in range(int(input())):
    phrase = list(input())
    freq = Counter(phrase)

    if freq.get('A', 0) >freq.get('B',0):
        print('A')
    else:
        print('B')