import scrapy

from DemoScrapy.items import DemoscrapyItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def wenzi(n):
    return ''.join(''.join(''.join(n.split(' ')).split('\t')).split('\n'))

class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["demo.com"]
    start_urls = ('http://yyk.99.com.cn/city.html',)

    def parse(self, response):
        item = DemoscrapyItem()
        i = 0
        sheng = response.xpath('//div[@class="cityarea"]/h4/text()').extract()
        for site in response.xpath('//div[@class="cityarea"]'):
            for cssite in site.xpath('ul'):
                i += 1
                for cslisite in cssite.xpath('li'):
                    item['shenglishu'] = sheng[i-1]
                    item['chengshimingcheng'] = cslisite.xpath('a/text()').extract()
                    item['chengshiurl'] = ''.join(['http://yyk.99.com.cn']+cslisite.xpath('a/@href').extract())   
                    yield item
            