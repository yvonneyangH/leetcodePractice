'''
334. Increasing Triplet Subsequence
Medium
7.6K
409
company
TikTok
company
Google
company
Facebook
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
'''
'''
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<=2:
            return False
        for i in range(len(nums)-2):
            if nums[i]<nums[i+1] and nums[i+1]< nums[i+2]:
                return True
            
        return False
 
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tempArr = []
        for i in nums:
            print('i:',i)
            print('line65:',tempArr)
            if len(tempArr) == 0:
                tempArr.append([i])
            else:
                for idx in range(len(tempArr)):
                    print('idx:',idx)
                    print('tempArr[idx][-1]:',tempArr[idx][-1])
                    if i > tempArr[idx][-1]:
                        tempArr[idx].append(i)
                    elif i<=tempArr[idx][-1] and i>tempArr[idx][0]:
                        tempArr[idx].pop()
                        tempArr[idx].append(i)
                    else:
                        if len(tempArr[idx])==1:
                            tempArr[idx] = [i]
                        else:
                            tempArr.append([i])
                    if len(tempArr[idx])>=3:
                        return True
        return False  
'''

class Solution:
    def increasingTriplet(self, nums) :
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else: 
                return True
        return False
    
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
solution = Solution()
print(solution.increasingTriplet(nums))