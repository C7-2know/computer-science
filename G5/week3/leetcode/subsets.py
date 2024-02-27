class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(nums,s_set,indx):
            # print(s_set,res,indx)
            if s_set not in res:
                res.append(s_set[:])
            for i in range(indx,len(nums)):
                if nums[i] not in s_set:
                    s_set.append(nums[i])
                    # backtrack(nums,s_set,indx+1)
                    backtrack(nums,s_set,i+1)
                    s_set.pop()
        backtrack(nums,[],0)
        return res
