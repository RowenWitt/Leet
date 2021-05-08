class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # self.nums = nums
        # self.target = target
        for i in range(0, len(nums)):
            a = nums[i]
            print(a)
            for j in range(0, len(nums)):
                t = nums[j]
                guess = a + t
                if (guess == target) and (i != j):
                    out = [i, j]
                    return out
