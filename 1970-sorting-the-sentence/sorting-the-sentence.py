class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        result = ['']*len(words)
        for word in words:
            print(word[len(word)-1])
            result[int(word[len(word)-1])-1] = word[:len(word)-1] + ' '
        return ''.join(result).strip()