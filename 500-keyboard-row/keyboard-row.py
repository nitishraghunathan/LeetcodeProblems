class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        set_one = {"q","w", "e","r","t","y","u", "i", "o", "p"}
        set_two = {"a","s", "d", "f", "g", "h","j", "k","l"}
        set_three = {"z","x","c","v","b","n","m"}
        result = []
        for word in words:
            flag_one, flag_two, flag_three = False, False, False
            break_flag = False
            for i in range(0, len(word)):
                if word[i].lower() in set_one:
                    if flag_two or flag_three:
                        break_flag = True
                        break
                    flag_one = True
                elif word[i].lower() in set_two:
                    if flag_three or flag_one:
                        break_flag = True
                        break
                    flag_two = True
                elif word[i].lower() in set_three:
                    if flag_one or flag_two:
                        break_flag = True
                        break
                    flag_three = True
            if not break_flag:
                result.append(word)
        return result


        