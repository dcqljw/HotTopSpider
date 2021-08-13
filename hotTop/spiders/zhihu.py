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
            "cookie": '_zap=236448f0-97a0-4fef-8e6b-3a1559542769; d_c0="AFDSSQnOZBKPTrl-J2ETyui9u4bXebHW0yo=|1608782542"; _xsrf=D2PGncLeHPyiwoA8c2SQgdiVCGnV3ohh; q_c1=a952e211ab614b4dacdaa4974d1444de|1608809290000|1608809290000; __snaker__id=IOhPHvrVPwuS4Gb4; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=2%2B4wS3xanohBVFVQRAdvwFpxhyRhtQty; gdxidpyhxdE=IEdZuogRUdrt%2FVtOYNjePLGHSZJf2notM7rMb6e5unr6r%2Bc5COw1zHmi4OcAXyuHtYWxMyetyX5hHMz4%2BlI%2BngbMLyh6C0sfEXKnIPC%2FnRSNlltcXWTncrOZZ0JkAB%2FieSdsMTfQ3pXDXQ%5C7C9l6Z%2B5Amt5SmGROdPYSATSJ%5C3brZZ3b%3A1628650806580; YD00517437729195%3AWM_NI=nOGBdfbZl%2BaHSFnao0O5Z8IayO4l2OnQcNZhQ4MTyFXN6vbYqHXw925cuSydV2abc%2F5Cey3oa%2FdFYvaiuyym%2F4Lrux7rBhjLyDSwNq3B3jrTzrwyYdXUGaOoWnUzg3kbQ0w%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee8de66ef195839bc87da9eb8ea2d84b838f9aaaf563b5b1aaa6bc46aab199b0e52af0fea7c3b92aae9189a3e76ea286a4cce444919aa282ee3c8deb96d9cc6bbb91fc8db145ae8fadafd96493ec83b5fc4e9c92fa97e153b3989898bc3af7bdbbb4fc7096eeaf83e225f79dab9ab265a3f1aca7dc7ea3b7bb9afc67edec8493f874f5ae8e89e948bb9c9d98cd7bf19efd8bf160baaeb99adc709c8b8982ce6595b29b9be639a9be9fd1f637e2a3; captcha_session_v2="2|1:0|10:1628650027|18:captcha_session_v2|88:VzgvUkdwOU1KaHB0bWZSU0lkYXVCWTNvQXVhNlJ4enJSVWJ1UUVEcldqSnpFK1ZLYmxrZTJ2M2RCSGVGWENnWg==|b143357f80f129dbe18cc0aec1c4e49045f949fbf63c217157d6f289bb0d1d57"; l_n_c=1; r_cap_id="Mjg2MjMxYmY2ZTI5NDY4OGE1YTRhYWI1Njg4MmViMjA=|1628650029|040cc541881eeef847d5e2b854a6d93ba0297108"; cap_id="MmY3MjViZTg5MDMzNDhhN2FiZDQxYzY3ODE1ZjYyOGM=|1628650029|cef37a9125a7410a6e14538275a535c0e21dfdbc"; l_cap_id="YTNmNGNlYzk0YWM1NDJhM2FhNjU4YjNkYWEwODEyYTQ=|1628650029|2fc92a46e8b63d0a27831aa746cd0a480f29ee0a"; n_c=1; z_c0=Mi4xTEVWV0RRQUFBQUFBVU5KSkNjNWtFaGNBQUFCaEFsVk5PWWdBWWdEWkZHdUoxZXhSLWd6OW9kZUpfdE02RWI3RFNR|1628650041|c1b5ed41dc5cc96a9dd1bc0d1bbd34c7ddc20574; tst=h; tshl=; SESSIONID=o1HiWkLaX60ZNOdgiHUGrUmYIpApaNcc4Y4xpxInKQs; JOID=VVkVAk7A9KBhiepBIsYA-y22sw03qcTpDNyHDEKaxJE6w6cjRKXOtgaN7UEnJxrgy0xzYYozGG0hLdRwTl7wnn0=; osd=VFAcCkPB_alphOtIK84N-iS_uwA2oM3hAd2OBUqXxZgzy6oiTazGuweE5EkqJhPpw0FyaIM7FWwoJNx9T1f5lnA=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1628649958,1628649970,1628649979,1628650218; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1628650218; KLBRSID=b5ffb4aa1a842930a6f64d0a8f93e9bf|1628661250|1628656123'
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
