class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix1=''
        word=''
        letter=float("inf")
        for i in strs:
            letter=min(letter,len(i))
            word=i
        for i in range(letter):
            for j in strs:
                if word[i]!= j[i]:
                    return prefix1
            else:
                prefix1+=word[i]
        return prefix1
                   