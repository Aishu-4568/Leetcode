class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        i = 2
        while i<n:
            if nums[i-2] == 0:
                nums[i-2] ^= 1
                nums[i-1 ]^= 1
                nums[i] ^= 1
                count +=1
            i+=1
        if 0 in nums:
            return -1
        return count        

        