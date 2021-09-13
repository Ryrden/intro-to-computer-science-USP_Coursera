# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import item, Field

class ScrapyCulturalSpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Atracao(Item):
    cidade = Field()
    endereco = Field()
    dia = Field()
    hora = Field()
    artista = Field()