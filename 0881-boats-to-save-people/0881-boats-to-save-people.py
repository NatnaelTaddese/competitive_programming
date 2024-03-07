class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # 5
        # 3, 3, 4, 5

        # 3
        # 1, 2, 2, 3
        # 
        people = sorted(people)

        left = 0
        right = len(people) - 1

        boats = 0

        while(left <= right):
            # just in case
            if (people[left] > limit):
                left +=1
                continue
            if (people[right] > limit):
                right -=1
                continue
            
            if(people[right] + people[left] <= limit):
                boats += 1
                left += 1
                right -= 1

            else:
                if(people[right] <= limit):
                    boats += 1
                    right -= 1
                    continue
                else:
                    right -= 1
                if (people[left] <= limit):
                    boats += 1
                    left += 1
                else:
                    left += 1

                
        
        return boats
                