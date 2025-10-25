class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        """
        Conditions
        1. Are the same letters found in each string
        2. If both strings are same, do they have repeating letters
        """
        if len(s) != len(goal):
            return False
        map_dict = {}
        duplicates = False
        for letter in s:
            if letter not in map_dict:
                map_dict[letter] = 0
            map_dict[letter] +=1
            if map_dict[letter] > 1:
                duplicates = True
        if s == goal:
            return duplicates
        difference = 0
        for index, letter in enumerate(goal):
            if letter not in map_dict or map_dict[letter]==0:
                return False
            map_dict[letter] -=1
            if letter != s[index]:
                difference+=1
        return difference<=2

            
            
        