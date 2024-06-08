import random

def shuffle_string(s):
    s_list = list(s)
    while True:
        random.shuffle(s_list)
        r = ''.join(s_list)
        if r != s:
            return r



for _ in range(int(input())):
    s = input()

    if len(set(s)) == 1:
        print("NO")
    else:
        # sorted_s = ''.join(sorted(s))
        diff_str = shuffle_string(s)
        print("YES")
        print(diff_str)