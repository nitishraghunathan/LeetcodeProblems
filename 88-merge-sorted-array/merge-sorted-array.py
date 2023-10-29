class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        1. Incorporate nums2 into nums1
        2. sort these lements in the array
        3. merge and return the array in place
        4. use two pointer and compare each element in nums1 with nums2 and place the smaller element in nums 1 till we end the zeros
        """
        i = m-1
        j = n-1
        k = m+n-1
        while j >=0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k-=1
                i -=1
            else:
                nums1[k]=nums2[j]
                k-=1
                j-=1
        return
        