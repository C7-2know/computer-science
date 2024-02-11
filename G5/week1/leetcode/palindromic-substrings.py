class Solution:
    def countSubstrings(self, s: str) -> int:
        pali=0
        n=len(s)
        for i in range(n):
            pali_end=''
            for j in range(i,n):
                pali_end=s[j]+pali_end
                n_p=len(pali_end)
                if s[j+1:j+1+n_p]==pali_end:
                    pali+=1
                if s[j:j+n_p]==pali_end:
                    pali+=1
                # print(s[j+1:j+1+n_p],pali_end, s[j:j+n_p],pali)
        return pali