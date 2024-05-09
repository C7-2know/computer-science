class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def dp(n):
            if n>=len(nums):
                return 0
            if n in memo:
                return memo[n]
            take = nums[n] + dp(n + 2)
            dontake = dp(n + 1)
            memo[n] = max(take,dontake)
            return memo[n]
        return dp(0)


        # value=[(nums[1],nums[0],0)]
        # set_={i:0 for i in range(len(nums))}
        # for i in range(1,len(nums)-1):
        #     value.append((nums[i-1]+nums[i+1],(nums[i]),i))
        # value.append((nums[len(nums)-2],nums[len(nums)-1],len(nums)-1))
        # money=0
        # heapify(value)
        # while set_:
        #     lose,h,i=heappop(value)
        #     print(i)
        #     if i not in set_:
        #         continue
        #     if i-1 in set_:
        #         set_.pop(i-1)
        #     if i+1 in set_:
        #         set_.pop(i+1)
        #     set_.pop(i)
        #     money+=h
        # return money