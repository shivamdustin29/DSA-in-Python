####################### by using min heap #############

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        F_ans=[]
        n=len(nums)
        temp_heap=[(-1*nums[i], i) for i in range(k)]
        heapq.heapify(temp_heap)
        F_ans.append(-1*temp_heap[0][0])
        for i in range(k,n):
            while len(temp_heap)!=0 and i-temp_heap[0][1]>=k:
                heapq.heappop(temp_heap)
            heapq.heappush(temp_heap,(-1*nums[i],i))
            F_ans.append(-1*temp_heap[0][0])
        return F_ans
