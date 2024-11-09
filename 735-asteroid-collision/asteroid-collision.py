class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for asteroid in asteroids:
            result.append(asteroid)
            while len(result) > 1 and result[-1] < 0 and result[-2] > 0:
                a = result.pop()
                b = result.pop()
                if abs(a) > abs(b):
                    result.append(a)
                elif abs(b) > abs(a):
                    result.append(b)
                else:
                    continue
        return result