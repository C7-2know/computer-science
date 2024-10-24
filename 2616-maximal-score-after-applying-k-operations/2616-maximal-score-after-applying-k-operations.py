class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums=[-i for i in nums]
        heapify(nums)
        score=0
        while k>0:
            cur=heappop(nums)
            score+=(-1*cur)
            # print(floor(cur/3),cur)
            heappush(nums,(floor(cur/3)))
            k-=1
        return score