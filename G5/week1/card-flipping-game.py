class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        good=float('inf')
        front={i for i in fronts}
        back={i for i in backs}
        
        for i in range(len(fronts)):
            count=fronts.count(fronts[i])
            if count==1:
                if fronts[i]!=backs[i]:
                    good=min(good,fronts[i])
            else:
                indx=-1
                for j in range(count):
                    indx=fronts.index(fronts[i],indx+1)
                    if backs[indx]==fronts[indx]:
                        break   
                else:
                    good=min(good,fronts[i])
        for i in range(len(backs)):
            if backs[i] not in front:
                good=min(backs[i],good) 
        if good==float('inf'):
            return 0
        return good

            