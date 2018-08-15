import scrapy
from scrapy.http import Request
import time
from lxml import etree
from ..items import LianjiaCrawlerItem
from scrapy.selector import Selector
class YeminSpider(scrapy.Spider):
    name = 'lianjia'
    #  设置允许的域名
    allow_domains = ['bj.lianjia.com']
    #  设置需要爬取的开始网页
    start_urls = ('https://bj.lianjia.com/ershoufang/')


    # 开始爬取
    def start_requests(self):
        header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                  "Accept-Encoding": "gb2312,utf-8",
                  "Accept-Language": "zh-CN,zh;q:0.8",
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE",
                  "Connection": "keep-alive",
                  "refer": "https://bj.lianjia.com"}

        for i in range(1,6):  # !!
            url = "https://bj.lianjia.com/ershoufang/pg"+str(i)+"/"
            # 实现自动爬取,休息3秒再爬
            time.sleep(3)
            yield Request(url,callback=self.parse,headers=header)

    def parse(self, response):
        item = LianjiaCrawlerItem()

        item['name'] = response.xpath("//a[@class='']/text()").extract()
        item['total_price'] = response.xpath("//div[@class='totalPrice']/span/text()").extract()
        item['unit_price'] = response.xpath("//div[@class='unitPrice']/span/text()").extract()
        # 爬起houseInfo html片段

        items_target = ['style', 'size', 'orientation', 'decoration', 'elevator']
        dictclass = {}
        dictclass['size']= response.xpath("//div[@class='houseInfo']").extract()

        item['style'] = []
        item['size'] = []
        item['orientation'] = []
        item['decoration'] = []
        item['elevator'] = []

        for kv in range(0, 30):
            selector = etree.HTML(dictclass['size'][kv], parser=etree.HTMLParser(encoding='utf-8'))
            content = selector.xpath("//span/text()")
            content2 = selector.xpath("//div/text()")
            for each in range(len(content)):
                item[items_target[each]].append(content2[each])
                #print(str(each) + '====', content2[each])
                if len(content) < 5 and each == 3:
                    each = 4
                    item[items_target[each]].append("空值")
                    #print(str(each) + '====', "空值")
                if len(content) > 5:
                    break
        # 爬取五类时候回出现空值，导致无法分类
        # dictele3 = {}
        # dictele3['fiveclass']=response.xpath("//div[@class='houseInfo']/text()").extract()
        # item['orientation']= response.xpath("//div[@class='houseInfo']/text()").extract()
        # for k,v in dictele3.items():
        #     item['style'] = dictele3[k][::5]
        #     # item['size'] = dictele3[k][1::5]
        #     # item['orientation'] = dictele3[k][2::5]
        #     # item['decoration'] = dictele3[k][3::5]
        #     # item['elevator'] = dictele3[k][4::5]

        dictele4 =  {}
        dictele4['positionInfo'] = response.xpath("//div[@class='positionInfo']/text()").extract()
        item['floor'] = dictele4['positionInfo'][::2]
        item['build_year'] = dictele4['positionInfo'][1::2]

        item['area']=response.xpath("//div[@class='positionInfo']/a/text()").extract()

        yield item  # 不断释放返回
        # 自动翻页爬取: 通过循环自动爬取100页的数据


