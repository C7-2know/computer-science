class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        j,k=0,0
        res=[]
        while j< len(firstList) and k<len(secondList):
            min1,max1=firstList[j]
            min2,max2=secondList[k]
            min_=max(min1,min2)
            max_=min(max1,max2)
            if min_<=max_:
                res.append([min_,max_])
            if max2>max_:
                j+=1
            else:
                k+=1
        return res
        
            
