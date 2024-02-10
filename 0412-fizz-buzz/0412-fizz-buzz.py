class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for i in range(1,n+1):
            result = ""
            divisible = False
            if i % 3 == 0:
                result += "Fizz"
                divisible = True
            if i % 5 == 0:
                result += "Buzz"
                divisible = True

            if(divisible):
                answer.append(result)
            else:
                answer.append(str(i))

        return answer