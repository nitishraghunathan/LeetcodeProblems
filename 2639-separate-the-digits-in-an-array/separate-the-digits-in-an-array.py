class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        string = ''
        for num in nums:
            string += str(num)
        result = []
        for i in range(len(string)):
            result.append(int(string[i]))
        return result