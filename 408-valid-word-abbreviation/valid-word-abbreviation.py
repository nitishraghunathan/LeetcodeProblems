class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        1. only characters
        2. only numbers
        3. cannot have adjacent numbers 
        4. cannot have leading zeros 
        5. no empty substring replace 
        """
        index = 0
        number = -1
        length = len(word)
        new_string = ''
        for i in abbr:
            if i.isalpha():
                old_index= index
                index += number if number!=-1 else 0 
                if index < length and word[index] == i:
                    index +=1
                    new_string += word[old_index:index]
                    number= -1
                else:
                    return False
            else:
                if number == -1: 
                    if int(i) == 0:
                        return False
                    else:
                        number = int(i)
                else:
                    number = number*10+int(i)
        if number !=-1:
            if len(word)-index==number:
                return True
            else:
                return False
        return new_string == word
                
        