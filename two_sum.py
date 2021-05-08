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
            shite_eye = (len(nums) - 1) - i
            a = nums[i]
            print(shite_eye)
            sh = nums[shite_eye]
            guess = a + sh
            print(guess)
            if guess == target:
                out = [i,shite_eye]
                break
                return out