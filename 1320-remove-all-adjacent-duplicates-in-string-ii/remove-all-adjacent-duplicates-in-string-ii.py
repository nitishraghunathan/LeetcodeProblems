class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        1. Need to deduplicate k instance fo an alphabet and rremove them
        2. We store all the alphabets with their count in  a stack
        3. We check the lats elemnt of the stack while iteration to see if the alphabet is the same, if same we increase the count if not we add the elemtn with count 1
        4. Once the count reaches K we pop the element from the stack
        5. we join by concatenating the elements in the stack
        """
        stack = []
        for character in s:
            if stack and stack[-1][0] == character:
                stack[-1][1] +=1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([character, 1])
        return "".join([count*character for character, count in stack])
        