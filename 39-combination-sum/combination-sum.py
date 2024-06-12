class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def recursion(sum_value, list_numbers,start):
            if sum_value == 0:
                result.append(list(list_numbers))
                return
            elif sum_value < 0:
                return 
            for i in range(start, len(candidates)):
                list_numbers.append(candidates[i])
                recursion(sum_value-candidates[i], list_numbers, i)
                list_numbers.pop()
        recursion(target,[],0)
        return result
