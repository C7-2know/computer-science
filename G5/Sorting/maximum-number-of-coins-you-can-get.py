class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ind=len(piles)-2
        st=0
        coin=0
        while st<ind:
            coin+=piles[ind]
            st+=1
            ind-=2
        return coin