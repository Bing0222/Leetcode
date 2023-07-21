from typing import List
"""
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
输入：nums = [1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(map(len, ''.join(map(str, nums)).split('0')))

nums = [1,1,0,1,1,1]

print(Solution().findMaxConsecutiveOnes(nums))