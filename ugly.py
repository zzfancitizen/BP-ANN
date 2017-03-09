class Solution:
    def isUgly(self, num):
        rem2 = num % 2
        rem3 = num % 3
        rem5 = num % 5
        while rem2 == 0 or rem3 == 0 or rem5 == 0:
            if rem2 == 0:
                num = num / 2
            elif rem3 == 0:
                num = num / 3
            elif rem5 == 0:
                num = num / 5

            rem2 = num % 2
            rem3 = num % 3
            rem5 = num % 5

        return num == 1

x = 1

sol = Solution()
for x in range(1, 1680):
    if sol.isUgly(x) == True:
       print(x)


