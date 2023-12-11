class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dict_={}
        for i in range(len(nums)):
            dict_[nums[i]]=i
        for i in range(len(operations)):
            indx=dict_[operations[i][0]]
            dict_.pop(operations[i][0])
            dict_[operations[i][1]]=indx
            nums[indx]=operations[i][1]
        return nums