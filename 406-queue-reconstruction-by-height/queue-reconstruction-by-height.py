class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        people = sorted(people, key=lambda x:(-x[0], x[1]))
        output = []
        for i in range(len(people)):
            output.insert(people[i][1], people[i])
        return output
