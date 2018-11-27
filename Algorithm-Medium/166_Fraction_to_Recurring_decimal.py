class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # to put negativeFlag TRUE or FALSE
        negativeFlag = numerator * denominator < 0
        numerator = abs(numerator)
        denominator = abs(denominator)

        numList = []
        cnt = 0
        loopDict = dict()
        loopStr = None

        while True:
            numList.append(str(numerator / denominator))
            cnt += 1
            numerator = 10 * (numerator % denominator)
            if numerator == 0:
                break
            loc = loopDict.get(numerator)
            if loc:
                loopStr = "".join(numList[loc:cnt])
                break
            loopDict[numerator] = cnt

        ans = numList[0]

        if len(numList) > 1:
            ans += "."
        if loopStr:
            ans += "".join(numList[1:len(numList) - len(loopStr)]) + "(" + loopStr + ")"
        else:
            ans += "".join(numList[1:])
        if negativeFlag:
            ans = "-" + ans

        return ans

if __name__ == "__main__":
    print(Solution().fractionToDecimal(1,8))






    """
        Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

        If the fractional part is repeating, enclose the repeating part in parentheses.

        Example 1:

        Input: numerator = 1, denominator = 2
        Output: "0.5"

        Example 2:

        Input: numerator = 2, denominator = 1
        Output: "2"

        Example 3:

        Input: numerator = 2, denominator = 3
        Output: "0.(6)"
    """
