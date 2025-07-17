import scrapy

class ServicesSpider(scrapy.Spider):
    name = "services"
    start_urls = ["https://bcdtravel.com"]

    def parse(self, response):
        for service in response.css("div.service-title"):
            yield {
                "title": service.css("h3::text").get(),
                "description": service.css("p::text").get()
            }

        # Pagination logic
        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)