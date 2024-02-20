class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[0]
        ans=[0]*len(temperatures)
        for i in range(1,len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                ind=stack.pop()
                ans[ind]=i-ind
            stack.append(i)
        return ans
                    