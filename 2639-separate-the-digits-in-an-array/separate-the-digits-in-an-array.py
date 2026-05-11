class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.extend(list(str(num)))
        for i in range(len(ans)):
            ans[i]=int(ans[i])
        return ans