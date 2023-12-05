# -*- coding: utf-8 -*-

'''
283. Move Zeroes
Easy
15.7K
403
company
Facebook
company
Yandex
company
Amazon
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
'''

class Solution1(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count_0 = 0
        popIdx = []
        for idx in range(len(nums)):
            if nums[idx] == 0:
                count_0 +=1
                popIdx.append(idx)
        for i in range(len(popIdx)-1,-1,-1):
            nums.pop(popIdx[i])
            nums.append(0)
        return nums
    
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for num in nums:
            if num !=0:
                nums[idx] = num
                idx+=1
        while idx < len(nums):
            nums[idx] = 0
            idx+=1
    
nums = [0,1,0,3,12]
solution = Solution()
print(solution.moveZeroes(nums))