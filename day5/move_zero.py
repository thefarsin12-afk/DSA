"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

nums = [1,0,4,0,9,0,2]
#       0 1 2 3 4 5 6
#       1 4 9 2 0 0 0

postion = 0 # postion 1

for number in nums:

    if number != 0: # 1 != 0 true 0 !=0 false 4 != 0 true

        nums[postion] = number # 0 = 1 ,1 index add = 4

        postion = postion + 1 # (0 + 1)=1 , 1 + 1 = 2

for i in range(postion,len(nums)):

    nums[i] = 0     

print(nums)       