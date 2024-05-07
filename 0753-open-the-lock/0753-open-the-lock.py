class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends=set(deadends)
        queue=[target]
        direction=[1,-1]
        visited=set([target])
        opr=0
        while queue:
            size=len(queue)
            for i in range(size):
                cur=queue[i]
                if cur=="0000":
                    return opr
                for k in range(4):
                    for ch in direction:
                        num=ch+int(cur[k])
                        if num>9:
                            num=0
                        elif num<0:
                            num=9
                        new=cur[:k]+str(num)+cur[k+1:]
                        
                        if new not in deadends and new not in visited :
                            queue.append(new)
                            visited.add(new)
                            if new=="0000":
                                return opr+1
                            
                            # print(new)
            queue=queue[i+1:]
            opr+=1
        return -1
