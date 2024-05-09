class Solution:
    def longestDecomposition(self, text: str) -> int:
        l=0
        r=len(text)-1
        l_w=""
        r_w=""
        count=0
        while l<=r:
            while text[l]!=text[r]:
                l_w+=text[l]
                l+=1
            l_w+=text[l]
            r_w=text[r-len(l_w)+1:r+1]
            print(r_w,l_w)
            if l_w==r_w:
                if l<r:
                    count+=2
                else:
                    count+=1
                r-=len(l_w)
                r_w=""
                l_w=""
                
            l+=1
        return count