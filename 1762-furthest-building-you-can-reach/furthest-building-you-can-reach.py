class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Lets use maxheap to solve this problem,
        we iterate every building one by one and check the difference between the next and the current
        if difference is negative we know we are climbing down so we dont need to use ladder or bricks 
        else we use the difference as bricks and add the difference to the max queue
        if bricks are negative we pop the element from max heap and add it back to bricks if there is a ladder else we just return the current index
        In the end we just return the last index 
        """
        max_heap = []
        heapq.heapify(max_heap)
        for num in range(len(heights)-1):
            difference = heights[num+1] - heights[num]
            if difference < 0:
                continue 
            bricks -= difference 
            heapq.heappush(max_heap, -1*difference)
            if bricks < 0:
                if ladders > 0:
                    bricks += -1*heapq.heappop(max_heap)
                    ladders -=1 
                else:
                    return num
        return len(heights)-1




