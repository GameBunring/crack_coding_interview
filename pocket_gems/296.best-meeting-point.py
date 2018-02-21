#
# [296] Best Meeting Point
#
# https://leetcode.com/problems/best-meeting-point/description/
#
# algorithms
# Hard (52.30%)
# Total Accepted:    16K
# Total Submissions: 30.6K
# Testcase Example:  '[[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]'
#
# A group of two or more people wants to meet and minimize the total travel
# distance. You are given a 2D grid of values 0 or 1, where each 1 marks the
# home of someone in the group. The distance is calculated using Manhattan
# Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
# 
# For example, given three people living at (0,0), (0,4), and (2,2):
# 
# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# 
# The point (0,2) is an ideal meeting point, as the total travel distance of
# 2+2+2=6 is minimal. So return 6.
#
class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import bisect
        horizon = []
        vertical = []
        for i, row in enumerate(grid):
            for j, p in enumerate(row):
                if p:
                    bisect.insort(horizon, j)
                    bisect.insort(vertical, i)

        res = 0
        i = 0
        for i in range(len(horizon) // 2):
            res += horizon[-i - 1] - horizon[i]

        i = 0
        for i in range(len(vertical) // 2):
            res += vertical[-i - 1] - vertical[i]
        return res