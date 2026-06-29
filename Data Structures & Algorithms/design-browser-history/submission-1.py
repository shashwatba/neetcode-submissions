class Node:
    def __init__ (self, url:str, next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.currentPage = self.head

        

    def visit(self, url: str) -> None:
        self.currentPage.next = Node(url, None, self.currentPage)
        self.currentPage = self.currentPage.next

        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.currentPage.prev:
                self.currentPage = self.currentPage.prev

        return self.currentPage.url

        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.currentPage.next:
                self.currentPage = self.currentPage.next

    
        return self.currentPage.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)