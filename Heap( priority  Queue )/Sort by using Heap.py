class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap=nums[:]
        heapify(heap)
        n=len(nums)

        for i in range(n):
            nums[i]=heappop(heap)
        return nums
