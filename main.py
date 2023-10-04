from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
	l = []
	for i in range(len(nums)-1):
		for j in range(i+1,len(nums)):
			sum = 0
			sum = sum + nums[i]
			sum = sum + nums[j]
			if sum == target:
				l.append(i)
				l.append(j)
				return l
	return l

nums = [3,2,4]
target = 7
output = twoSum(nums,target)
print(output)