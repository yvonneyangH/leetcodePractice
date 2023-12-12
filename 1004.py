# -*- coding: utf-8 -*-

'''
1004. Max Consecutive Ones III
Medium
7.9K
101
company
Facebook
company
Amazon
company
Google
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxCount = 0
        for i in range(len(nums)):
            print("i:",i)
            j = i
            temp_k = k
            countEnd = False
            currCount = 0
            while countEnd != True:
                print("line 54 i:",i,"j:",j,"temp_k:",temp_k,"currCount:",currCount)
                if nums[j] == 1:
                    currCount += 1
                    j += 1
                elif nums[j] == 0 and temp_k > 0:
                    currCount +=1
                    j += 1
                    temp_k -= 1
                else:
                    countEnd = True
                if j >= len(nums):
                    countEnd = True
            if currCount > maxCount:
                maxCount = currCount
            print("j:",j," currCount:",currCount)      
        return maxCount

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
solution = Solution()
print(solution.longestOnes(nums, k))
