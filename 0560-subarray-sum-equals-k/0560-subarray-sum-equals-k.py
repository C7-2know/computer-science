class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dc={}
        count=0
        
        if nums[0]==k:
            count+=1
        dc[nums[0]]=1
        for i in range(1, len(nums)):
            # if nums[i]==k:
            #     count+=1
            nums[i]+=nums[i-1]

            if nums[i]==k:
                count+=1
            if (nums[i]-k)in dc:
                count+=dc[nums[i]-k]
            if nums[i] not in dc:
                dc[nums[i]]=0
            dc[nums[i]]+=1
        return count