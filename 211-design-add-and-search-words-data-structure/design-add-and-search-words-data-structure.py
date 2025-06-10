class WordDictionary:

    def __init__(self):
        self.root = Node("/")

    def addWord(self, word: str) -> None:
        current = self.root
        for index, value in enumerate(word):
            if value not in current.map_dict:
                current.map_dict[value] = Node(value)
            current = current.map_dict[value]
        current.is_word = True
            
    def search_helper(self, word: str, current: Optional["Node"]):
        for index, value in enumerate(word):
            if value == ".":
                for key, value in current.map_dict.items():
                    result = self.search_helper(word[index+1:], current.map_dict[key])
                    if result:
                        return True
                return False
            elif value not in current.map_dict:
                return False
            else:
                current = current.map_dict[value] 
        return current.is_word

    def search(self, word: str) -> bool:
        current = self.root
        return self.search_helper(word, current)
        
class Node:
    def __init__(self, char: str):
        self.key = char
        self.map_dict = {}
        self.is_word = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)