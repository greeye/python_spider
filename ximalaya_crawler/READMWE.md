## 喜马拉雅FM网音频标签获取爬虫
================================
### 一、项目介绍
从**喜马拉雅FM网**(https://www.ximalaya.com/) 的爬取音频的全部分类网页(https://www.ximalaya.com/category/) 的**分类节目信息**，并且获取各分类下的**音频节目标签信息**。将分类信息表和音频标签信息表的两个文档集合存入**Mongodb数据库**中。
两个文档集合的设计结构如下：
#### album_content：分类节目信息
![image](https://github.com/greeye/python_spider/blob/master/ximalaya_crawler/img/album_content.png)

#### album_information：音频节目信息
![image](https://github.com/greeye/python_spider/blob/master/ximalaya_crawler/img/album_information.png)

### 二、项目工作过程
#### 2.1 技术模块
该爬虫工程没有使用类似于scrapy的爬虫框架去爬取数据,使用的主要模块包括：**urllib**、**request**、**BeaufulSoup**、**json**、**pymongo**、**re**等;
- requeste
requeste模块通过模拟用户访问web网站，获取数据,里面内置了post和get的html请求方法。
- BeatulSoup
BeatulSoup模块可以很方便地提取HTML或者XML标签的内容，
- urllib
urllib 模块主要用于处理URL，在该工程中，我采用它来拼接从网页中获取的相对路径和网站主页
- json
json 模块可以进行json数据的处理,可以很方便地映射成Python对象，或者转化为json字符串，和mongodb用非常高效解析数据
- pymongo
用于连接mongodb数据库
- re
进行正则计算，抽取需要的数据，该工程中从一段字符串中抽取数字段。
#### 2.2 运行流程
- 从喜马拉雅网的全部分类网址中抓取分类信息的json地址,然后进行一一解析，将需要的字段存入表中。
- 首先获取所有的分类页面url,再爬进分类页面下的音频节目单，获取所有音频节目的url,最后进入到一个个音频节目中获取相应的标签信息。

#### 2.3 问题与解决
- 查找下一页地址
> - 采用递归的思路，循环获取下一页面信息。
- 定位标签问题
> - 遇到在浏览器查看的html标签与实际爬取到html标签不同的情况，将爬到的html进行解析树结构，采用soup.prettify()整理树结构，定位正确的标签内容
- 爬虫封禁问题
> - 1.对header的“User-Agent”进行不断变更;
> - 2.调整休眠实际，设置随机休眠时间。
