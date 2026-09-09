class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min eating speed is sum(piles)/h
        # max eating speed is max(piles)
        # binary search to find the optimal k, but would need to test by traversing through the list, so O(n*log(n))
        min_k = -(-sum(piles)//h)
        max_k = max(piles)
        final_k = float("inf")

        while min_k <= max_k:
            mid_k = (max_k+min_k)//2
            hours_take = 0
            for p in piles:
                hours_take += -(-p//mid_k)
            if hours_take <= h:
                final_k = min(final_k, mid_k)
                max_k = mid_k - 1  
            else:
                min_k = mid_k + 1
            
        return final_k
            

