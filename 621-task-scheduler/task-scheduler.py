class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        We have a list of tasks, count them and create a map 
        A '3'
        B '3'
        create a priority Queue, max_queue A
        While Prirotiy queue, take list A if we havemore duplicate tasks 
        Run a for looptill range n+1 which would 
        return cpu units to compute
        """
        queue = []
        map_dict = {}
        for task in tasks:
            if task not in map_dict:
                map_dict[task] = 0
            map_dict[task] +=1
        for key, value in map_dict.items():
            heapq.heappush(queue, (-value, key))
        counter = 1
        while queue:
            task_result = []
            for i in range(n+1):
                if queue:
                    value, task = heapq.heappop(queue)
                    if value + 1 < 0:
                        task_result.append((value+1, task))
                    if not queue and not task_result:
                        return counter
                counter +=1
            for tasks in task_result:
                heapq.heappush(queue, tasks)
        return counter

                


         