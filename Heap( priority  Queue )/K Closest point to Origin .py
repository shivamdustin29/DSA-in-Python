class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_size_heap = []
        for x, y in points:
            d = x**2 + y**2            
            heapq.heappush(k_size_heap, (-d, (x, y)))
            if len(k_size_heap) > k:
                heapq.heappop(k_size_heap)            
        return [tup[1] for tup in k_size_heap]
