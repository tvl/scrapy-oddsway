# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from oddsway.items import Odds
from urllib.parse import parse_qs
from datetime import datetime, timezone
#from soccerway.competitions import competitions_id_list

class OddsSpider(Spider):
    name = "odds"
    #allowed_domains = ["http://www.soccerway.mobi/"]
    start_urls = ['http://liveodds.oddsway.com/betting?function=home']

    def start_requests(self):

        start_url = 'http://liveodds.oddsway.com/betting?function=home'
        request = Request(url=start_url, callback=self.parse_odds)
        request.meta['proxy'] = 'http://127.0.0.1:8118'
        yield request

    def parse_odds(self, response):
        rows = response.xpath('//tr[@id="datarow-home"]')
        for r in rows:
            item = Odds()
            item['home_team'] = r.xpath('./td[@id="lhs-cells-team-ah"]/text()').extract_first()
            item['away_team'] = r.xpath('./td[@id="mid-cells-team-ah"]/text()').extract_first()
            item['home'], item['draw'], item['away'] = r.xpath('./td[@id="mid-cells-odds"]//td//a/text()').extract()
            item['id'] = parse_qs(r.xpath('./td[@id="oddslink"]//a/@href').extract_first())['matchnumber'][0]
            item['competition_id'] = parse_qs(r.xpath('./td[@id="oddslink"]//a/@href').extract_first())['/betting?competitionid'][0]

            item['datetime'] = datetime.fromtimestamp(int(r.xpath('./td[@id="mid-cells-date-ah"]//script/text()').extract_first().strip()[17:-5]), timezone.utc).isoformat(' ')
            item['updated'] = datetime.utcnow().isoformat(' ')
            yield item
            #return item
            #self.log('URL: {}'.format(response.url))

