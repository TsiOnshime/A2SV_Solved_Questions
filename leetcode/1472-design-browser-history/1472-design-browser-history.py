class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.visits = []
        self.forwards = []
        self.b = 0
        self.f = 0

    def visit(self, url: str) -> None:
        self.visits.append(url)
        self.forwards.clear()
     

    def back(self, steps: int) -> str:
        # print(self.visits)
        self.b = 0
        while self.visits and self.b < steps:
            # if self.visits[-1] == "youtube.com":
            #     print(self.vi)
            self.forwards.append(self.visits.pop())
            self.b += 1
        return self.visits[-1] if self.visits else self.homepage
        
        

    def forward(self, steps: int) -> str:
        self.f = 0
        while self.forwards and self.f < steps:
            self.visits.append(self.forwards.pop())
            self.f +=1
        return self.visits[-1] if self.visits else self.homepage 
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)