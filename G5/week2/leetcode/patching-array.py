class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        r_sum=0
        count=0
        nums.append(n)
        for i in range(len(nums)):
            # print(r_sum,i,count)
            while r_sum+1<nums[i]:      # we do this because r_sum+1 is already present in the given array so we don't have to count it
                r_sum+=(r_sum+1)
                count+=1
                if r_sum>n:
                    break
            r_sum+=nums[i]
            if r_sum>n:
                break
        return count

