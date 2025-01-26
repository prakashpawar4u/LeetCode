class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        int_min = -2 ** 31
        int_max = 2 ** 31 -1

        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_x = 0

        while x != 0:
            digit = x % 10
            x //=10
           #push the digit to reveres_x

            reversed_x  = reversed_x * 10 + digit

        reversed_x *= sign

        if reversed_x < int_min or reversed_x > int_max:
            return 0
        return reversed_x

        