class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
            constructed_string = ""
            print(len(strs[0]))
            for i in range(len(strs[0])):
                for string in strs:
                    print(string[:i+1])
                    if string[:i+1] != strs[0][:i+1]:
                        return constructed_string
                constructed_string = strs[0][:i+1]
            return constructed_string

        