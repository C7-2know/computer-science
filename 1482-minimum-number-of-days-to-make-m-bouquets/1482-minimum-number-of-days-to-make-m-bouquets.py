class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def can_make_m_bouquets(m,k,d):
            bouq = 0
            cur = 0
            for i in bloomDay:
                if i<=d:
                    cur+=1
                else:
                    cur=0
                if cur == k:
                    cur =0
                    bouq+=1
                if bouq==m:
                    return True
            return False

        max_d = max(bloomDay)
        min_d = min(bloomDay)

        mid = min_d + (max_d-min_d)//2
        while max_d>min_d:
            if can_make_m_bouquets(m, k, mid):
                max_d= mid
            else:
                min_d=mid+1
            mid= (min_d +max_d)//2
            print(max_d, min_d, mid)
        if can_make_m_bouquets(m,k,max_d):
            return max_d
        return -1
        