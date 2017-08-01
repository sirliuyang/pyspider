import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://en.wikipedia.org/wiki/Main_Page/',
    ]

    def parse(self, response):
        for div in response.css('div.quote'):
            yield {
                'text': div.css('span.text::text').extract_first(),
                'author': div.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)