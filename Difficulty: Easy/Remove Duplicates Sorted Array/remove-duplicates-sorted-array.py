class Solution:
    def removeDuplicates(self, arr):
        arr1 = []
        for i in arr:
            if not arr1 or arr1[-1] != i:
                arr1.append(i)
        return arr1