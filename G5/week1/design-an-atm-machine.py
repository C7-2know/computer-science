class ATM:

    def __init__(self):
        self.atm={20:0,50:0,100:0,200:0,500:0}
        self.money={0:20,1:50,2:100,3:200,4:500}
        # self.atm={i:0 for i in range(5)}
        # self.money=[20,50,100,200,500]
    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            money=self.money[i]
            self.atm[money]=self.atm.get(money,0)+banknotesCount[i]*1
        
    def withdraw(self, amount: int) -> List[int]:
        print('atm',self.atm)
#
        st=0
        for i in range(4,-1,-1):
            if amount>=self.money[i]:
                st=i
                break
        withd=[0,0,0,0,0]
        while amount>0:
            mon=self.money[st]
            print(self.atm[mon]-withd[st],amount>=self.money[st])
            if self.atm[mon]-withd[st]>0 and amount>=self.money[st]:
                mon=self.money[st]
                amnt=amount//mon
                if amnt > self.atm[mon]:
                    amnt=self.atm[mon]
                amount-=mon*amnt
                withd[st]+=amnt
            else:
                st-=1
            if st<0:
                break
        print(amount)
        if amount!=0:
            return [-1]
        for k in range(5):
            money=self.money[k]
            self.atm[money]-=withd[k]
        return withd

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)