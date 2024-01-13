class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count=0
        p_sub=0
        right=0
        left=0
        odd=0
        while right<len(nums):
            if nums[right]%2!=0:
                odd+=1
                if p_sub!=0:
                    p_sub=0
            else:
                count+=p_sub
            while odd==k:
                count+=1
                p_sub+=1
                if nums[left]%2!=0:
                    odd-=1
                left+=1
            right+=1
            # print(odd,right,left,p_sub,count)
        return count
            
                
        
