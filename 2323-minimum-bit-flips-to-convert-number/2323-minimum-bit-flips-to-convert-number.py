class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor=start^goal
        count=0
        for i in bin(xor)[2:]:
            if i=="1":
                count+=1
        return count