class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for distance, velocity in sorted(zip(position,speed), reverse=True):
            required_distance= target - distance
            time = required_distance/velocity
            if not stack:
                stack.append(time)
            if stack[-1] < time:
                stack.append(time)
        return len(stack)

            