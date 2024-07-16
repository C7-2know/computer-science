class Solution:
    def canWinNim(self, n: int) -> bool:
        player='p1'
        turn = n%4
        if turn ==0:
            return False
        else:
            return True