class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums2_dict = {}
        for index, value in enumerate(nums2):
            nums2_dict[value] = index
        result = []
        for index, value in enumerate(nums1):
            if value not in nums2_dict:
                result.append(-1)
            else:
                indice = nums2_dict[value]
                flag = False
                for i in range(indice, len(nums2)):
                    if nums2[i] > value:
                        result.append(nums2[i])
                        flag = True
                        break
                if not flag:
                    result.append(-1)
        return result
                    
        