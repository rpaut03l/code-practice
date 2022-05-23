# Squares of a Sorted Array:

Q). Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Solution1:
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        z = []
        for i in nums:
            k = i * i
            z.append(k)
        z.sort()
        return (z)
