class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for i,a in enumerate(nums):
            print(map)
            if a in map:
                return [map[a], i]
            
            else:
                map[target-a] = i
        
        return []