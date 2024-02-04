class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        print(nums)
        result=[]
        for j in range(len(nums)):
            abs_d=0
            if j==0:
                num=nums[j]
                abs_d=nums[-1]-num*(len(nums)-1-j)-nums[j]
            else:
                num=nums[j]-nums[j-1]
                abs_d=num*j-nums[j-1]
                abs_d+=nums[-1]-num*(len(nums)-1-j)-nums[j]
            result.append(abs_d)
        return result