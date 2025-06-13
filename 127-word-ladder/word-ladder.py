class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        1. check if endword is found int the transformation list, if yes then continue, if no tehn return 0
        2. Iterate the wordlist array and for every word in the wordlist create keys in the dictionary such that one letter is *(supposed to be the differing character) and the other letters untouched. The value for the corresponding key would be list, add the word to the list
        3. Create queue and add startword.
        4. Use bfs to iterate the shorted path and then add them to the queue
        5. Keep a counter everytime a bfs iteration is completed
        6. Once the end word is found return the word.
        """
        if endWord not in set(wordList):
            return 0
        word_dict = {}
        for word in wordList:
            size = len(word)
            for i in range(size):
                word_key = word[:i] + '*' + word[i+1:]
                if word_key not in word_dict:
                    word_dict[word_key] = []
                word_dict[word_key].append(word)
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
                word_size = len(word)
                for i in range(word_size):
                    word_key = word[:i] + '*' + word[i+1:]
                    if word_key in word_dict:
                        new_list = word_dict[word_key]
                        for new_word in new_list:
                            if new_word not in visited:
                                visited.add(new_word)
                                queue.append(new_word)
            counter+=1
        return 0

        