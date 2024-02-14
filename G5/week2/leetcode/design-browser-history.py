class Node:
    def __init__(self,page):
        self.page=page
        self.prev=None
        self.next=None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.home=Node(homepage)
        
    def visit(self, url: str) -> None:
        new_page=Node(url)
        self.home.next=new_page
        new_page.prev=self.home
        self.home=new_page

    def back(self, steps: int) -> str:
        curr=self.home
        for _ in range(steps):
            print('while viisting',curr.page)
            if curr and curr.prev:
                curr =curr.prev 
            else:
                self.home=curr
                return curr.page
        self.home=curr
        return curr.page
    def forward(self, steps: int) -> str:
        curr=self.home
        for _ in range(steps):
            if curr and curr.next:
                curr=curr.next
            else:
                self.home=curr
                return self.home.page
        self.home=curr
        return curr.page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)