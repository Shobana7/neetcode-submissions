class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2

        if len(B)<len(A):
            A,B = B,A

        total = len(A) + len(B) 
        half = total // 2

        l,r = 0, len(A)-1

        while True:
            mid = (l + r )// 2
            Bmid = half - mid - 2

            Aleft = A[mid] if mid >=0 else float('-inf')
            Aright = A[mid+1] if mid + 1 < len(A) else float('inf') 
            Bleft = B[Bmid] if Bmid >= 0 else float('-inf')
            Bright = B[Bmid + 1] if Bmid + 1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright) )/ 2
            elif Aleft > Bright:
                r = mid - 1
            else:
                l = mid + 1