class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_list = [(pos, vel) for pos, vel in zip(position, speed)]
        new_list.sort(reverse=True)
        stack=[]
        for pos, vel in new_list:
            stack.append((target-pos)/vel)
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)

            