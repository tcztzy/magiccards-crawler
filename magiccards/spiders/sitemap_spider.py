import scrapy

from magiccards.items import LanguageItem, LanguageItemLoader


class MagicCardsSpider(scrapy.Spider):
    name = 'magiccards'
    start_urls = [
        'https://magiccards.info/sitemap.html'
    ]

    def parse(self, response):
        for language in response.css('img.flag+a[href^="#"]'):
            loader = LanguageItemLoader(LanguageItem(), selector=language)
            loader.add_css('name', '::text')
            loader.add_css('code', '::attr(href)', re=r'#(.+)')
            yield loader.load_item()
