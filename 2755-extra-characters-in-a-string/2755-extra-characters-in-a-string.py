class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        memo={}
        def dp(i,st):
            nonlocal memo
            if i>=len(st):
                return 0
            # print("call",i)
            if i not in memo:
                count=0
                for j in range(i,len(st)):
                    for k in range(j,len(st)):
                        if st[j:k+1] in dictionary:
                            t=k-j+1+dp(k+1,st)
                            count=max(count,t)
                        dt=dp(j+1,st)
                        count=max(count,dt)
                memo[i]=count
            return memo[i]
        ans=dp(0,s)
        return len(s)-ans
