
import scrapy
from scrapy.loader import ItemLoader, Item
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Identity


class MatchItem(scrapy.Item):
    match_id = scrapy.Field()
    match_url = scrapy.Field()
    ms = scrapy.Field()
    date = scrapy.Field()
    league = scrapy.Field()
    attendance = scrapy.Field()
    stadium = scrapy.Field()
    home_team = scrapy.Field()
    away_team = scrapy.Field()
    result = scrapy.Field()
    result_time = scrapy.Field()
    result_agg = scrapy.Field()
    home_score = scrapy.Field()
    away_score = scrapy.Field()
    home_shots = scrapy.Field()
    home_shots_on_goal = scrapy.Field()
    home_fouls = scrapy.Field()
    home_corner_kicks = scrapy.Field()
    home_offsides = scrapy.Field()
    home_possession = scrapy.Field()
    home_yellow_cards = scrapy.Field()
    home_red_cards = scrapy.Field()
    home_saves = scrapy.Field()
    away_shots = scrapy.Field()
    away_shots_on_goal = scrapy.Field()
    away_fouls = scrapy.Field()
    away_corner_kicks = scrapy.Field()
    away_offsides = scrapy.Field()
    away_possession = scrapy.Field()
    away_yellow_cards = scrapy.Field()
    away_red_cards = scrapy.Field()
    away_saves = scrapy.Field()



class MatchLoader(ItemLoader):
    default_item_class = MatchItem
    default_output_processor = TakeFirst()

    league_in = MapCompose(unicode.lower, unicode.strip)
    home_team_in = MapCompose(unicode.lower, unicode.strip)
    away_team_in = MapCompose(unicode.lower, unicode.strip)
    result_in = MapCompose(unicode.lower, unicode.strip)
    result_time_in = MapCompose(unicode.lower, unicode.strip)
    stadium_in = MapCompose(unicode.lower, unicode.strip)
