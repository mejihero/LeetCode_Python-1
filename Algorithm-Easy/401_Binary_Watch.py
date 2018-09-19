class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hours = [8 ,4 ,2, 1]
        minutes = [32, 16, 8, 4, 2, 1]

        res = []
        for i in range(num + 1):
            hour = i
            minute = num - i

            hour_solutions = []
            self.dfs(hours, i, hour_solutions, [], 0)

            minute_solutions = []
            self.dfs(minutes, num - i, minute_solutions, [], 0)

            for hour in hour_solutions:
                for minute in minute_solutions:
                    if 0<= hour <= 11 and 0 <= minute <= 59:
                        if 0 <= minute <= 9:
                            res.append(str(hour) + ':' + '0' + str(minute))
                        else:
                            res.append(str(hour) + ':' + str(minute))
        return res


    def dfs(self, nums, cnt, res, tmp, start):

        if len(tmp) == cnt:
            res.append(sum(tmp))
            return

        if start >= len(nums):
            return

        for i in range(start, len(nums)):
            self.dfs(nums, cnt, res, tmp + [nums[i]], i + 1)






    """
        Time Complexity = O(1)
        Space Complexity = O(1)

        A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the
        minutes (0-59).
        Each LED represents a zero or one, with the least significant bit on the right.
        For example, the above binary watch reads "3:25".
        Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times
        the watch could represent.

        Example:
        Input: n = 1
        Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
        Note:
        The order of output does not matter.
        The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
        The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should
        be "10:02".1
    """
