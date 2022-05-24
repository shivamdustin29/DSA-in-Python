********************************nlog(n) by max heap approch******************
class Solution(object):
    def frequencySort(self, s):
        mydict = {}
        for i in s:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        heap = []
        heapify(heap)
     
        for key,value in mydict.items():
            heappush(heap,(-1*value,key))
            
        res = ''
       
        while len(heap):
            value,key = heappop(heap)
            res += key * (-1*value)
        return res
      
      
      
      **********************************neive approch*********************
     class Solution(object):
    def frequencySort(self, s):
        count =Counter(s)
        return sorted(s, key=lambda c: [count.get(c), c],reverse =True)
