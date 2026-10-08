class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        map_dict = {}
        for licenses in licensePlate:
            if licenses.isalpha():
                if licenses.lower() not in map_dict:
                    map_dict[licenses.lower()] = 0
                map_dict[licenses.lower()] +=1
        result = ""
        for word in words:
            copy_dict = map_dict.copy()
            for i in range(len(word)):
                if word[i].lower() in copy_dict:
                    copy_dict[word[i].lower()]-=1
                    if copy_dict[word[i].lower()] == 0:
                        copy_dict.pop(word[i].lower())
                if not copy_dict:
                    if not result:
                        result = word
                    elif len(result) > len(word):
                        result = word
        return result

                
        