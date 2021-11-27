import scrapy


class AlamedacrawlerSpider(scrapy.Spider):
    name = 'alamedacrawler'
    allowed_domains = ['https://patch.com/california/alameda/calendar']
    start_urls = ['http://https://patch.com/california/alameda/calendar/']

    def parse(self, response):
           for href in response.css(".styles_Card__TitleLink__1wfDO::attr('href')"):
                url = response.urljoin(href.extract())
                yield scrapy.Request(url, callback = self.parse_dir_contents)
                
    def parse_dir_contents(self, response):
        for sel in response.css('styles_Section__card__Mi-RV'):
            item['Eventname'] = sel.css(".styles_CardDetail__Title__3L-vO::text").extract()
           
            yield item

    
