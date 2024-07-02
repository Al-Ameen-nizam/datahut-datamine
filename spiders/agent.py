import scrapy
from scrapy import Request
from datamine.items import BhhsambItem  

class AgentSpider(scrapy.Spider):
    name = "agent"
    allowed_domains = ["bhhsamb.com"]
    start_urls = ["https://www.bhhsamb.com/agents"]

    def parse(self, response):
    
        profile_links = response.css("a.cms-int-roster-card-image-container::attr(href)").getall()
        for link in profile_links:
            yield Request(response.urljoin(link), callback=self.parse_profile)
    
        next_page = response.css("a.page-link-next::attr(href)").get()
        if next_page:
            yield Request(response.urljoin(next_page), callback=self.parse)

    def parse_profile(self, response):
        item = BhhsambItem()
        item['name'] = response.xpath('//h2/text()').get().strip() if response.xpath('//h2/text()').get() else None
        item['title'] = response.xpath('//div[@class="site-roster-card-content-title"]/span/text()').get().strip() if response.xpath('//div[@class="site-roster-card-content-title"]/span/text()').get() else None
        item['phone'] = response.xpath('//a[contains(@href, "tel")]/text()').get().strip() if response.xpath('//a[contains(@href, "tel")]/text()').get() else None
        item['email'] = response.xpath('//a[contains(text(), "Email")]/@href').get().strip().replace("mailto:", "") if response.xpath('//a[contains(text(), "Email")]/@href').get() else None
        item['address'] = response.xpath('//ul/li[last()]/text()').get().strip() if response.xpath('//ul/li[last()]/text()').get() else None
        # image
        item['image_url'] = response.css('.cms-int-roster-card-image::attr(style)').re_first(r"url\(()\)")  
        yield item
