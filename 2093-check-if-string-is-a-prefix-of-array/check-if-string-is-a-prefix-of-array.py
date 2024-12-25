class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        new_string = ""
        for word in words:
            new_string += word
            if s[:len(new_string)] == new_string:
                if len(s) == len(new_string):
                    return True
            else:
                return False

        return False
                 
        