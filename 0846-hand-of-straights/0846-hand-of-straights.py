class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        dc = {}
        for i in hand:
            if i not in dc:
                dc[i]=0
            dc[i]+=1
        cards = []
        for i in hand:
            if dc[i]==0:
                continue
            cards.append([i])
            dc[i]-=1
            while len(cards[-1]) < groupSize:
                next_= cards[-1][-1]+1
                if next_ not in dc or dc[next_] == 0:
                    return False
                dc[next_]-=1
                cards[-1].append(next_)
        return True