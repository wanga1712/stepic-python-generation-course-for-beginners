# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# nums = [3, 2, 4]
# target = 6


# index_one = 0
# index_two = 0
# for i in range(len(nums)):
#     if nums[i] + nums[i + 1] == target:
#         print(f'{nums[i]} {nums[i + 1]}')


# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#
# if __name__ == "__main__":
# # Create an instance of the Solution class
#     solution = Solution()
#
#     nums = [3, 2, 4]
#     target = 6
#     result = solution.twoSum(nums, target)
#
#     print(result)  # Output: [1, 2]


# string = int(input())
# modify_string = str(string)
# if modify_string[::] == modify_string[::-1]:
#     print('YES')
# else:
#     print('NO')

def romanToInt(Self, s):
    roman_arabic_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = list(s)
    for keys, value in roman_arabic_numerals:
        print(keys, value)
    return s

s = 'III'
print(romanToInt(s))