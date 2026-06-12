class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        arr = 0
        for i in matrix:
            if i[-1] < target:
                continue
            
            arr = i
            break
        
        if not arr:
            return False
        
        l,r = 0, len(arr) - 1
        while l <= r:
            mid = (l+r) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid -1
        
        return False
        
