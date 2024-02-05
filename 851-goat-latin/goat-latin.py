class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        goat_sentence = ''
        vowels = {'a', 'e', 'i', 'o','u'}
        for index, value in enumerate(sentence.split(' ')):
            if value[0].lower() in vowels:
                goat_sentence += value + 'm' + (index+2)*'a' + ' '
            else:
                goat_sentence += value[1:] + value[0] +  'm' + (index+2)*'a' + ' '
        return goat_sentence.strip()
        