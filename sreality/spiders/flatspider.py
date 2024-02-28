import scrapy
import json
from sreality.items import SrealityItem   

class FlatSpider(scrapy.Spider):
    name = 'sreality'
    allowed_domains = ['https://www.sreality.cz']
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500']

    def parse(self, response):
        database_item = SrealityItem()
        data = json.loads(response.body)
        for flat in data['_embedded']['estates']:
            database_item['title'] = flat['name']
            database_item['imgs'] = [img_link['href'] for img_link in flat['_links']['images']]
            yield database_item