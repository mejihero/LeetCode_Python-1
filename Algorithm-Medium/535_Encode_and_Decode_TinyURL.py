import string
import random
import math
full_tiny = {}
tiny_full = {}
letters = string.ascii_letters + string.digits

class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        # 我们的主要任务是写两个函数：encode、decode。先把encode编好，decode根据encode的短URL，直接可以读取原始的URL。
        # 对于encode要考虑几个问题：

        # 短URL怎么来？
        # 我们可以取26个字母，大小写敏感，10个数字。这样总共有62个字符。这62个字符随机排列组合，得到http://tinyurl.com/xxxxxx
        # 中的xxxxxx短码，从而得到一个短的URL：http://tinyurl.com/xxxxxx 代码如下：

        def six_addr():
            ans=''
            tmp=''
            for i in range(6):
                tmp=letters[random.randint(0,10000)%62]
                ans=ans+tmp
            return ans

        #  letters[random.randint(0,10000)%62]是在62个字符中随机选择一个。这里我写了一个for循环来随机生成6个字符，
        # 并ans=ans+tmp拼在了一起，组成了上面我们要得到的六个字符ans。

        # 要怎么对应？长URL与短URL是一一对应的关系。在python中可以创建字典(其他语言中叫做map)去存储它们。在这里要创建两个字典：
        # full_tiny和tiny_full。full_tiny的key是长URL，vaule是短URL。tiny_full则相反。

        # 考虑重复的问题一个长URL对应一个短URL。如果重复输入长URL，则不会分配新的短URL。所以在分配之前，要看看长URL是否已经存在，
        # 如果已经存在，则直接返回现有的短URL，而不再重新分配：
        if longUrl in full_tiny:
            return "http://tinyurl.com/" + full_tiny[longUrl]
        else:
            suffix = six_addr()
            full_tiny[longUrl]=suffix
            tiny_full[suffix] = longUrl
            return "http://tinyurl.com/" + suffix

        # 怎么解码？首先我们要获得需要解码的东西，也就是我们编码的那六位字符串。那是拼在http://tinyurl.com/ 后面的，
        # 所以要先提取出来：shortUrl = shortUrl.split('/')[-1]。编码时我们创建了tiny_full字典，它的key就是短URL。
        # 我们根据短的URL，在tiny_full字典中查找它对应的长URL即可解码。

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        shortUrl = shortUrl.split('/')[-1]
        if shortUrl in tiny_full:
            return tiny_full[shortUrl]
        else:
            return None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))






    """
            Note: This is a companion problem to the System Design problem: Design TinyURL.

            TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl
            and it returns a short URL such as http://tinyurl.com/4e9iAk.

            Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode
            algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be
            decoded to the original URL.

    """
