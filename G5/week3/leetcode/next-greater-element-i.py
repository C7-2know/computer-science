class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dc={}
        stack=[]
        for i in nums2:
            while stack and stack[-1]<i:
                num=stack.pop()
                dc[num]=i
            stack.append(i)
        for i in range(len(nums1)):
            gnum=-1
            if nums1[i] in dc:
                print(nums1[i])
                gnum=dc[nums1[i]]
            nums1[i]=gnum
        return nums1