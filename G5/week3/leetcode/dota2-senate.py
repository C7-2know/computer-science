class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_q=deque()
        d_q=deque()
        for i in range(len(senate)):
            if senate[i]=='D':
                d_q.append(i)
            else:
                r_q.append(i)
        
        while d_q and r_q:
            d=d_q.popleft()    
            r=r_q.popleft()
            if r<d:
                r_q.append(r+len(senate))
            else:
                d_q.append(d+len(senate))
        if d_q:
            return 'Dire'
        else:
            return 'Radiant'    
