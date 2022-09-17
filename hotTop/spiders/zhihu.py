import scrapy
import datetime
from ..items import HottopItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/hot']

    def start_requests(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            'cookie':''
        }
        yield scrapy.Request(self.start_urls[0], self.parse, headers=headers)

    def parse(self, response):
        tops = response.xpath('//*[@id="TopstoryContent"]/div/div/div[2]/section')
        idx = 1
        for top in tops:
            item = HottopItem()
            item["idx"] = idx
            item["title"] = top.xpath('div[2]/a/@title').extract_first()
            item["url"] = top.xpath('div[2]/a/@href').extract_first()
            item["data"] = int(datetime.datetime.now().timestamp())
            item["source"] = self.name
            idx += 1
            yield item
