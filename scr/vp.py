import re

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # regex replace
        s = re.sub('[^A-Za-z0-9]', '', s)
        print(s)
        if s == "":
            return True
        return s[::-1] == s
        # check reversed



print(Solution().isPalindrome("a"))


print(reversed("123"))