import json
from itemadapter import ItemAdapter

class BhhsambPipeline:
    def open_spider(self, spider):
        self.file = open('agents.json', 'w')
        self.file.write("[\n")

    def close_spider(self, spider):
        self.file.write("\n]")
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(ItemAdapter(item))) + ",\n"
        self.file.write(line)
        return item

class DataminePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        if adapter.get('name'):
            item['name'] = adapter['name'].strip()
        if adapter.get('title'):
            item['title'] = adapter['title'].strip()
        if adapter.get('phone'):
            item['phone'] = adapter['phone'].strip()
        if adapter.get('email'):
            item['email'] = adapter['email'].strip()
        if adapter.get('address'):
            item['address'] = adapter['address'].strip()
        return item
