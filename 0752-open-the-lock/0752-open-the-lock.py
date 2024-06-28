class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        dead_set = set(deadends)
    
        if '0000' in dead_set or target in dead_set:
            return -1

        queue = deque([('0000', 0)])
        visited = set('0000')

        while queue:
            state, turns = queue.popleft()

            if state == target:
                return turns

            for i in range(4):
                for direction in [-1, 1]: 
                    
                    new_digit = (int(state[i]) + direction) % 10
                    new_state = state[:i] + str(new_digit) + state[i+1:]

                    if new_state not in visited and new_state not in dead_set:
                        visited.add(new_state)
                        queue.append((new_state, turns + 1))

        return -1
            