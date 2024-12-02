class Solution:
    def subsets(self, nums):
        self.output = []
        self.n, self.k = len(nums), None
        for self.k in range(self.n + 1):
            self.backtrack(0, [], nums)
        return self.output

    def backtrack(self, first, curr, nums):
        if len(curr) == self.k:
            self.output.append(curr[:])
        for i in range(first, self.n):
            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums)
            curr.pop()