import re

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # get rid of the left and right space
        # Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
        # 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
        stripS=str.strip()
        print('stripS', stripS)

        # deal with three special strings - "","-" and "+"
        if stripS=="" or stripS=="-" or stripS=="+":
            return 0

        # get rid of left "-" and "+", be award of the sequence
        # '+-42-' or '- -42-' or '+ -42-'
        # lstrip() 方法用于截掉字符串左边的空格或指定字符。
        # Python提供了两种不同的原始操作：match和search。
        # match是从字符串的起点开始做匹配，而search（perl默认）是从字符串做任意匹配。
        print(stripS.lstrip("-"))
        print((stripS.lstrip("-")).lstrip("+"))
        s1=re.match('[^\d]+',(stripS.lstrip("-")).lstrip("+"))
        print('s1', s1)

        # found any non-num char from string beginning, return 0
        if s1 != None:
            return 0
        else:
            # found the num with/without "-","+" starts
            s1 = re.search('\-*\+*\d+',stripS).group()
        print('s1', s1)

        # get rid of "--","-+" and "+-"
        if s1[0:2]=="--" or s1[0:2]=="-+" or s1[0:2]=="++":
            return 0

        i1=int(s1)
        if i1>0:
            return 2147483647 if i1>2147483647 else i1
        else:
            return -2147483648 if i1<-2147483648 else i1

if __name__ == "__main__":
    print(Solution().myAtoi('   -42   '))






    """
        Implement atoi which converts a string to an integer.

        The function first discards as many whitespace characters as necessary until the first
        non-whitespace character is found. Then, starting from this character, takes an optional
        initial plus or minus sign followed by as many numerical digits as possible, and interprets
        them as a numerical value.

        The string can contain additional characters after those that form the integral number,
        which are ignored and have no effect on the behavior of this function.

        If the first sequence of non-whitespace characters in str is not a valid integral number,
        or if no such sequence exists because either str is empty or it contains only whitespace
        characters, no conversion is performed.

        If no valid conversion could be performed, a zero value is returned.

        Note:

            Only the space character ' ' is considered as whitespace character.
            Assume we are dealing with an environment which could only store integers within the 32-bit
            signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of
            representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

        Example 1:

        Input: "42"
        Output: 42

        Example 2:

        Input: "   -42"
        Output: -42
        Explanation: The first non-whitespace character is '-', which is the minus sign.
                     Then take as many numerical digits as possible, which gets 42.

        Example 3:

        Input: "4193 with words"
        Output: 4193
        Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

        Example 4:

        Input: "words and 987"
        Output: 0
        Explanation: The first non-whitespace character is 'w', which is not a numerical
                     digit or a +/- sign. Therefore no valid conversion could be performed.

        Example 5:

        Input: "-91283472332"
        Output: -2147483648
        Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
                     Thefore INT_MIN (−231) is returned.


    """
