class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i,a in enumerate(nums):
            print(i,a)
            if (target - a) in map:
                return [map[target-a], i]

            else:
                map[a] = i
        