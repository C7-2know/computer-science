class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        seen=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                p1,p2=j+1, len(nums)-1
                while p1<p2:
                    sum_=nums[i]+nums[j]+nums[p1]+nums[p2]
                    if sum_==target:
                        if (nums[i],nums[j],nums[p1],nums[p2]) not in seen:
                            ans.append([nums[i],nums[j],nums[p1],nums[p2]])
                            seen.add((nums[i],nums[j],nums[p1],nums[p2]))
                        p1+=1
                    elif sum_>target:
                        p2-=1
                    else:
                        p1+=1
        return ans
                    