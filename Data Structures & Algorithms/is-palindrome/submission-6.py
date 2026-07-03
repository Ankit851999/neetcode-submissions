class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = [i.lower() for i in s if i.isalpha() or i.isdigit()]

        for i in range(len(string) // 2):
            if string[i] != string[-(i + 1)]:
                return False

        return True