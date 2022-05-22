class Solution(object):
    def findClosestElements(self, arr, k, x):
        l=[abs(a-x) for a in arr]
        x=list(zip(l,arr))
        heapq.heapify(x)
        p=[]
        for i in range(k):
            p.append(heapq.heappop(x)[1])
        return sorted(p)
        
        
        
