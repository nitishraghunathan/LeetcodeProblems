class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
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

# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         st=[]
#         for n in asteroids:
#             st.append(n)
#             while len(st)>1 and ((st[-2]>0) and (st[-1]<0)):
#                 m,n = st.pop(),st.pop()
#                 if abs(m)!=abs(n):
#                     if abs(m)>abs(n):
#                         st.append(m)
#                     else:
#                         st.append(n)
        
#         return st