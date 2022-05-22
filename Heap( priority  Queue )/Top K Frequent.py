class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
        
        # use a min heap to only maintain the k most frequent elements
        min_heap = []
        for val, freq in d.items():
            heapq.heappush(min_heap, (freq, val))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
              
        return [j for i, j in min_heap]
        
