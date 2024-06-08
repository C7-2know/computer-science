class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        memo={}
        def dp(i):
            if i==len(s)-1:
                if s[i].isalpha():
                    return [s[i].lower(),s[i].upper()]
                return [s[i]]
            if i not in memo:
                memo[i]=[]
                if s[i].isalpha():
                    pre=dp(i+1)
                    for w in pre:
                        memo[i].append((s[i]).lower()+w)
                        memo[i].append((s[i]).upper()+w)
                else:
                    pre=dp(i+1)
                    for w in pre:
                        memo[i].append(s[i]+w)
            return memo[i]
        return dp(0)
