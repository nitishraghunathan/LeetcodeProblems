class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        1. If the asteroid is positive, it is moving towards right.
        2. if the asteroid is negative, it is moving towards left.
        3. We are going to use a stack to store all asteroids.
        4. We will pop the stack elements if there is negative and postive asteroid else we continue adding elements to the stack.
        5. When there is a collison, we take the greatest asteroid if the size is unequal else we assume the asteroids destroy themselves.
        """
        stack = []
        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack) > 1 and (stack[-1] < 0 and stack[-2] > 0):
                first = stack.pop()
                second = stack.pop()
                abs_first = abs(first)
                abs_second = abs(second)
                if abs_first == abs_second:
                    continue 
                elif abs_first > abs_second:
                    stack.append(first)
                else:
                    stack.append(second)
        return stack