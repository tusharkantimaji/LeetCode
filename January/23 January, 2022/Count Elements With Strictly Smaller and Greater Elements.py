class Solution:
    def countElements(self, nums: List[int]) -> int:
        c = 0
        left = min(nums)
        right = max(nums)
        for i in nums:
            if left < i and i < right:
                c += 1
        return c

        