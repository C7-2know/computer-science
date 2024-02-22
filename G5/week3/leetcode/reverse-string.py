class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Iterative approach
        # for i in range(len(s)//2):
        #     s[i],s[len(s)-1-i]=s[len(s)-1-i],s[i]
        # return s
        def rev(s,l,r):
            if l>=r:
                return
            s[l],s[r]=s[r],s[l]
            return rev(s,l+1,r-1)
        rev(s,0,len(s)-1)


        