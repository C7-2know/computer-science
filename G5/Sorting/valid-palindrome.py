class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left<right:
            lef=s[left].lower()
            righ=s[right].lower()
            if (ord(lef)<97 or ord(lef)>122) and not lef.isnumeric() :
                left+=1
                if (ord(righ)<97 or ord(righ)>122) and not righ.isnumeric():
                    right-=1
                continue
            if (ord(righ)<97 or ord(righ)>122) and not righ.isnumeric():
                right-=1
                continue
            else:
                if ord(lef)!=ord(righ):
                    lef,righ
                    return False
                right-=1
                left+=1
        return True
