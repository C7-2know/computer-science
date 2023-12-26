class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first=float('inf')
        second=float('inf')
        for i in nums:
            if i<=first:
                first=i
            elif i<=second:
                second=i
            else:
                return True      
        
        # if len(nums)<3:

        #     return False
        # nums=nums[::-1]
        # n1=nums[2]
        # n2=nums[1]
        # n3=nums[0]
        
        # for i in range(3,len(nums)):
        #     if n3>n2>n1:
        #         return True
        #     if n3<n2 and n1>n2:
        #         n3=n2
        #         n2=n1
        #         n1=nums[i]
        #         continue
        #     if n2<n1 and n1<n3:
        #         n2=n1
        #         n1=nums[i]
        #         continue
        #     else:
        #         n1=min(n1,nums[i])
        #     print(n1,n2,n3)
        # if n1<n2<n3:
        #     return True
        # return False


        #     if m1<m2 and m2<m3:
        #         return True
        #     if m2<m1 :
        #         m1=m2
        #         m2=m3
        #     if m3<m2 :
        #         m2=m3
        #     if m2==m3:
        #         m3=nums[i]
        #     else:
        #         m3=max(m3,nums[i])
        #     print(m1,m2,m3)
        # if m1<m2 and m2<m3:
        #     return True
        # return False