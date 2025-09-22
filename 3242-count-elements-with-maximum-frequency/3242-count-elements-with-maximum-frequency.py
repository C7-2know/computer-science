class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dc = {}
        for i in nums:
            if i not in dc:
                dc[i]=0
            dc[i]+=1
        counts = list(dc.values())
        counts.sort()
        maxs, i = 0, len(counts)-1
        while i>=0:
            if counts[i]<counts[-1]:
                return maxs*counts[-1]
            maxs+=1
            i-=1
        return maxs*counts[-1]