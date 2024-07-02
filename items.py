# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy

class BhhsambItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    address = scrapy.Field()
    image_url = scrapy.Field()

    

