class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        total = 0
        n = len(costs) // 2

        # for cost in costs:
        #     diff = abs(cost[0] - cost[1])
        #     cost.append(diff)
        costs.sort(key = lambda x: x[0] - x[1])
        for i in range(n):
            total += costs[i][0]
        for i in range(n, n * 2):
            total += costs[i][1]
        
        # sorted_list = sorted(costs, key=lambda x: x[2])
        # for i in range(len(costs) / 2):
        #     total += costs[i][0] + costs[len(costs) - i - 1][1]
         
        return total
        