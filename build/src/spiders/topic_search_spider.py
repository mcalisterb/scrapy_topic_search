import scrapy
from scrapy.utils.project import get_project_settings

class TopicSearchSpider(scrapy.Spider):
    name = 'topic_search_spider'

    def __init__(self):      
        #custom_settings = {
        #    'WAYBACK_MACHINE_TIME_RANGE': (20181201, 20181218)
        #}
        self.topic = get_project_settings().get("TOPIC")
        self.start_urls= get_project_settings().get("START_URLS")
        
    #def start_requests(self):
    #    yield scrapy.Request('http://www.news24.com/')
        #yield scrapy.Request('http://www.ewn.co.za/')
        #yield scrapy.Request('http://www.reddit.com/r/gameofthrones/')
        #yield scrapy.Request('https://ewn.co.za/Topic/Shack-fires')     

    def parse(self, response):
        print("Starting search")
        items = []

        titles = response.css('.title.may-blank::text').extract()
        titles = response.selector.xpath('//*[contains(text(), "%s")]' % (self.topic)).extract()#response.css('title').extract()
        print("---- TITLES ---")
        print(u' '.join(titles).encode('utf-8').strip())
        
        #for div in response.css('titles'):#'div.sitetable div.thing'):
        #    print("hells bells")
        #    print(div)
        #    try:
        #        title = div.css('p.title a::text').extract_first()
        #        votes_div = div.css('div.score.unvoted')
        #        votes = votes_div.css('::attr(title)').extract_first()
        #        votes = votes or votes_div.css('::text').extract_first()

        #        items.append({'title': title, 'votes': int(votes)})
        #    except:
        #        pass

        print("Length of items: " + str(items))

        if len(titles) > 0:
            timestamp = response.meta['wayback_machine_time'].timestamp()
            return {'timestamp': timestamp, 'items': titles}
