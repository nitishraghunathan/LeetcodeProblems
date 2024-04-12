class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        1. Add the beginword to the list if endword not in the list return 0
        2. add all wild card combinations of everyword in the list with one letter matched as wild card
        3. Start with beginWord and find all words at distance 1,
            -creare the same wildcard match words validate the values i the dictionary 
            a. if not visited add them to the queue and visited set 
            b.else proceed with other words 
        4. If we find the end word submit the step else return 0
        """
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

