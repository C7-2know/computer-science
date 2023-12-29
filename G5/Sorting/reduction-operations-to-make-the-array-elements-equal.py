class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        mn=min(nums)
        # count=nums.count(mn)
        dc={}
        nums.sort(reverse=True)
        for i in nums:
          dc[i]=dc.get(i,0)+1
        opr=0
        change=0
        for j in dc:
            # print(opr)
            if j==mn:
                continue
            change+=dc[j]
            opr+=change
        # print(dc)
        return opr