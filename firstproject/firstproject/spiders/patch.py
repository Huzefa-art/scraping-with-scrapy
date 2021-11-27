import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class PatchSpider(CrawlSpider):
    name = 'patch'
    allowed_domains = ['patch.com']
    start_urls = ['https://patch.com/california/alameda/calendar']
    rules = [Rule(LinkExtractor(allow='/calendar/event'),
                      callback='parse_event', follow=True)]
    custom_settings = {"FEEDS":{"Alameda.csv":{"format":"csv"}}}

     
    def parse_event(self, response):
        exists = response.xpath('//article[@class="styles_Section__card__Mi-RV"]').extract_first()
        if exists:
            event_name =  response.xpath('//div/h1/text()').extract_first()
            URL  =   response.xpath('//link[@rel="canonical"]/@href').extract_first()
            event_image = response.xpath('//img[@class="styles_CardDetail__FeaturedImage__2JL_O"]/@src').extract_first()
            more_info_url = response.xpath('//a[@class="styles_EventDetails__moreInfoLink__3Mh9Y"]/@href').extract_first()
            event_date_time = response.xpath('//div[@class="styles_EventDetails__Datetime__2wWQM"]/time/text()').extract()
            event_address = response.xpath('//address[@class="styles_EventDetails__Address__3jqD7"]/text()').extract_first()
            event_description = response.xpath('//div[@class="styles_HTMLContent__3H7Tr"]/p/text()').extract()
            
            yield {
               
               'URL': URL,
                'Event Image' :event_image,
                'More Info URL' : more_info_url,
                'Event Name': event_name,
                'Event Date': event_date_time,
                'Event Venue Name/Address':event_address,
                'Event Description':event_description,            
                }
        else:
            print(response.url)



  
        