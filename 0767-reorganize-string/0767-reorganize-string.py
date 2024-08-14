class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        answer = []
        prev_f, prev_c = 0, ''

        heap =[(-freq, char) for char, freq in count.items()]

        # print(heap)
        heapify(heap)
        # print(count)

        while heap:
            freq, char = heappop(heap)
            answer.append(char)

            if prev_f < 0:
                heappush(heap, (prev_f, prev_c))

            prev_f, prev_c = freq + 1, char
        
        answer = ''.join(answer) 


        for i in range(1, len(answer)):
            if answer[i] == answer[i-1]:
                return ""
        return answer if len(answer) == len(s) else ""
            