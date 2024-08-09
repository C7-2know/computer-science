class Solution:
    def minimumPushes(self, word: str) -> int:
        dc={}
        for i in word:
            if i not in dc:
                dc[i]=0
            dc[i]-=1
        arr=list(dc.values())
        heapify(arr)
        push=0
        turn=1
        key=2
        while arr:
            lt=abs(heappop(arr))
            push+=(lt*turn)
            key+=1
            if key>=10:
                key=2
                turn+=1
        return push
            