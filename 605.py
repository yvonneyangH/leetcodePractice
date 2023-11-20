# -*- coding: utf-8 -*-
'''
605. Can Place Flowers
Easy
6K
1.1K
company
Amazon
company
Facebook
company
Adobe
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        tempArr = []
        tempVal = 0
        maxN = 0
        for i in flowerbed:
            if i == 0:
                tempVal += 1
            else:
                tempArr.append(tempVal)
                tempVal = 0
        tempArr.append(tempVal)
        if len(tempArr) < 2:
            maxN = (tempArr[0]+1)//2
        elif len(tempArr)<3 and len(tempArr)>=2:
            maxN = tempArr[0]//2 +tempArr[1]//2
        else:
            for i in range(len(tempArr)):
                print('maxN:',maxN,'.tempArr[',i,']:',tempArr[i])
                if i == 0:
                    maxN += tempArr[i]//2
                elif i== len(tempArr)-1:
                    maxN += tempArr[i]//2
                else:
                    maxN += (tempArr[i]-1)//2
        print(maxN)
        print('temmArr:',tempArr)
        if n <= maxN:
            return True
        else:
            return False
        
flowerbed = [1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,1]
n = 17
solution = Solution()
print(solution.canPlaceFlowers(flowerbed,n))