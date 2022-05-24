class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        lst=sorted(score,reverse=True)
        count={}
        for i in range (len(lst)):
            if (i==0):
                count[lst[i]]='Gold Medal'
            elif(i==1):
                count[lst[i]]='Silver Medal'
            elif(i==2):
                count[lst[i]]='Bronze Medal'
            else:
                count[lst[i]]= str(i+1)
        result=[]
        for i in score:
            result.append(count[i])
        return result
        
