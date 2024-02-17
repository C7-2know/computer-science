class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        ln=len(palindrome)
        if ln==1:
            return ''
        half=palindrome[:ln//2]
        # print(half)
        for i in range(len(half)):
            if ord(half[i])>97:
                half=half[:i]+chr(97)+half[i+1:]
                break
        else:
            if len(half)>0:
                palindrome=palindrome[:ln-1]+chr(ord(palindrome[-1])+1)
        half+=palindrome[ln//2:]
        return half