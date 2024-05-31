class Solution:

    def calculateLCM(self, a, b):
        return (a * b) // gcd(a, b)

    def calculateMax(self, count, divisor1, divisor2=1):
        lcm_result = self.calculateLCM(divisor1, divisor2)
        return count + count // (lcm_result - 1) - (0 if count % (lcm_result - 1) else 1)

    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        return max(
            self.calculateMax(uniqueCnt1, divisor1),
            self.calculateMax(uniqueCnt2, divisor2),
            self.calculateMax(uniqueCnt1 + uniqueCnt2, divisor1, divisor2)
        )