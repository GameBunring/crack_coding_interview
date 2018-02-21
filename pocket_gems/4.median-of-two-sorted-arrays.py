#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (22.48%)
# Total Accepted:    232K
# Total Submissions: 1M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# Example 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# 
# Example 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1:
            return (nums2[(len(nums2) - 1) // 2] + nums2[(len(nums2)) // 2]) / 2.0
        if not nums2:
            return (nums1[(len(nums1) - 1) // 2] + nums1[(len(nums1)) // 2]) / 2.0
        m, n = len(nums1), len(nums2)
        l, r = (m + n + 1) // 2, (m + n + 2) // 2
        return (self.findKth(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, l) + \
        self.findKth(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, r)) / 2.0

        
    def findKth(self, nums1, s1, e1, nums2, s2, e2, k):
        m = e1 - s1 + 1
        n = e2 - s2 + 1
        if m > n:
            return self.findKth(nums2, s2, e2, nums1, s1, e1, k)
        if m == 0:
            return nums2[s2 + k - 1]
        if k == 1:
            return min(nums1[s1], nums2[s2])
        i = s1 + min(m, k // 2) - 1
        j = s2 + k // 2 - 1
        if nums2[j] > nums1[i]:
            return self.findKth(nums1, i + 1, e1, nums2, s2, e2, k - min(m, k // 2))
        else:
            return self.findKth(nums1, s1, e1, nums2, j + 1, e2, k - (k // 2))
