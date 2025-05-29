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
        dependent_courses = {}
        queue = []
        for i in range(numCourses):
            if i not in dependent_courses:
                dependent_courses[i] = set()

        for arr in prerequisites:
            if arr[0] not in dependent_courses:
                dependent_courses[arr[0]] = set()
            dependent_courses[arr[0]].add(arr[1])
        for key, value in dependent_courses.items():
            if len(value) == 0:
                queue.append(key)
        final_list = []
        while queue:
            size = len(queue)
            course_id = queue.pop(0)
            for key, value in dependent_courses.items():
                if course_id in value:
                    value.remove(course_id)
                    if len(value) == 0:
                        queue.append(key)
            final_list.append(course_id)
        return numCourses == len(final_list)
            


