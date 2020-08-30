学习笔记

## 作业一
1. MySQL里建表语句：
    ```
    use test;
    create table maoyanmovie (
        id int(11) NOT NULL AUTO_INCREMENT,
        title varchar(255) default null,
        varity varchar(255) default null,
        time varchar(255) default null,
        primary key(id)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;
    ```

2. 运行爬虫，长时间处于telnet console listening时，可能是代理IP失效，选择更换可用代理IP后解决。
https://github.com/clarketm/proxy-list/blob/master/proxy-list-raw.txt

但是，在vscode底部终端telnet代理IP不通，尚不清楚原因。

3. 重写后中间件调用顺序
    1. from_crawler：类方法，对象初始化前调用，从配置中读取代理IP配置项
    2. \_\_init\_\_：实例初始化方法，初始化proxy变量
    3. \_set_proxy\_\_：根据proxy变量随机设置request发送到downloader之前的头部proxy参数。


## 作业二
1. 先下载对应浏览器chromedriver，解压到python3 bin目录。