class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        dc={'a','e','i','o','u'}
        count=0
        for j in range(k):
            if s[j] in dc:
                count+=1
        max_voule=count
        for i in range(k,len(s)):
            if s[i] in dc:
                if s[i-k] not in dc:
                    count+=1
            elif s[i-k] in dc:
                count-=1
            max_voule=max(count,max_voule)
        return max_voule