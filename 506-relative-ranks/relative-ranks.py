class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        new_list = sorted(score)
        map_dict = {}
        counter = 4
        for i in range(len(new_list)-1, -1, -1):
            if i == len(new_list)-1:
                map_dict[new_list[i]] = "Gold Medal"
            elif i == len(new_list)-2:
                map_dict[new_list[i]] = "Silver Medal"
            elif i == len(new_list)-3:
                map_dict[new_list[i]] = "Bronze Medal"
            else:
                map_dict[new_list[i]] = str(counter)
                counter+=1

        return [map_dict[num] for num in score]
        