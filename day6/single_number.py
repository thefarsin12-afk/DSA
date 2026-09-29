"""
136. Single Number
Easy
Topics
premium lock icon
Companies
Hint
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
"""

nums = [2,2,1,1]

for n in nums:

    if nums.count(n) == 1:
        print(n)
        break

else:
    print("no one")