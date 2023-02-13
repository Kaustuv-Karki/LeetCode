class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = dict()
        for index, value in enumerate(nums):
            find = target - value
            if find in elements:
                return [elements[find], index]
            elements[value] = index
        return []
