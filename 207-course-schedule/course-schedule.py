class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        1. Create a map of all courses and it depedencies
        2. Create a queue and add all the courses with zero depenncies 
        3. Iterate the map and use every element in the queue to remove dependencies
        4. There can be multiple orders
        5. remove each course from the map depdency as we are ordering them. 
        6. once any course has no more depdencies add them to the queue and find its dependent courses
        7. After completing the iteration add the element to the result
        8. Once all the queue elements are evaluated if the len of result != numOfCourses then we cannot form a course schedule 
        9. Otherwise we can
        """
        course_dictionary = {}
        for i in range(numCourses):
            if i not in course_dictionary:
                course_dictionary[i] = set()
        for req in prerequisites:
            course_dictionary[req[0]].add(req[1])
        queue = []
        for key, value in course_dictionary.items():
            if not value:
                queue.append(key)
        result = []
        while queue:
            course_id = queue.pop(0)
            result.append(course_id)
            for key, value in course_dictionary.items():
                if course_id in value:
                    value.remove(course_id)
                    if not value:
                        queue.append(key)
        return len(result) == numCourses