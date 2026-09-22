"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""

nums = [2,7,11,15]

target = 9

left = 0

right = len(nums)-1

while left < right:

    current_sum = nums[left] + nums[right]

    if current_sum == target:

        print(left,right)
        break

    elif current_sum > target:

        right = right - 1

    elif current_sum < target:

        left = left + 1

else:print(-1)            

