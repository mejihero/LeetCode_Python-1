class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        table = "0123456789abcdef"
        if num < 0:
            num = 0xffffffff - ~num

        res = ""
        while num:
            res = table[num % 16] + res
            num //= 16

        return res






    """
        Time Complexity = O(n)
        Space Complexity = O(1)

        Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement
        method is used.

        Note:

        All letters in hexadecimal (a-f) must be in lowercase.
        The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single
        zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
        The given number is guaranteed to fit within the range of a 32-bit signed integer.
        You must not use any method provided by the library which converts/formats the number to hex directly.

        Example:
        Input:
        26

        Output:
        "1a"
    """
