class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        def bs(num,arr):
            left,right=0,len(arr)-1
            while left<=right:
                mid=(left+right)//2
                if arr[mid]<num:
                    left=mid+1
                else:
                    right=mid-1
            return left

        if len(instructions)<3:
            return 0
        nums=instructions[:2]
        nums.sort()
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        ans=0
        for i in range(2,len(instructions)):
            ind=bs(instructions[i],nums)
            equal=count.get(instructions[i],0)
            greater=len(nums)-ind-equal
            # if nums and ind<len(nums) and nums[ind]==instructions[i] and len(nums)-ind>equal+1:
            #     greater-=1
            ans+=min(greater,ind)
            if ind>len(nums)-1:
                nums.append(instructions[i])
            else:
                nums.insert(ind,instructions[i])
            # print(i,ind,nums,greater,ans)
            count[instructions[i]]=count.get(instructions[i],0)+1
        return ans%(10**9 + 7)

            
