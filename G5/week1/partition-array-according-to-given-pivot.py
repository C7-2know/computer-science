class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_ind=0
        arr=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                arr.insert(less_ind,nums[i])
                less_ind+=1
            elif nums[i]==pivot:
                arr.insert(less_ind,pivot)
            else:
                arr.append(nums[i])
        return arr
            
