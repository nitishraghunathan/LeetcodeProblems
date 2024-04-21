class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        check is sum of gas is less than cost 
        if yes then return no solution else there is atleast one solution 
        keep a total and start index 
        keep adding total with difference between gas and cost 
        if total is negative we  know that the start index is probably the position ahead of the current one
        keep doing it till we get a positive total 
        """
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
        