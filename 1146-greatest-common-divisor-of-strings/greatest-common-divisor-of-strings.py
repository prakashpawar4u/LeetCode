class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""

        gcd_length = self.gcd_math(len(str1), len(str2))

        return(str1[:gcd_length])
    
    def gcd_math(self, a, b):
        while b:
            a, b = b, a % b
        return a

               