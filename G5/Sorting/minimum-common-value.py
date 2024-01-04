class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        first=0
        sec=0
        while first<len(nums1) and sec<len(nums2) and  nums1[first]!=nums2[sec]:
            if nums1[first]>nums2[sec]:
                sec+=1
            else:
                first+=1
            
        if first<len(nums1) and sec<len(nums2):
            return nums1[first]
        else:
            return -1