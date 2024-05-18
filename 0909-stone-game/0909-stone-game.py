class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def dp(i,alice,bob):
            if i>=len(piles):
                return alice>bob
            return dp(i+1,alice+piles[i],bob) or dp(i+1,alice,bob+piles[i])
        return dp(0,0,0)