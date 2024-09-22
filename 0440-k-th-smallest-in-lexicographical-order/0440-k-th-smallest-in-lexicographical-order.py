class Trie:
    def __init__(self):
        self.kth = 0

    def insert(self, val, num, turn, count, k):
        if turn <= 0 or count >= k:
            return count

        st = 0 
        if val == "":
            st = 1  

        for i in range(st, 10):
            next_val = val + str(i)
            prefix = int(next_val)
            subtree_size = self.countNumbersWithPrefix(prefix, num)
            if count + subtree_size >= k:
                count = self.insert(next_val, num, turn - 1, count + 1, k)
                if count == k and self.kth == 0:
                    self.kth = prefix  
                return count
            else:
                count += subtree_size

        return count

    def countNumbersWithPrefix(self, prefix, limit):
        current = prefix
        next_prefix = prefix + 1
        count = 0
        while current <= limit:
            count += min(next_prefix, limit + 1) - current
            current *= 10
            next_prefix *= 10
        return count

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        tri = Trie()
        tri.insert("", n, n // 10 + 1, 0, k)
        return tri.kth
