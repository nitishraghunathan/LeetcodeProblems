class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # remove adjacent duplicates but preserve order
        stack = []
        for num in nums:
            if stack and stack[-1] == num:
                continue
            else:
                stack.append(num)
        count = 0
        for i in range(1, len(stack)-1):
            if (stack[i] > stack[i-1] and stack[i] > stack[i+1]) or (stack[i] < stack[i-1] and stack[i] < stack[i+1]):    
                count += 1
        return count  

