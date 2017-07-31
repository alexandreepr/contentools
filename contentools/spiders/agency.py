# -*- coding: utf-8 -*-
import scrapy


class AgencySpider(scrapy.Spider): #creates the spider
    name = 'agency'
    allowed_domains = ['digitalagencynetwork.com']
    start_urls = ['https://digitalagencynetwork.com//agencies/dubai/']


    def parse(self, response):

        agencies = response.selector.xpath(   #selecting from where the information will be taken
            '//section[@id="AgenciesListing"]/div[@class="vc_row wpb_row vc_row-fluid agency-item-container"]')
        for agency in agencies:
            yield {
                'name': agency.css('.agency-info h3 a::text').extract_first(), #extracting the data
                'address': agency.css('.agency-info p::text').extract_first(),
                'phone': agency.css('.agency-info').xpath('.//p[2]/text()').extract_first(),
                'email': agency.css('.agency-info p::text').re_first(r"[^@]+@[^@]+\.[^@]+"),
                'url': agency.css('.agency-links .link.website a::attr(href)').extract_first()
            }

#In the terminal, go to the project directory and type 'scrapy crawl agencies -o agencies.csv' to run the project