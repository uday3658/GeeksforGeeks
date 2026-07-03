class Solution:
    def armstrongNumber (self, n):
        num=0
        for i in str(n):
            num=num+int(i)**3
        return num == n
        