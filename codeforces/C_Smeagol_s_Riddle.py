for _ in range(int(input())):
    swapped = 0

    # Operation
    word = input()
    s = [char for char in word]

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            swapped += 1
            left += 1
            right -= 1

    print(swapped)
