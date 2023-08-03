# -*- coding: utf-8 -*-
"""
205. Isomorphic Strings
Easy
7.3K
1.6K
company
Yandex
company
Microsoft
company
Adobe
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dict ={}
        for idx in range(len(s)) :
            if t[idx] in dict:
                if dict[t[idx]] != s[idx]:
                    return False
            else:
                if s[idx] in dict.values():
                    return False
                else:
                    dict[t[idx]] = s[idx]
        return True

s = "paper"
t = "title"     
solution = Solution()
print(solution.isIsomorphic(s, t))    
                
            