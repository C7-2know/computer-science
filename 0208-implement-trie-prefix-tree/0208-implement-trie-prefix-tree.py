class Trie:

    def __init__(self):
        self.children=[None for _ in range(26)]    
        self.is_end=False    

    def insert(self, word: str) -> None:
        cur=self
        for l in word:
            ind=ord(l)-97
            if not cur.children[ind]:
                cur.children[ind]=Trie()
            cur=cur.children[ind]
        cur.is_end=True

    def search(self, word: str) -> bool:
        cur=self
        for l in word:
            ind=ord(l)-97
            if cur.children[ind]==None:
                return False
            cur=cur.children[ind]
        else:
            if cur.is_end:
                return True
            return False

        

    def startsWith(self, prefix: str) -> bool:
        cur=self
        for l in prefix:
            ind=ord(l)-97
            if cur.children[ind]==None:
                return False
            cur=cur.children[ind]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)