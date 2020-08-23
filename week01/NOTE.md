学习笔记

## 作业一
1. 访问提示认证，暂时通过页面滑块完成认证。
2. 访问提示403，被反爬，暂时通过等待几分钟后重试。尝试引入fake_useragent，随机模拟各种浏览器headers，但提示`fake_useragent.errors.FakeUserAgentError: Maximum amount of retries reached`，尝试了下面3种方法，均失败。

   - 禁用服务器缓存：`ua = UserAgent(use_cache_server=False)`
   - 不缓存数据：`ua = UserAgent(cache=False)`
   - 忽略ssl验证：`ua = UserAgent(verify_ssl=False)`

   最后通过使用临时Json文件方式解决，步骤如下：

   - 下载url json到本地：`wget https://fake-useragent.herokuapp.com/browsers/0.1.11`
   - 保存到临时目录
        ```
        mv 0.1.11 fake_useragent_0.1.11.json

        # 获取临时目录路径
        >>> import tempfile
        >>> tempfile.gettempdir()
        '/var/folders/yn/2qvfzbw93ql7l8_2x9csngkc0000gn/T'

        cp fake_useragent_0.1.11.json /var/folders/yn/2qvfzbw93ql7l8_2x9csngkc0000gn/T

        >>> from fake_useragent import UserAgent
        >>> ua = UserAgent()
        >>> print(ua.random)
        Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36
        >>> print(ua.random)
        Mozilla/5.0 (Windows; U; Windows NT 6.0; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4
        >>> print(ua.random)
        Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36
        ```
    参考链接：https://blog.csdn.net/yilovexing/article/details/89044980

## 作业二
1. 刚开始，没注意settings.py配置项：
   - 没有配置USER_AGENT_LIST，导致无法爬取到内容。
   - 没有配置ITEM_PIPELINES，导致爬取结果只输出到屏幕，无法写入文件。
2. 作业一是直接在页面`https://maoyan.com/films?showType=3`上爬取了影片信息，作业二是先从页面`https://maoyan.com/films?showType=3`获取单个影片详情链接，再借助Scrapy框架迭代去每个影片详情页爬取。