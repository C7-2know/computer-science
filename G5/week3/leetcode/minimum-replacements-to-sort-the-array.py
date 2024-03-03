class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>nums[i+1]:
                rem=nums[i]%nums[i+1]
                div=nums[i]//nums[i+1]

                if rem==0:
                    nums[i]=nums[i+1]
                    if div>=2:
                        div-=1
                    count+=div
                else:
                    div+=1
                    nums[i]//=div
                    count+=(div-1)
        return count
                    


