class TriNode:
    def __init__(self):
        self.children=[None for _ in range(26+1)]
        self.end=False

class WordDictionary:

    def __init__(self):
        self.root=TriNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            ind=ord(c)-ord('a')
            if cur.children[ind]==None:
                cur.children[ind]=TriNode()
            cur=cur.children[ind]
        cur.end=True
       


    def search(self, word,cur=None) -> bool:
        if cur==None:
            cur=self.root
        i=0        
        while cur!=None and i<len(word):
            if word[i]==".":
                ans=False
                for j in range(len(cur.children)):
                    if cur.children[j]!=None:
                        ans = ans or self.search(word[i+1:],cur.children[j])
                    if ans:
                        return ans
                return ans  
            ind=ord(word[i])-ord('a')
            if abs(ind)<26:
                cur=cur.children[ind]
            i+=1
        
        return cur and cur.end==True

        # while i<len(word):
        #     if word[i]==".":
        #         i+=1
        #         continue
        #     ind=ord(word[i])-ord('a')
        #     if not cur:
        #         return False
        #     if cur.children[ind]==None:
        #         return False
        #     cur=cur.children[ind]
        #     print(word[i],ind)
        #     if cur==None:
        #         return False
        #     i+=1
        # return cur.end



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)