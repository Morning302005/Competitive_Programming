class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        result = ""

        for ch in s:
            if ch.isalnum():
                result += ch

        return result == result[::-1]