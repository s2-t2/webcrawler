# webcrawler
web crawler based on Python's scrapy that stores data to mongodb database

## Technology stack and libraries used
- Python, Scrapy framework
- Database: MongoDB

#### From the top level directory, i.e., vacancies/ run the following command 
- scrapy crawl vacancies

Running this command will create a database named items and vacancies collection that stores the data (job title, company name, and job location) from monster.se and stepstone.se 

##### REFERENCES 
- https://docs.scrapy.org/en/latest/topics/item-pipeline.html#writing-your-own-item-pipeline
- https://docs.scrapy.org/en/latest/intro/tutorial.html#our-first-spider
- https://realpython.com/web-scraping-and-crawling-with-scrapy-and-mongodb/
