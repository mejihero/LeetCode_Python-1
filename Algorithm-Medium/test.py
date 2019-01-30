class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            print('i', i)
            last, now = now, max(last + i, now)
            print('last', 'now', last, now)
            print('')
        return now


if __name__ == '__main__':
        print(Solution().rob([2,7,9,3,1]))
