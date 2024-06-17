class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack) > 1 and stack[-1] < 0 and stack[-2] > 0:
                one = stack.pop()
                two = stack.pop()
                if abs(one) > abs(two):
                    stack.append(one)
                elif abs(two) > abs(one):
                    stack.append(two)
                else:
                    continue
        return stack