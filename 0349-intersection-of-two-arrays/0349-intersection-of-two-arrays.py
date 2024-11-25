class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set(nums1)
        nums2=list(set(nums2))
        com=[]
        for i in nums2:
            if i in set1:
                com.append(i)
        return com