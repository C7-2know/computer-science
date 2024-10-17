class Solution:
    def maximumSwap(self, num: int) -> int:
        nums=set([i for i in str(num)])
        nums=list(nums)
        nums.sort()
        dc={}
        for i in range(len(nums)):
            dc[nums[i]]=i
        arr=[0]*len(nums)
        for i in str(num):
            arr[dc[i]]+=1
        max_=len(arr)-1
        num=str(num)
        for i in range(len(num)):
            if num[i]!=nums[max_]:
                for j in range(i+1,len(num)):
                    if num[j]==nums[max_]:
                        arr[max_]-=1
                        if arr[max_]==0:
                            num=num[:i]+num[j]+num[i+1:j]+num[i]+num[j+1:]
                            return int(num)
            else:
                arr[max_]-=1
                if arr[max_]==0:
                    max_-=1
        return int(num)
                