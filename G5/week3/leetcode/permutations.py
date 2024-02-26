class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        def backtrack(indx,cand):
            if len(cand)==len(nums):
                arr.append(cand[:])
                return
            for j in range(len(nums)):
                if nums[j] not in cand:
                    cand.append(nums[j])
                    backtrack(j+1,cand)
                    cand.pop()
        backtrack(0,[])
        return arr
