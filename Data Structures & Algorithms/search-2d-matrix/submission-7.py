class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)-1

        while l <r :
            mid = l + (r-l)//2
            if matrix[mid][0] >= target:
                r = mid
            else:
                l = mid + 1
            
        if target == matrix[l][0]:
            return True

        print(l)
        
        row = l - 1 if matrix[l][0] > target else l
        l,r = 0, len(matrix[0])-1

        while l <r :
            mid = l+ (r-l)//2
            if matrix[row][mid]>= target:
                r = mid
            else:
                l = mid + 1
        
        return target == matrix[row][l]