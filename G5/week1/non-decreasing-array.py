class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        mod=0
        for i in range(1,len(nums)):
            if nums[i]>=nums[i-1]:
                continue
            else:
                if i==1:
                    mod+=1
                elif nums[i]>=nums[i-2]:
                    mod+=1
                else:
                    nums[i]=nums[i-1]
                    mod+=1
            if mod>=2:
                return False
        return True

                    

        # for i in range(len(nums)-1):
        #     if nums[i]>nums[i+1]:
        #         mod+=1
        #     else:
        #         mod-=1
        # if mod<=1:
        #     return True
        # else:
        #     return False
