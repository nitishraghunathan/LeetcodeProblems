class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        toopological_sort = [0]*numCourses
        in_degree = [0]*numCourses
        queue = []
        for course in prerequisites:
            in_degree[course[1]] +=1
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
        print(in_degree)
        index = numCourses-1
        while queue:
            destination = queue.pop(0)
            toopological_sort[index] = destination
            index-=1
            for i in range(len(prerequisites)):
                if prerequisites[i][0] == destination:
                    in_degree[prerequisites[i][1]] -=1
                    if in_degree[prerequisites[i][1]] == 0:
                        queue.append(prerequisites[i][1])
        print(toopological_sort)
        if index!=-1:
            return []
        return toopological_sort

        