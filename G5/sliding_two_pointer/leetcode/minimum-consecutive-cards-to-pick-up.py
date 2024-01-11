class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dc={}
        max_c=float('inf')
        count=0
        for i in range(len(cards)):
            if cards[i] in dc:
                count=i-dc[cards[i]]+1
                max_c=min(max_c,count)
                count-=1
                dc[cards[i]]=i
            else:
                dc[cards[i]]=i
        return -1 if max_c==float('inf') else max_c
            
            
             