class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        We need to construct a sequence from pushed to form popped
        1. We can iterate pushed array and check if we find the first matching element in the pushed array.
        2. Increase the counter in popped array and push elements till will find the next element which is the same
        3. If we hit the end of the list we stop
        4. We pop the elements in the stack and check with popped array if the sequence is formed
        5. We return our result based on the comparison
        """
        if not popped or not pushed or len(pushed) != len(popped):
            return False
        stack = []
        counter = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[counter]:
                counter +=1
                stack.pop()
        return len(stack) == 0