class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        map_dict = {
            '6': '9',
            '9': '6',
            '8': '8',
            '0': '0',
            '1': '1',
        }
        nums = str(num)
        i = 0
        j= len(nums)-1
        while i <= j:
            if nums[j] not in map_dict:
                return False
            if nums[i] != map_dict[nums[j]]:
                return False
            i+=1
            j-=1
        return True
