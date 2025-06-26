class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Create a dictionary keeping count of the task 
        create a max heap in python (use heapq with negative values to make min heap behave as a max heap)
        Iterate hrough the interval and pop the elements out and reduce the count by 1 if the the count  is zero don not add it back to the task list if it is then add it back
        """
        scheduler = {}
        for task in tasks:
            if task not in scheduler:
                scheduler[task] = 0
            scheduler[task] +=1
        queue = []
        for key, value in scheduler.items():
            heapq.heappush(queue, [-value, key])
        counter = 1
        while queue:
            task_result = []
            for i in range(n+1):
                if queue:
                    value, key = heapq.heappop(queue)
                    if value +1 < 0:
                        task_result.append([value+1, key])
                    if not queue and not task_result:
                        return counter
                counter +=1
            for task in task_result:
                heapq.heappush(queue, task)
        return counter       