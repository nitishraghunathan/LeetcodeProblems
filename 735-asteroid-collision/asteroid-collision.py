class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        """
        1. We will use a stack for this problem
        2. If the stack is empty push the asteroid to the stack
        3. Compare the the most reent element in the stack with the asteroid.
            if at most recent element and asteroid are in the same sign then push them to stack
            if different sign, pop the element from the stack and push the greater element, this might need a while loop.
        """
        def same_direction(a, b):
            if a < 0 and b > 0:
                return True
            return False
        for index, value in enumerate(asteroids):
            stack.append(value)
            while len(stack) > 1 and same_direction(stack[-1], stack[-2]):
                new_asteroid = stack.pop()
                old_asteroid = stack.pop()
                if abs(old_asteroid) == abs(new_asteroid):
                    continue
                elif abs(old_asteroid) > abs(new_asteroid):
                    stack.append(old_asteroid)
                else: 
                    stack.append(new_asteroid)
        return stack