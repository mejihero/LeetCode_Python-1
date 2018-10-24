class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        """
        一只小猪在一小时可以验5桶水
        既然一只能验5桶，那么用二维的思路，2只猪应该可以验5*5桶：猪A负责行，猪B负责列
        每15分钟试喝一行/一列的所有5桶水，通过2只猪上天的时间能推断出毒水在几行几列。

        比如第12号有毒, 30分钟的时候猪B上天了, 猪A继续, 45分钟的时候猪A上天了,这时候我们就知道是12号有毒了
        1  2  3  4  5
        6  7  8  9  10
        11 12 13 14 15
        16 17 18 19 20
        21 22 23 24 25

        如此类推到N只的情况，使用N维去分区，则5^N >= 1000即为解决本题的公式
        """
        states=minutesToTest//minutesToDie+1
        return int(math.ceil(math.log(buckets, states)))






        """
        There are 1000 buckets, one and only one of them contains poison, the rest are filled with water.
        They all look the same. If a pig drinks that poison it will die within 15 minutes. What is the
        minimum amount of pigs you need to figure out which bucket contains the poison within one hour.

        Answer this question, and write an algorithm for the follow-up general case.

        Follow-up:

        If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you
        need to figure out the "poison" bucket within p minutes? There is exact one bucket with poison.

        那么我们来一步一步从最简单的情况来分析吧，假设只有1只猪，只有15分钟，那么我们能测几个水桶呢？很显然是两个，因为只能测一次的话，
        让猪去随便喝一桶，如果毒死了，就是喝的那桶，反之则是另一桶。好，那么如果有两只猪呢，能测几桶？怎么喝呢，两只猪一猪喝一桶，
        再同时喝一桶，剩下一桶谁也不喝，那么如果两只猪都毒死了，说明是共同喝的那桶有毒，如果某个猪毒死了，说明该猪喝的那桶有毒，如果都没事，
        说明是谁也没喝的那桶。那么我们应该看出规律了吧，没错，三猪能测8桶，其实就是2的指数倍。

        如果只能测一次的话，实际上相当一个一维数组，而如果能测两次的话，情况就不一样了，我们就可以重复利用猪了。比如还是两只猪，能测两次，
        功能测几个桶，答案可以测9桶，为啥，我们组个二维数组：

        1  2  3

        4  5  6

        7  8  9

        如果我们让第一头猪第一次喝1，2，3桶，第二次喝4，5，6桶，而让第二头猪第一次喝1，4，7桶，第二次喝2，5，8桶，我们可以根据猪的死亡
        情况来确定是哪一桶的问题，实际上就把猪被毒死的那个节点当作了二维数组的横纵坐标来定位毒桶的位置，巧妙吧～更巧妙的是，如果再增加一头
        猪，实际上是给数组增加一个维度，变成了一个三维数组，那么三只猪，测两次，可以测27桶，叼不叼。这道题让我们求最少用多少猪来测，那么
        就是求数组的维度，我们知道了数组的总个数，所以要尽量增加数组的长宽，尽量减少维度。这里，数组的长宽其实都是测试的次数+1，所以我们
        首先要确定能测的次数，通过总测试时间除以毒发时间，再加上1就是测试次数。有了数组长宽m，那么如果有x只猪，能测的桶数为m的x次方，现在
        我们给定了桶数N，要求x，就log一下就行，然后用个换底公式，就可以求出x的值了
        """
