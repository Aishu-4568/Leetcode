class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        check = 0
        for i in nums:
            if i != val:
                nums[check] = i
                check +=1
        return check

        