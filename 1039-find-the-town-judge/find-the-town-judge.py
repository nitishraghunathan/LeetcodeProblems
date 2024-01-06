class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        map_dict = {}
        judge_dict = {}
        if n==1 and not trust:
            return 1
        for plebs in trust:
            if plebs[0] not in map_dict:
                map_dict[plebs[0]] = []
            map_dict[plebs[0]].append(plebs[1])
            if plebs[1] not in judge_dict:
                judge_dict[plebs[1]] = []
            judge_dict[plebs[1]].append(plebs[0])
        for i in range(0, n+1):
            if i not in map_dict and (i in judge_dict and len(judge_dict[i]) == n-1):
                return i
        return -1