import scrapy
from scrapy.utils.project import get_project_settings

class TopicSearchSpider(scrapy.Spider):
    name = 'topic_search_spider'

    def __init__(self):
        self.topic = get_project_settings().get("TOPIC")
        self.start_urls= get_project_settings().get("START_URLS")       

    def parse(self, response):
        print("Starting search")
        items = []

        titles = response.css('.title.may-blank::text').extract()
        titles = response.selector.xpath('//*[contains(text(), "%s")]' % (self.topic)).extract()
        if len(titles) > 0:
            timestamp = response.meta['wayback_machine_time'].timestamp()
            return {'timestamp': timestamp, 'items': titles}
