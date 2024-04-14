for _ in range(int(input())):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    k = 0
    result = []
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        swapped = False
        for j in range(i+1, n):
            if a[j] < a[min_idx] or b[j] < b[min_idx]:
                min_idx = j
                swapped = True
                # the answer was 1-indexed (Read next time)
                result.append([min_idx + 1, i + 1])
                k += 1
        if swapped:
            a[i], a[min_idx] = a[min_idx], a[i]
            b[i], b[min_idx] = b[min_idx], b[i]

    isSorted = True
    # check if a is sorted first
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            isSorted = False
            break
    
    for i in range(n - 1):
        if b[i] > b[i + 1]:
            isSorted = False
            break
    
    if  not isSorted:
        print(-1)
    else:
        print(k)
        for i in result:
            print(i[0],i[1])