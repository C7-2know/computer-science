class Solution:
    def printVertically(self, s: str) -> List[str]:
        outpt=[]
        max_word_len=1
        i=0
        s=s.split(' ')
        while max_word_len>0 :
            word=''
            print(max_word_len)
            for j in range(len(s)):
                if i==0:
                    if len(s[j])>max_word_len:
                        max_word_len=len(s[j])
                if i>=len(s[j]):
                    word+=' '
                else:
                    word+=s[j][i]
                print(word.rstrip(' '))
            outpt.append(word.rstrip(' '))
            word=''
            max_word_len-=1
            i+=1
            print(outpt)
        return outpt

           