class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        p1,p2=0,0
        res=[]
        while p1<len(nums1) and p2<len(nums2):
            i,val=nums1[p1]
            i2,val2=nums2[p2]
            if i==i2:
                res.append([i,val+val2])
                p1+=1
                p2+=1
            elif i<i2:
                res.append([i,val])
                p1+=1
            else:
                res.append([i2,val2])
                p2+=1
        if p1<len(nums1):
            res+=nums1[p1:]
        elif p2<len(nums2):
            res+=nums2[p2:]
        return res

