def split(word): 
    return [char for char in word]  

for _ in range(int(input())):
    n, m, k = map(int, input().split())

    a = input()
    b = input()

    # if a in b:
    #     a , b = b , a
        

    a = ''.join(sorted(a))
    b = ''.join(sorted(b))

    a = split(a)
    b = split(b)

    result = []

    i = 0
    j = 0

    consecutive_a = 0
    consecutive_b = 0

    

    while(i < len(a) and j < len(b)):
        if a[i] < b[j]:
            if consecutive_a != k:
                result.append(a[i])
                consecutive_a += 1
                i+=1
            else:
                result.append(b[j])
                consecutive_a = 0
                consecutive_b += 1
                j+=1

        
        else:
            consecutive_a = 0

            if consecutive_b != k:
                result.append(b[j])
                j+=1
                consecutive_b += 1
            else:
                result.append(a[i])
                i+=1
                consecutive_b = 0
                consecutive_a += 1

            


    print("".join(result))

