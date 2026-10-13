class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr = "" # remove all the alphanumeric chars

        for i in s:
            if i.isalnum():
                newStr += i.lower()
        return newStr == newStr[::-1]

        