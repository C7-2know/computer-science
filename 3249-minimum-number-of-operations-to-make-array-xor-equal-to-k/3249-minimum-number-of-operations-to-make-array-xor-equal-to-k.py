class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor=nums[0]
        for i in nums[1:]:
            xor^=i
        org_len=xor.bit_length()
        count=0
        xor^=k
        b_xor=bin(xor)
        for i in b_xor:
            if i=='1':
                count+=1
        print(count)
        return count