class Solution:
    def reverseWords(self, s: str) -> str:
        s= s.split(' ')
        res= ''
        for word in s:
            res+= ''.join(word[::-1])+' '
        return res[:len(res)-1]
            