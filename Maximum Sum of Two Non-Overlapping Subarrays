class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        maxSum = 0
        i = 0
        max1 , max2 = 0, 0
        while i < (len(nums) - firstLen) + 1:
            max1 = sum(nums[i:i + firstLen])
            if secondLen <= len(nums) - (i + firstLen):
                j = 0
                while j <= len(nums) - (i + firstLen + secondLen):
                    max2 = sum(nums[i + j + firstLen: i + j + firstLen + secondLen])
                    maxSum = max(maxSum, max1 + max2)
                    j += 1
            if secondLen <= i:
                j = 0
                while j <= i - secondLen:
                    max2 = sum(nums[j:j + secondLen])
                    maxSum = max(maxSum, max1 + max2)
                    j += 1
            i += 1
        return maxSum
