class Bitset:

    def __init__(self, size: int):
        self.size=size
        self.Bitset={i:'0' for i  in range(size)}
        self.Bit={'0':size}
        self.flips=0
    def fix(self, idx: int)-> None:
        if self.Bitset[idx]=='0'and self.flips%2==0:
            self.Bit['1']=self.Bit.get('1',0)+1
            self.Bit['0']=self.Bit.get('0')-1
            self.Bitset[idx]='1'

        if self.Bitset[idx]=='1'and self.flips%2!=0:
            self.Bit['1']=self.Bit.get('1',0)+1
            self.Bit['0']=self.Bit.get('0',0)-1
            self.Bitset[idx]='0'


    def unfix(self, idx: int) -> None:
        if self.Bitset[idx]=='1' and self.flips%2==0:
            self.Bit['1']=self.Bit.get('1',0)-1
            self.Bit['0']=self.Bit.get('0')+1
            self.Bitset[idx]='0'

        elif self.Bitset[idx]=='0' and self.flips%2!=0:
            self.Bit['1']=self.Bit.get('1',0)-1
            self.Bit['0']=self.Bit.get('0')+1
            self.Bitset[idx]='1'

    def flip(self) -> None:
        self.flips+=1
        # for i in self.Bitset:
        #     upd='0'
        #     if self.Bitset[i]=='0':
        #         upd='1'
        #     self.Bitset[i]=upd
        self.Bit['0']=self.Bit.get('1',0)
        self.Bit['1']=self.size-self.Bit['0']
    def all(self) -> bool:
        # print(self.Bitset.values(),self.Bit, self.flips)   
        # if self.flips%2!=0:
        #     return self.Bit.get('0',0)==self.size
        return self.Bit.get('1',0)==self.size
    def one(self) -> bool:
        # if self.flips%2!=0:
        #     return self.Bit.get('0',0)>=1
        return self.Bit.get('1',0)>=1
    def count(self) -> int:
        # if self.flips%2!=0:
        #     return self.Bit.get('0',0)
        return self.Bit.get('1',0)
    def toString(self) -> str:
        # print('flip',self.flips,self.Bit,self.Bitset.values())
        if self.flips%2!=0:
            out=''
            for i in self.Bitset:
                if self.Bitset[i]=='0':
                    out+='1'
                else:
                    out+='0'
            return out
            # self.flips=0
        return ''.join(self.Bitset.values())


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()