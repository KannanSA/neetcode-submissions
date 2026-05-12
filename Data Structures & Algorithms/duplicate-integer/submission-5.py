class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Snum = set(nums)
        if len(nums) == len(Snum):
            return False
        else:
            return True