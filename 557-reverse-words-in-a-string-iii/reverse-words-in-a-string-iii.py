class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        for index, string in enumerate(s):
            s[index] = string[::-1]
        new_result = ""
        for string in s:
            new_result += string + " "
        return new_result.strip()

            
