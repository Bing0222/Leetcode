from typing import List
"""
给你一个整数数组 nums，返回 数组 answer ，
其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请不要使用除法，且在 O(n) 时间复杂度内完成此题

输入: nums = [1,2,3,4]
输出: [24,12,8,6]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        left = 1
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]
        right = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
    
nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))

nums = [-1,1,0,-3,3]
print(Solution().productExceptSelf(nums))