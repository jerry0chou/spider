# -*- coding: utf-8 -*-
import scrapy
import re
import json


class HbspiderSpider(scrapy.Spider):
    name = "hbspider"
    # 使用COOkies
    cookies = {}
    raw_cookie = "uab_collina=149577707296964033740514; UM_distinctid=15c4342dde343e9-0ed3fa21162a39-6776a51-100200-15c4342ddf31f6; _umdata=A502B1276E6D5FEF2D3DCB8F335F00F7126294C8765621BD2BB71B32A50CFC0920161FD54C139A5BCD43AD3E795C914C68BD83421CB7F842E2184D00C705EDF0; _f=iVBORw0KGgoAAAANSUhEUgAAADIAAAAUCAYAAADPym6aAAABJElEQVRIS%2B1VOxYCIQwMF7KzsvFGXmW9kY2VnQfxCvgCRmfzCD9lnz53myWQAJOZBEfeeyIi7xz%2FyEXzZRPFhYbPc3hHXO6I6TbFixmfEyByeQQSxu6BcAXSkIGMazMjuBcz8pQcq44o0Iuyyc1p38C62kNsOdeSZDOQlLRQ80uOMalDgWCGMfsW2B5%2FATMUyGh2uhgptV9Ly6l5nNOa1%2F6zmjTqkH2aGEk2jY72%2B5k%2BNd9lBfLMh8GIP11iK95vw8uv7RQr4oNxOfbQ%2F7g5Z4meveyt0uKDEIiMLRC4jrG1%2FjkwKxCRE2e5lF30leyXYvQ628MZKV3q64HUFvnPAMkVuSWlEouLSiuV6dp2WtPBrPZ7uO5I18tbXWvEC27t%2BTcv%2Bx0JuJAoROEHogAAAABJRU5ErkJggg%3D%3D%2CWin32.1366.768.24; _hmt=1; _cnzz_CV1256903590=is-logon%7Clogged-in%7C1497352538311%26urlname%7Cqmymkfdg1n%7C1497352538312; _ga=GA1.2.265908819.1495777074; __asc=2db608f915ca10c31bf0b405d58; __auc=a8dd4f7f15c4342f624a2314b30; CNZZDATA1256903590=1196393121-1495772275-null%7C1497348592; uid=21207958; sid=ikC9Gc4rqKemXzCJyNEjqmqmXIn.VelAsXQgP9bZcLZ379otW9Mx%2BjcDOrzDAb21Z3Lfmz0"
    for line in raw_cookie.split(';'):
        key, value = line.split('=', 1)  # 1代表只分一次，得到两个数据
        cookies[key] = value

    def start_requests(self):
        start_url = 'http://huaban.com/favorite/beauty/'
        yield scrapy.Request(start_url, callback=self.parse, cookies=self.cookies)

    def parse(self, response):
        s = json.loads(re.search('app.page\["pins"\] = (.*?);', response.body_as_unicode(), re.S).group(1))
        for nums in range(0, len(s)):
            img_link = ['http://img.hb.aicdn.com/%s' % s[nums]['file']['key']]
            yield {
                'image_urls': img_link
            }
        next_page = 'http://huaban.com/favorite/beauty/?j3vgljf1&max=%s&limit=20&wfl=1' % s[-1]['pin_id']
        yield scrapy.Request(next_page, callback=self.parse, cookies=self.cookies)
