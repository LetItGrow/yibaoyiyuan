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
    name = "demo3"
    allowed_domains = ["demo.com"]
    start_urls =Json_GetUrl('ybdata.json','yiyuanwangzhi','jianjie.html')

    def parse(self, response):
        item = DemoscrapyItem()
        item['yiyuanbianhao'] = response.url.split('/')[-2]

        if response.xpath('//p[@class="bnleft"]/a[2]/text()').extract() ==  [u'\u5317\u4eac\u5e02'] or (response.xpath('//p[@class="bnleft"]/a[2]/text()').extract()) ==  [u'\u4e0a\u6d77\u5e02'] or (response.xpath('//p[@class="bnleft"]/a[2]/text()').extract()) ==  [u'\u91cd\u5e86\u5e02'] or (response.xpath('//p[@class="bnleft"]/a[2]/text()').extract()) ==  [u'\u5929\u6d25\u5e02'] :
            item['shenglishu'] = [u'\u76f4\u8f96\u5e02']
            item['shilishu'] = response.xpath('//p[@class="bnleft"]/a[2]/text()').extract()
            item['xianlishu'] = response.xpath('//p[@class="bnleft"]/a[3]/text()').extract()
        else:
            item['shenglishu'] = response.xpath('//p[@class="bnleft"]/a[2]/text()').extract()
            item['shilishu'] = response.xpath('//p[@class="bnleft"]/a[3]/text()').extract()
            item['xianlishu'] = response.xpath('//p[@class="bnleft"]/a[4]/text()').extract()

        item['yiyuanmingcheng'] = wenzi(response.xpath('//p[@class="bnleft"]/text()').extract()[-1][3:])
        item['yiyuanxingzhi'] = wenzi(response.xpath('//div[@class="hpi_content clearbox"]/ul/li[2]/text()').extract()[0])
        item['yiyuandengji'] = wenzi(response.xpath('//div[@class="hpi_content clearbox"]/ul/li[3]/span/text()').extract()[0])
        item['lianxidianhua'] = wenzi(response.xpath('//div[@class="hpi_content clearbox"]/ul/li[4]/span/text()').extract()[0])
        item['yiyuandizhi'] = wenzi(response.xpath('//div[@class="hpi_content clearbox"]/ul/li[5]/span/text()').extract()[0])

        item['yiyuanyuanzhang'] = wenzi(response.xpath('//div[@class="leftpad10 hpbasicinfo"]/table/tr[2]/td[2]/text()').extract()[0])
        item['nianfen'] = wenzi(response.xpath('//div[@class="leftpad10 hpbasicinfo"]/table/tr[2]/td[4]/text()').extract()[0])
        item['keshishu'] = wenzi(response.xpath('//div[@class="leftpad10 hpbasicinfo"]/table/tr[3]/td[4]/a/u/text()').extract()[0])
        item['yihurenshu'] = wenzi(response.xpath('//div[@class="leftpad10 hpbasicinfo"]/table/tr[3]/td[6]/a/u/text()').extract()[0])
        item['bingchangshu'] = wenzi(response.xpath('//div[@class="leftpad10 hpbasicinfo"]/table/tr[4]/td[2]/text()').extract()[0])
        item['nianmenzhenliang'] = wenzi(response.xpath('//div[@class="leftpad10 hpbasicinfo"]/table/tr[4]/td[4]/text()').extract()[0])

        if response.xpath('//div[@class="hpcontent"]/p').extract()[1:] == []:
            item['yiyuanjianjie'] = response.xpath('//div[@class="hpcontent"]/p').extract()
        else:
            item['yiyuanjianjie'] = response.xpath('//div[@class="hpcontent"]/p').extract()[1:]
        item['yiyuanwangzhi'] = response.xpath('//a[@rel="nofollow"]/@href').extract()[-1]
        yield item