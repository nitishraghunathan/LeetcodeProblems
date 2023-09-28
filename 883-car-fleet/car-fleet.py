class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        1. Sort all the vehicles by position and speed
        2. Add them to a stack ande check if time taken is less than the other car if yes then a fleet is not formed and we pop the time out. If not we continue forming a new fleet
        3. we return the length of the stack
        """
        new_list = [(pos,vel) for pos, vel in zip(position, speed)]
        new_list.sort(reverse=True)
        stack = []
        for pos, vel in new_list:
            stack.append((target-pos)/vel)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
