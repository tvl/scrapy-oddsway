# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class Odds(Item):
    id = Field()
    datetime = Field()
    #area_id = Field()
    #area_name = Field()
    competition_id = Field()
    #competition_name = Field()
    home_team = Field()
    away_team = Field()
    home = Field()
    draw = Field()
    away = Field()
    #kick_off = Field()
    #score = Field()
    updated = Field()


