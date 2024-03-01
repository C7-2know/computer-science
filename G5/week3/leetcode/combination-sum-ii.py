class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def calculate(candidates,target,cand,ind):

            if sum(cand)==target:
                ans.append(cand[:])
                return
            i=ind
            while i<len(candidates):
                cand.append(candidates[i])
                if sum(cand)<=target:
                    calculate(candidates,target,cand,i+1)
                # if ( i==0 or candidates[i]!=candidates[i-1]):
                #     calculate(candidates,target,cand,i+1)
                cand.pop()
                while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                    i+=1
                i+=1
        calculate(candidates,target,[],0)
        return ans
                    