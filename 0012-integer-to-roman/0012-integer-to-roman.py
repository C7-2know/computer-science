class Solution:
    def intToRoman(self, num: int) -> str:
        roman=""
        num=str(num)
        romans = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        digits = [1, 5, 10, 50, 100, 500, 1000]
        for i in range(len(num)):
            s= 10**(len(num)-i-1)
            n = int(num[i])*s
            if num[i] == '4' or num[i]=='9':
                n+= s
                i= len(digits)-1
                st= True
                while n>0:
                    if digits[i] > n:
                        i-=1
                    else:
                        if st:
                            j=i
                            while True:
                                if digits[j]!= s:
                                    j-=1
                                else:
                                    roman += romans[j]
                                    break
                            st= False
                        roman += romans[i]
                        n-=digits[i]
            else:
                i= len(digits)-1
                while n>0:
                    if digits[i] > n:
                        i-=1
                    else:
                        roman += romans[i]
                        n-=digits[i]
        return roman
