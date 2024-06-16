class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=nums[0]
        for i in nums[1:]:
            xor^=i
        n=0
        while xor>0:
            if (xor>>n)&1==1:
                break
            n+=1
        n = 0
        while (xor >> n) & 1 == 0:
            n += 1
        zeros=0
        ones=0
        for i in nums:
            if (i>>n)&1:
                ones^=i
            else:
                zeros^=i
        return [zeros,ones]
