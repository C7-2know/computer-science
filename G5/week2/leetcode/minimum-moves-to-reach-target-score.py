class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count=0
        while target>1:
            if maxDoubles==0:
                return int(count+target-1)
            elif target%2==0:
                count+=1
                target/=2
                maxDoubles-=1
                pass
            else:
                count+=1
                target-=1
        return int(count)