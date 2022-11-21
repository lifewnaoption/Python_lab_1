class Solution:
    def arrangeCoins(self, n: int) -> int:
            total = 0
            row = 0
            for i in range(1, n+1):
                total += i
                if total >= n:
                    row = i
                    break
            print(total)
            if total != n:
                row = row-1
            print(row)
            return row