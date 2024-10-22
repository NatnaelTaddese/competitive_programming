class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        isprime = [True for _ in range(n+1)]
        isprime[0] = False
        isprime[1] = False

        i = 2

        while i * i <= n:
            if isprime[i]:
                j = i * i
                while j <= n:
                    isprime[j] = False
                    j+=i
            
            i += 1
        
        print(isprime)
        primes = 0
        for num in isprime:
            if num:
                primes += 1
        
        return primes