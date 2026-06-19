class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_=0
        prev=0
        for i in gain:
            prev+=i
            max_=max(max_, prev)
        return max_