"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]

Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.
"""

def contain_duplicate(num):

    lst = []

    for n in num:

        if n not in lst:
            
            lst.append(n)

        else:
            return True

    return False

print(contain_duplicate([1,2,3,1]))        