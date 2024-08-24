class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for ind,i in enumerate(temperatures):
            while stack and stack[-1][0]<i:
                ls=stack.pop()
                res[ls[1]]=ind-ls[1]
            stack.append((i,ind))
        return res
