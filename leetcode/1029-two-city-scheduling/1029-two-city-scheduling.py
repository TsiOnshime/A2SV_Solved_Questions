class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # calculate the diff between the two costs

        # b - a => if b - a is greater it means the cost of going to b is higher 
        # [[10], [170], [-350], [-10]]

        # so the second person should not go to city b since city b's price is so high
        # the third person should  go to city b because city b's price is so low

        # [[-350], [-10], [10], [170]]

        # so the first n values should go to city b and the rest should go to a

        sorted_costs = []

        for i in range(len(costs)):
            sorted_costs.append([costs[i][1] - costs[i][0], i])
            
        sorted_costs.sort(key=lambda x: x[0])
        
        count = 0
        half = len(costs) // 2
        total_cost = 0
        for i in range(len(costs)):
            if count < half:
                idx = sorted_costs[i][1]
                total_cost += costs[idx][1]
            else:
                idx = sorted_costs[i][1]
                total_cost += costs[idx][0]
            count += 1

        return total_cost



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna