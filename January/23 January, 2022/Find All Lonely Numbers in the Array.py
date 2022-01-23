class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        # p1 = nums[0]
        l = len(nums)
        if l > 1:
            if nums[1] - nums[0] == 1 or nums[1] - nums[0] == 0:
                pass
            else:
                ans.append(nums[0])
            for i in range(1, l-1):
                if nums[i] == nums[i-1] or nums[i] - nums[i-1] == 1 or nums[i] == nums[i+1] or nums[i+1] - nums[i] == 1:
                    pass
                else:
                    ans.append(nums[i])
                # p1 = nums[i]
            if nums[-1] - nums[-2] == 1 or nums[-1] == nums[-2]:
                pass
            else:
                ans.append(nums[-1])
            return ans
        return nums