class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_w=''
        for i in range(len(word1)):
            new_w+=word1[i]
            if i<len(word2):
                new_w+=word2[i]
        i+=1
        if i<len(word2):
            new_w+=word2[i:]
        return new_w