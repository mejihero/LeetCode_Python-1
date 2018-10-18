class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) - 1
        j = len(num2) - 1
        result = ''
        carry = 0
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += ord(num1[i]) - ord('0')
            if j >= 0:
                carry += ord(num2[j]) - ord('0')
            result += chr(carry % 10 + ord('0'))
            carry //= 10
            i -= 1
            j -= 1
        if carry == 1:
            result += '1'
        return result[::-1]






    """
        Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

        Note:

        The length of both num1 and num2 is < 5100.
        Both num1 and num2 contains only digits 0-9.
        Both num1 and num2 does not contain any leading zero.
        You must not use any built-in BigInteger library or convert the inputs to integer directly.

        1. 想要低位对齐，就同步从两个字符串的最后一个字符向前遍历，直到两个字符串均遍历完成。若中途有一个字符串遍历完成，
        则此后将此字符串的字符认作0。
        2. 定义变量carry记录低位的进位，初始值为0。
        3. 每次遍历时，将carry更新为加上两个字符值之后的值，再以carry的个位的数字作为当前位置的结果，更新carry为其十位上的数字（进位）。
        4. 遍历字符串完成后，如果carry为1（最高位有进位），则将1添加到结果。
        输出结果。
    """
