class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = nums[0]
        for i in nums[1:]:
            xor^=i
        return xor