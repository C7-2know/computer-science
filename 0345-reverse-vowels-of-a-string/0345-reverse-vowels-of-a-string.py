class Solution:
    def reverseVowels(self, s: str) -> str:
        ans=""
        vowles = set(["A", "E", "I", "O", "U"])
        s=list(s)
        i,j= 0, len(s)-1
        while i<j and i<len(s):
            if s[i].upper() in vowles:
                while s[j].upper() not in vowles and j>=0:
                    j-=1
                s[i], s[j]= s[j], s[i]
                j-=1
            i+=1
        return "".join(s)
                