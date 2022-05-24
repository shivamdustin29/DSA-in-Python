******************************by the help of Counter *******************
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mydict = Counter(words)
        # for i in words:
        #     if i in mydict:
        #         mydict[i] += 1
        #     else:
        #         mydict[i] = 1
        heap = []
        heapify(heap)
     
        for key,value in mydict.items():
            heappush(heap,(-1*value,key))
        while len(heap):
            return [heappop(heap)[1] for i in range(k)]
            
            ************************By the help of dict={}**************
            class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mydict = {}
        for i in words:
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
            #value,key = heappop(heap)
            return [heappop(heap)[1] for i in range(k)]
