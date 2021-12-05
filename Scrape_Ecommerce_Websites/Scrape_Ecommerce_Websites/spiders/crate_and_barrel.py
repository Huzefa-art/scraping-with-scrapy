import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class CrateAndBarrelSpider(CrawlSpider):
    name = 'crate_and_barrel'
    allowed_domains = ['crateandbarrel.com']
    start_urls = ['https://www.crateandbarrel.com/whats-new/new-furniture/1']
    rules = [Rule(LinkExtractor(allow='/s'),
                      callback='parse_event', follow=True)]
    custom_settings = {"FEEDS":{"crate_and_barrel.csv":{"format":"csv"}}}
    
        
        

    def parse_event(self, response):
  
        exists = response.xpath('//div[@class="main-product-and-family section-recently-viewed-spill"]').extract_first()
        if exists:
            image_link = response.xpath('//button[@class="gallery-img-button button-transparent"]/img/@src').extract_first()
            Name = response.xpath('//h1[@class="product-name text-xl-bold"]/text()').extract_first()
            SKU = response.xpath('//span[@class="sku-number"]/text()').extract_first()
            price = response.xpath('//span[@class="regPrice"]/text()').extract_first()
            depth_size_fabric = response.xpath('//div[@class="accordion-sor-description text-md-reg"]/text()').extract()
            description = response.xpath('//div[@class="text-md-reg description-text"]/div/text()').extract()
            rating =  response.xpath('//span[@class="review-stars-bar"]/@title').extract_first()

            yield {
               
               
               'Image link': image_link,
                'Product name' :Name,
                'SKU' : SKU,
                'Price': price,
                'Depth/size/fabric': depth_size_fabric,
                'Product Description':description,
                'Rating':rating,            
                }
        else:
            print(response.url)
                
                

                
            
            

        
            
        
        
        
