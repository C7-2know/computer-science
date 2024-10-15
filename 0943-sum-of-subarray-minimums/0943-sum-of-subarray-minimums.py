class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack=[]
        sum_=0
        for i in arr[::-1]:
            count=1
            while stack and stack[-1][0]>i:
                n,t=stack.pop()
                sum_+=(n*t*count)
                count+=t
            stack.append((i,count))
        count=0
        for num,t in stack[::-1]:
            sum_+=(num*t+(num*t)*count)%(10**9 + 7)
            count+=t
            
        return sum_%(10**9 + 7)