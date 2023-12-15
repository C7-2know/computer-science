class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_={}
        for j in range(len(nums)):
            dict_[nums[j]]=j
        for i in range(len(nums)):
            sec=target-nums[i]
            if sec in dict_:
                if dict_[sec]!=i:
                    return i,dict_[sec] 
