from scrapy.selector import Selector
from scrapy.http import Request
from items import Atracao
from scrapy.spiders import CrawlSpider
from datetime import date
from datetime import datetime
import unicodedata


class ViradaCulturalSpider(CrawlSpider):
    name = "Virada_cultural"
    start_urls = [
        "http://web.archive.org/web/20160825145532/http://www.viradaculturalpaulista.sp.gov.br/cidades"]

    def parse(self, response):
        body_sel = Selector(response)  # Seletor para analisar o HTML
        # Extraindo links das cidades
        url_cidade = body_sel.xpath(
            "//div[@class='list-cities']//ul//li//a/@href").exctract()

        for url in url_cidade:
            yield Request(url, self.parse_atracao)

    def parse_atracao(self, response):
        body_sel = Selector(response)

        cidade = self.to_str(body_sel.xpath("//h1/text()"))
        endereco = self.to_str(body_sel.xpath(
            "//span[@class='address']/text()"))

        atracao_selectores = body_sel.xpath("//ul[@class='list-events']//li")

        for sel in atracao_selectores:
            atracao = Atracao(cidade=cidade, endereco=endereco)
            atracao['dia'] = self.to_date(
                sel.xpath(".//span[@class='date']//text()"))
            atracao["hora"] = self.to_str(
                sel.xpath(".//span[@class='hour']//text()"))
            atracao["artista"] = self.to_str(
                sel.xpath(".//span[@class='artist']//text()"))

            self.print_item(atracao)

    def to_date(self, selector):
        data = self.to_str(selector)  # "14/5"
        dia, mes = data.split("/")  # ["14", "5"]
        ano = date.today().year  # 2016
        return datetime(ano, int(mes), int(dia)).strftime("%d-%m-%Y")

    def to_str(self, selector):
        return selector.extract()[0].encode("utf-8")
