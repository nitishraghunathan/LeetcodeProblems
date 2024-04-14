class Solution:
    def alienOrder(self, words: List[str]) -> str:
        alien_dict = { alpha: set() for word in words for alpha in word}
        for i in range(len(words)-1):
            min_length = min(len(words[i]), len(words[i+1]))
            if len(words[i]) > len(words[i+1]) and words[i][:min_length] == words[i+1][:min_length]:
                return ''
            for j in range(min_length):
                if words[i][j]!= words[i+1][j]:
                    alien_dict[words[i][j]].add(words[i+1][j])
                    break
        result = []
        queue = []
        for node in alien_dict:
            if not alien_dict[node]:
                queue.append(node)
        while queue:
            node = queue.pop(0)
            result.insert(0, node)
            for rem in alien_dict:
                if node in alien_dict[rem]:
                    alien_dict[rem].remove(node)
                    if not alien_dict[rem]:
                        queue.append(rem)
        if len(alien_dict) != len(result):
            return ''

        return ''.join(result)
        