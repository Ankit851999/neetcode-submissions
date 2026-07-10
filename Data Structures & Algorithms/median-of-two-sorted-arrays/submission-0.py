class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        l1= 0
        l2 = 0
        while True:
            if l1 >= len(nums1) and l2 >= len(nums2):
                break
            elif l1 >= len(nums1):
                arr.append(nums2[l2])
                l2 += 1
            elif  l2 >= len(nums2):
                arr.append(nums1[l1])
                l1 += 1
            elif nums1[l1] > nums2[l2]:
                arr.append(nums2[l2])
                l2 += 1
            else:
                arr.append(nums1[l1])
                l1 += 1
        if len(arr) == 0:
            return -1
        if len(arr) == 1:
            return arr[0]
        elif (len(arr) -1) % 2 == 0:
            return arr[int((len(arr)-1 )/ 2) ]
        else:
            left = ((len(arr) -1) //2)
            right = left +1
            return (arr[left] + arr[right]) /2

