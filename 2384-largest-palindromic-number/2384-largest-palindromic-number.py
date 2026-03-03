class Solution:
    def largestPalindromic(self, num: str) -> str:
        nums={}
        for i in num:
            if i not in nums:
                nums[i]=0
            nums[i]+=1
        out=''
        ls=''
        md=''
        keys=list(nums.keys())
        keys.sort(reverse=True)
        for key in keys:
            ln=nums[key]//2
            if md=='' and nums[key]%2!=0:
                md=str(key)
            if out == '' and key == '0':
                continue
            out+=str(key)*ln
            ls+=str(key)*ln
        return (out+md+ls[::-1]) if md or out else '0'
        



