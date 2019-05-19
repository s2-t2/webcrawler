import scrapy
from vacancies.items import VacanciesItem

class VacanciesSpider(scrapy.Spider):

    name = "vacancies"

    start_urls = [
            'https://www.monster.se/jobb/q-it-jobb.aspx',
            'https://www.stepstone.se/lediga-jobb-i-hela-sverige/'
            ]

    def parse(self, response):

        page = response.url.split("/")[2]

        if (page == "www.monster.se"):

            print ('[+]Crawling data from www.monster.se')

            summaries = response.css('div.summary')
            for summary in summaries:
                item = VacanciesItem()

                item['job'] = summary.css('header.card-header h2.title a::text').get()
                item['company'] = summary.css('div.company a::text').get()
                item['location'] = summary.css('div.location span.name::text').get()

                yield item

        if (page == "www.stepstone.se"):

            print ('[+]Crawling data from www.stepstone.se')

            descriptions = response.css('div.description')
            for description in descriptions:
                item = VacanciesItem()
                jobvar = description.css('h5 a::text').get()
                item['job'] = description.css('h5 a::text').get()
                item['company'] = description.css('span a::text').get()
                item['location'] = description.css('span.subtitle span.text-opaque::text').getall()[1]

                yield item


