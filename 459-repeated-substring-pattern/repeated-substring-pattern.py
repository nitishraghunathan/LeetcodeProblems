class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2):
            sub_str = s[:i+1]
            check_flag = True
            for j in range(0, len(s), len(sub_str)):
                if s[j:j+len(sub_str)] != sub_str:
                    check_flag = False
                    break
            if check_flag:
                return True
        return False

        