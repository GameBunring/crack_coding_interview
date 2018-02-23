#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (26.59%)
# Total Accepted:    130.5K
# Total Submissions: 491K
# Testcase Example:  '[-2]'
#
# 
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest product.
# 
# 
# 
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
# 
#
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        for n in nums[1:]:
            if n < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(n, n * cur_max)
            cur_min = min(n, n * cur_min)
            res = max(res, cur_max)
        return res
        