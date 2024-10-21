primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

# arthimetic sum formula: n * (n + 1) // 2 

for _ in range(int(input())):
    n = int(input())
    mx_sum = 0    
    optimal_x = 2

    for x in range(2, n + 1):
        k = n // x

        curr = x * (k * (k + 1)) // 2

        if curr > mx_sum:
            mx_sum = curr
            optimal_x = x  
    
    print(optimal_x)

