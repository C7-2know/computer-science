class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) ->bool:
        max_len=max(len(word1), len(word2))
        w1=''
        w2=''
        for i in range(max_len):
            if i<len(word1):
                w1+=word1[i]
            if i<len(word2):
                w2+=word2[i]
        return w1==w2
                