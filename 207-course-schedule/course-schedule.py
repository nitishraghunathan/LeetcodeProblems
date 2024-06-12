class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map_dict ={}
        for i in range(numCourses):
            if i not in map_dict:
                map_dict[i] = set()
        for pre in prerequisites:
            map_dict[pre[1]].add(pre[0])
        queue = []
        for key, value in map_dict.items():
            if not value:
                queue.append(key)
        result = []
        while queue:
            id = queue.pop(0)
            result.insert(0, id)
            for key, value in map_dict.items():
                if id in value:
                    value.remove(id)
                    if not value:
                        queue.append(key)
        return len(result)==numCourses
