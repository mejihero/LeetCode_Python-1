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

        Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
        The digits are stored such that the most significant digit is at the head of the list, and each
        element in the array contain a single digit.
        You may assume the integer does not contain any leading zero, except the number 0 itself.

        Example:
        Input: [1,2,3]
        Output: [1,2,4]
        Explanation: The array represents the integer 123.
    """
