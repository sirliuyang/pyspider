import scrapy
from scrapy.selector import Selector

class MicroSoftSpider(scrapy.Spider):
    name = "microsoft downloads"
    count = 0
    start_urls = [
        'https://www.microsoft.com/en-us/download/search.aspx?first=1',
    ]

    def parse(self, response):
        rootPath='https://www.microsoft.com'
        #table = {}
        #table['result'] = response.css('h3 a::attr(href)').extract()
        for item in response.css('h3'):
            yield {
                item.css('a span::text').extract_first() : item.css('a::attr(href)').extract_first()
            }

        next_page=''
        for next in response.css('div.pager_items'):
            if next.css('a::attr(title)').extract() == 'next page':
                result = rootPath + next.css('a::attr(href)').extract_first()
                print(result) # problem here

        if next_page is not None:
            yield response.follow(next_page, self.parse)

        '''
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        '''
