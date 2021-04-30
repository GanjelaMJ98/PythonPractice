from typing import List

class Solution:
	'''	
		Given an array of integers nums and an integer target,
		return indices of the two numbers such that they add up to target.
	'''
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		seen = {}
		for i, v in enumerate(nums):
			remaining = target - v
			if remaining not in seen:
				seen[v] = i
			else:
				return [seen[remaining], i]
		return []



def test_twoSum():
	assert solution.twoSum([0,2,3,6], target = 5) == [1,2]
	assert solution.twoSum([0,2,4,6], target = 5) == []
	assert solution.twoSum([], target = 5) == []
	print(solution.twoSum,'OK')

if __name__ == '__main__':
	solution = Solution()
	test_twoSum()