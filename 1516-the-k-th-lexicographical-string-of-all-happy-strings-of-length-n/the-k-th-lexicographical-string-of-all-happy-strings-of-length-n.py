class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        sequence = ['a', 'b', 'c']
        def dfs(sequence, new_str, length, result):
            if len(new_str) == length:
                result.append(new_str)
                return result
            for i in sequence:
                if len(new_str) == 0:
                    result = dfs(sequence, str(new_str)+ i, length, result)
                else:
                    if i!= new_str[len(new_str)-1]:
                        result = dfs(sequence, str(new_str)+ i, length, result)
            return result
        result = dfs(sequence, '', n, result)
        return result[k-1] if len(result) >=k else ''

