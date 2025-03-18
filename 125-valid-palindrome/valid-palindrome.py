class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filter_st = []
        for c in s:
            if c.isalnum():
                filter_st.append(c.lower())

        filter_st = "".join(filter_st)
        return (filter_st == filter_st[::-1])

                