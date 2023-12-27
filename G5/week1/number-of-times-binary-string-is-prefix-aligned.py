class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_vis=0
        visited=0
        count=0
        for i in range(len(flips)):
            max_vis=max(max_vis,flips[i])
            visited+=1
            if visited==max_vis:
                count+=1
        return count

        