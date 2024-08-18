class Solution:
    def reachNumber(self, target: int) -> int:
        moves=0
        st=0
        target=abs(target)
        while st<target:
            moves+=1
            st+=moves
        while (st-target)%2!=0:
            moves+=1
            st-=moves
        print(moves)
        return moves
        