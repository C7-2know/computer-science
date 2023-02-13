class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        i = 0
        j = len(piles)-1
        stack = []
        piles.sort()
        while i < j-1:
            stack.append(piles[j-1])
            i += 1
            j -= 2
        return sum(stack)
