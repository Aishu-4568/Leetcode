class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}
        for i ,num in enumerate(nums):
            want = target - num
            if want in nmap:
                return [nmap[want],i]
            nmap[num] = i
        return []