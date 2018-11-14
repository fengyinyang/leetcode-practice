class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = dict()
        for i, v in enumerate(nums):
            if target - v in a:
                return [a[target-v], i]
            else:
                a[v] = i