import json

import scrapy

from DemoScrapy.items import DemoscrapyItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def wenzi(n):
    return ''.join(''.join(''.join(n.split(' ')).split('\n')).split('\r'))

def Json_GetUrl ( filename , e ):
    f = open ( filename , "r" )
    for data in f.readlines ( ):
        yield json.loads(data)[e][0]

class DemoSpider(scrapy.Spider):
    name = "demo2"
    allowed_domains = ["demo.com"]
    start_urls =('http://yyk.99.com.cn/yibao/foshan.html',
                'http://yyk.99.com.cn/yibao/shenzhen.html',
                'http://yyk.99.com.cn/yibao/guangzhou.html',
                'http://yyk.99.com.cn/yibao/suzhou.html',
                'http://yyk.99.com.cn/yibao/wuxi.html',
                'http://yyk.99.com.cn/yibao/szxxzdw.html',
                'http://yyk.99.com.cn/yibao/shaoguan.html',
                'http://yyk.99.com.cn/yibao/zhanjiang.html',
                'http://yyk.99.com.cn/yibao/baoan.html',)

    def parse(self, response):
        item = DemoscrapyItem()
        for site in response.xpath('//div[@class="tablist"]'):
            for yiyuandata in site.xpath('ul/li/a'):
                item['yiyuanmingcheng'] = wenzi(yiyuandata.xpath('text()').extract()[-1])
                item['yiyuanwangzhi'] = wenzi(yiyuandata.xpath('@href').extract()[-1])
                yield item