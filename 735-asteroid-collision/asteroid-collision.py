# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         while len(asteroids) > 1 and ((asteroids[-1] < 0 and asteroids[-2] > 0) or (asteroids[-1] > 0 and asteroids[-2] <0)):
#             first = asteroids.pop()
#             second = asteroids.pop()
#             abs_first = abs(first)
#             abs_second = abs(second)
#             if abs_first == abs_second:
#                 continue
#             elif abs_first > abs_second:
#                 asteroids.append(first)
#             else:
#                 asteroids.append(second)
            
#         return asteroids

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for n in asteroids:
            st.append(n)
            while len(st)>1 and ((st[-2]>0) and (st[-1]<0)):
                m,n = st.pop(),st.pop()
                if abs(m)!=abs(n):
                    if abs(m)>abs(n):
                        st.append(m)
                    else:
                        st.append(n)
        
        return st