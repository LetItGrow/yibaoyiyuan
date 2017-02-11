import json
import scrapy

from DemoScrapy.items import DemoscrapyItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def wenzi(n):
    return ''.join(''.join(''.join(n.split(' ')).split('\n')).split('\r'))

def Json_GetUrl ( filename ,e ,html):
    f = open ( filename , "r" )
    for data in f.readlines( ):
        yield json.loads(data)[e]+html

class DemoSpider(scrapy.Spider):
    name = "demo4"
    allowed_domains = ["demo.com"]
    start_urls = ("http://yyk.99.com.cn/dongcheng/68030/zhuanjia.html",)#Json_GetUrl('ybdata.json','yiyuanwangzhi','zhuanjia.html')

    # def parse(self, response):
    #     item = DemoscrapyItem()
    #     item['yiyuanbianhao'] = response.url.split('/')[-2]
    #     item['yiyuanmingcheng'] = wenzi(response.xpath('//p[@class="bnleft"]/text()').extract()[-1][3:])
    #     for site in response.xpath('//table[@class="hpdoc_table"]/tbody/tr'):
    #         item['keshi'] = site.xpath('td[1]/a/text()').extract()
    #         item['yisheng'] = site.xpath('td[2]/span/a/text()').extract()
    #         yield item

    # def parse(self, response):
    #     item = DemoscrapyItem()
    #     item['keshihuizong'] = response.xpath('//table[@class="hpdoc_table"]/tbody/tr/td[1]/a/text()').extract()
    #     item['yiyuanbianhao'] = response.url.split('/')[-2]
    #     item['yiyuanmingcheng'] = wenzi(response.xpath('//p[@class="bnleft"]/text()').extract()[-1][3:])
    #     yield item