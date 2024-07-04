class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def search(num,arr):
            left,right=0,len(arr)
            while left<right:
                mid=(left+right)//2
                if arr[mid]<num:
                    left=mid+1
                else:
                    right=mid
            return left
            
        ans=[0]*len(nums)
        right=[nums[len(nums)-1]]
        for i in range(len(nums)-2,-1,-1):
            ind=search(nums[i],right)
            ans[i]=ind
            right.insert(ind,nums[i])
            # right=right[:ind]+[nums[i]]+right[ind:]
            # print('ans',ans)
        return ans
