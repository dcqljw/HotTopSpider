import scrapy
import datetime
from ..items import HottopItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://top.baidu.com/board?tab=realtime']

    def start_requests(self):
        yield scrapy.Request("https://top.baidu.com/board?tab=realtime", self.parse)

    def parse(self, response):
        tops = response.xpath('//*[@id="sanRoot"]/main/div[2]/div/div[2]/div')
        idx = 1
        for top in tops:
            item = HottopItem()
            item["idx"] = idx
            item["title"] = top.xpath('div[2]/a/div/text()').extract_first().strip()
            item["url"] = top.xpath('div[2]/a/@href').extract_first()
            item["data"] = int(datetime.datetime.now().timestamp())
            item["source"] = self.name
            idx += 1
            yield item
