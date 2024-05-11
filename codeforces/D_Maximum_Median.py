'''
4 1 2 4 3 4 4
1 2 3 4 4 4 4: 7
1 2 3 4 4 4 5: 6
1 2 3 4 4 5 5: 5
1 2 3 4 5 5 5: 4
1 2 3 5 5 5 5: 3
1 2 3 5 5 5 6: 2
1 2 3 5 5 6 6: 1


1 1 1 1 2: 5
1 1 1 2 2: 4
1 1 2 2 2: 3
1 1 2 2 3: 2
1 1 2 3 3: 1

'''

n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

median = (n // 2)


while k > 0:
    if a[median + 1] - a[median] > 0:
        a[median] += (a[median + 1] - a[median])
        k -= (a[median + 1] - a[median])
        continue
    else:
        # break
        # find the difference between the next greater and the greater

        greater = median + 1
        next_greater = median + 2
        while(next_greater < n and k ):
            if a[next_greater] > a[greater]:
                #

    
    # find next greater
    # todo

print(a[median])


