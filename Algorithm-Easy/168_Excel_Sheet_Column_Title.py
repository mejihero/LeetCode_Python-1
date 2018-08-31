class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result, num = "", n

        while num:
            result += chr((num - 1) % 26 + ord('A'))
            num = (num - 1) / 26

        return result[::-1]

if __name__ == "__main__":
    for i in range(1, 29):
        print(Solution().convertToTitle(i))






    """
            Time Complexity = O(log(n))
            Space Complexity = O(1)

            Given a positive integer, return its corresponding column title as appear in an Excel sheet.
            For example:
            1 -> A
            2 -> B
            3 -> C
            ...
            26 -> Z
            27 -> AA
            28 -> AB
            ...

            Example:
            Input: 28
            Output: "AB"

            有两个点需要说明：
            1）为什么要n-1，因为是tar的下标签是从0开始的，例如传进来一个1，要减1来匹配字符串的下标。
            2）为什么要n+1，因为没有0！例如传入的是27，当n-1了之后余数为0了，说明应该+1跳过一个0这个数字了。

            This code cannot run through terminal, but works for passing the LeetCode test.
    """
