class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet='abcdefghijklmnopqrstuvwxyz'
        dict_={f'{i}':alphabet[i-1] for i in range(1,len(alphabet)+1)} 

        word=''
        for i in range(len(s)):
            if s[i]=='#':
                word=word[:len(word)-1]
                word=word[:len(word)-1]
                word+=dict_[s[i-2]+s[i-1]]
            else:
                if s[i]=='0':
                    word+='.'
                else:
                    word+=dict_[s[i]]  
        return word