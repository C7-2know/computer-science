class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_dis=float('inf')
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                summ=nums[j]+nums[k]
                # print(nums[i],[nums[k],nums[j]])
                if abs(target-min_dis)>abs(target-(nums[i]+summ)):
                    min_dis=nums[i]+summ
                # if summ==target:
                #     break
                if summ+nums[i]<target:
                    j+=1
                else:
                    k-=1
        return min_dis
