class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones=nums[0:].count(1)
        zeros=0
        summ=ones
        indx=[0]
        for i in range(1,len(nums)+1):
            if nums[i-1]==0:
                zeros+=1
            else:
                ones-=1
            # print(nums[:i],nums[i:],zeros,ones)
            if zeros+ones>summ:
                summ=zeros+ones
                indx=[i]
            elif zeros+ones==summ:
                indx.append(i)
            # print(indx,summ)
        return indx



        # summ=0
        # indx=[]
        # for i in range(len(nums)+1):
        #     ones=nums[i:].count(1)
        #     zeros=nums[:i].count(0)
        #     if zeros+ones>summ:
        #         summ=zeros+ones
        #         indx=[i]
        #     elif zeros+ones==summ:
        #         indx.append(i)
        # return indx
