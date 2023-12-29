class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # for i in range(len(nums)):
        #     if nums[i]>10:
        #         nums[i]/=10**(len(str(i))-1)
        # nums.sort()
        # st=''
        # for j in nums:
        #     st=st+str(j*010**(len(j)))
        # return st

        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if str(nums[i])+str(nums[j])<str(nums[j])+str(nums[i]):
                    nums[i],nums[j]=nums[j],nums[i]
        num="".join(str(i) for i in nums)
        return num if int(num)!=0 else "0"

        # print(3.000<3.00)