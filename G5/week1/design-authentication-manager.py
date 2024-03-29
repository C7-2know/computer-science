class AuthenticationManager:


    def __init__(self, timeToLive: int):
        self.time_live=timeToLive
        self.tokens={}
        
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId]=currentTime+self.time_live
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens:
            if self.tokens[tokenId]>currentTime:
                self.tokens[tokenId]=self.time_live + currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        unexpired=0
        for tok,tim in self.tokens.items():
            if tim>currentTime:
                unexpired+=1
        return unexpired


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)