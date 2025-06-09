class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        map_dict = {}
        for word in words:
            if word not in map_dict:
                map_dict[word] = 0
            map_dict[word] +=1
        result = []
        queue = []
        for key,value in map_dict.items():
            heapq.heappush(result, (-value, key))
        while k > 0:
            value, key = heapq.heappop(result)
            queue.append(key)
            k-=1
        return queue