import scrapy
from books_scraper.items import BooksScraperItem  # استفاده از BooksScraperItem

class BookSpider(scrapy.Spider):
    name = 'books'
    custom_settings = {
        'FEEDS': {'data.csv': {'format': 'csv',}}
    }

    def start_requests(self):
        url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        product = response.css("div.product_main")

        book_item = BooksScraperItem() 
        book_item["title"] = product.css("h1::text").get()
        book_item["category"] = response.xpath("//ul[@class='breadcrumb']/li[3]/a/text()").get()
        book_item["description"] = response.xpath("//meta[@name='description']/@content").get()
        book_item["price"] = response.css('p.price_color::text').get()

        
       
        
        
        
        
        yield book_item

        


