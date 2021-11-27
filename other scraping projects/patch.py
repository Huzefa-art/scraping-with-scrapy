import scrapy


class PatchSpider(scrapy.Spider):
    name = 'patch'
    allowed_domains = ['patch.com']
    start_urls = ['https://patch.com/california/alameda/calendar']
    
     
    def parse(self, response):
        eventnames = response.css(".styles_Card__TitleLink__1wfDO::text").extract()
        eventurls = response.css(".styles_Card__TitleLink__1wfDO::attr(href)").extract()
        eventurls2 = response.xpath("//a[starts-with(@href,'/')]").extract()

        
        for event in zip(eventnames, eventurls, eventurls2):
            #create a dictionary to store the scraped info
            scraped_info = {
                'EventName' : event[0],
                'EventUrls': event[1],
                'EventUrls2' : event[2],
            }
            yield scraped_info

  
        