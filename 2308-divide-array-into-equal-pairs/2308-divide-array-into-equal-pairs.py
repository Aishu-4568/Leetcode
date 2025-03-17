class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        return all(val %2 ==0 for val in counter.values())
        
        