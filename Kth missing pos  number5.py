class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        last, count = 0, 0
        
        for i in range(len(arr)):
            count += arr[i] - last - 1
            last = arr[i]
            
            if count >= k: return arr[i] - count + k - 1
        
        return arr[-1] + k - count