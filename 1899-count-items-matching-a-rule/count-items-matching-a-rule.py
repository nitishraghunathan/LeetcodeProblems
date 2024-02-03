class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        map_dict ={
            'type' : 0,
            'color': 1,
            'name': 2,
        }
        for item in items:
            if ruleValue == item[map_dict[ruleKey]]:
                count +=1
        return count