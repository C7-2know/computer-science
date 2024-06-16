class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bits_={}
        for i in words:
            bit_='0b'+('0'*26)
            for l in i:
                ind=ord(l)-97
                bit_=bit_[:ind+2]+'1'+bit_[ind+3:]
            bits_[i]=bit_
        max_=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if int(bits_[words[i]],2)&int(bits_[words[j]],2)==0:
                    max_=max(max_,len(words[i])*len(words[j]))

        return max_

