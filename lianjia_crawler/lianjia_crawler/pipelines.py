# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class LianjiaCrawlerPipeline(object):

    # 创建mysql的连接
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", user="root", password="931015", db="lianjia",
                                    charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):

        for i in range(0, 30):
            try:
                name=item['name'][i]
                total_price=item['total_price'][i]
                unit_price=item['unit_price'][i]
                style=item['style'][i]
                orientation=item['orientation'][i]
                decoration=item['decoration'][i]
                elevator=item['elevator'][i]
                floor=item['floor'][i]
                build_year=item['build_year'][i]
                area=item['area'][i]
                size=item['size'][i]

                sql_insert = "insert into bj_ershoufang(name,style,area,orientation,decoration,elevator,floor,build_year,unit_price,total_price,size) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                self.cur.execute(sql_insert, (name,style,area,orientation,decoration,elevator,floor,build_year,unit_price,total_price,size))
                self.conn.commit()
                print("写入成功！")
            except Exception as e:
                self.conn.rollback()
                print('插入数据失败' + str(e.args))
        return item
    pass