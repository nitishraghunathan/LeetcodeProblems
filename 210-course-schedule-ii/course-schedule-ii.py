class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph_dict = {}
        for i in range(numCourses):
            if i not in graph_dict:
                graph_dict[i] = []
        for req in prerequisites:
            graph_dict[req[0]].append(req[1])
        queue = []
        for i in range(numCourses):
            if not graph_dict[i]:
                queue.append(i)
        result = []
        while queue:
            course_id = queue.pop(0)
            for key,value in graph_dict.items():
                if course_id in value:
                    value.remove(course_id)
                    if not value:
                        queue.append(key)
            result.append(course_id)
        return result if len(result) == numCourses else []