class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = set()

        length = len(nums)
        for i, n in enumerate(nums[:-3]):
            for j in range(i+1, length-2):
                m = nums[j]
                if n + m + nums[j+1] + nums[j+2] <= target and n + m + nums[-1] + nums[-2] >= target:
                    l, r = j + 1, length - 1
                    while l < r:
                        s = n + m + nums[l] + nums[r]
                        if s < target:
                            l += 1
                        elif s > target:
                            r -= 1
                        else:
                            res.add((n, m, nums[l], nums[r]))
                            l += 1
                            r -= 1

        return [list(x) for x in res]
