class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        neg=[]
        pos=[]
        for i in range(len(nums)):
            if nums[i]<0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        min_am=min(len(neg),len(pos))
        j=1
        while j < len(pos):
            if len(neg)==0:
                break
            pos.insert(j,neg.pop(0))
            j+=2
        return pos+neg
                    
            