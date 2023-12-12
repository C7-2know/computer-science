class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(' ')
        s=s[-1:-(len(s))-1:-1]
        arr=[]
        for i in range(len(s)):
            if s[i]!='':
                s[i]=s[i].strip()
                arr.append(s[i])
        arr=" ".join( arr)
        return arr 