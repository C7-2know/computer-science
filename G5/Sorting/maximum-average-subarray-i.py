class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # summ=sum(nums[:k])
        # for i in range(1,len(nums)-k+1):
        #     new=summ-nums[i-1]+nums[k+i-1]
        #     summ=max(new,summ)
        #     print(nums[i-1],summ)
        # return summ/k

        w_sum=sum(nums[:k])
        max_sum=w_sum
        for i in range(1,len(nums)-(k-1)):
            # print(w_sum)
            w_sum=w_sum-nums[i-1]+nums[i+k-1]
            max_sum=max(max_sum,w_sum)
            # print(w_sum,max_sum,nums[i-1])
        return max_sum/k