class Solution:
    def areSentencesSimilar(self, sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]) -> bool:
        if len(sentence2) != len(sentence1):
            return False
        map_dict = {}
        for index, value in enumerate(similarPairs):
            if value[0] not in map_dict:
                map_dict[value[0]] = set()
            map_dict[value[0]].add(value[1])
            if value[1] not in map_dict:
                map_dict[value[1]] = set()
            map_dict[value[1]].add(value[0])

        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue
            if sentence1[i] not in map_dict  or sentence2[i] not in map_dict[sentence1[i]]:
                return False
        return True
