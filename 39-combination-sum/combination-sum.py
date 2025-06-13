class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def recursion(new_list, index, sum_index):
            if sum_index == 0:
                result.append(list(new_list))
                return
            if sum_index < 0:
                return
            for i in range(index, len(candidates)):
                new_list.append(candidates[i])
                recursion(new_list, i, sum_index - candidates[i])
                new_list.pop()
            return
        recursion([], 0, target)
        return result
