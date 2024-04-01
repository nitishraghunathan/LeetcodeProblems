class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        longest_string = 0
        result = set() 
        def dfs(s, index, string_array, left, right):
            nonlocal longest_string
            if index == len(s):
                if left == right:
                    if len(string_array) > longest_string:
                        result.clear()
                        longest_string = len(string_array)
                        result.add(''.join(string_array))
                    elif len(string_array) == longest_string:
                        result.add(''.join(string_array))
                return
            if s[index] == '(':
                string_array.append(s[index])
                dfs(s, index+1, string_array , left+1, right)
                string_array.pop()
                dfs(s, index+1, string_array, left, right)
            elif s[index] == ')':
                dfs(s, index+1, string_array, left, right)
                if left > right:
                    string_array.append(s[index])
                    dfs(s, index+1, string_array, left, right+1)
                    string_array.pop()
            else:
                string_array.append(s[index])
                dfs(s, index+1, string_array, left, right)
                string_array.pop()
        dfs(s,0,[], 0,0)
        return list(result)

        