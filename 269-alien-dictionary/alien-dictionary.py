class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        1. Build the graph 
        2. If prefix of of words are same but lenght of first word is greater than second return no alienOrder 
        return new order
        we are using topological sort
        1. Do basic cvalidations 
            a. Same prefix but first word is greater than second return empty string.
            b. create a dictionary mapping of all those letters in each word.
        2. Add elements in the queue which hvae no adjacencies
        3. Pop each element from the queue and the elements from the lists which teh map keys have
        4. Once adjaceny of the key is zero add them to queue 
        5. Finally add the element to the result
        6. Validate the the length of the result and dictionary
        7 if they are the same return the order else return ''
        """
        graph = {alphabet:set() for word in words for alphabet in word}
        for i in range(len(words)-1):
            word_one, word_two = words[i], words[i+1]
            min_length = min(len(word_one), len(word_two))
            if word_one[:min_length] == word_two[:min_length] and len(word_one) > len(word_two):
                return ""
            for j in range(min_length):
                if word_one[j] != word_two[j]:
                    graph[word_one[j]].add(word_two[j])
                    break
        queue = []
        for key, value in graph.items():
            if len(value) == 0:
                queue.append(key)
        result = []
        while queue:
            size = len(queue)
            for i in range(size):
                alphabet = queue.pop(0)
                for key, value in graph.items():
                    if alphabet in value:
                        value.remove(alphabet)
                        if not value:
                            queue.append(key)
                result.insert(0, alphabet)
        if len(result) != len(graph):
            return ""
        return "".join(result)





       