class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
    
        for i in nums1:
            stack = []
            index = nums2.index(i)
            counter = 0
            for j in range(index+1, len(nums2)):
                if nums2[j] >= i and not(stack) and counter < 1:
                    stack.append(nums2[j])
                    counter +=1
                elif nums2[j] >= i and stack and counter < 1:
                    top = stack.pop()
                    maxx= max(top , nums2[j])
                    stack.append(maxx)
                    counter +=1
            if not(stack):
                output.append(-1)
            else:
                output.append(stack.pop())
        return output
