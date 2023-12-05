class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i=0
        out_put=[]
        while i <len(nums):
            pair=nums[i:i+2]
            freq_elm=[]
            for j in range(pair[0]):
                freq_elm.append(pair[1])
            i+=2
            out_put.extend(freq_elm)
        return out_put