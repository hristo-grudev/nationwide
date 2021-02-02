import scrapy

from scrapy.loader import ItemLoader
from ..items import NationwideItem
from itemloaders.processors import TakeFirst


class NationwideSpider(scrapy.Spider):
	name = 'nationwide'
	start_urls = ['https://www.nationwide.co.uk/news']
	page = 1

	def parse(self, response):
		post_links = response.xpath('//h4/a/@href')
		yield from response.follow_all(post_links, self.parse_post)

		page_links = response.xpath('//div[@id="PaginationPanel"]/nav/ol/li/a[@class="iconLink"]/@href')
		yield from response.follow_all(page_links, self.parse)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@id="content_2_newsarticlecontent_0_grid_b05485cec11c4ef5818bbbf7977e5d56_0_ColumnContainer"]/descendant-or-self::*/text()[normalize-space() and not(ancestor::span | ancestor::p[@class="textStyle04"])]').getall()
		description = ' '.join(description)
		date = response.xpath('//div[@class="col col8"]/p//text()').get()

		item = ItemLoader(item=NationwideItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
