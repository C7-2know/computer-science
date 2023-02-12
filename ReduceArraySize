class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = {}
        for index in range(len(arr)):
            if arr[index] not in freq:
                freq[arr[index]] = 1
            else:
                freq[arr[index]] += 1
        sum = 0
        counter = 0
        sortd = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        for fr in sortd:
            sum += sortd[fr]
            counter += 1
            if sum >= len(arr)/2:
                break
        return counter
