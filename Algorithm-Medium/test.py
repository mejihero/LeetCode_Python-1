import re

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        print('input:', str)
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
        print('After stripS.lstrip("-"):', stripS.lstrip("-"))
        print('After (stripS.lstrip("-")).lstrip("+"):', (stripS.lstrip("-")).lstrip("+"))
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
    print(Solution().myAtoi('  -+42  32 '))
