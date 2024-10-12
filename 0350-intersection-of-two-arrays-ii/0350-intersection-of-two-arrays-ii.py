class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dc={}
        for i in range(len(nums1)):
            dc[nums1[i]]=dc.get(nums1[i],0)+1
        arr=[]
        for j in range(len(nums2)):
            k=nums2[j]
            if k in dc:
                dc[k]-=1
                if dc[k]==0:
                    dc.pop(k)
                arr.append(k)
        return arr