class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        for char in s:
            if ans and ans[-1] == char:
                ans.pop()
            else:
                ans.append(char)
        return ''.join(ans)
                

            