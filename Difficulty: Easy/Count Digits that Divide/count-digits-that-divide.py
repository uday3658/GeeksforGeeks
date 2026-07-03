class Solution:
    def evenlyDivides(self, n):
        count = 0
        digits = [int(i) for i in str(n)]

        for digit in digits:
            if digit != 0 and n % digit == 0:
                count += 1

        return count