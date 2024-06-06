class TrieNode:
    def __init__(self):
        self.is_end=False
        self.children=[None for _ in range(26)]
class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        cur=self.root
        for i in word:
            ind=ord(i)-ord('a')
            if cur.children[ind]==None:
                cur.children[ind]=TrieNode()
            cur=cur.children[ind]
        cur.is_end=True
    

    def search(self, word: str) -> bool:
        cur=self.root
        inx=0
        ind=ord(word[0])-ord("a")
        while cur.children[ind]!=None and inx<len(word):
            cur=cur.children[ind]
            inx+=1
            if inx<len(word):
                ind=ord(word[inx])-ord("a")
        return cur.is_end and inx>=len(word)
        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        i=0
        ind=ord(prefix[i])-ord('a')
        while cur.children[ind]!=None and i<len(prefix):
            cur=cur.children[ind]
            i+=1
            if i<len(prefix):
                ind=ord(prefix[i])-ord('a')
        return i==len(prefix)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)