class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top,bottom = 0, len(matrix)-1
        row = -1

        while top <= bottom:
            mid = (top + bottom)//2

            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row = mid
                break
            
            elif matrix[mid][0] >= target:
                bottom = mid -1
            
            else:
                top = mid + 1
        
        if not row>=0:
            return False

        for i in matrix[row]:
            if i == target:
                return True
        
        return False






