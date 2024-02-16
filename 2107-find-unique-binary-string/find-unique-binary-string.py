class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        if not nums:
            return ''
        length = len(nums[0])
        nums_set = set(nums)
        seq = ['0', '1']
        counter = 0
        while True:
            new_str = ''
            index = 0
            while len(new_str) < length:
                new_str += random.choice(seq)
            if new_str not in nums_set:
                return new_str
        return ''