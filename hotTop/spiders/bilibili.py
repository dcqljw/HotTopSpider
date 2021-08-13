import scrapy
import datetime
from ..items import HottopItem


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://s.search.bilibili.com/main/hotword']

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], self.parse)

    def parse(self, response):
        results = response.json()["list"]
        idx = 1
        for result in results:
            item = HottopItem()
            item["idx"] = idx
            item["title"] = result["keyword"]
            item["url"] = "https://search.bilibili.com/all?keyword=" + result["keyword"]
            item["data"] = int(datetime.datetime.now().timestamp())
            item["source"] = self.name
            idx += 1
            yield item
