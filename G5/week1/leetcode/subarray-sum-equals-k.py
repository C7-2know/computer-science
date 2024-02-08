class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dc={0:1}
        total=0
        count=0
        for i in range(len(nums)):
            total+=nums[i]
            if total-k in dc:
                count+=dc[total-k]
            dc[total]=dc.get(total,0)+1
        
            
        # dc={}
        # total = 0
        # count=0
        # for i in range(len(nums)):
        #     total += nums[i]
        #     if total - k == 0:
        #         count += 1
        #     if total - k in dc:
        #         count+=dc[total-k]

        #     dc[total]=dc.get(total,0)+1
        
        # count=0
        # for j in range(len(nums)):
        #     if nums[j] in visited:
        #         continue
        #     elif nums[j]-k==0:
        #         count+=1
        #         if nums[j]-k in dc:
        #             count+=dc[nums[j]-k]
        #             visited[nums[j]-k]
        #     else:
        #         if nums[j]-k in dc:
        #             count+=dc[nums[j]-k]
        return count
            