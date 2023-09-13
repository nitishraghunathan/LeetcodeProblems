class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        we need to construct a sequence from pushed to form popped 
        1. We can iterate pushed array and check if we find the first matching element in popped array.
        2. then we increase counter in popped array and push elements till we find the next element.
        3. If we hit the end of the list we stop.
        4. we pop all the elements from the stack and compare with popped.
        5. If it is the same we will not find any issues.
        6. else we return false
        """
        if not popped or not pushed or len(pushed)!= len(popped):
            return False
        
        stack = []
        counter = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] ==  popped[counter]:
                    counter+=1
                    stack.pop()

        return len(stack) == 0
