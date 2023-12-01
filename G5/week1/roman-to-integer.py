class Solution:
    def romanToInt(self, s: str) -> int:
        dict_={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num=0
        for i in range(len(s)):
            if i>=1 and dict_[s[i]]>dict_[s[i-1]]:
                num+=dict_[s[i]]-dict_[s[i-1]]
                num-=dict_[s[i-1]]
                print(num)
            else:
                num+=dict_[s[i]]
        return num