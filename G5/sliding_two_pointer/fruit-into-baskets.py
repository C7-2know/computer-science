class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits)<=2:
            return len(fruits)
        dc={fruits[0]:1}
        dc[fruits[1]]=dc.get(fruits[1],0)+1
        left=0
        right=2
        sub=2
        max_s=sub
        while right<len(fruits):
            # print('dc',dc,sub)
            if fruits[right] not in dc:
                if len(dc)<2:
                    dc[fruits[right]]=1
                    sub+=1
                else:
                    rem=fruits[left]
                    while len(dc)==2:
                        dc[fruits[left]]-=1
                        if dc[fruits[left]]==0:
                            dc.pop(fruits[left])
                        left+=1
                        sub-=1
                    dc[fruits[right]]=1
                    sub+=1
            else:
                dc[fruits[right]]+=1
                sub+=1
            max_s=max(sub,max_s)
            right+=1
        return max_s
