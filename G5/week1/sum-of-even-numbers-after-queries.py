class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        summ=0
        arr=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                summ+=nums[i]
        for i in range(len(queries)):
            indx=queries[i][1]
            num=queries[i][0]
            if nums[indx]%2!=0:
                nums[indx]+=num
                if num%2!=0:
                    summ+=nums[indx]
            else:
                if num%2==0:
                    summ+=num
                else:
                    summ-=nums[indx]
                nums[indx]+=num
            arr.append(summ)
        return arr
