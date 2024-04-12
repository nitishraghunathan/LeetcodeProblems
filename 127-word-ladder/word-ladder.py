class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        word_dict = {}
        for word in wordList:
            for i in range(len(word)):
                new_word = word[:i] + '*' + word[i+1:]
                if new_word not in word_dict:
                    word_dict[new_word] = []
                word_dict[new_word].append(word)
        queue = []
        visited = set()
        queue.append(beginWord)
        visited.add(beginWord)
        counter = 1
        while queue:
            size = len(queue)
            for i in range(size):
                word = queue.pop(0)
                if word == endWord:
                    return counter
                for i in range(len(word)):
                    new_word = word[:i] + '*' + word[i+1:]
                    for iter_word in word_dict[new_word]:
                        if iter_word not in visited:
                            queue.append(iter_word)
                            visited.add(iter_word)
            counter+=1
        return 0

