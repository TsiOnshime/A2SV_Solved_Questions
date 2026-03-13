class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    
        costs.sort(key= lambda x:  x[1] - x[0])
        print(costs)
        min_cost = 0

        l = 0
        r = len(costs) -1
        while l < r:
            ab = costs[l][0] + costs[r][1]
            ba = costs[l][1] + costs[r][0]

            l += 1
            r -= 1
            min_cost += min(ab, ba)
        return min_cost


      