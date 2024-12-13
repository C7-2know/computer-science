class Solution:
    def findScore(self, nums: List[int]) -> int:
        zipp=[(nums[i],i) for i in range(len(nums))]
        marked=set()
        zipp.sort()
        i=0
        score=0
        while len(marked)<len(nums):
            num,ind=zipp[i]
            if ind not in marked:
                score+=num
                if ind-1>=0:
                    marked.add(ind-1)
                if ind+1<len(nums):
                    marked.add(ind+1)
                marked.add(ind)
            i+=1
        return score
        