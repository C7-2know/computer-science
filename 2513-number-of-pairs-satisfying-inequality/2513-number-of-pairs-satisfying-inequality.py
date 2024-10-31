class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        new_arr=[nums1[i]-nums2[i] for i in range(len(nums1))]
        def divide(arr):
            if len(arr)<2:
                return arr,0
            mid=len(arr)//2
            left,num1=divide(arr[:mid])
            right,num2=divide(arr[mid:])
            res,num= merge(left,right)
            return res,num+num2+num1
        
        def merge(left,right):
            i,j=0,0
            new=[]
            num=0
            while i<len(left)and j<len(right):
                if left[i]<=right[j]+diff:
                    num+=len(right)-j 
                    i+=1
                else:
                    j+=1 
            i,j=0,0
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    new.append(left[i])
                    i+=1
                else:
                    new.append(right[j])
                    j+=1
            while i<len(left):
                new.append(left[i])
                i+=1
            while j<len(right):
                new.append(right[j])
                j+=1
            return new,num
        arr,ans=divide(new_arr)
        return ans