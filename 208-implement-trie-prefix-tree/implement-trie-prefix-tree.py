class Trie:

    def __init__(self):
        self.root = TrieNode("/")
        

    def insert(self, word: str) -> None:
        current = self.root
        for character in word:
            if character not in current.word_dict:
                current.word_dict[character] = TrieNode(character)
            current = current.word_dict[character]
        current.isWord = True        

    def search(self, word: str) -> bool:
        return self.search_helper(word, False)
        
    def search_helper(self, word, flag):
        current = self.root
        for character in word:
            if character not in current.word_dict:
                return False
            current = current.word_dict[character]
        return current.isWord if not flag else True

    def startsWith(self, prefix: str) -> bool:
        return self.search_helper(prefix, True)

class TrieNode:
    def __init__(self, character):
        self.word_dict = {}
        self.character = character 
        self.isWord = False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)