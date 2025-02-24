import scrapy
import json
from sreality.items import SrealityItem   

class FlatSpider(scrapy.Spider):
    name = 'sreality'
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=100']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/json',
            'Accept-Language': 'cs,en-US;q=0.9,en;q=0.8',
        }
    }

    def get_room_layout(self, title):
        import re
        match = re.search(r'(\d\+(?:kk|1|2|3|4))', title.lower())
        return match.group(1) if match else "unknown"

    def parse(self, response):
        data = json.loads(response.body)

        for flat in data['_embedded']['estates']:
            database_item = SrealityItem() 
            database_item['title'] = flat['name']
            database_item['price'] = flat['price']

            database_item['imgs'] = [img_link['href'] for img_link in flat['_links']['images']]
            room_layout = self.get_room_layout(flat['name'])
            locality = flat['seo']['locality']  
            hash_id = flat['hash_id']  
            database_item['detail_url'] = f"https://www.sreality.cz/detail/prodej/byt/{room_layout}/{locality}/{hash_id}"
            yield database_item