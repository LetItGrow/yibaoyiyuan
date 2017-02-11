import scrapy

from DemoScrapy.items import DemoscrapyItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def wenzi(n):
    return ''.join(''.join(''.join(n.split(' ')).split('\t')).split('\n'))
def createurl():
    yield ''
class DemoSpider(scrapy.Spider):
    name = "demo1"
    allowed_domains = ["demo.com"]
    start_urls = ('http://yyk.99.com.cn/yibao',)

    def parse(self, response):
        item = DemoscrapyItem()
        for site in response.xpath('//div[@class="tablist"]/h4'):
            item['shenglishu'] =(site.xpath('a/text()').extract())
            item['chengshimingcheng'] = site.xpath('em/a/text()').extract()
            item['chengshiurl'] =[''.join(['http://yyk.99.com.cn']+site.xpath('em/a/@href').extract())]
            yield item