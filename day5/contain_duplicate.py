"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Input: nums = [1,2,3,1]

Output: true

Explanation:
The element 1 occurs at the indices 0 and 3.
"""

nums = [1,2,3,2]

lst = []

is_duplicate = False

for n in nums:

    if n in lst:

        is_duplicate = True
        break

    else:lst.append(n)
    
print(is_duplicate)    



        

  