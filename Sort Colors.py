class Solution:
    def sortColors(self, nums):
        
        size = len(nums)
        if size == 0 or size == 1:
            return
        count = [0,0,0]
        for c in nums:
            count[c] += 1
        
        nums[0:count[0]] = [0 for k in range(count[0])]
        nums[count[0]:count[0]+count[1]] = [1 for k in range(count[1])]
        nums[count[0]+count[1]:] = [2 for k in range(count[2])]