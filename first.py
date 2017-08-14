import scrapy
from scrapy.selector import Selector

class QuotesSpider(scrapy.Spider):
    name = "downloads"
    start_urls = [
        'https://www.microsoft.com/en-us/download/search.aspx',
    ]

    def parse(self, response):
        for eachdiv in response.css('h3'):
            yield {
                'links':eachdiv.xpath('')
            }
        '''
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()8
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        '''
