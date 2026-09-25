class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        new_result = ""
        for index, string in enumerate(s):
            s[index] = string[::-1]
            new_result += s[index] + " "
        return new_result.strip()

            
