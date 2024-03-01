class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def combSum(candidates,cand,target,ind):
            if sum(cand)==target:
                cop=cand.copy()
                cop.sort()
                ans.append(cop)
                return
            for i in range(ind,len(candidates)):
                cand.append(candidates[i])
                if sum(cand)<=target:
                    combSum(candidates,cand,target,i)
                cand.pop()
            return
        combSum(candidates,[],target,0)
        return ans