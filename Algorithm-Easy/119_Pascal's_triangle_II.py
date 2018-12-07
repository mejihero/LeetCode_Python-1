class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1] + [0] * rowIndex
        for i in range(rowIndex):
            result[0] = 1
            print(' ')
            print('i', i)
            for j in range(i+1, 0, -1):
                print('j',j)
                result[j] = result[j] + result[j-1]
                print(result)
            print('reuslt', result)
        return result

if __name__ == '__main__':
    print(Solution().getRow(3))






    """
            Time Complexity = O(n^2)
            Space Complexity = O(1)


            Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
            Note that the row index starts from 0.
            In Pascal's triangle, each number is the sum of the two numbers directly above it.

            Example:
            Input: 3
            Output: [1,3,3,1]

            用到一个小trick，即：每一行的结果可以由上一行和上一行的偏移相加得到。例如求第4行：
                1 3 3 1 0
             +  0 1 3 3 1
             =  1 4 6 4 1
    """
