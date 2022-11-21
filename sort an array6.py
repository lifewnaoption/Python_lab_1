class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left_arr, right_arr):
            arr = []
            while left_arr and right_arr:
                if left_arr[0] <= right_arr[0]:
                    arr.append(left_arr.pop(0))
                else:
                    arr.append(right_arr.pop(0))
            
            while left_arr:
                arr.append(left_arr.pop(0))
            while right_arr:
                arr.append(right_arr.pop(0))
            return arr
        
        def merge_sort(arr):
            n = len(arr)
            if n < 2:
                return arr
            mid = n // 2
            left_arr = arr[:mid]
            right_arr = arr[mid:]
            return merge(merge_sort(left_arr), merge_sort(right_arr))
        
        return merge_sort(nums)