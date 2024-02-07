class Solution:
    def romanToInt(self, nums: str) -> int:
        map_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        total = 0
        for i in range(len(nums)):
            if i < len(nums)-1 and ((nums[i] == 'I' \
            and nums[i+1] in {'V', 'X'}) \
            or (nums[i] == 'X' and nums[i+1] in {'L', 'C'}) \
            or (nums[i] == 'C' and nums[i+1] in {'D', 'M'})):
                total -= map_dict[nums[i]]
            else:
                total += map_dict[nums[i]]
        return total
            

                    
