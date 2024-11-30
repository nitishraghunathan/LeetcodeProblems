class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def recursion(candidates: List[int], target: int, candid_list: List[int], start: int):
            nonlocal result
            if target == 0:
                result.append(list(candid_list))
                return 
            elif target < 0:
                return 
            for i in range(start, len(candidates)):
                candid_list.append(candidates[i])
                recursion(candidates, target - candidates[i], candid_list, i)
                candid_list.pop()
            return 
        recursion(candidates, target, [], 0)
        return result