class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            if i not in graph:
                graph[i] = set()
        for pre in prerequisites:
            graph[pre[1]].add(pre[0])
        queue = []
        for key, value in graph.items():
            if len(value) ==0:
                queue.append(key)
        result= []
        while queue:
            node_id = queue.pop(0)
            result.insert(0, node_id)
            for key, value in graph.items():
                if node_id in value:
                    value.remove(node_id)
                    if len(value) == 0:
                        queue.append(key)
        if len(result) == numCourses:
            return True
        return False
