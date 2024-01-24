class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[]
        prod=math.prod(nums)
        num_zero=nums.count(0)
        for i in range(len(nums)):
            if num_zero>0:
                answer.append(math.prod(nums[:i]+nums[i+1:]))
            else:
                answer.append(int(prod/nums[i]))
        return answer