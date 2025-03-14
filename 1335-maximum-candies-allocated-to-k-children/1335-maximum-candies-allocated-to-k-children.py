class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies)<k:
            return 0

        l ,h = 1, max(candies)
        best = 0
        while l<= h:
            mid = (l+h) // 2
            count = sum(c //mid for c in candies)
            if count >= k:
                best = mid
                l = mid+ 1
            else:
                h = mid - 1
        return best    

        