class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result, carry, val = "", 0, 0
        for i in range(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            carry, val = val // 2, val % 2
            result += str(val)
        if carry:
            result += str(1)
        return result[::-1]

if __name__ == '__main__':
    print(Solution().addBinary("1111", "1111"))






    """
        Time Complexity = O(N)
        Space Complexity = O(1)

        Given two binary strings, return their sum (also a binary string).
        The input strings are both non-empty and contains only characters 1 or 0.

        Example:
        Input: a = "1010", b = "1011"
        Output: "10101"
    """
