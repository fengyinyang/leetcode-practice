class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def find_kth(a, b, k):
            if len(a) == 0:
                return b[k-1]
            if len(b) == 0:
                return a[k-1]
            if k == 1:
                return min(a[0], b[0])
            ak = a[]