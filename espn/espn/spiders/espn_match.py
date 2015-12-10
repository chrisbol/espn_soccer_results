import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from espn.items import MatchItem,MatchLoader
from scrapy.loader import ItemLoader
import datetime

class getMatches(scrapy.Spider):
    name = "espn_match"
    allowed_domains = ["espnfc.com"]
    base_date = datetime.date.today()
    base_date_format = base_date.strftime('%Y%m%d')
    start_urls = [
        'http://www.espnfc.com/scores?date=%s' % base_date_format
    ]


    def parse(self, response):
        for match in response.xpath('//div[@class="score full"]/@data-gameid')[:]:
            match_id = match.extract()
            match_url = 'http://www.espnfc.com/gamecast/statistics/id/%s/statistics.html' % match_id
            req = scrapy.Request(match_url, callback=self.parse_match)
            req.meta['match_id'] = match_id
            yield req

    def parse_match(self, response):
        l = MatchLoader(response=response)
        l.add_value('match_id', response.meta['match_id'])
        l.add_value('match_url', response.url)
        l.add_xpath('league', '//div[@class="match-details"]/p[@class="floatleft"]/text()[1]')
        l.add_xpath('stadium', '//div[@class="match-details"]/p[@class="floatright upperCase"]/text()[1]')
        l.add_xpath('ms', '//div[@class="match-details"]/p[@class="floatleft"]/span', re='new Date\(([0-9]+)')
        l.add_xpath('attendance', '//div[@class="matchup"]/p/span/text()[1]', re='Attendance.*?([0-9]+)')
        l.add_xpath('home_team', '//div[@class="team away"]/p/a/text()')
        l.add_xpath('away_team', '//div[@class="team home"]/p/a/text()')
        l.add_xpath('result', '//div[@class="score-time"]//p[@class="score"]/text()')
        l.add_xpath('result_time', '//div[@class="score-time"]//p[@class="time"]/text()')
        l.add_xpath('result_agg', '//div[@class="score-time"]//p[@class="agg"]/text()')
        stats_table = response.xpath('//section[@class="mod-container"]/table[@class="no-borders"]')
        if stats_table:
            l.add_xpath('home_shots', '//tbody/tr/td[@id="home-shots"]/text()', re='([0-9]+)\(')
            l.add_xpath('home_shots_on_goal', '//tbody/tr/td[@id="home-shots"]/text()', re='\(([0-9]+)\)')
            l.add_xpath('away_shots', '//tbody/tr/td[@id="away-shots"]/text()', re='([0-9]+)\(')
            l.add_xpath('away_shots_on_goal', '//tbody/tr/td[@id="away-shots"]/text()', re='\(([0-9]+)\)')
            l.add_xpath('home_fouls', '//tbody/tr/td[@id="home-fouls"]/text()')
            l.add_xpath('away_fouls', '//tbody/tr/td[@id="away-fouls"]/text()')
            l.add_xpath('home_corner_kicks', '//tbody/tr/td[@id="home-corner-kicks"]/text()')
            l.add_xpath('away_corner_kicks', '//tbody/tr/td[@id="away-corner-kicks"]/text()')
            l.add_xpath('home_offsides', '//tbody/tr/td[@id="home-offsides"]/text()')
            l.add_xpath('away_offsides', '//tbody/tr/td[@id="away-offsides"]/text()')
            l.add_xpath('home_possession', '//tbody/tr/td[@id="home-possession"]/text()')
            l.add_xpath('away_possession', '//tbody/tr/td[@id="away-possession"]/text()')
            l.add_xpath('home_offsides', '//tbody/tr/td[@id="home-offsides"]/text()')
            l.add_xpath('away_offsides', '//tbody/tr/td[@id="away-offsides"]/text()')
            l.add_xpath('home_yellow_cards', '//tbody/tr/td[@id="home-yellow-cards"]/text()')
            l.add_xpath('away_yellow_cards', '//tbody/tr/td[@id="away-yellow-cards"]/text()')
            l.add_xpath('home_red_cards', '//tbody/tr/td[@id="home-red-cards"]/text()')
            l.add_xpath('away_red_cards', '//tbody/tr/td[@id="away-red-cards"]/text()')
            l.add_xpath('home_saves', '//tbody/tr/td[@id="home-saves"]/text()')
            l.add_xpath('away_saves', '//tbody/tr/td[@id="away-saves"]/text()')
        yield l.load_item()

