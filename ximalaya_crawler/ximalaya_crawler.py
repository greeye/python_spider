import json
import random
import time
import pymongo
import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
import re
from urllib import parse
# 连接 mongodb
client = pymongo.MongoClient('localhost')
db= client['XimaLaYa']
col1 = db['album_content']
col2 = db['album_infomation']

UA_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5789.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

headers1 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'max-age=0',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.ximalaya.com/',
    'Upgrade-Insecure-Requests': '1',
    "User-Agent": random.choice(UA_LIST)
}

headers2 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'max-age=0',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.ximalaya.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': random.choice(UA_LIST)
}



def get_category_url():
    # category_id !  category_name !   part_category!   has_child  level  link!
    docu_dict = requests.get('https://www.ximalaya.com/revision/category/allCategoryInfo',headers=headers2).text
    docu_dict = json.loads(docu_dict)

    id = 1
    for cate_dict in docu_dict.get('data'):
           category_info1={
              'root_category':cate_dict.get('name')
           }
           for subcate_dict in cate_dict.get('categories'):
              category_info2 = {
                   'parent_category': subcate_dict.get('displayName')
               }
              for item_dict in subcate_dict.get('subcategories'):

                  for key,value in item_dict.items():
                        category_info3 = {
                          '_id': id,
                          'parent_categoryId': item_dict.get('categoryId'),
                          'child_categoryName':item_dict.get('displayValue'),
                          'child_categoryId': item_dict.get('id'),
                          'link':item_dict.get('link'),
                          'has_child': True
                        }
                        # 整合字典数据
                        category_infoSum= dict(category_info1,**category_info2,**category_info3)

                  #插入整合的信息到 mongodb 中
                  id += 1
                  col1.insert(category_infoSum)

                  print(category_infoSum)
                  print('---------item_dict-------item_dict---------item_dict-------')
              print('---------subcate-------subcate---------subcate-------')
           print('----------cate_dict----------------cate_dict--------------')


def get_url_test():
    start_urls = ['https://www.ximalaya.com{}'.format(item.get('link')) for item in col1.find()]
    for start_url in start_urls:
        print('爬取当前页面：{}'.format(start_url))
        html = requests.get(start_url, headers=headers1).text
        soup = BeautifulSoup(html, 'html5lib')
        #soup1 = soup.prettify()  整理树结构
        #print(soup.prettify())
        #catagory = soup.find_all(class_="bread-crumb-link rBL")
        catagory={
            "root_catagory":soup.find_all(class_="bread-crumb-link rBL")[1].string,
            "parent_category":soup.find_all(class_="bread-crumb-link rBL")[2].string
        }
        print("分类信息")
        print(catagory)
        for item in soup.find_all(class_="album-title line-2 lg Iki"):
            print("------音频信息-------")
            content1 = {
                'href': item['href'],
                'title': item['title'],
            }
            another('https://www.ximalaya.com' + item['href'], content1,catagory)
        next_url(start_url,catagory)

    # 找下一页的相对路径
def next_url(url_next,catagory):
        print("--------")
        html = requests.get(url_next, headers=headers1).text
        soup = BeautifulSoup(html, 'lxml')
        next_page = soup.find(class_="page-next page-item tthf")
        if next_page:
            print("======")
            next_pp = next_page.a['href']
            url_next = parse.urljoin('https://www.ximalaya.com/youshengshu/wenxue/', next_pp)
            print('爬取当前页面：{}'.format(url_next))
            # 解析下一页的数据
            html_next = requests.get(url_next, headers=headers1).text
            soup_next = BeautifulSoup(html_next, 'lxml')
            time.sleep(random.randint(1,2)+random.random())
            # 解析
            for item in soup_next.find_all(class_="album-title line-2 lg Iki"):
                content = {
                    'href': item['href'],
                    'title': item['title']
                }
                print(content)
                another('https://www.ximalaya.com' + item['href'],content ,catagory)
            # 递归遍历页面
            next_url(url_next,catagory)

        else:
            print("over!")
            print('last_url:{}'.format(url_next))

# item 页面解析
def another(url2,content,catagory):
    # title_id title link label root_category parent_category
    html = requests.get(url2,headers=headers2).text
    soup2 = BeautifulSoup(html,'lxml')

    # 获取归属分类标题
    # for item in soup2.find_all(class_="category PIuT"):
    #     content2 ={
    #         'category':item.a['title']
    #     }
    #     print(content2)
    # 获取音频标签
    print('----------音频标签-----------')
    for item in soup2.find_all(class_="tags PIuT"):
        list_lag = []
        for item2 in item.find_all('a'):

            if item2:
                list_lag.append(item2.string)
            else:
                continue
        print(list_lag)
        content1 = {
         '_id': re.sub(r'\D',"",url2),
         'title': '',
         'link': url2,
         'label': list_lag
            }

        content_sum = dict(content1, **content,**catagory)
        print(content_sum)
        # 音频相关信息插入到mongodb中
        col2.insert(content_sum)
        time.sleep(random.randint(1, 3)+random.random())

if __name__ == '__main__':
    #get_category_url()
    get_url_test()