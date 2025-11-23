class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        """
        1. Red edges  [0, 1]      [1,2]
        2. blue edges none
        0 - 0 , 0-1 0-1-2 both edges are red hence -1
        collect all edges and stores in a dictionary a list of tuples.
        use dfs to traverse from 0 and see what nodes one can reach. Have an array full of -1s if there is an alternating path place the shortest distance else place it as -1 
        """
        map_dict = {}
        result = [-1]*(n)
        queue = []
        queue.append([0, "", 0])
        visited = set()
        for index, red in enumerate(redEdges):
            if red[0] not in map_dict:
                map_dict[red[0]] = []
            map_dict[red[0]].append((red[1], 'r'))
        for index, blue in enumerate(blueEdges) :
            if blue[0] not in map_dict:
                map_dict[blue[0]] = []
            map_dict[blue[0]].append((blue[1], 'b'))

        while queue:
            size = len(queue)
            for i in range(size):
                destination, color, counter = queue.pop(0)
                if result[destination] ==-1:
                    result[destination] = counter
                for index, value in enumerate(map_dict.get(destination, [])):
                    if (value[0], value[1]) in visited or value[1] == color:
                        continue
                    visited.add((value[0], value[1]))
                    queue.append([value[0], value[1], counter+1])
        return result
       

        