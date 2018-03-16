from scrapy.http import Response
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from magiccards.items import (LanguageItem, LanguageItemLoader,
                              CardSetItem, CardSetItemLoader)


class MagicCardsSpider(CrawlSpider):
    name = 'magiccards'
    allowed_domains = ['magiccards.info']
    start_urls = [
        'https://magiccards.info/sitemap.html'
    ]

    def parse_start_url(self, response: Response):
        for language in response.css('img.flag+a[href^="#"]'):
            loader = LanguageItemLoader(LanguageItem(), selector=language)
            loader.add_css('name', '::text')
            loader.add_css('code', '::attr(href)', re=r'#(.+)')
            code = loader.get_value('code')
            self.rules.extend([
                Rule(LinkExtractor(allow=(f'/{code}\.html',)),
                     callback='parse_set'),
                Rule(LinkExtractor(allow=f'/{code}/[1-9]\d*\w*\.html'),
                     callback='parse_card')
            ])
            yield loader.load_item()
        self._compile_rules()

    def parse_set(self, response: Response):
        loader = CardSetItemLoader(CardSetItem(), response=response)
        loader.add_css('name', 'h1::text')
        yield loader.load_item()

    def parse_card(self, response: Response):
        pass
