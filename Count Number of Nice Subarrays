class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        no_nice = 0
        no_odd = 0
        start = 0
        for end in range(len(nums)):
            if nums[end]%2:
                no_odd += 1
                no_nice = 0
            while no_odd == k:
                if nums[start]%2:
                    no_odd -= 1
                no_nice += 1
                start += 1
            res += no_nice
        return res
