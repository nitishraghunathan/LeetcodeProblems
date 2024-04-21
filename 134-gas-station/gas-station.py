class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total_cost = 0
        start = 0
        for i in range(len(cost)):
            total_cost += gas[i]-cost[i]
            if total_cost < 0:
                total_cost = 0
                start = i+1
        return start
        