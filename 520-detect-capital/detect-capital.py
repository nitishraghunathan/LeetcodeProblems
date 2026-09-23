class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        counter = 0
        flag = False
        for index, letter in enumerate(word):
            if index == 0 and letter == letter.upper():
                flag = True
            if letter != letter.lower():
                counter+=1
        return counter ==0 or counter == len(word) or (flag and counter==1)
        