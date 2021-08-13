import scrapy


class BilitopSpider(scrapy.Spider):
    name = 'biliTop'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/v/popular/rank/all']

    def start_requests(self):
        yield scrapy.Request(self.start_urls, self.parse)

    def parse(self, response):
        tops = response.xpath()
