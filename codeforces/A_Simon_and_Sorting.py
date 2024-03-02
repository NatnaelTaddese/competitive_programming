for _ in range(int(input())):
    test = input()
    test = [char for char in test]

    swapped = False
    for i in range(len(test)):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i+1, len(test)):
            if test[j] < test[min_idx]:
                min_idx = j
                swapped = True
        if swapped:
             test[i], test[min_idx] = test[min_idx], test[i]
             break
    
    if test[0] < test[1] and test[1] < test[2]:
        print("YES")
    else:
        print("NO")
       